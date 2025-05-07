# GWOS Fibery Implementation - Iteration 1 Plan

## Goal for Iteration 1: Implement Remaining Core Fibery Entities and Basic Relations

---

## Task `GWOS-FIB-IT1-ENT-Crm`: Implement CRM Entities (CLI, DLR) in `Sales` Space
Objective: As the Founder, I want to create the `Client (CLI)` and `Deal (DLR)` Fibery databases within the `Sales` Space, with all their specified fields and establish basic relations between them and to existing core entities, so that foundational CRM capabilities are in place.
Related Goal/Requirement: Iteration 1 Goal, PRD Sections 2.7 (CLI), 2.8 (DLR); REQ-FR-ENT-1, REQ-FR-ENT-2, REQ-FR-ENT-3.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `Client (CLI)` database created with all fields as per PRD Section 2.7.
-   Deliverable 2: `Deal (DLR)` database created with all fields as per PRD Section 2.8.
-   Deliverable 3: Relation CLI to DLR (one-to-many) established.
-   Deliverable 4: Relation CLI to Project (PRJ) (one-to-many) established.
-   Deliverable 5: Default values (e.g., Deal Amount currency) set as per PRD.
-   **Deliverable 6 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: CLI and DLR databases exist in the `Sales` Space with all specified fields and types.
-   Check 2: A sample Client can be created, and multiple Deals can be linked to it.
-   Check 3: A sample Client can be linked to an existing Project.
-   Check 4: Enums for fields like `Client.Tier`, `Client.Status`, `Deal.Stage` are correctly populated.

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`, `GWOS-FIB-SETUP-004-EXE-ent`
Relevant Resources: Fibery, `Fibery-PRD.md`
Relevant Risks: RISK-001, RISK-005

---

## Task `GWOS-FIB-IT1-ENT-Inboxes`: Implement Inbox Entities (EIN, IIN) in `Systems` Space
Objective: As the Founder, I want to create the `External Inbox (EIN)` and `Internal Inbox (IIN)` Fibery databases within the `Systems` Space, with all their specified fields, so that raw inputs can be captured.
Related Goal/Requirement: Iteration 1 Goal, PRD Section 2.9 (EIN/IIN); REQ-FR-ENT-1, REQ-FR-ENT-2.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `External Inbox (EIN)` database created with all fields as per PRD Section 2.9.
-   Deliverable 2: `Internal Inbox (IIN)` database created with all fields as per PRD Section 2.9 (identical structure to EIN).
-   Deliverable 3: Enum for `Source` and Multi-select for `Labels` configured.
-   **Deliverable 4 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: EIN and IIN databases exist in the `Systems` Space with all specified fields and types.
-   Check 2: Fields `Received At` and `Processed` have correct types and defaults.
-   Check 3: Enums for `Source` and placeholder `Labels` are correctly set up.

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`
Relevant Resources: Fibery, `Fibery-PRD.md`
Relevant Risks: RISK-001, RISK-005

---

