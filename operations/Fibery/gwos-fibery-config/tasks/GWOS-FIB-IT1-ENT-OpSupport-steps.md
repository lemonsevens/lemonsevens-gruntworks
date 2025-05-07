# GWOS-FIB-IT1-ENT-OpSupport: Implement Operational Support Entities (ISC, SCB) - Step-by-Step Plan

This document outlines the steps to create the `Issue (ISC)` and `Scorecard (SCB)` Fibery databases, as part of Iteration 1 for the GWOS Fibery setup.

## Task Objective
To create the `Issue (ISC)` and `Scorecard (SCB)` Fibery databases with all their specified fields, as per PRD Sections 2.10 and 2.11.

## Relevant PRD Sections
-   PRD Section 2.10: Issue (ISC)
-   PRD Section 2.11: Scorecard (SCB)

## Steps

**Step 1: Determine Target Fibery Space for Operational Support Entities**
- Status: [ ] Pending
- Action:
    1.  Based on `operations/OPS-Systems-Overview.md`:
        *   `Issue (ISC)` entity will be created in the `Support` Fibery Space.
        *   `Scorecard (SCB)` entity will be created in the `Systems` Fibery Space (for operational health metrics).
- Verification:
    - [ ] Target spaces confirmed: `Support` for ISC, `Systems` for SCB.
- Notes: Strategic scorecards might also exist in the `Strategy` space, but for this task, SCB will be in `Systems`.

**Step 2: Create `Issue (ISC)` Database in `Support` Space**
- Status: [ ] Pending
- Action:
    1.  Define the JSON payload for `fibery.schema/batch` to create the `Support/Issue` type, including all fields specified in PRD Section 2.10.
        *   Fields: Rock (Relation to RCK - optional), Description (Rich text), Category (Enum: Sell; Ship; Strategy; Systems; Support), Severity (Enum: Low; Medium; High), Owner (User - Default Founder), Next_Step (Text), Root_Cause (Rich text), Status (Enum: Open; Closed), Created At (DateTime), Resolved At (DateTime).
        *   Use placeholder types (e.g., `fibery/text`) for Enum, Rich Text, Relation, and User types, to be refined in UI.
        *   Ensure standard system fields and `fibery/rank-mixin`.
    2.  Save payload to `temp_fibery_payload.json`.
- Execution:
    - `curl -X POST {FiberyDomain}/api/commands -H 'Authorization: Token {APIToken}' -H 'Content-Type: application/json' -d @temp_fibery_payload.json | cat`
- Verification:
    - [ ] `curl` command reports success.
    - [ ] `mcp_fibery-mcp-graphql_list_spaces_and_types` confirms `Support/Issue` type and fields exist (as placeholders).
    - [ ] User to verify/adjust field types in UI.

**Step 3: Create `Scorecard (SCB)` Database in `Systems` Space**
- Status: [ ] Pending
- Action:
    1.  Define the JSON payload for `fibery.schema/batch` to create the `Systems/Scorecard` type, including fields from PRD Section 2.11 (excluding `Color` formula for now).
        *   Fields: Week_Start (Date), KPI Name (Text), Value (Number), Target (Number), Owner (User - Default Founder), Created At (DateTime), Updated At (DateTime).
        *   Use placeholder types for User type.
        *   Ensure standard system fields and `fibery/rank-mixin`.
    2.  Save payload to `temp_fibery_payload.json`.
- Execution:
    - `curl -X POST {FiberyDomain}/api/commands -H 'Authorization: Token {APIToken}' -H 'Content-Type: application/json' -d @temp_fibery_payload.json | cat`
- Verification:
    - [ ] `curl` command reports success.
    - [ ] `mcp_fibery-mcp-graphql_list_spaces_and_types` confirms `Systems/Scorecard` type and fields exist.
    - [ ] User to verify/adjust field types in UI.

**Step 4: Final Verification and Commit**
- Status: [ ] Pending
- Action: Review deliverables for `GWOS-FIB-IT1-ENT-OpSupport`.
    *   [ ] D1: `Issue (ISC)` database created with key fields (as placeholders).
    *   [ ] D2: `Scorecard (SCB)` database created with key fields (as placeholders).
    *   [ ] D3: Enums for `Issue` fields noted for UI setup.
- Execution:
    1.  Update this `GWOS-FIB-IT1-ENT-OpSupport-steps.md` file.
    2.  Delete `temp_fibery_payload.json`.
    3.  Commit changes.
- Verification:
    - [ ] All deliverables met at scaffolding level.
- Notes: Complex formulas (e.g., `Scorecard.Color`) and specific default value handling (e.g., `Issue.ResolvedAt` on status change) are deferred. User will need to manually refine field types (Enum, Rich Text, Relation, User) in Fibery UI. 