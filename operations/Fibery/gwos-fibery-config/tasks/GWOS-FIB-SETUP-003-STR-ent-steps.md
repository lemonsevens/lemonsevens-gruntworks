# GWOS-FIB-SETUP-003-STR-ent: Scaffold Core Strategic Entities (OBJ, KR, RCK) - Step-by-Step Plan

This document outlines the steps to implement the Fibery databases for Objectives (OBJ), Key Results (KR), and Rocks (RCK), including their key fields and basic relations, as part of the GWOS Fibery scaffolding.

## Task Objective
To create the foundational Fibery databases for strategic planning: `Objective (OBJ)`, `Key Result (KR)`, and `Rock (RCK)` with their primary fields and basic inter-relations, as per PRD Sections 2.2, 2.3, 2.4 and `scaffolding-stories.md`.

## Steps

**Step 1: Determine Target Fibery Space**
- Status: [X] Complete
- Action: Request user to specify the Fibery Space where the `Objective (OBJ)`, `Key Result (KR)`, and `Rock (RCK)` databases should be created.
- Verification: [X] User provides the target space name.
- Notes: User specified "Strategy" space.

**Step 2: Create Core Strategic Databases (OBJ, KR, RCK) with Key Primitive Fields**
- Status: [X] Complete
- Action: 
    1. Construct a JSON payload in `temp_fibery_payload.json`. This payload will use the `fibery.schema/batch` command to create three new types in the target space:
        *   `Strategy/Objective` with key primitive fields (Name, Primary S, Year, Narrative, Owner - as text placeholders for complex types like Enum/User initially).
        *   `Strategy/KeyResult` with key primitive fields (Name, Metric Name, Target, Actual, Unit, Primary S, Support S, Start Date, Due Date, Status, Description, Owner - as text placeholders).
        *   `Strategy/Rock` with key primitive fields (Name, Description, Phase, Owner, Due Date, Impact, Confidence, Effort, Status - as text placeholders).
    2. All types will include the standard Fibery system fields (`fibery/id`, `fibery/public-id`, `fibery/creation-date`, `fibery/modification-date`) with their correct meta properties, and the `fibery.app/install-mixins` command for `fibery/rank-mixin`.
- Execution: Ran `curl -X POST https://gruntworks.fibery.io/api/commands -H 'Authorization: Token 605bbbb5.d08eb70695e6c8d455faff55ae72d2dbf9c' -H 'Content-Type: application/json' -d @temp_fibery_payload.json | cat`.
- Verification:
    - [X] `curl` command reports success for all type creation operations (returned three "ok" results for the schema batches).
    - [X] `mcp_fibery-mcp-graphql_list_spaces_and_types` confirms `Objective`, `KeyResult`, and `Rock` types are present in the "Strategy" Fibery space.
- Notes: Payload updated to use `fibery/int` and `fibery/decimal` for numeric types. An unexpected "Database_1" also appeared in the "Strategy" space, origin unknown but not blocking.

**Step 3: Establish Basic Relations (OBJ <-> KR, KR <-> RCK)**
- Status: [X] Complete
- Action: For each side of each relation, construct a JSON payload in `temp_fibery_payload.json` using `fibery.schema/batch` and `schema.field/create` commands.
    *   Defined "Key Results" field (collection of KeyResults) in Objective, and its reverse "Objective" field (single Objective) in KeyResult using shared UUID `11111111-aaaa-bbbb-cccc-000000000001`.
    *   Defined "Rocks" field (collection of Rocks) in KeyResult, and its reverse "Key Result" field (single KeyResult) in Rock using shared UUID `22222222-aaaa-bbbb-cccc-000000000002`.
- Execution: Ran `curl -X POST https://gruntworks.fibery.io/api/commands -H 'Authorization: Token 605bbbb5.d08eb70695e6c8d455faff55ae72d2dbf9c' -H 'Content-Type: application/json' -d @temp_fibery_payload.json | cat`.
- Verification:
    - [X] `curl` command(s) report success for relation field creation (returned "ok").
    - [X] User confirmed via UI that schema inspection confirms relations are correctly established.
- Notes: Successfully used the Field API documentation structure. Delete-then-create for `temp_fibery_payload.json` was necessary to avoid stale/merged content issues.

**Step 4: Final Verification and Commit**
- Status: [ ] Pending
- Action: Review deliverables for `GWOS-FIB-SETUP-003-STR-ent` as per `scaffolding-stories.md`:
    *   [ ] D1: OBJ database created with key fields.
    *   [ ] D2: KR database created with key fields.
    *   [ ] D3: RCK database created with key fields.
    *   [ ] D4: Basic relations OBJ-KR and KR-RCK established.
- Execution:
    1. Update this `GWOS-FIB-SETUP-003-STR-ent-steps.md` file with actual outcomes, decisions, and any commands run.
    2. Commit the updated `GWOS-FIB-SETUP-003-STR-ent-steps.md` file.
- Verification: [ ] All checks pass and deliverables are met.
- Notes: 