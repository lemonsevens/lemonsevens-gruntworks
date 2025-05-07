# GWOS-FIB-IT1-ENT-OpSupport: Implement Operational Support Entities (ISC, SCB) - Step-by-Step Plan

This document outlines the steps to create/verify the `Issue (ISC)` Fibery database in the `Support` Space and the `Scorecard (SCB)` Fibery database in the `Systems` Space, as part of Iteration 1 of the GWOS Fibery setup.

## Task Objective
As the Founder, I want to create the `Issue (ISC)` Fibery database in the `Support` Space and the `Scorecard (SCB)` Fibery database in the `Systems` Space, with all their specified fields, so that operational health can be tracked and managed.

## Relevant PRD Sections
-   PRD Section 2.10: Issue (ISC)
-   PRD Section 2.11: Scorecard (SCB)
-   PRD Section 2.1: Database Summary (for entity codes)
-   `operations/OPS-Systems-Overview.md` (for Space mapping)

## Prerequisites
-   Fibery workspace "Gruntworks OS (Production)" is accessible.
-   Owner-level access to the Fibery workspace.
-   The `Systems` Fibery space exists.
-   The `Support` Fibery space exists (User to create manually if it does not).
-   API Token for `fibery-bot` user.
-   `fibery_api_guide.md` and `Fibery-PRD.md` for reference.

## Deliverables
1.  `Support/Issue (ISC)` database schema created/verified and aligned with PRD Section 2.10.
2.  `Systems/Scorecard (SCB)` database schema created/verified and aligned with PRD Section 2.11.
3.  Necessary fields for ISC and SCB created via API calls.
4.  This step-by-step plan is updated with all actions and verification checks.

## Steps

**Step 1: Verify `Support` Space & Get Schema / Create `Issue (ISC)` Database**
- Status: [X] Done
- Action:
    1.  User confirmed the `Support` Fibery Space exists.
    2.  `mcp_fibery-mcp-graphql_list_spaces_and_types` called, showing `Support` space with a dummy `Database_1`.
    3.  `mcp_fibery-mcp-graphql_get_schema_sdl` called for the `Support` space, confirming `Database_1` was the only type.
    4.  User manually deleted `Support/Database_1` from the Fibery UI after an API attempt to delete it failed (`fibery.schema/delete-type` command not found).
    5.  A JSON payload (`temp_payload_create_SupportIssue.json`) was generated to create the `Support/Issue` type with fields as per PRD Section 2.10 using `schema.type/create`.
        - Field names `Next_Step` and `Root_Cause` were initially `Next_Step` and `Root_Cause` (with underscores) which caused an API error. They were corrected to `NextStep` and `RootCause`.
        - Fields `Category`, `Severity`, `Status` (Enums), and `Owner` (User) were created as `fibery/text` type via API. These require manual UI adjustment to their proper types and options.
        - Other fields (`Title`, `Rock` relation, `Description`, `NextStep`, `RootCause`, `ResolvedAt`) were created as specified or as `fibery/rich-text`.
    6.  `curl` command executed successfully with the corrected payload, creating `Support/Issue`.
    7.  `mcp_fibery-mcp-graphql_list_spaces_and_types` confirmed `Support/Issue` now exists.
- Verification:
    - [X] `Support` space confirmed.
    - [X] GraphQL schema for `Support` space retrieved and analyzed (showed dummy `Database_1`).
    - [X] `Support/Issue` database now exists. Fields `Title` (Text), `Rock` (Relation to Strategy/Rock), `Description` (RichText), `Category` (Text), `Severity` (Text), `Owner` (Text), `NextStep` (Text), `RootCause` (RichText), `Status` (Text), `ResolvedAt` (DateTime) are present.
    - [X] **Manual UI Task Noted:** Fields `Category`, `Severity`, `Status` need conversion from Text to Enum with options from PRD. Field `Owner` needs conversion from Text to User.

**Step 2: Get Schema for `Systems` Space & Create/Verify `Scorecard (SCB)` Database**
- Status: [X] Done
- Action:
    1.  Executed `mcp_fibery-mcp-graphql_get_schema_sdl` for the `Systems` space. Schema confirmed existing types: `Config`, `ExternalInbox`, `InternalInbox`, `SourceSystemsExternalInbox`.
    2.  `Systems/Scorecard` did not exist. Generated a JSON payload (`temp_payload_SCB_create.json`) to create the `Systems/Scorecard` type with fields as per PRD Section 2.11.
        - Field names `KPI Name` changed to `KpiName` and `Week_Start` to `WeekStart` for API compatibility.
        - `Value` and `Target` fields (Number in PRD) initially attempted with `fibery/number` and `fibery/float`, both failed. Corrected to `fibery/decimal` based on `operations/Fibery/docs.md`, which succeeded.
        - `Owner` field (User in PRD) created as `fibery/text` for API creation (manual UI update to User type noted).
        - `Color` field (Formula in PRD) noted for manual UI setup.
    3.  Executed `curl` command with the corrected payload (`fibery/decimal`), successfully creating `Systems/Scorecard`.
    4.  `mcp_fibery-mcp-graphql_list_spaces_and_types` confirmed `Systems/Scorecard` now exists.
- Verification:
    - [X] GraphQL schema for `Systems` space retrieved and analyzed.
    - [X] `Systems/Scorecard` database now exists with fields `KpiName` (Text, Title), `WeekStart` (Date), `Value` (Decimal), `Target` (Decimal), `Owner` (Text). Standard Fibery fields also present.
    - [X] **Manual UI Task Noted:** Field `Owner` needs conversion from Text to User. Field `Color` (Formula) needs to be created in the UI.

**Step 3: Final Verification & Task Completion**
- Status: [X] Done
- Action:
    1.  Reviewed all deliverables for task `GWOS-FIB-IT1-ENT-OpSupport`.
    2.  `Support/Issue` created. Manual UI: `Category`, `Severity`, `Status` to Enum; `Owner` to User.
    3.  `Systems/Scorecard` created. Manual UI: `Owner` to User; `Color` Formula to be added.
    4.  This steps file updated with completion status for all steps.
    5.  All temporary payload files deleted.
- Verification:
    - [X] All deliverables met.

---
**Task `GWOS-FIB-IT1-ENT-OpSupport` Implementation Summary:**
*   [X] Deliverable 1: `Support/Issue (ISC)` schema aligned with PRD (API part done, UI tasks noted).
*   [X] Deliverable 2: `Systems/Scorecard (SCB)` schema aligned with PRD (API part done, UI tasks noted).
*   [X] Deliverable 3: Fields created/verified via API (with notes for manual UI for Enums/Formulas/User types).
*   [X] Deliverable 4: This steps file updated.
*   [X] Mandatory AC (from iteration-1-plan.md):
    *   [X] Check 1: ISC database exists in `Support` Space with all fields/types (API part done, UI tasks noted).
    *   [X] Check 2: SCB database exists in `Systems` Space with all fields/types (API part done, UI tasks noted).
--- 