# Core Requirements for Gruntworks OS Fibery Implementation

## Functional Requirements

### FR-WCR: Workspace Configuration & Roles
- REQ-FR-WCR-1: The Fibery workspace shall be named "Gruntworks OS (Production)".
- REQ-FR-WCR-2: A "Primary User (Owner)" role shall exist with full access to all entities, schema, and Config.
- REQ-FR-WCR-3: A "Bot User" role shall exist as a service account with API-only rights to create/edit data.
- REQ-FR-WCR-4: A "Contractor Role" shall exist with view/edit permissions for assigned Tasks, and no schema or Config permissions.
- REQ-FR-WCR-5: The "Config" entity shall be restricted to the "Owner" role.
- REQ-FR-WCR-6: An audit log shall be enabled on all entity create and update operations.
- REQ-FR-WCR-7: A weekly data and schema backup process via API shall be implemented.

### FR-ENT: Entities & Fields
- REQ-FR-ENT-1: All Entities (OBJ, KR, RCK, PRJ, TSK, CLI, DLR, EIN, IIN, ISC, SCB, TM, SOP, CFG, RET) as defined in Section 2 of `Fibery-PRD.md` shall be created.
- REQ-FR-ENT-2: Each entity shall have all fields, field types, descriptions, options, and formulas precisely as specified in Sections 2.2 through 2.15 of `Fibery-PRD.md`.
- REQ-FR-ENT-3: All specified relations between entities shall be correctly implemented, including backreferences where noted.
- REQ-FR-ENT-4: All Enum fields shall have their options defined exactly as listed in the PRD.
- REQ-FR-ENT-5: All Formula fields shall be implemented with the exact formulas provided in the PRD.
- REQ-FR-ENT-6: Default values for fields (e.g., Owner, Status) shall be set as specified.
- REQ-FR-ENT-7: Auto-timestamp fields (`createdAt`, `updatedAt`) shall function as expected.

### FR-BTN: Fibery Buttons
- REQ-FR-BTN-1: A "Start Focus" button shall be implemented on the "Task" entity.
- REQ-FR-BTN-2: The "Start Focus" button shall trigger a POST action to the webhook URL stored in the "WebhookStartToken" Config key.
- REQ-FR-BTN-3: A "Stop Focus" button shall be implemented on the "Task" entity.
- REQ-FR-BTN-4: The "Stop Focus" button shall trigger a POST action to the webhook URL stored in the "WebhookStopToken" Config key.
- REQ-FR-BTN-5: A "Decompose" button shall be implemented on the "Project" entity.
- REQ-FR-BTN-6: The "Decompose" button shall trigger a POST action (sending Project ID & Method) to the webhook URL stored in the "WebhookDecompToken" Config key.
- REQ-FR-BTN-7: A "Retry Triage" button shall be implemented on the "Inbox" (EIN/IIN) entities.
- REQ-FR-BTN-8: The "Retry Triage" button shall trigger a POST action (sending Inbox ID) to the webhook URL stored in the "WebhookTriageToken" Config key.

### FR-AUT: Fibery Automations
- REQ-FR-AUT-1: (Scorecard Color Alert) An automation shall send a Slack notification when `Scorecard.Color` changes to "Red" or "Yellow".
- REQ-FR-AUT-2: (Auto-Create Task from Issue) An automation shall create a new "Task" when a new "Issue" is created, pre-filling Task details from the Issue and linking them.
- REQ-FR-AUT-3: (Auto-Inherit on Task - Create) On Task creation, `Task.DecompMethod` shall be copied from `Project.DecompMethod`.
- REQ-FR-AUT-4: (Auto-Inherit on Task - Create) On Task creation, `Task.Mode` shall be set based on defined logic (e.g., default, inferred from Project.Type, or manually set).
- REQ-FR-AUT-5: (WIP Guard) An automation shall prevent a Task's status from changing to "In Progress" if the owner has >3 "In Progress" tasks, revert the status, and send a Slack DM.
- REQ-FR-AUT-6: (Priority Due Alert) A scheduled hourly automation shall send a Slack DM for "High Priority" tasks due in ≤24 hours.
- REQ-FR-AUT-7: (Rock Issue Spawn) A scheduled daily automation shall create an "Issue" for "Rocks" that are past their "Due Date" and not "Done".
- REQ-FR-AUT-8: Time Log data flow as described in Section 4.7 (external automation updating TM, Task.Time Tracked as formula) shall be confirmed.

### FR-VDD: Views & Dashboards
- REQ-FR-VDD-1: A "Task Kanban" view shall be created (Tasks by Status, swimlanes by Mode).
- REQ-FR-VDD-2: A "Daily Focus" view shall be created (Tasks Ready/In Progress sorted by Priority).
- REQ-FR-VDD-3: A "Sell vs Ship Chart" view shall be created (Weekly hours by Mode).
- REQ-FR-VDD-4: A "Key Results Table" view shall be created (Key Results, filterable by year, grouped by Primary_S and Support_S).
- REQ-FR-VDD-5: A "Rocks Progress Board" view shall be created (Rocks Kanban, grouped by Status).
- REQ-FR-VDD-6: An "OKR Board" view shall be created (Objectives → KRs → Rocks progress).
- REQ-FR-VDD-7: A "Capacity Planner" view shall be created (Task estimates vs tracked by Week).
- REQ-FR-VDD-8: An "Inbox Manager" view shall be created (unprocessed Inbox items).
- REQ-FR-VDD-9: An "Issue Log" view shall be created (Open issues by Severity).
- REQ-FR-VDD-10: A "Weekly Scorecard Dashboard" view shall be created (visual summary of Scorecard entities).

### FR-SDS: Seed Data & Setup Steps
- REQ-FR-SDS-1: "Config" entity rows shall be created with keys: `WIP_CAP`, `SELL_RATIO_MIN`, `SHIP_RATIO_MIN`, `WebhookStartToken`, `WebhookStopToken`, `WebhookDecompToken`, `WebhookTriageToken`.
- REQ-FR-SDS-2: Values for `WIP_CAP` (3), `SELL_RATIO_MIN` (60), and `SHIP_RATIO_MIN` (30) shall be set. Webhook token values shall be set.
- REQ-FR-SDS-3: All Enum options shall be defined exactly as listed in the PRD (covered by REQ-FR-ENT-4).
- REQ-FR-SDS-4: Sample Q2 Objectives, KRs, and Rocks shall be created.
- REQ-FR-SDS-5: Top-10 SOP Link records shall be created.
- REQ-FR-SDS-6: The "Bot User" shall be invited, and its API token recorded securely if necessary for external integrations.

## Non-Functional Requirements

### NFR-ACC: Acceptance Criteria Alignment
- REQ-NFR-ACC-1: The implemented Fibery workspace must ensure all Entities & fields exactly match the PRD specification (validates REQ-FR-ENT-*).
- REQ-NFR-ACC-2: The implemented Fibery workspace must ensure all Buttons are visible and correctly bound to their respective Config keys (validates REQ-FR-BTN-*).
- REQ-NFR-ACC-3: The implemented Fibery workspace must ensure all Automations fire correctly in defined test scenarios (validates REQ-FR-AUT-*).
- REQ-NFR-ACC-4: The implemented Fibery workspace must ensure all Views display sample data accurately (validates REQ-FR-VDD-*).
- REQ-NFR-ACC-5: The implemented Fibery workspace must ensure Config data is present and access is secured to the Owner role (validates REQ-FR-WCR-5 and REQ-FR-SDS-1, REQ-FR-SDS-2). 