## Task `GWOS-FIB-IT1-ENT-OpSupport`: Implement Operational Support Entities (ISC in `Support` Space, SCB in `Systems` Space)
Objective: As the Founder, I want to create the `Issue (ISC)` Fibery database in the `Support` Space and the `Scorecard (SCB)` Fibery database in the `Systems` Space, with all their specified fields, so that operational problems and KPIs can be tracked.
Related Goal/Requirement: Iteration 1 Goal, PRD Sections 2.10 (ISC), 2.11 (SCB); REQ-FR-ENT-1, REQ-FR-ENT-2.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `Issue (ISC)` database created with all fields as per PRD Section 2.10.
-   Deliverable 2: `Scorecard (SCB)` database created with all fields as per PRD Section 2.11 (excluding Color formula for now, if complex).
-   Deliverable 3: Enums for `Issue.Category`, `Issue.Severity`, `Issue.Status` configured.
-   **Deliverable 4 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: ISC database exists in the `Support` Space and SCB database exists in the `Systems` Space, with all specified fields and types.
-   Check 2: Default values (e.g., `Issue.Owner`) set as per PRD.
-   Check 3: Enums are correctly populated.

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`
Relevant Resources: Fibery, `Fibery-PRD.md`
Relevant Risks: RISK-001, RISK-005

---

## Task `GWOS-FIB-IT1-ENT-Knowledge`: Implement Tracking & Knowledge Entities (TM in `Ship` Space, SOP & RET in `Systems` Space)
Objective: As the Founder, I want to create the `Time Log (TM)` database in the `Ship` Space, and the `SOP Link (SOP)` and `Retrospective (RET)` databases in the `Systems` Space, with all their specified fields, so that time, procedures, and learnings can be managed.
Related Goal/Requirement: Iteration 1 Goal, PRD Sections 2.12 (TM), 2.13 (SOP), 2.15 (RET); REQ-FR-ENT-1, REQ-FR-ENT-2.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: `Time Log (TM)` database created with all fields as per PRD Section 2.12 (excluding Duration formula for now, if complex).
-   Deliverable 2: `SOP Link (SOP)` database created with all fields as per PRD Section 2.13.
-   Deliverable 3: `Retrospective (RET)` database created with all fields as per PRD Section 2.15.
-   Deliverable 4: Enums for `SOP.Vertical` configured.
-   **Deliverable 5 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: TM database exists in the `Ship` Space, and SOP and RET databases exist in the `Systems` Space, with all specified fields and types.
-   Check 2: MultiUser field for `RET.Participants` correctly configured.
-   Check 3: Enums are correctly populated.

Dependencies: `GWOS-FIB-SETUP-001-WSP-adm`
Relevant Resources: Fibery, `Fibery-PRD.md`
Relevant Risks: RISK-001, RISK-005

---

## Task `GWOS-FIB-IT1-REL-CoreConnect`: Establish Core Entity Relations & Simple Lookups Across Spaces
Objective: As the Founder, I want to establish all remaining direct relations and simple lookup fields between all core Fibery entities (new and scaffolded, across their respective Spaces: `Sales`, `Systems`, `Support`, `Ship`, `Strategy`) as defined in the PRD, so that the data model is fully interconnected.
Related Goal/Requirement: Iteration 1 Goal, PRD Section 2 (all subsections); REQ-FR-ENT-3.
Key Deliverables / Acceptance Criteria:
-   Deliverable 1: Relation `Task.Project` (many-to-one) confirmed/established.
-   Deliverable 2: Relation `Task.Rock` (lookup: `Project.Rock`) configured.
-   Deliverable 3: Relation `Task.SOP Links` (many-to-many) established.
-   Deliverable 4: Relation `Task.Inbox Record` (to EIN/IIN) established.
-   Deliverable 5: Relation `Project.Rock` (many-to-one, optional) established.
-   Deliverable 6: Relation `Issue.Rock` (many-to-one, optional) established.
-   Deliverable 7: Relation `Retrospective.Project` and `Retrospective.Rock` established.
-   Deliverable 8: All other explicit relations mentioned in PRD field tables (e.g., `Key Result.Objective`, `Rock.Key Result`) are verified and correctly configured (including backreferences where noted).
-   **Deliverable 9 - Mandatory AC**: Verification Criteria defined below are met.

**Verification Criteria (Checks):**
-   Check 1: Create a Task and link it to a Project, verify Rock lookup if Project is linked to Rock.
-   Check 2: Link multiple SOPs to a Task. Link a Task to an Inbox item.
-   Check 3: Link an Issue to a Rock. Link a Retrospective to a Project and a Rock.
-   Check 4: Spot-check 3-5 other key relations from the PRD tables to ensure they function as expected (e.g., can link a KR to an Objective).

Dependencies: `GWOS-FIB-SETUP-003-STR-ent`, `GWOS-FIB-SETUP-004-EXE-ent`, `GWOS-FIB-IT1-ENT-Crm`, `GWOS-FIB-IT1-ENT-Inboxes`, `GWOS-FIB-IT1-ENT-OpSupport`, `GWOS-FIB-IT1-ENT-Knowledge`
Relevant Resources: Fibery, `Fibery-PRD.md`
Relevant Risks: RISK-001, RISK-005

--- 