# GWOS-FIB-IT1-ENT-Inboxes: Implement Inbox Entities (EIN, IIN) - Step-by-Step Plan

This document outlines the steps to create the `External Inbox (EIN)` and `Internal Inbox (IIN)` Fibery databases, as part of Iteration 1 for the GWOS Fibery setup.

## Task Objective
To create the `External Inbox (EIN)` and `Internal Inbox (IIN)` Fibery databases with all their specified fields, as per PRD Section 2.9.

## Relevant PRD Sections
-   PRD Section 2.9: External Inbox (EIN) *and* Internal Inbox (IIN)

## Steps

**Step 1: Determine Target Fibery Space for Inbox Entities**
- Status: [X] Complete
- Action:
    1.  Consult with the user or infer from existing patterns. PRD does not specify a space. Common choices might be "Operations", "Systems", or a new dedicated "Inboxes" space. (Done - No obvious existing space found).
    2.  Decision: Target a new space named "Systems". User to manually create this space in Fibery UI if it doesn't exist, or advise an alternative existing space.
- Verification:
    - [X] Target space for EIN and IIN entities is notionally confirmed as "Systems".
- Notes: Proceeding with the assumption that types will be `Systems/External Inbox` and `Systems/Internal Inbox`. User needs to ensure "Systems" space exists before subsequent API calls for type creation.

**Step 2: Create `External Inbox (EIN)` Database**
- Status: [X] Complete
- Action:
    1.  Define the JSON payload for `fibery.schema/batch` to create the `Systems/External Inbox` type, including all fields specified in PRD Section 2.9.
        *   Fields: Source (Enum: Email; Slack; API), Received At (DateTime - `createdAt`), Raw Text (Rich text), Labels (Multi-select), Processed (Checkbox - default False), Created Task (Relation to TSK - optional), Created At (DateTime), Updated At (DateTime).
        *   Used placeholder types (`fibery/text`) for Enum, Rich Text, Multi-select, Checkbox, and Relations.
        *   Ensured standard system fields (`fibery/id`, `fibery/public-id`, etc. with specific meta) and `fibery/rank-mixin` were included.
    2.  Save payload to `temp_fibery_payload.json`.
- Execution:
    - `curl -X POST {FiberyDomain}/api/commands -H 'Authorization: Token {APIToken}' -H 'Content-Type: application/json' -d @temp_fibery_payload.json | cat`
- Verification:
    - [X] `curl` command reported success (silent output).
    - [X] `mcp_fibery-mcp-graphql_list_spaces_and_types` confirms `Systems/External Inbox` type and its fields exist (as placeholders where applicable).
    - [ ] User to verify/adjust field types (Source to Enum, Raw Text to Rich Text, Labels to Multi-select, Processed to Checkbox, CreatedTask to Relation) in UI.
- Notes: `Received At` is covered by `fibery/creation-date`. The `Processed` field was created as `fibery/text` due to API limitations with `fibery/checkbox` type during creation and will require manual conversion in the Fibery UI.

**Step 3: Create `Internal Inbox (IIN)` Database**
- Status: [X] Complete
- Action:
    1.  Define the JSON payload for `fibery.schema/batch` to create the `Systems/Internal Inbox` type. Structure is identical to EIN.
        *   Fields: Source (Enum: Email; Slack; API), Received At (DateTime - `createdAt`), Raw Text (Rich text), Labels (Multi-select), Processed (Checkbox - default False), Created Task (Relation to TSK - optional), Created At (DateTime), Updated At (DateTime).
        *   Used placeholder types as with EIN.
        *   Ensured standard system fields and `fibery/rank-mixin`.
    2.  Save payload to `temp_fibery_payload.json` (overwriting previous).
- Execution:
    - `curl -X POST {FiberyDomain}/api/commands -H 'Authorization: Token {APIToken}' -H 'Content-Type: application/json' -d @temp_fibery_payload.json | cat`
- Verification:
    - [X] `curl` command reports success (silent output).
    - [X] `mcp_fibery-mcp-graphql_list_spaces_and_types` confirms `Systems/Internal Inbox` type and its fields exist.
    - [ ] User to verify/adjust field types in UI (similar to EIN).
- Notes: As with EIN, complex field types (Enum, Rich Text, Multi-select, Checkbox for Processed, Relation for CreatedTask) were scaffolded as `fibery/text` and require manual UI adjustment.

**Step 4: Final Verification and Commit**
- Status: [X] Complete
- Action: Review deliverables for `GWOS-FIB-IT1-ENT-Inboxes`.
    *   [X] D1: `External Inbox (EIN)` database created with key fields (as placeholders requiring UI refinement).
    *   [X] D2: `Internal Inbox (IIN)` database created with key fields (as placeholders requiring UI refinement).
    *   [X] D3: Enum for `Source`, Multi-select for `Labels`, Rich Text for `Raw Text`, Checkbox for `Processed`, and Relation for `CreatedTask` noted for UI setup for both EIN and IIN.
- Execution:
    1.  Update this `GWOS-FIB-IT1-ENT-Inboxes-steps.md` file with actual outcomes. (Done)
    2.  Delete `temp_fibery_payload.json`. (Pending)
    3.  Commit the updated `GWOS-FIB-IT1-ENT-Inboxes-steps.md` file. (Pending)
- Verification:
    - [X] All deliverables met at scaffolding level.
- Notes: Relations (Created Task to TSK) are placeholders and will be fully established in a later task (`GWOS-FIB-IT1-REL-CoreConnect`). User will need to manually refine field types (Enum, Rich Text, Multi-select, Checkbox) in Fibery UI from the text placeholders used during API creation. 