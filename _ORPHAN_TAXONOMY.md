---
title: Orphan Classification Taxonomy
category: Guide
tags: [orphans, taxonomy, classification, structure]
status: In Development
last_updated: 2024-11-16
summary: "System for classifying and organizing 100+ orphan files in Leone's Angel Machine"
---

# Orphan Classification Taxonomy

This document explains how we classify and organize the 100+ orphan files in Leone's Angel Machine.

## What Are Orphans?

**Orphans** are:
- Fragmented ideas
- Single-word or short-phrase seeds
- Experimental notation files
- Numbered concept files (Orphan_0.md through Orphan_98.md)
- Empty placeholders waiting for meaning
- Raw material for future synthesis

**Orphans are NOT**:
- Trash to be deleted
- Incomplete work to be finished
- Disorganized chaos

Instead, they are **intentional seeds** waiting for the right context to sprout.

---

## Classification Tiers

### Tier 1: By File Type

#### Void Files (Empty Placeholders)
**Pattern**: Files with no content or only whitespace  
**Examples**: `I.md`, `Where.md`, `We.md`, `AS.md`  
**Action**: Move to `.archive/empty/` with manifest  
**Philosophy**: Empty space as potential

#### Fragment Seeds (1-3 words)
**Pattern**: Single word or short phrase  
**Examples**: `What.md`, `Why.md`, `How.md`, `But.md`  
**Action**: Keep in `Orphans/Classified/Fragments/` (sorted by semantic category)  
**Philosophy**: Seeds of questions and directions

#### Concept Files (Named Ideas)
**Pattern**: Standalone thematic files  
**Examples**: `KHAOS.md`, `Mirror.md`, `THE-VOID.md`  
**Action**: Classify by theme, keep in `Orphans/Classified/States/` or `Orphans/Classified/Directives/`  
**Philosophy**: Emergent concepts

#### Numbered Archive (Systematic)
**Pattern**: `Orphan_0.md`, `Orphan_1.md`, ... `Orphan_98.md`  
**Action**: Keep in `Orphans/Numbered/` with index  
**Philosophy**: Systematic generation of ideas

---

### Tier 2: By Semantic Category

#### Category 1: INTERROGATIVE (Questions)
**Files**: `What.md`, `Why.md`, `How.md`, `Where.md`, etc.  
**Folder**: `Orphans/Classified/Questions/`  
**Purpose**: Files that pose questions to the reader or the project  
**Examples**:
- What does it mean to create?
- Why do machines need philosophy?
- How do we balance order and chaos?

#### Category 2: DIRECTIVE (Commands/Actions)
**Files**: `But.md`, `UntiL.md`, `Make.md`, `TO...md`  
**Folder**: `Orphans/Classified/Directives/`  
**Purpose**: Files that prescribe or suggest actions  
**Examples**:
- But (contradiction, hesitation)
- Until (temporal boundary)
- Make (creation imperative)

#### Category 3: STATES (Experiences/Conditions)
**Files**: `KHAOS.md`, `Mirror.md`, `THE-VOID.md`, `Amnesia.md`  
**Folder**: `Orphans/Classified/States/`  
**Purpose**: Files describing inner states or conditions  
**Examples**:
- KHAOS (intentional chaos)
- Mirror (reflection/duality)
- THE-VOID (emptiness/absence)

