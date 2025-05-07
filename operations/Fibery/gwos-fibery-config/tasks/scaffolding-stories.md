# GWOS Fibery Implementation - Scaffolding Sprint Tasks

## Task `GWOS-FIB-SETUP-001-WSP-adm`: Initialize Fibery Workspace & Core Admin Setup
Objective: To establish the "Gruntworks OS (Production)" Fibery workspace and configure foundational administrative settings as per the PRD.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: Fibery workspace named "Gruntworks OS (Production)" is confirmed to exist or is created.
-   Deliverable 2: "Owner" user role capabilities verified (full access).
-   Deliverable 3: "Bot User" account invited/created in Fibery.
-   Deliverable 4: "Contractor Role" defined in Fibery with base permissions (view/edit assigned tasks, no schema/Config).
-   Deliverable 5: Audit log functionality confirmed as enabled for create/update operations.
-   **Deliverable 6 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: Log in as Owner and confirm workspace name and access to admin settings.
-   Check 2: View user list and confirm Bot User is present (even if pending invitation acceptance).
-   Check 3: View roles and confirm "Contractor Role" exists with intended permission shell.
-   Check 4: Perform a test entity creation/update and confirm an audit log entry is generated (if directly viewable, or confirm setting is on).

Dependencies: None
Relevant Risks: RISK-001
Notes: Refer to PRD Section 1 and Requirements REQ-FR-WCR-1 to REQ-FR-WCR-6, REQ-FR-SDS-6.

---

## Task `GWOS-FIB-SETUP-002-CFG-ent`: Create and Populate Config (CFG) Entity
Objective: To create the `Config (CFG)` Fibery database and populate it with initial configuration keys and values as specified in the PRD.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `Config (CFG)` database created in Fibery with fields: `Key` (Text), `Value` (Text), `Description` (Text), `Created At` (DateTime), `Updated At` (DateTime).
-   Deliverable 2: Initial config rows created for:
    *   `WIP_CAP` (Value: 3)
    *   `SELL_RATIO_MIN` (Value: 60)
    *   `SHIP_RATIO_MIN` (Value: 30)
    *   `WebhookStartToken` (Value: "TBD_N8N_START_FOCUS_URL")
    *   `WebhookStopToken` (Value: "TBD_N8N_STOP_FOCUS_URL")
    *   `WebhookDecompToken` (Value: "TBD_N8N_DECOMP_URL")
    *   `WebhookTriageToken` (Value: "TBD_N8N_TRIAGE_URL")
-   Deliverable 3: Access to the CFG entity is restricted to the "Owner" role (as per REQ-FR-WCR-5).
-   **Deliverable 4 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: View the CFG database and confirm all specified fields exist with correct types.
-   Check 2: Confirm all initial Key-Value pairs are present and correctly populated.
-   Check 3: Attempt to view/edit CFG data as a user without Owner privileges (e.g., if a test "Contractor" user is temporarily made); access should be denied. (Alternatively, verify restriction setting).

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`
Relevant Risks: RISK-001
Notes: Refer to PRD Section 2.14, 6.1 and Requirements REQ-FR-SDS-1, REQ-FR-SDS-2, REQ-FR-WCR-5.

---

## Task `GWOS-FIB-SETUP-003-STR-ent`: Scaffold Core Strategic Entities (OBJ, KR, RCK)
Objective: To create the foundational Fibery databases for strategic planning: `Objective (OBJ)`, `Key Result (KR)`, and `Rock (RCK)` with their primary fields.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `Objective (OBJ)` database created with key fields (Name, Primary S, Year, Narrative, Owner, Created At, Updated At) as per PRD Section 2.2.
-   Deliverable 2: `Key Result (KR)` database created with key fields (Name, Metric Name, Target, Actual, Unit, Primary S, Support S, Start Date, Due Date, Status, Created At, Updated At, Description, Owner) as per PRD Section 2.3.
-   Deliverable 3: `Rock (RCK)` database created with key fields (Name, Description, Phase, Owner, Due Date, Impact, Confidence, Effort, Status, Created At, Updated At) as per PRD Section 2.4.
-   Deliverable 4: Basic relations established: OBJ to KR (one-to-many), KR to RCK (one-to-many). Full formula fields for progress can be deferred if complex.
-   **Deliverable 5 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: Verify each database (OBJ, KR, RCK) exists with the listed key fields and correct types.
-   Check 2: Test creating a sample OBJ, then linking a sample KR to it.
-   Check 3: Test creating a sample KR, then linking a sample RCK to it.

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`
Relevant Risks: RISK-001, RISK-005
Notes: Focus on structural setup. Complex formulas (`Progress %`, `ICE Score`) can be implemented in later, more specific tasks.

---

## Task `GWOS-FIB-SETUP-004-EXE-ent`: Scaffold Core Execution Entities (PRJ, TSK)
Objective: To create the foundational Fibery databases for work execution: `Project (PRJ)` and `Task (TSK)` with their primary fields.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `Project (PRJ)` database created with key fields (Name, Project Type, Decomp Method, Complexity, Status, Created At, Updated At) as per PRD Section 2.5.
-   Deliverable 2: `Task (TSK)` database created with key fields (Title, Description, Owner, Mode, Priority, Estimate hrs, Status, Decomp Method, Start Date, Due Date, Created At, Updated At) as per PRD Section 2.6.
-   Deliverable 3: Basic relations established: PRJ to TSK (one-to-many). Linkage to RCK can be basic for now.
-   **Deliverable 4 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: Verify each database (PRJ, TSK) exists with the listed key fields and correct types.
-   Check 2: Test creating a sample PRJ, then linking a sample TSK to it.

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`
Relevant Risks: RISK-001, RISK-005
Notes: Focus on structure. Formula fields (`Progress %`, `Time Tracked`) and dynamic lookups (Task.Rock) can be refined later.

---

## Task `GWOS-FIB-SETUP-005-GIT-cfg`: Initialize Git for Project Configuration
Objective: To ensure the project's planning and task documents are version controlled in the specified Git repository.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: The `operations/Fibery/gwos-fibery-config/` directory is a Git working directory.
-   Deliverable 2: A `.gitignore` file is present in `operations/Fibery/gwos-fibery-config/` (if needed, e.g., for local temp files, though likely not critical for markdown).
-   Deliverable 3: Existing planning files (`vision-statement.md`, `requirements.md`, `resource-plan.md`, `architecture.md`, `architecture.mmd`, `methodology.md`, `risk-register.md`) are committed to the local Git repository.
-   Deliverable 4: The local repository is connected to the remote `https://github.com/lemonsevens/gruntworks.git` (or confirms it's part of a larger clone already pushed).
-   **Deliverable 5 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: Run `git status` in the `operations/Fibery/gwos-fibery-config/` directory; it should report a clean working tree after commit.
-   Check 2: Confirm committed files are visible in the Git history (`git log --oneline -5`).
-   Check 3: (Manual) Verify files pushed to the remote repository on GitHub if a new push is made.

Dependencies: None (can be done in parallel but logically follows creation of initial docs)
Relevant Risks: None directly, but supports overall project management.
Notes: This task ensures project artifacts are versioned.

--- 