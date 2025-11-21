# Linear Import Guide for Leonne's Angel Machine

This guide will help you import the `linear-import-full-roadmap.csv` file into your Linear workspace.

## Prerequisites

Before importing, ensure your Linear workspace has the following configured:

### 1. Status Labels

Your CSV uses these status values. Make sure these exist in your Linear workspace:

- **Done** (or map to "Completed")
- **Ready** (or map to "In Progress" / "Todo")
- **Backlog** (or map to "Backlog")

**To check/create statuses:**

- Go to Settings → Statuses
- Create any missing statuses or note which existing ones to map to

### 2. Priority Labels

Your CSV uses these priority values:

- **High**
- **Medium**

**To check/create priorities:**

- Go to Settings → Priorities
- Ensure "High" and "Medium" exist (or note mappings)

### 3. Cycles/Projects

Your CSV references these cycles:

- Phase 1
- Phase 1b
- Phase 1c
- Phase 2
- Phase 4

**To prepare:**

- Create Cycles or Projects in Linear for each phase (or map to existing ones)
- Go to Settings → Cycles or Projects to create them

## CSV File Structure

Your CSV contains the following columns:

- **Title**: Issue/task title
- **Description**: Detailed description of the task
- **Cycle**: Phase/cycle name (Phase 1, Phase 1b, Phase 1c, Phase 2, Phase 4)
- **Status**: Current status (Done, Ready, Backlog)
- **Priority**: Priority level (High, Medium)
- **Assignee**: Currently empty (can be filled with email addresses)

## Import Steps

### Step 1: Access Linear Import Tool

1. Log into your Linear workspace
2. Click your profile picture (top-left)
3. Select **Settings**
4. In the sidebar, click **Import / Export**

### Step 2: Choose Import Source

1. Select **CSV** as your import source
2. Click **Import** or **Upload CSV**

### Step 3: Upload Your File

1. Click **Choose File** or drag-and-drop
2. Select `linear-import-full-roadmap.csv`
3. Click **Next** or **Continue**

### Step 4: Map CSV Columns to Linear Fields

Linear will show a mapping interface. Map your columns as follows:

| CSV Column | Linear Field | Notes |
|------------|--------------|-------|
| Title | Title | Required field |
| Description | Description | Will populate issue description |
| Cycle | Cycle or Project | Map to your Linear Cycles/Projects |
| Status | Status | Must match existing status names |
| Priority | Priority | Must match existing priority labels |
| Assignee | Assignee | Leave empty or map if you have assignees |

**Important Mapping Notes:**

- If your Linear status names differ, you may need to edit the CSV first
- If Cycle doesn't exist as a field, you may need to use Labels or Projects instead
- Assignee can be left unmapped if empty

### Step 5: Review Import Preview

1. Linear will show a preview of issues to be created
2. Review the first few issues to ensure mapping is correct
3. Check that:
   - Titles are correct
   - Descriptions are populated
   - Statuses match
   - Priorities are set
   - Cycles/Projects are assigned

### Step 6: Confirm and Import

1. Click **Import** or **Confirm Import**
2. Wait for the import to complete (may take a few minutes for 66 issues)
3. Linear will show a summary of imported issues

### Step 7: Verify Import

1. Navigate to your project/workspace view
2. Check that all 66 issues were imported
3. Verify:
   - Issues are organized by Cycle/Project
   - Statuses are correctly set
   - Priorities are assigned
   - Descriptions are complete

## Troubleshooting

### Issue: Status names don't match

**Solution:** Either:

1. Create matching status names in Linear, OR
2. Edit the CSV to use your existing Linear status names

### Issue: Cycle field not available

**Solution:**

- Use Projects instead of Cycles
- Or add Cycle as a custom field in Linear
- Or use Labels to tag issues by phase

### Issue: Some issues failed to import

**Solution:**

- Check Linear's import error log
- Common issues: missing required fields, invalid status/priority names
- Fix the CSV and re-import only the failed issues

### Issue: Assignees not mapping

**Solution:**

- Ensure assignee column contains email addresses or Linear usernames
- Or leave assignee column empty and assign manually after import

## Post-Import Tasks

After successful import:

1. **Review Issues**: Go through imported issues to ensure accuracy
2. **Set Assignees**: Manually assign issues if needed
3. **Add Labels**: Consider adding additional labels for organization
4. **Create Views**: Set up custom views by Phase, Status, or Priority
5. **Link Issues**: Create relationships between related issues if needed

## CSV Statistics

- **Total Issues**: 66
- **Phase 1**: 15 issues (all Done)
- **Phase 1b**: 13 issues (all Ready)
- **Phase 1c**: 24 issues (all Backlog)
- **Phase 2**: 8 issues (all Backlog)
- **Phase 4**: 6 issues (all Backlog)

## Need Help?

- Linear Support: <https://linear.app/docs>
- Linear Community: <https://linear.app/community>
- Check Linear's import documentation for latest features

---

**Last Updated**: 2025-01-27
**CSV File**: `linear-import-full-roadmap.csv`
