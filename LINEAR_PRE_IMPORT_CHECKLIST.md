# Linear Import Pre-Flight Checklist

Use this checklist before importing `linear-import-full-roadmap.csv` into Linear.

## ✅ Pre-Import Setup

### Status Configuration
- [ ] Check existing statuses in Linear (Settings → Statuses)
- [ ] Create missing statuses OR note mappings:
  - [ ] "Done" → (your equivalent: _______________)
  - [ ] "Ready" → (your equivalent: _______________)
  - [ ] "Backlog" → (your equivalent: _______________)

### Priority Configuration
- [ ] Check existing priorities in Linear (Settings → Priorities)
- [ ] Create missing priorities OR note mappings:
  - [ ] "High" → (your equivalent: _______________)
  - [ ] "Medium" → (your equivalent: _______________)

### Cycle/Project Setup
- [ ] Create Cycles or Projects for each phase:
  - [ ] Phase 1
  - [ ] Phase 1b
  - [ ] Phase 1c
  - [ ] Phase 2
  - [ ] Phase 4

### CSV File Verification
- [ ] CSV file is saved and accessible
- [ ] File has 66 data rows (plus header)
- [ ] No empty rows in the middle
- [ ] All required columns present: Title, Description, Cycle, Status, Priority, Assignee

## 📋 Import Mapping Plan

Before starting import, decide how to map:

| CSV Value | Linear Field | Your Mapping |
|-----------|--------------|--------------|
| Cycle | Cycle/Project | ________________ |
| Done | Status | ________________ |
| Ready | Status | ________________ |
| Backlog | Status | ________________ |
| High | Priority | ________________ |
| Medium | Priority | ________________ |
| (empty) | Assignee | Leave empty / Manual assignment |

## 🚀 Ready to Import?

Once all checkboxes are complete:
1. Open Linear → Settings → Import / Export
2. Select CSV import
3. Upload `linear-import-full-roadmap.csv`
4. Follow the mapping wizard
5. Review preview
6. Confirm import

## 📊 Expected Results

After import, you should have:
- **66 total issues**
- **15 issues** in Phase 1 (Status: Done)
- **13 issues** in Phase 1b (Status: Ready)
- **24 issues** in Phase 1c (Status: Backlog)
- **8 issues** in Phase 2 (Status: Backlog)
- **6 issues** in Phase 4 (Status: Backlog)

---

**Tip**: Keep this checklist handy during import to verify each step!

