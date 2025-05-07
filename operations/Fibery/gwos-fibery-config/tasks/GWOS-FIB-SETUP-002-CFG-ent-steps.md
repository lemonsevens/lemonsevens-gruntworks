# Implementation Steps for GWOS-FIB-SETUP-002-CFG-ent: Create and Populate Config (CFG) Entity

## Objective:
To create the `Config (CFG)` Fibery database and populate it with initial configuration keys and values as specified in the PRD, ensuring access is restricted to the "Owner" role.

## Prerequisites:
-   Fibery workspace "Gruntworks OS (Production)" is accessible.
-   Owner-level access to the Fibery workspace is available.
-   `Fibery-PRD.md` (Sections 2.14, 6.1) and `requirements.md` (REQ-FR-SDS-1, REQ-FR-SDS-2, REQ-FR-WCR-5) are available for reference.

## Implementation Steps:

[ ] 1.  **Create `Config (CFG)` Database (Deliverable 1, Check 1 part 1):**
    *   Action: Using Fibery tools (e.g., `mcp_fibery-mcp-server_create_entity` or UI actions if MCP doesn't directly support DB creation, then manual field creation), create a new database named `Config`. The PRD uses `CFG` as a code; ensure the primary identifier reflects this if applicable, or the display name is "Config".
    *   Fields to create:
        *   `Key`: Text (Set as Fibery's primary field for this database)
        *   `Value`: Text
        *   `Description`: Text
        *   `Created At`: DateTime (Use Fibery's built-in "Created At" field for entities)
        *   `Updated At`: DateTime (Use Fibery's built-in "Updated At" field for entities)
    *   Verification: Visually confirm in the Fibery UI that the `Config` database and all specified fields exist with the correct types.

[ ] 2.  **Populate Initial Config Data (Deliverable 2, Check 2):**
    *   Action: Using Fibery tools (e.g., `mcp_fibery-mcp-server_create_entities_batch`), create seven new records in the `Config` database.
    *   Records to create:
        1.  `Key`: "WIP_CAP", `Value`: "3", `Description`: "Max Work-In-Progress limit for tasks"
        2.  `Key`: "SELL_RATIO_MIN", `Value`: "60", `Description`: "Target minimum percentage of time for Sell activities"
        3.  `Key`: "SHIP_RATIO_MIN", `Value`: "30", `Description`: "Target minimum percentage of time for Ship activities"
        4.  `Key`: "WebhookStartToken", `Value`: "TBD_N8N_START_FOCUS_URL", `Description`: "n8n webhook URL for Start Focus button"
        5.  `Key`: "WebhookStopToken", `Value`: "TBD_N8N_STOP_FOCUS_URL", `Description`: "n8n webhook URL for Stop Focus button"
        6.  `Key`: "WebhookDecompToken", `Value`: "TBD_N8N_DECOMP_URL", `Description`: "n8n webhook URL for Decompose Project button"
        7.  `Key`: "WebhookTriageToken", `Value`: "TBD_N8N_TRIAGE_URL", `Description`: "n8n webhook URL for Retry Triage Inbox button"
    *   Verification: Visually confirm in the Fibery UI that all seven records exist with the correct Key, Value, and Description.

[ ] 3.  **Restrict `Config (CFG)` Entity Access (Deliverable 3, Check 3):**
    *   Action: Manually, in Fibery's permission settings for the `Config` database, configure it so that **only** users with the "Owner" role have full access (view, create, edit, delete). Ensure all other current and future roles (e.g., default "Member", any guest roles, the deferred "Contractor Role") have **no access** to this database.
    *   Verification: This is primarily a manual check of Fibery's permission settings for the `Config` database. If a non-Owner test account is available, attempt to access or view the `Config` database; access should be denied. Otherwise, meticulously review the applied permission rules.

[ ] 4.  **Final Verification & Task Completion:**
    *   Action: Review all deliverables and verification checks for this task (`GWOS-FIB-SETUP-002-CFG-ent`) to ensure they are met.
    *   Mark this task as complete in relevant tracking (e.g., by updating this steps file).

---
**Task `GWOS-FIB-SETUP-002-CFG-ent` Implementation Summary:**
*   [ ] Deliverable 1: `Config (CFG)` database created with specified fields.
*   [ ] Deliverable 2: Initial config rows created.
*   [ ] Deliverable 3: Access to CFG entity restricted to "Owner".
*   [ ] Deliverable 4 - Mandatory AC:
    *   [ ] Check 1: CFG database and fields confirmed.
    *   [ ] Check 2: Initial Key-Value pairs confirmed.
    *   [ ] Check 3: Access restriction confirmed.
--- 