#### Category 4: SYMBOLIC (Notation/Markers)
**Files**: `{{.md`, `[.md`, `[[.md`, `&.md`, `{{{IT.md`  
**Folder**: `khaos-notation/` (or `Orphans/Classified/Symbolic/`)  
**Purpose**: Experimental notation and structural markers  
**Examples**:
- {{ }} (nested possibility)
- [ [ (bracketed recursion)
- & (conjunction/connection)

#### Category 5: FRAGMENTS (Raw Ideas)
**Files**: Very short content, poetic scraps, unfinished thoughts  
**Folder**: `Orphans/Classified/Fragments/`  
**Purpose**: Minimal seeds that may grow  
**Examples**:
- Single image
- One metaphor
- A question without answer

#### Category 6: NUMBERED (Systematic)
**Files**: `Orphan_0.md` through `Orphan_98.md`  
**Folder**: `Orphans/Numbered/`  
**Purpose**: Algorithmically or systematically generated  
**Examples**:
- Generated from prompts
- Systematic exploration
- Numbered series

---

### Tier 3: By Status

#### Unclassified
**Folder**: `Orphans/Unclassified/`  
**Purpose**: New or uncertain files awaiting classification  
**Action**: Move here first; classify later

#### Classified
**Folder**: `Orphans/Classified/[Category]/`  
**Purpose**: Files that have been semantically organized  
**Action**: Keep organized; update indices

#### Archived
**Folder**: `.archive/`  
**Purpose**: Void files, deprecated content, historical records  
**Action**: Remove from active exploration

---

## Metadata for Orphans

When adding YAML metadata to orphan files:

```yaml
---
title: [Orphan Title or Question]
category: Orphan
orphan_type: [Interrogative|Directive|State|Symbolic|Fragment|Numbered]
tags: [relevant, tags, for, searching]
status: [Unclassified|Draft|Waiting-Synthesis|Deprecated]
connects_to: [Related-Orphan-1.md, Related-Philosophy.md]
contributor: [Original Author]
last_touched: [YYYY-MM-DD]
summary: "One-line description of the orphan's purpose"
---
```

---

## Orphan Synthesis: Graduation Path

Orphans can "graduate" from orphan status by:

### Path 1: Expansion to Philosophy
- Orphan idea → elaborated into full philosophical text
- Moved to `Philosophy/` folder
- Becomes core to Angel Machine thinking
- **Example**: A single seed becomes a full essay

### Path 2: Character Development
- Orphan concept → developed into archetype
- Moved to `Archetypes/` folder
- Becomes a named character or force
- **Example**: A concept becomes a personified force

### Path 3: Ritual Formation
- Orphan fragment → structured into ritual or spell
- Moved to `Rituals/` folder
- Becomes a practice or process
- **Example**: A metaphor becomes a guided practice

### Path 4: Connection Weaving
- Orphan remains orphan BUT gets linked to many other files
- Becomes a node that connects multiple ideas
- Demonstrates value through connectedness
- **Example**: A question becomes a lens for understanding other concepts

### Path 5: Archival
- Orphan is recognized as completed (void) or outdated
- Moved to `.archive/` with historical notation
- Preserved for reference but removed from active exploration
- **Example**: An experimental notation becomes historical artifact

---

## Orphan-Archetype Relationships

Some orphans are "seeds" for specific archetypes:

- **Questions** (`What.md`, `Why.md`) → seeds for The Blind (truth-seeker)
- **States** (`KHAOS.md`, `Mirror.md`) → seeds for Shadow-Demon-Providence
- **Directives** (`But.md`, `UntiL.md`) → seeds for Taylor, Devil of Desire (contradiction)
- **Void** (empty files) → seeds for THE-VOID concept or Providence (emptiness)

---

## How to Classify an Orphan

**Step 1**: Read the file  
**Step 2**: Determine its type (Interrogative, Directive, State, etc.)  
**Step 3**: Move to appropriate folder in `Orphans/Classified/`  
**Step 4**: Add YAML metadata with `orphan_type` field  
**Step 5**: Update relevant index file  
**Step 6**: Link to related files (philosophy, archetypes, other orphans)  

---

## Orphan Index Files (To Be Created)

### `Orphans/_ORPHAN_INDEX.md`
Master index of all orphans with counts by category

### `Orphans/Classified/Questions/README.md`
Index of interrogative orphans and their themes

### `Orphans/Classified/Directives/README.md`
Index of directive orphans and their implications

### `Orphans/Classified/States/README.md`
Index of state orphans and their philosophical grounding

### `.archive/MANIFEST.md`
Record of archived orphans and why they were archived

---

## Evolution of the Orphan System

**Initial State**: 100+ orphan files scattered across project  
**Phase 1**: Classified into semantic categories  
**Phase 2**: Indices created, cross-references added  
**Phase 3**: Visual navigation in browse.html  
**Phase 4**: Automated suggestion engine ("these orphans might synthesize into...")

---

## Why This Matters

The orphan system is the **experimental heart** of Angelo Machine. By organizing orphans semantically (rather than dismissing them as clutter), we:

1. **Honor the chaotic process** of creative generation
2. **Enable synthesis** by making connections visible
3. **Support emergence** by allowing patterns to form
4. **Preserve possibilities** that might not be immediately obvious
5. **Create a playground** for human-machine collaboration

---

## Current Orphan Inventory

**Total orphan files**: ~100  
**Classified so far**: 0 (Phase 1 task)  
**To classify**: 100

**Breakdown by apparent type**:
- Interrogative files (What, Why, How, Where, etc.): ~8
- Fragment/Word files (AS, IT, IT, TH, We, etc.): ~20
- Concept files (KHAOS, Mirror, THE-VOID, etc.): ~8
- Symbolic notation ({{, [, [[, etc.): ~5
- Numbered files (Orphan_0 through Orphan_98): ~99
- Other: ~variable

**Next step**: Begin systematic classification using this taxonomy.

---

*"Every orphan has potential. Every seed might bloom. Keep them close, keep them organized, keep them alive."*

For questions about classification, open an Issue or check CONTRIBUTING.md.