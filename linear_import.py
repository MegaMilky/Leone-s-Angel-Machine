#!/usr/bin/env python3
"""
Linear CSV Import Script for Leonne's Angel Machine

This script imports issues from linear-import-full-roadmap.csv into Linear using their GraphQL API.

Prerequisites:
1. Install required packages: pip install requests python-dotenv
2. Get your Linear API key from: https://linear.app/settings/api
3. Create a .env file with: LINEAR_API_KEY=your_api_key_here
4. Get your Team ID from Linear (found in workspace settings or URL)

Usage:
    python linear_import.py
"""

import csv
import os
import sys
import time
from typing import Dict, List, Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Linear API configuration
LINEAR_API_URL = "https://api.linear.app/graphql"
LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")
TEAM_ID = os.getenv("LINEAR_TEAM_ID")  # Optional: can be set in .env

if not LINEAR_API_KEY:
    print("❌ ERROR: LINEAR_API_KEY not found in environment variables")
    print("\nTo set it up:")
    print("1. Get your API key from: https://linear.app/settings/api")
    print("2. Create a .env file in this directory with:")
    print("   LINEAR_API_KEY=your_api_key_here")
    print("   LINEAR_TEAM_ID=your_team_id_here  # Optional")
    sys.exit(1)


class LinearImporter:
    def __init__(self, api_key: str, team_id: Optional[str] = None):
        self.api_key = api_key
        self.team_id = team_id
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }
        self.status_map = {}
        self.priority_map = {}
        self.cycle_map = {}
        self.project_map = {}

    def make_request(self, query: str, variables: Dict = None) -> Dict:
        """Make a GraphQL request to Linear API"""
        response = requests.post(
            LINEAR_API_URL,
            json={"query": query, "variables": variables or {}},
            headers=self.headers,
        )
        response.raise_for_status()
        data = response.json()
        if "errors" in data:
            raise Exception(f"GraphQL errors: {data['errors']}")
        return data["data"]

    def get_teams(self) -> List[Dict]:
        """Get all teams in the workspace"""
        query = """
        query {
            teams {
                nodes {
                    id
                    name
                    key
                }
            }
        }
        """
        data = self.make_request(query)
        return data["teams"]["nodes"]

    def select_team(self) -> str:
        """Select or get team ID"""
        if self.team_id:
            return self.team_id

        teams = self.get_teams()
        if not teams:
            raise Exception("No teams found in workspace")

        if len(teams) == 1:
            print(f"✓ Using team: {teams[0]['name']} ({teams[0]['key']})")
            return teams[0]["id"]

        print("\nAvailable teams:")
        for i, team in enumerate(teams, 1):
            print(f"  {i}. {team['name']} ({team['key']})")

        while True:
            try:
                choice = input(f"\nSelect team (1-{len(teams)}): ").strip()
                idx = int(choice) - 1
                if 0 <= idx < len(teams):
                    return teams[idx]["id"]
                print("Invalid choice. Please try again.")
            except (ValueError, KeyboardInterrupt):
                print("\nCancelled.")
                sys.exit(0)

    def get_workflow_states(self, team_id: str) -> Dict[str, str]:
        """Get workflow states and create mapping"""
        query = """
        query($teamId: String!) {
            team(id: $teamId) {
                states {
                    nodes {
                        id
                        name
                        type
                    }
                }
            }
        }
        """
        data = self.make_request(query, {"teamId": team_id})
        states = data["team"]["states"]["nodes"]

        # Create mapping: CSV status -> Linear state ID
        mapping = {}
        for state in states:
            name_lower = state["name"].lower()
            mapping[name_lower] = state["id"]

        # Map CSV statuses to Linear states
        csv_to_linear = {
            "done": ["done", "completed", "closed"],
            "ready": ["ready", "in progress", "todo", "started"],
            "backlog": ["backlog", "triage", "unstarted"],
        }

        result = {}
        for csv_status, linear_names in csv_to_linear.items():
            for linear_name in linear_names:
                if linear_name in mapping:
                    result[csv_status] = mapping[linear_name]
                    break
            if csv_status not in result:
                # Try exact match
                if csv_status in mapping:
                    result[csv_status] = mapping[csv_status]

        return result

    def get_priorities(self) -> Dict[str, str]:
        """Get priority values"""
        # Linear priorities: 0=None, 1=Urgent, 2=High, 3=Medium, 4=Low
        return {
            "high": "2",
            "medium": "3",
            "low": "4",
            "urgent": "1",
            "none": "0",
        }

    def get_or_create_cycle(self, team_id: str, cycle_name: str) -> Optional[str]:
        """Get or create a cycle for the phase"""
        # First, try to find existing cycle
        query = """
        query($teamId: String!) {
            team(id: $teamId) {
                cycles {
                    nodes {
                        id
                        name
                    }
                }
            }
        }
        """
        data = self.make_request(query, {"teamId": team_id})
        cycles = data["team"]["cycles"]["nodes"]

        for cycle in cycles:
            if cycle["name"].lower() == cycle_name.lower():
                return cycle["id"]

        # Cycle not found - user will need to create it manually or we skip
        print(f"⚠️  Cycle '{cycle_name}' not found. Issues will be created without cycle.")
        return None

    def create_issue(
        self,
        team_id: str,
        title: str,
        description: str,
        state_id: Optional[str] = None,
        priority: Optional[str] = None,
        cycle_id: Optional[str] = None,
    ) -> str:
        """Create an issue in Linear"""
        mutation = """
        mutation($input: IssueCreateInput!) {
            issueCreate(input: $input) {
                success
                issue {
                    id
                    identifier
                    title
                }
            }
        }
        """

        input_data = {
            "teamId": team_id,
            "title": title,
            "description": description,
        }

        if state_id:
            input_data["stateId"] = state_id
        if priority:
            input_data["priority"] = int(priority)
        if cycle_id:
            input_data["cycleId"] = cycle_id

        variables = {"input": input_data}
        data = self.make_request(mutation, variables)

        if data["issueCreate"]["success"]:
            issue = data["issueCreate"]["issue"]
            return issue["id"]
        else:
            raise Exception("Failed to create issue")

    def import_csv(self, csv_path: str = "linear-import-full-roadmap.csv"):
        """Import issues from CSV file"""
        if not os.path.exists(csv_path):
            print(f"❌ ERROR: CSV file not found: {csv_path}")
            sys.exit(1)

        # Get team ID
        team_id = self.select_team()

        # Get mappings
        print("\n📋 Loading workflow states...")
        self.status_map = self.get_workflow_states(team_id)
        print(f"✓ Found {len(self.status_map)} status mappings")

        self.priority_map = self.get_priorities()
        print("✓ Priority mappings loaded")

        # Read CSV
        print(f"\n📖 Reading CSV file: {csv_path}")
        issues = []
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                issues.append(row)

        print(f"✓ Found {len(issues)} issues to import")

        # Confirm import
        print(f"\n⚠️  About to import {len(issues)} issues into Linear")
        response = input("Continue? (yes/no): ").strip().lower()
        if response not in ["yes", "y"]:
            print("Import cancelled.")
            return

        # Import issues
        print("\n🚀 Starting import...\n")
        successful = 0
        failed = 0

        for i, issue in enumerate(issues, 1):
            try:
                title = issue["Title"].strip()
                description = issue["Description"].strip()
                cycle_name = issue["Cycle"].strip()
                status = issue["Status"].strip().lower()
                priority = issue["Priority"].strip().lower()

                # Get state ID
                state_id = self.status_map.get(status)
                if not state_id:
                    print(f"⚠️  [{i}/{len(issues)}] Skipping '{title}' - status '{status}' not found")
                    failed += 1
                    continue

                # Get priority
                priority_value = self.priority_map.get(priority)

                # Get cycle ID
                cycle_id = self.get_or_create_cycle(team_id, cycle_name)

                # Create issue
                issue_id = self.create_issue(
                    team_id=team_id,
                    title=title,
                    description=description,
                    state_id=state_id,
                    priority=priority_value,
                    cycle_id=cycle_id,
                )

                print(f"✓ [{i}/{len(issues)}] Created: {title}")
                successful += 1

                # Rate limiting - be nice to the API
                time.sleep(0.5)

            except Exception as e:
                print(f"❌ [{i}/{len(issues)}] Failed '{title}': {str(e)}")
                failed += 1

        # Summary
        print(f"\n{'='*50}")
        print(f"✅ Import complete!")
        print(f"   Successful: {successful}")
        print(f"   Failed: {failed}")
        print(f"   Total: {len(issues)}")
        print(f"{'='*50}")


def main():
    print("=" * 50)
    print("Linear CSV Importer for Leonne's Angel Machine")
    print("=" * 50)

    importer = LinearImporter(LINEAR_API_KEY, TEAM_ID)
    importer.import_csv()


if __name__ == "__main__":
    main()

