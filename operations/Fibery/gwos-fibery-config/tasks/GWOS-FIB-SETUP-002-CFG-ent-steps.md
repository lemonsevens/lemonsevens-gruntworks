# Implementation Steps for GWOS-FIB-SETUP-002-CFG-ent: Create and Populate Config (CFG) Entity

## Objective:
To create the `Config (CFG)` Fibery database and populate it with initial configuration keys and values as specified in the PRD, ensuring access is restricted to the "Owner" role.

## Prerequisites:
-   Fibery workspace "Gruntworks OS (Production)" is accessible.
-   Owner-level access to the Fibery workspace is available.
-   `Fibery-PRD.md` (Sections 2.14, 6.1) and `requirements.md` (REQ-FR-SDS-1, REQ-FR-SDS-2, REQ-FR-WCR-5) are available for reference.

## Implementation Steps:

[X] 1.  **Create `Config (CFG)` Database in `Systems` Space (Deliverable 1, Check 1 part 1):**
    *   Action: The `Systems/Config` database schema was created using a `curl` command with the Fibery API. This supersedes previous considerations of using MCP tools or manual UI creation for the initial schema.
    *   The target space `Systems` should exist in Fibery (manual creation if not already present).
    *   JSON Payload (`operations/Fibery/gwos-fibery-config/tasks/temp_payload_GWOS-FIB-SETUP-002.json`):
        ```json
        [
          {
            "command": "fibery.schema/batch",
            "args": {
              "commands": [
                {
                  "command": "schema.type/create",
                  "args": {
                    "fibery/name": "Systems/Config",
                    "fibery/meta": {
                      "fibery/domain?": true,
                      "ui/color": "#FFD700"
                    },
                    "fibery/fields": [
                      {
                        "fibery/name": "Systems/Key",
                        "fibery/type": "fibery/text",
                        "fibery/meta": { "ui/title?": true }
                      },
                      {
                        "fibery/name": "Systems/Value",
                        "fibery/type": "fibery/text"
                      },
                      {
                        "fibery/name": "Systems/Description",
                        "fibery/type": "fibery/text"
                      },
                      {
                        "fibery/name": "fibery/id",
                        "fibery/type": "fibery/uuid",
                        "fibery/meta": { "fibery/id?": true, "fibery/readonly?": true }
                      },
                      {
                        "fibery/name": "fibery/public-id",
                        "fibery/type": "fibery/text",
                        "fibery/meta": { "fibery/public-id?": true, "fibery/readonly?": true }
                      },
                      {
                        "fibery/name": "fibery/creation-date",
                        "fibery/type": "fibery/date-time",
                        "fibery/meta": { "fibery/creation-date?": true, "fibery/readonly?": true, "fibery/default-value": "$now" }
                      },
                      {
                        "fibery/name": "fibery/modification-date",
                        "fibery/type": "fibery/date-time",
                        "fibery/meta": { "fibery/modification-date?": true, "fibery/required?": true, "fibery/readonly?": true, "fibery/default-value": "$now" }
                      }
                    ]
                  }
                },
                {
                  "command": "fibery.app/install-mixins",
                  "args": {
                    "types": {
                      "Systems/Config": ["fibery/rank-mixin"]
                    }
                  }
                }
              ]
            }
          }
        ]
        ```
    *   `curl` Command Executed:
        ```bash
        curl -X POST https://gruntworks.fibery.io/api/commands \
          -H 'Authorization: Token 605bbbb5.d08eb70695e6c8d455faff55ae72d2dbf9c' \
          -H 'Content-Type: application/json' \
          -d @operations/Fibery/gwos-fibery-config/tasks/temp_payload_GWOS-FIB-SETUP-002.json | cat
        ```
    *   Fields created (as per PRD Section 2.14, within `Systems/Config`):
        *   `Systems/Key`: Text (Primary field)
        *   `Systems/Value`: Text
        *   `Systems/Description`: Text
        *   `fibery/creation-date`: DateTime (Corresponds to PRD `CreatedAt`)
        *   `fibery/modification-date`: DateTime (Corresponds to PRD `UpdatedAt`)
    *   Verification:
        *   [X] `curl` command executed.
        *   [X] User visually confirmed in the Fibery UI that the `Systems/Config` database and all specified fields (`Key`, `Value`, `Description`, and system date fields) exist with the correct types (per user-provided screenshot).
        *   [X] User confirmed the `Systems` Fibery space exists and contains the `Config` database (per user-provided screenshot).

[X] 2.  **Populate Initial Config Data (Deliverable 2, Check 2):**
    *   Action: User has confirmed data was migrated/is present in the `Systems/Config` database.
    *   Records to create:
        1.  `Key`: "WIP_CAP", `Value`: "3", `Description`: "Max Work-In-Progress limit for tasks"
        2.  `Key`: "SELL_RATIO_MIN", `Value`: "60", `Description`: "Target minimum percentage of time for Sell activities"
        3.  `Key`: "SHIP_RATIO_MIN", `Value`: "30", `Description`: "Target minimum percentage of time for Ship activities"
        4.  `Key`: "WebhookStartToken", `Value`: "TBD_N8N_START_FOCUS_URL", `Description`: "n8n webhook URL for Start Focus button"
        5.  `Key`: "WebhookStopToken", `Value`: "TBD_N8N_STOP_FOCUS_URL", `Description`: "n8n webhook URL for Stop Focus button"
        6.  `Key`: "WebhookDecompToken", `Value`: "TBD_N8N_DECOMP_URL", `Description`: "n8n webhook URL for Decompose Project button"
        7.  `Key`: "WebhookTriageToken", `Value`: "TBD_N8N_TRIAGE_URL", `Description`: "n8n webhook URL for Retry Triage Inbox button"
    *   Verification: User visually confirmed in the Fibery UI that the required records exist with the correct Key, Value, and Description (per user-provided screenshot).

[X] 3.  **Restrict `Config (CFG)` Entity Access (Deliverable 3, Check 3):**
    *   Action: Manually, in Fibery's permission settings for the `Config` database, configured it so that **only** users with the "Owner" role have full access (view, create, edit, delete). Ensured all other current and future roles (e.g., default "Member", any guest roles, the deferred "Contractor Role") have **no access** to this database.
    *   Verification: User confirmed manual check of Fibery's permission settings for the `Config` database.

[X] 4.  **Final Verification & Task Completion:**
    *   Action: All deliverables and verification checks for task `GWOS-FIB-SETUP-002-CFG-ent` have been met.
    *   This task is now marked as complete.

---
**Task `GWOS-FIB-SETUP-002-CFG-ent` Implementation Summary:**
*   [X] Deliverable 1: `Config (CFG)` database created with specified fields.
*   [X] Deliverable 2: Initial config rows created.
*   [X] Deliverable 3: Access to CFG entity restricted to "Owner".
*   [X] Deliverable 4 - Mandatory AC:
    *   [X] Check 1: CFG database and fields confirmed (API + User Visual).
    *   [X] Check 2: Initial Key-Value pairs confirmed (User Visual).
    *   [X] Check 3: Access restriction confirmed.
--- 