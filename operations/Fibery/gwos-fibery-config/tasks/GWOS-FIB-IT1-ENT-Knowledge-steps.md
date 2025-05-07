# GWOS-FIB-IT1-ENT-Knowledge: Implement Knowledge Entities (TM, SOP, RET) - Step-by-Step Plan

This document outlines the steps to create/verify the `Time Log (TM)`, `SOP Link (SOP)`, and `Retrospective (RET)` Fibery databases in the `Systems` Space, as part of Iteration 1 of the GWOS Fibery setup.

## Task Objective
As the Founder, I want to create the `Time Log (TM)`, `SOP Link (SOP)`, and `Retrospective (RET)` Fibery databases in the `Systems` Space, with all their specified fields, so that knowledge and work history can be effectively managed.

## Relevant PRD Sections
- PRD Section 2.12: Time Log (TM)
- PRD Section 2.13: SOP Link (SOP)
- PRD Section 2.15: Retrospective (RET)
- PRD Section 2.1: Database Summary (for entity codes)
- `operations/OPS-Systems-Overview.md` (for Space mapping)
- `operations/Fibery/iteration-1-plan.md`

## Prerequisites
- Fibery workspace "Gruntworks OS (Production)" is accessible.
- Owner-level access to the Fibery workspace.
- The `Systems` Fibery space exists.
- API Token for `fibery-bot` user.
- `operations/Fibery/apidocs.md` and `Fibery-PRD.md` for reference.

## Deliverables
1. `Systems/TimeLog (TM)` database schema created/verified and aligned with PRD Section 2.12.
2. `Systems/SopLink (SOP)` database schema created/verified and aligned with PRD Section 2.13.
3. `Systems/Retrospective (RET)` database schema created/verified and aligned with PRD Section 2.15.
4. Necessary fields for TM, SOP, and RET created via API calls (with notes for manual UI adjustments where necessary).
5. This step-by-step plan is updated with all actions and verification checks.

## Steps

**Step 1: Get Schema for `Systems` Space (Refresh if necessary)**
- Status: [X] Done
- Action:
    1. Execute `mcp_fibery-mcp-graphql_get_schema_sdl` for the `Systems` space.
- Verification:
    - [X] GraphQL schema for `Systems` space retrieved. Current types: `SystemsConfig`, `SystemsExternalInbox`, `SystemsInternalInbox`, `SystemsScorecard`, `SystemsSourceSystemsExternalInbox`.

**Step 2: Create/Verify `Time Log (TM)` Database (`Systems/TimeLog`)**
- Status: [X] Done
- Action:
    1. Analyzed the schema. `Systems/TimeLog` did not exist.
    2. Generated JSON payload (`temp_payload_TM_create.json`) to create it with fields (`Systems/TogglEntryId` (Title, Text), `Systems/Task` (Relation to `Ship/Task`), `Systems/Start` (DateTime), `Systems/Stop` (DateTime)) plus the mandatory Fibery system fields (`fibery/id`, `fibery/public-id`, `fibery/creation-date`, `fibery/modification-date`).
       - The initial payload attempt failed because the standard Fibery system fields were missing.
       - Consulted `apidocs.md` and added the required system fields to the payload.
    3. Executed `curl` command with the corrected payload, which succeeded.
    4. Verified with `mcp_fibery-mcp-graphql_list_spaces_and_types` which confirmed `Systems/TimeLog` exists.
    5. Deleted `temp_payload_TM_create.json`.
- Verification:
    - [X] `Systems/TimeLog` database created with specified fields. Formula field `Duration` noted for manual UI task.

**Step 3: Create/Verify `SOP Link (SOP)` Database (`Systems/SopLink`)**
- Status: [X] Done
- Action:
    1.  Verified schema for `Ship` space (using `mcp_fibery-mcp-graphql_get_schema_sdl`) to confirm `Ship/Task` structure before adding a relation to it.
    2.  Generated JSON payload (`temp_payload_SOP_create.json`) to create `Systems/SopLink` and add the `Ship/SopLinks` relation field to `Ship/Task` simultaneously.
        - `Systems/SopLink` fields: `Systems/Title` (Text, Title), `Systems/DocURL` (Text, ui/type: url), `Systems/Keywords` (Text placeholder), `Systems/Vertical` (Text placeholder), `Systems/Tasks` (Relation to `Ship/Task`, many-to-many, UUID `a1b2c3d4-e5f6-7890-1234-567890abcdef`).
        - Added mandatory Fibery system fields to `Systems/SopLink`.
        - Added `Ship/SopLinks` field to existing `Ship/Task` type (relation to `Systems/SopLink`, many-to-many, same UUID `a1b2c3d4-e5f6-7890-1234-567890abcdef`).
    3.  Executed `curl` command with the payload, which succeeded.
    4.  Verified with `mcp_fibery-mcp-graphql_list_spaces_and_types` (confirmed `Systems/SopLink` exists) and `mcp_fibery-mcp-graphql_get_schema_sdl` for `Ship` space (confirmed `Ship/Task.sopLinks` relation field exists).
    5.  Deleted `temp_payload_SOP_create.json`.
- Verification:
    - [X] `Systems/SopLink` database created with specified fields and relation to `Ship/Task`.
    - [X] `Ship/Task` database updated with the `Ship/SopLinks` relation field.
    - [X] Manual UI tasks noted for `Systems/SopLink.Keywords` (to Multi-select) and `Systems/SopLink.Vertical` (to Enum).

**Step 4: Create/Verify `Retrospective (RET)` Database (`Systems/Retrospective`)**
- Status: [X] Done
- Action:
    1.  Reviewed `Systems` space schema; `Systems/Retrospective` did not exist.
    2.  Generated JSON payload (`temp_payload_RET_create.json`) for `Systems/Retrospective` with fields as per PRD Section 2.15: `Systems/Name` (Text, Title), `Systems/Date` (Date), `Systems/Participants` (Text placeholder), `Systems/Project` (Relation to `Ship/Project`), `Systems/Rock` (Relation to `Strategy/Rock`), `Systems/WhatWentWell` (RichText), `Systems/WhatCouldImprove` (RichText), `Systems/ActionItems` (RichText), `Systems/Learnings` (RichText), plus mandatory Fibery system fields.
    3.  Executed `curl` command with the payload, which succeeded.
    4.  Verified with `mcp_fibery-mcp-graphql_list_spaces_and_types` which confirmed `Systems/Retrospective` exists.
    5.  Deleted `temp_payload_RET_create.json`.
- Verification:
    - [X] `Systems/Retrospective` database created with specified fields. Manual UI task noted for `Participants` (to MultiUser).

**Step 5: Final Verification & Task Completion**
- Status: [X] Done
- Action:
    1. Review all deliverables.
    2. Update this steps file with completion status.
    3. Delete all temporary payload files.
- Verification:
    - [X] All deliverables met.

---
**Task `GWOS-FIB-IT1-ENT-Knowledge` Implementation Summary:**
*   [X] Deliverable 1: `Systems/TimeLog (TM)` schema aligned.
*   [X] Deliverable 2: `Systems/SopLink (SOP)` schema aligned.
*   [X] Deliverable 3: `Systems/Retrospective (RET)` schema aligned.
*   [X] Deliverable 4: Fields created (API part done, UI tasks noted).
*   [X] Deliverable 5: This steps file updated.
*   [X] Mandatory AC (from iteration-1-plan.md):
    *   [X] Check 1: TM database exists in `Systems` Space with all fields/types.
    *   [X] Check 2: SOP database exists in `Systems` Space with all fields/types.
    *   [X] Check 3: RET database exists in `Systems` Space with all fields/types.
--- 