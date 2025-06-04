# Fibery Space PRD

**Version:** v1.0 – 2025-05-06
Scope: Comprehensive specification for the Gruntworks Operating System inside Fibery. Includes all types, fields, formulas, relations, buttons, automations, views, seed data, roles, permissions, and acceptance criteria—no placeholders.

---

## Overview: How Gruntworks OS Works (No Fixed Times)

Gruntworks OS directs a solo founder's workflow across the two core modalities—**Sell** (60% of time) and **Ship** (30% of time)—and the three support layers **Strategy**, **Systems**, and **Support** (10% of time).

### Core Cadences

* **Daily Rhythm**:
  • *Morning Digest:* review Slack summary of priority Sell/Ship tasks.
  • *Focus Blocks:* use Fibery's **Start Focus** button to begin a block, track via Toggl, then **Stop Focus**, mark done, and invoke **Next Task** suggestion.
  • *Systems Review:* process inboxes, enforce Work-In-Progress limits, log quick SOP refinements.
  • *Shutdown:* capture daily wins and set tomorrow's top Sell target.

* **Weekly Rhythm**:
  • *Weekly Kickoff:* review 'This Week' Tasks and capacity.
  • *Midweek Check:* inspect KPI trends for drift.
  • *Scorecard & Retro:* finalize weekly metrics, draft retrospective, then plan next week by moving Rocks and Tasks.

* **Monthly / Quarterly / Annual**:
  • *Monthly Systems Day:* automate one key workflow.
  • *Quarterly Rock Reset:* evaluate and set new Rocks under OKRs.
  • *Annual Vision Refresh:* update high-level Objectives and review capacity models (capacity is managed via Task estimates, time tracking, target allocation percentages (e.g., Sell 60%, Ship 30%), and the 'Capacity Planner' view).

Each cadence maps directly to the Fibery workspace defined below.

---

## 1  Space Configuration & Roles

* **Space:** Gruntworks OS (Production)
* **Primary User (Owner):** full access to all entities, schema, and Config.
* **Bot User:** service account; API-only rights to create/edit data.
* **Contractor Role:** view/edit Tasks assigned; no schema or Config permissions.
* **Security:**
  • Config entity restricted to Owner.
  • Audit log enabled on all create/update.
  • Weekly data/schema backup via API.

---

## 2  Types & Fields

### 2.1  Type Summary

| Code | Type (Display Name)    | Description                                                                   |
| ---- | ---------------------- | ----------------------------------------------------------------------------- |
| OBJ  | Objective              | Annual north‑star outcomes under Sell or Ship                                 |
| KR   | Key Result             | Quantified target driving an Objective                                        |
| RCK  | Rock                   | 90‑day commitments linked to Key Results                                      |
| PRJ  | Project                | Work containers for client/internal/ops initiatives                           |
| TSK  | Task                   | Individual work items                                                         |
| CLI  | Client                 | Account records for CRM                                                       |
| DLR  | Deal                   | Sales opportunities                                                           |
| EIN  | External Inbox         | Raw inbound requests from external sources                                    |
| IIN  | Internal Inbox         | Raw internal ideas, bugs, spontaneous tasks                                   |
| ISC  | Issue                  | Problem log entries (L10)                                                     |
| SCB  | Scorecard              | Weekly KPI tracking rows                                                      |
| TM   | Time Log               | Detailed time entries synced from Toggl                                       |
| SOP  | SOP Link               | Pointers to versioned Markdown SOPs                                           |
| CFG  | Config                 | Key‑value settings and webhook/API tokens                                     |
| RET  | Retrospective          | Captures learnings from projects or periods                                   |
| CLS  | Client Segment         | Represents different segments of clients                                      |
| CWS  | Client Workflow State  | Defines the stages in a client's lifecycle or a deal's progression            |
| PWS  | Project Workflow State | Defines granular states for the project lifecycle                             |
| TWS  | Task Workflow State    | Defines granular states for the task lifecycle                                |
| PRI  | Task Priority          | Defines urgency levels for tasks                                              |
| INT  | Interaction            | Tracks individual touchpoints with companies (e.g., calls, emails, meetings). |
| CMT  | Comment                | User-generated comments on other types                                        |
| FILE | File                   | Represents files attached to other types                                      |
| DTY  | Deal Type              | Represents different types of deals                                           |

---

### Space: Strategy

#### 2.2  Objective (OBJ)

| Field       | Type          | Description                        | Options / Formula                                        |
| ----------- | ------------- | ---------------------------------- | -------------------------------------------------------- |
| Name        | Text          | Title of the Objective             | n/a                                                      |
| Primary S   | Enum          | Core modality                      | Sell; Ship                                               |
| Year        | Integer       | Calendar year                      | e.g. 2025                                                |
| Narrative   | Rich text     | High‑level description             | n/a                                                      |
| Owner       | User          | Responsible leader                 | Default: Founder                                         |
| Key Results | Relation (KR) | Child Key Results                  | n‑to‑many                                                |
| Progress %  | Formula       | Avg progress of linked Key Results | `if(count(Key Results)=0,0,avg(Key Results.Progress %))` |
| Created At  | DateTime      | Auto timestamp                     | `createdAt`                                              |
| Updated At  | DateTime      | Auto timestamp                     | `updatedAt`                                              |

---

#### 2.3  Key Result (KR)

| Field       | Type           | Description                                                                                  | Options / Formula                           |
| ----------- | -------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Name        | Text           | Title of the Key Result                                                                      | n/a                                         |
| Objective   | Relation (OBJ) | Parent Objective                                                                             | 1‑to‑many backreference                     |
| Metric Name | Text           | What is measured                                                                             | e.g. "MQLs"                                 |
| Target      | Number         | Target numeric value                                                                         | n/a                                         |
| Actual      | Number         | Current measured value                                                                       | n/a                                         |
| Unit        | Text           | Unit of measurement for the metric                                                           | e.g. "USD", "%", "count"                    |
| Primary S   | Enum           | Core modality the KR primarily supports                                                      | Sell; Ship                                  |
| Support S   | Enum           | Supporting pillar the KR aligns with                                                         | Strategy; Systems; Support                  |
| Start Date  | Date           | Planned start date for working on the KR                                                     | n/a                                         |
| Due Date    | Date           | Target completion date for the KR                                                            | n/a                                         |
| Status      | Enum           | Health indicator                                                                             | On Track; At Risk; Off Track                |
| Progress %  | Formula        | `min(Actual/Target*100,100)`                                                                 | `if(Target=0,0,min(Actual/Target*100,100))` |
| Rocks       | Relation (RCK) | Child Rocks                                                                                  | n‑to‑many                                   |
| Created At  | DateTime       | Auto timestamp                                                                               | `createdAt`                                 |
| Updated At  | DateTime       | Auto timestamp                                                                               | `updatedAt`                                 |
| Description | Rich text      | Detailed explanation of the Key Result, its measurement, and its importance to the Objective | n/a                                         |
| Owner       | User           | Responsible person                                                                           | Default: Founder                            |

---

#### 2.4  Rock (RCK)

| Field       | Type              | Description                                             | Options / Formula                            |
| ----------- | ----------------- | ------------------------------------------------------- | -------------------------------------------- |
| Name        | Text              | Rock title                                              | n/a                                          |
| Key Result  | Relation (KR)     | Parent Key Result                                       | backreference                                |
| Description | Rich text         | Detailed explanation of the Rock's scope and objectives | n/a                                          |
| Phase       | Enum              | Primary phase this Rock belongs to                      | Sell; Ship                                   |
| Owner       | User              | Responsible person                                      | Default: Founder                             |
| Due Date    | Date              | Target completion date                                  | n/a                                          |
| Figma_Link  | URL               | Link to relevant Figma designs or mockups               | n/a                                          |
| Impact      | Number (1–10)     | Expected value                                          | n/a                                          |
| Confidence  | Number (1–10)     | Certainty level                                         | n/a                                          |
| Effort      | Number (hours)    | Estimated effort                                        | n/a                                          |
| ICE Score   | Formula           | `(Impact*Confidence)/max(Effort,1)`                     | `round((Impact*Confidence)/max(Effort,1),1)` |
| Status      | Enum              | Life cycle stage                                        | Proposed; Active; Blocked; Done              |
| Tasks       | Relation (TSK)    | Linked Tasks                                            | n‑to‑many                                    |
| Progress %  | Formula           | Avg progress of Tasks                                   | `if(count(Tasks)=0,0,avg(Tasks.Progress %))` |
| Issue Flag  | Formula (Boolean) | Past due and not done                                   | `and(Due Date<TODAY(),Status!='Done')`       |
| Created At  | DateTime          | Auto                                                    | `createdAt`                                  |
| Updated At  | DateTime          | Auto                                                    | `updatedAt`                                  |

---

### Space: Sales

#### 2.5  ClientSegment (CLS)

*Description:* Represents different segments of clients (e.g., Enterprise, SMB).

| Field                    | Type           | Description                                                  | Options / Formula                                                |
| ------------------------ | -------------- | ------------------------------------------------------------ | ---------------------------------------------------------------- |
| fibery/id                | ID             | Read-only, System Generated                                  |                                                                  |
| fibery/public-id         | Text           | Read-only, System Generated                                  |                                                                  |
| fibery/creation-date     | Date           | Read-only, System Generated                                  |                                                                  |
| fibery/modification-date | Date           | Read-only, System Generated                                  |                                                                  |
| fibery/rank              | Number         | Read-only, System Generated                                  |                                                                  |
| Sales/Name               | Text           | Name of the client segment                                   |                                                                  |
| Sales/Icon               | Text           | Stores an icon identifier or URL                             | e.g., emoji                                                      |
| Sales/Description        | Rich Text      | Details about this segment                                   |                                                                  |
| Sales/Companies          | Relation (CLI) | Companies in this segment (One-to-Many with `Company (CLI)`) | *Note: This represents the companies belonging to this segment.* |
| Created At               | DateTime       | Auto                                                         | `createdAt`                                                      |
| Updated At               | DateTime       | Auto                                                         | `updatedAt`                                                      |

*Default/Queried Entities:*
  - Name: Enterprise, Icon: (icon_value_if_known_or_NA)
  - Name: SMB, Icon: (icon_value_if_known_or_NA)
  - Name: Startup, Icon: (icon_value_if_known_or_NA)
  - Name: Mid-Size, Icon: (icon_value_if_known_or_NA)
  *(Actual icon values were present in the query but are generalized here for brevity)*

---

#### 2.6  ClientWorkflowState (CWS)

*Description:* Defines the stages in a client's lifecycle or a deal's progression, aligning with the revised sales process.

| Field                       | Type           | Description                                                                                      | Options / Formula                                                                                                                                     |
| --------------------------- | -------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| fibery/id                   | ID             | Read-only, System Generated                                                                      |                                                                                                                                                       |
| fibery/public-id            | Text           | Read-only, System Generated                                                                      |                                                                                                                                                       |
| fibery/creation-date        | Date           | Read-only, System Generated                                                                      |                                                                                                                                                       |
| fibery/modification-date    | Date           | Read-only, System Generated                                                                      |                                                                                                                                                       |
| fibery/rank                 | Number         | Read-only, System Generated                                                                      |                                                                                                                                                       |
| Sales/Name                  | Text           | Name of the workflow state                                                                       | e.g., "New Lead (Raw)", "Nurturing - Post Demo Follow-up" (SDL: name: String)                                                                         |
| Sales/StateCategory         | Single-Select  | Broad category of the state. For high-level grouping.                                            | Related to `SalesCategorySalesClientWorkflowState`. Options: "Pre-Engagement," "Prospecting," "Active Sales," "Active Client," "Nurturing," "Closed". |
| Sales/IsFinal               | Checkbox       | Is this a terminal state for a typical flow?                                                     | Boolean. Default: false                                                                                                                               |
| Sales/DefaultNextState      | Relation (CWS) | Optional. Can help guide users or automate transitions. (Many-to-One with `ClientWorkflowState`) |                                                                                                                                                       |
| Sales/DefaultPreviousStates | Relation (CWS) | Represents states for which this state is the default next state (One-to-Many, auto-generated).  |                                                                                                                                                       |
| Sales/DescriptionPurpose    | Rich Text      | Details about this state. To clarify the meaning and criteria for each state.                    | (SDL: description: RichField)                                                                                                                         |
| Sales/Companies             | Relation (CLI) | Companies currently in this workflow state (One-to-Many with `Company (CLI)`)                    | *Note: This represents the companies currently in this workflow state.*                                                                               |
| Created At                  | DateTime       | Auto                                                                                             | `createdAt`                                                                                                                                           |
| Updated At                  | DateTime       | Auto                                                                                             | `updatedAt`                                                                                                                                           |

*Default/Queried Entities (This is the complete list of states to be created/updated based on the Work Order):*
  - **Pre-Engagement Category:**
    - SpecificStateName: "Identified Target", StateCategory: "Pre-Engagement", IsFinal: false
  - **Prospecting Category:**
    - SpecificStateName: "New Lead (Raw)", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Enriching", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Lead - Verified", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Contacted (Delivery Confirmed)", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Contact Failed (Delivery Issue)", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Inbound Lead - Auto Qualified", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Inbound Lead - Pending Qualification Review", StateCategory: "Prospecting", IsFinal: false
    - SpecificStateName: "Qualified", StateCategory: "Prospecting", IsFinal: false
  - **Active Sales Category:**
    - SpecificStateName: "Demo Scheduled", StateCategory: "Active Sales", IsFinal: false
    - SpecificStateName: "Demo No Show", StateCategory: "Active Sales", IsFinal: false
    - SpecificStateName: "Tier Selection & Agreement", StateCategory: "Active Sales", IsFinal: false
    - SpecificStateName: "Proposal - Custom/Automation", StateCategory: "Active Sales", IsFinal: false
    - SpecificStateName: "Contract - Custom/Automation", StateCategory: "Active Sales", IsFinal: false
  - **Nurturing Category:**
    - SpecificStateName: "Nurturing - Awaiting Response (Initial Outreach)", StateCategory: "Nurturing", IsFinal: false
    - SpecificStateName: "Nurturing - Qualified Gone Cold (Pre-Demo)", StateCategory: "Nurturing", IsFinal: false
    - SpecificStateName: "Nurturing - Post Demo Follow-up", StateCategory: "Nurturing", IsFinal: false
    - SpecificStateName: "Nurturing - Stalled Tier Selection", StateCategory: "Nurturing", IsFinal: false
    - SpecificStateName: "Nurturing - Stalled Proposal (Custom/Automation)", StateCategory: "Nurturing", IsFinal: false
    - SpecificStateName: "Nurturing - Long Term (Lost Deal)", StateCategory: "Nurturing", IsFinal: false
    - SpecificStateName: "Nurturing - Churned Client Re-engagement", StateCategory: "Nurturing", IsFinal: false
  - **Active Client Category:**
    - SpecificStateName: "Onboarding", StateCategory: "Active Client", IsFinal: false
    - SpecificStateName: "First Impact", StateCategory: "Active Client", IsFinal: false
    - SpecificStateName: "Managing", StateCategory: "Active Client", IsFinal: false
    - SpecificStateName: "Max Impact", StateCategory: "Active Client", IsFinal: false
  - **Closed Category:**
    - SpecificStateName: "Enrichment Failed - Unusable", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Unreachable", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Unresponsive (Initial Outreach)", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Not Interested (Initial Contact)", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Not Qualified", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Closed Lost - Post Demo", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Closed Lost - Proposal Rejected (Custom/Automation)", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Closed Lost - Contract Stage (Custom/Automation)", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Do Not Contact", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Churned", StateCategory: "Closed", IsFinal: true
    - SpecificStateName: "Churned - DNC", StateCategory: "Closed", IsFinal: true

---

#### 2.7  Company (CLI)
*Description:* Represents client companies or potential leads. (Formerly Client (CLI))

| Field                         | Type               | Description                                                                     | Options / Formula                                                                                                                                                                                                                          |
| ----------------------------- | ------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| fibery/id                     | ID                 | Read-only, System Generated                                                     |                                                                                                                                                                                                                                            |
| fibery/public-id              | Text               | Read-only, System Generated                                                     |                                                                                                                                                                                                                                            |
| fibery/creation-date          | Date               | Read-only, System Generated                                                     |                                                                                                                                                                                                                                            |
| fibery/modification-date      | Date               | Read-only, System Generated                                                     |                                                                                                                                                                                                                                            |
| fibery/rank                   | Number             | Read-only, System Generated                                                     |                                                                                                                                                                                                                                            |
| fibery/created-by             | User               | Relation to `fibery/User`, System Generated                                     |                                                                                                                                                                                                                                            |
| Sales/Name                    | Text               | Company Name                                                                    |                                                                                                                                                                                                                                            |
| Sales/Description             | Rich Text          | Detailed notes about the company                                                |                                                                                                                                                                                                                                            |
| Sales/Short description       | Text               | Brief overview of the company                                                   |                                                                                                                                                                                                                                            |
| Sales/Industry                | Text               | Sector                                                                          | Fibery type: String                                                                                                                                                                                                                        |
| Sales/Website                 | URL                | Main domain                                                                     | Fibery type: String                                                                                                                                                                                                                        |
| Sales/Employees               | Number             | Number of employees                                                             | Fibery type: Integer or Decimal/Float                                                                                                                                                                                                      |
| Sales/ARR                     | Number             | Annual Recurring Revenue                                                        | Fibery type: Integer or Decimal/Float                                                                                                                                                                                                      |
| Sales/Source                  | Text               | Lead Source                                                                     | Fibery type: String                                                                                                                                                                                                                        |
| Sales/Segment                 | Relation (CLS)     | Client segmentation category (Many-to-One with `ClientSegment (CLS)`)           |                                                                                                                                                                                                                                            |
| Sales/WorkflowState           | Relation (CWS)     | Granular company lifecycle state (Many-to-One with `ClientWorkflowState (CWS)`) | Salespeople select the `Sales/Name` (SpecificStateName) via this relation.                                                                                                                                                                 |
| Sales/Status                  | Single-Select      | CRM stage                                                                       | Related to `SalesStatusSalesCompany`, options TBD. Formerly `Status` with options: Prospect; Active; Past                                                                                                                                  |
| Sales/Tier                    | Single-Select      | Account category                                                                | Related to `SalesTierSalesCompany`, options TBD. Formerly `Tier` with options: A; B; C                                                                                                                                                     |
| Sales/Deals                   | Relation (DLR)     | Pipeline opportunities (One-to-Many with `Deal (DLR)`)                          |                                                                                                                                                                                                                                            |
| Sales/Projects                | Relation (PRJ)     | Associated projects (One-to-Many with `Ship/Project`)                           |                                                                                                                                                                                                                                            |
| Sales/Contact Name            | Text               | Primary stakeholder                                                             |                                                                                                                                                                                                                                            |
| Sales/Email                   | Email              | Main email                                                                      | Fibery type: String                                                                                                                                                                                                                        |
| Sales/Contact Phone           | Phone              | Contact number                                                                  | Fibery type: String                                                                                                                                                                                                                        |
| Sales/Address                 | Text               | Physical or main address                                                        | Fibery type: String                                                                                                                                                                                                                        |
| Sales/LastOutreachMethod      | Single-Select      | Method of last outreach                                                         | Related to `SalesLastOutreachMethodSalesCompany`. Options: "Cold Email," "Cold Call," "Social DM - LinkedIn," "Social DM - Twitter," "Social DM - Facebook," "Social DM - Instagram," "Other DM," "Referral," "Inbound Web Form," "Event." |
| Sales/Sales person            | Relation (User)    | Primary sales contact (Many-to-Many with `fibery/User`)                         | Default: Founder                                                                                                                                                                                                                           |
| Sales/ClientSegments          | Relation (CLS)     | Auto-generated back-relation (Many-to-Many with `ClientSegment (CLS)`)          |                                                                                                                                                                                                                                            |
| Sales/ClientWorkflowStates    | Relation (CWS)     | Auto-generated back-relation (Many-to-Many with `ClientWorkflowState (CWS)`)    |                                                                                                                                                                                                                                            |
| Sales/Interactions            | Relation (INT)     | Linked interactions for this company (One-to-Many with `Interaction (INT)`)     | Back-relation                                                                                                                                                                                                                              |
| Sales/LastInteractionDate     | Formula (DateTime) | Date of the most recent interaction related to this company.                    | Formula: `max(Interactions.Sales/InteractionDateTime)`                                                                                                                                                                                     |
| Sales/LastInteractionType     | Formula (Text)     | Category of the most recent interaction for this company.                       | Formula to get `Sales/Category` of the latest interaction.                                                                                                                                                                                 |
| Sales/LastInteractionModality | Formula (Text)     | Modality of the most recent interaction for this company.                       | Formula to get `Sales/Modality` of the latest interaction.                                                                                                                                                                                 |
| Sales/TotalInteractions       | Formula (Number)   | Total count of interactions linked to this company.                             | Formula: `count(Interactions)`                                                                                                                                                                                                             |
| Created At                    | DateTime           | Auto                                                                            | `createdAt`                                                                                                                                                                                                                                |
| Updated At                    | DateTime           | Auto                                                                            | `updatedAt`                                                                                                                                                                                                                                |

*Default/Queried Entities:* (None explicitly queried for this type in the current context, beyond those created for deals)

---

#### 2.8  DealType (DTY)

*Description:* Defines distinct types of deals to manage different sales processes.

| Field                    | Type   | Description                 | Options / Formula                            |
| ------------------------ | ------ | --------------------------- | -------------------------------------------- |
| fibery/id                | ID     | Read-only, System Generated |                                              |
| fibery/public-id         | Text   | Read-only, System Generated |                                              |
| fibery/creation-date     | Date   | Read-only, System Generated |                                              |
| fibery/modification-date | Date   | Read-only, System Generated |                                              |
| fibery/rank              | Number | Read-only, System Generated |                                              |
| Sales/Name               | Text   | Name of the deal type       | e.g., "New Client Acquisition (Productized)" |

*Default/Queried Entities (Examples based on Work Order):*
  - Name: "New Client Acquisition (Productized)"
  - Name: "New Client Acquisition (Custom/Enterprise)"
  - Name: "Upsell/Cross-Sell (Existing Client)"

---

#### 2.9  Deal (DLR)

*Description:* Represents sales opportunities.

| Field                       | Type               | Description                                                                                                       | Options / Formula                                                                                                                                                                                                               |
| --------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fibery/id                   | ID                 | Read-only, System Generated                                                                                       |                                                                                                                                                                                                                                 |
| fibery/public-id            | Text               | Read-only, System Generated                                                                                       |                                                                                                                                                                                                                                 |
| fibery/creation-date        | Date               | System field, likely read-only                                                                                    | `createdAt`                                                                                                                                                                                                                     |
| fibery/modification-date    | Date               | System field, likely read-only                                                                                    | `updatedAt`                                                                                                                                                                                                                     |
| fibery/rank                 | Number             | Read-only, System Generated                                                                                       |                                                                                                                                                                                                                                 |
| Sales/Name                  | Text               | Deal Name/title                                                                                                   |                                                                                                                                                                                                                                 |
| Sales/Client                | Relation (CLI)     | Linked client/company (Many-to-One with `Company (CLI)`)                                                          | Primary company for the deal. Required.                                                                                                                                                                                         |
| Sales/DealTypeRelation      | Relation (DTY)     | Specifies the type of deal (Many-to-One with `DealType (DTY)`)                                                    | (SDL: dealTypeRelation: SalesDealType)                                                                                                                                                                                          |
| Sales/Amount                | Number             | Potential revenue (Currency)                                                                                      | Default currency USD. (SDL: amount: Float)                                                                                                                                                                                      |
| Sales/Probability %         | Number             | Forecast accuracy (Percent, 0-100)                                                                                | (SDL: probability: Int)                                                                                                                                                                                                         |
| Sales/Stage                 | Single-Select      | Sales process stage                                                                                               | Related to `SalesStageSalesDeal`, e.g., Proposal, Contract. Options TBD. (Formerly `Stage` with options: Qualification; Proposal; Negotiation; Closed‑Won; Closed‑Lost). Review if covered by `Sales/WorkflowState` on Company. |
| Sales/Close Date            | Date               | Expected closing date                                                                                             | Optional. (SDL: closeDate: String)                                                                                                                                                                                              |
| Sales/Owner                 | Users              | Sales rep (Relation Many-to-Many with `fibery/User`)                                                              | Default: Founder                                                                                                                                                                                                                |
| Sales/Notes                 | Rich Text          | General notes and context for the deal. Detailed interaction history should be logged in the 'Interactions' type. | (SDL: notes: RichField)                                                                                                                                                                                                         |
| Sales/Next Action           | Text               | Next step                                                                                                         | (SDL: nextAction: String)                                                                                                                                                                                                       |
| Sales/Interactions          | Relation (INT)     | Linked interactions for this deal (One-to-Many with `Interaction (INT)`)                                          | Back-relation                                                                                                                                                                                                                   |
| Sales/LastInteractionDate   | Formula (DateTime) | Date of the most recent interaction related to this deal.                                                         | Formula: `max(Interactions.Sales/InteractionDateTime)`                                                                                                                                                                          |
| Sales/LastInteractionType   | Formula (Text)     | Category of the most recent interaction for this deal.                                                            | Formula to get `Sales/Category` of the latest interaction.                                                                                                                                                                      |
| Sales/TotalDealInteractions | Formula (Number)   | Total count of interactions linked to this deal.                                                                  | Formula: `count(Interactions)`                                                                                                                                                                                                  |
*Note: `Sales/WorkflowState` was previously documented for `Sales/Deal` but is not present in the current Fibery SDL for this type.*

*Default/Queried Entities:* (The four deals created previously would be listed here if we re-queried them, e.g., "Enterprise Website Redesign", "SMB E-commerce Integration", etc.)

---

#### 2.9.1 Interaction (INT)
*Description:* Represents a specific engagement or touchpoint with a Company, such as an email, call, meeting, or automated communication. Used for tracking communication history, engagement levels, and informing sales/support strategies.

| Field                     | Type                   | Description                                                                                                  | Options / Formula / Notes                                                                                                                                   |
| ------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fibery/id                 | ID                     | Read-only, System Generated                                                                                  |                                                                                                                                                             |
| fibery/public-id          | Text                   | Read-only, System Generated                                                                                  |                                                                                                                                                             |
| fibery/creation-date      | DateTime               | Read-only, System Generated                                                                                  | `createdAt`                                                                                                                                                 |
| fibery/modification-date  | DateTime               | Read-only, System Generated                                                                                  | `updatedAt`                                                                                                                                                 |
| Sales/Name                | Text                   | Concise summary or title of the interaction (e.g., "Follow-up call re: proposal", "Introductory Email Sent") | Potentially auto-generated based on other fields, or manually entered. Enforce schema for consistency if auto-generated. E.g., "[Subtype] - [Company Name]" |
| Sales/Company             | Relation (CLI)         | The company involved in this interaction.                                                                    | Many-to-One with `Company (CLI)`. Required.                                                                                                                 |
| Sales/Deal                | Relation (DLR)         | The specific deal this interaction relates to, if applicable.                                                | Many-to-One with `Deal (DLR)`. Optional.                                                                                                                    |
| Sales/InteractionDateTime | DateTime               | Date and time the interaction occurred or was logged.                                                        | Required.                                                                                                                                                   |
| Sales/Category            | Enum                   | High-level classification of the interaction.                                                                | Options: Email; Call; Meeting; Message; Automated; Other. (Strict Schema)                                                                                   |
| Sales/Subtype             | Text                   | Granular, specific type of interaction, providing more context to the Category.                              | E.g., For "Email" Category: "Initial Outreach", "Follow-up", "Support Response". For "Call" Category: "Discovery", "Demo", "Support". (Strict Schema)       |
| Sales/Direction           | Enum                   | Indicates if the interaction was inbound or outbound.                                                        | Options: Inbound; Outbound. (Strict Schema)                                                                                                                 |
| Sales/Modality            | Enum                   | The primary functional area this interaction pertains to.                                                    | Options: Sales; Support; Strategy; Systems. (Strict Schema)                                                                                                 |
| Sales/User                | Relation (fibery/User) | The Gruntworks user who primarily handled or logged this interaction.                                        | Many-to-One with `fibery/User`. Default: current user or automation principal.                                                                              |
| Sales/ExternalContactName | Text                   | Name of the external person involved in the interaction, if applicable.                                      | Optional.                                                                                                                                                   |
| Sales/Content             | Rich Text              | Detailed notes, summary, transcript, or body of the interaction (e.g., email body, call notes).              | Optional.                                                                                                                                                   |
| Sales/Sentiment           | Enum                   | Automated or manually assessed sentiment of the interaction.                                                 | Options: Positive; Negative; Neutral; N/A. *(Future Feature: To be populated by automation)*                                                                |
| Sales/SentimentScore      | Number                 | Numerical score for sentiment (e.g., -1 to 1).                                                               | Optional. *(Future Feature: To be populated by automation)*                                                                                                 |
| Sales/SourceSystem        | Text                   | System that originated or logged the interaction, if automated.                                              | E.g., "Gmail Plugin", "Sales Dialer XYZ", "n8n Workflow". Optional.                                                                                         |
| Created At                | DateTime               | Auto timestamp                                                                                               | `createdAt` (Redundant with fibery/creation-date but kept for consistency if other types use it)                                                            |
| Updated At                | DateTime               | Auto timestamp                                                                                               | `updatedAt` (Redundant with fibery/modification-date but kept for consistency if other types use it)                                                        |

*Notes on "Strict Schema" for Enum/Text fields:* Fields marked with '(Strict Schema)' for Options/Notes imply that while they might be Enums or Text, their values should adhere to a predefined, documented set to ensure consistency for reporting and automation, even if not strictly enforced by Fibery's most restrictive field type.

*Example of Compiled/Concatenated for understanding (not a field):* For clarity, the combination of fields could describe an interaction like: 'Subtype: Support Ticket Update, Direction: Inbound, Modality: Support, Category: Email, Company: Acme Corp, DateTime: 2025-05-23 13:45'.

---

### Space: Ship

#### 2.10 Project (PRJ)

| Field          | Type            | Description                      | Options / Formula                                     |
| -------------- | --------------- | -------------------------------- | ----------------------------------------------------- |
| Name           | Text            | Project name                     | n/a                                                   |
| Project Type   | Enum            | Service vertical                 | Seedworks; Siteworks; Flowworks; Internal‑Ops         |
| Client         | Relation (CLI)  | Linked Client                    | optional                                              |
| Rock           | Relation (RCK)  | Linked Rock                      | optional                                              |
| Decomp Method  | Enum            | Decomposition approach           | Manual; RIPER‑5; Taskmaster                           |
| Complexity     | Enum            | Size estimate                    | Low; Medium; High                                     |
| Workflow State | Relation (PWS)  | Granular project lifecycle state | optional                                              |
| Duration       | DateRange       | Project start and end dates      | optional                                              |
| Total Effort   | Number          | Sum of task estimates            | optional, likely calculated                           |
| Description    | Rich text       | Detailed project overview        | optional                                              |
| Assignees      | Relation (User) | Users assigned to project        | optional, many-to-many                                |
| Tasks          | Relation (TSK)  | Child Tasks                      | n‑to‑many                                             |
| Progress %     | Formula         | Avg of child Task progress       | `if(count(Tasks)=0,0,round(avg(Tasks.Progress %),1))` |
| Files          | Relation (File) | Attached project files           | optional, many-to-many                                |
| Created At     | DateTime        | Auto                             | `createdAt`                                           |
| Updated At     | DateTime        | Auto                             | `updatedAt`                                           |

---

#### 2.11 Project Workflow State (PWS) - Placeholder

| Field       | Type      | Description                 | Options / Formula |
| ----------- | --------- | --------------------------- | ----------------- |
| Name        | Text      | Name of the workflow state  | n/a               |
| Description | Rich text | Details about this state    | n/a               |
| Is Final    | Boolean   | Is this a terminal state?   | Default: false    |
| Category    | Text      | Broad category of the state | optional          |
| Created At  | DateTime  | Auto                        | `createdAt`       |
| Updated At  | DateTime  | Auto                        | `updatedAt`       |

---

#### 2.12 SOP Link (SOP)

| Field      | Type           | Description               | Options / Formula                           |
| ---------- | -------------- | ------------------------- | ------------------------------------------- |
| Title      | Text           | SOP title                 | n/a                                         |
| Doc URL    | URL            | Link to MkDocs/GitHub doc | n/a                                         |
| Keywords   | Multi-text     | Search tags               | n/a                                         |
| Vertical   | Enum           | Service vertical          | Seedworks; Siteworks; Flowworks; Operations |
| Tasks      | Relation (TSK) | Linked Tasks              | many-to-many                                |
| Created At | DateTime       | Auto                      | `createdAt`                                 |
| Updated At | DateTime       | Auto                      | `updatedAt`                                 |

---

#### 2.13 Retrospective (RET)

| Field              | Type           | Description                                                 | Options / Formula                                       |
| ------------------ | -------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| Name               | Text           | Title of the Retrospective (e.g., "Q2 Project Alpha Retro") | n/a                                                     |
| Date               | Date           | Date the retrospective was held                             | n/a                                                     |
| Participants       | MultiUser      | Individuals who participated in the retrospective           | n/a                                                     |
| Project            | Relation (PRJ) | Linked Project (if applicable)                              | optional                                                |
| Rock               | Relation (RCK) | Linked Rock (if applicable)                                 | optional                                                |
| What Went Well     | Rich text      | Summary of successes and positives                          | n/a                                                     |
| What Could Improve | Rich text      | Summary of challenges and areas for improvement             | n/a                                                     |
| Action Items       | Rich text      | Specific actions to be taken based on learnings             | (Consider linking to created TSK entities for tracking) |
| Learnings          | Rich text      | Key insights and takeaways                                  | n/a                                                     |
| Created At         | DateTime       | Auto timestamp                                              | `createdAt`                                             |
| Updated At         | DateTime       | Auto timestamp                                              | `updatedAt`                                             |

---

### Space: Systems

#### 2.14 Task (TSK)

| Field            | Type               | Description                                                                                                        | Options / Formula                                     |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| Name             | Text               | Task summary (formerly Title)                                                                                      | n/a                                                   |
| Description      | Rich text          | Detailed context                                                                                                   | n/a                                                   |
| Project          | Relation (PRJ)     | Parent Project                                                                                                     | required                                              |
| Rock             | Relation (RCK)     | Parent Rock, dynamically looked up from the linked Project.                                                        | Lookup: Project.Rock                                  |
| Owner            | User               | Primary assignee                                                                                                   | default: Founder                                      |
| Assignees        | Relation (User)    | Additional users assigned                                                                                          | optional, many-to-many                                |
| Mode             | Enum               | 2S‑3S mode                                                                                                         | Sell; Ship; Strategy; Systems; Support                |
| Priority         | Relation (PRI)     | Urgency level (Points to Task Priority Type)                                                                       | optional, Link to PRI type                            |
| Estimate (Hours) | Number (decimal)   | Planned effort (formerly Estimate hrs)                                                                             | n/a                                                   |
| Hours Spent      | Formula            | Sum of Time Logs duration (formerly Time Tracked)                                                                  | `sum(Time Logs.\`Time Spent\`)`                       |
| Workflow State   | Relation (TWS)     | Granular task lifecycle state (formerly Status)                                                                    | optional, Link to TWS type                            |
| Decomp Method    | Enum               | From Project or override                                                                                           | Manual; RIPER‑5; Taskmaster                           |
| Start Date       | Date               | When work begins                                                                                                   | optional                                              |
| Due Date         | Date               | Deadline                                                                                                           | optional                                              |
| Done Date        | Date               | Date task was completed                                                                                            | optional                                              |
| Progress %       | Formula            | State indicator. Note: Blocked tasks should retain their last known progress; this formula reflects active states. | `if(Status='Done',100,if(Status='In Progress',50,0))` |
| SOP Links        | Relation (SOP)     | Relevant SOPs                                                                                                      | many‑to‑many                                          |
| Inbox Record     | Relation (EIN/IIN) | Source inbox entry                                                                                                 | optional                                              |
| Time Logs        | Relation (TM)      | Linked time entries                                                                                                | optional, one-to-many                                 |
| Files            | Relation (File)    | Attached task files                                                                                                | optional, many-to-many                                |
| Comments         | Relation (CMT)     | Linked comments                                                                                                    | optional, one-to-many                                 |
| Created At       | DateTime           | Auto                                                                                                               | `createdAt`                                           |
| Updated At       | DateTime           | Auto                                                                                                               | `updatedAt`                                           |

---

#### 2.15 Task Workflow State (TWS) - Placeholder

| Field       | Type      | Description                 | Options / Formula |
| ----------- | --------- | --------------------------- | ----------------- |
| Name        | Text      | Name of the workflow state  | n/a               |
| Description | Rich text | Details about this state    | n/a               |
| Is Final    | Boolean   | Is this a terminal state?   | Default: false    |
| Category    | Text      | Broad category of the state | optional          |
| Created At  | DateTime  | Auto                        | `createdAt`       |
| Updated At  | DateTime  | Auto                        | `updatedAt`       |

---

#### 2.15 Task Priority (PRI) - Placeholder

| Field      | Type     | Description                | Options / Formula                 |
| ---------- | -------- | -------------------------- | --------------------------------- |
| Name       | Text     | Name of the priority level | e.g., Low, Normal, High, Critical |
| Icon       | Text     | Visual identifier          | optional                          |
| Created At | DateTime | Auto                       | `createdAt`                       |
| Updated At | DateTime | Auto                       | `updatedAt`                       |

---

#### 2.16 External Inbox (EIN) *and* Internal Inbox (IIN)

Note: These are two distinct Fibery Types that share an identical field structure. The primary rationale for separation is to reduce potential log fatigue or separate processing queues. An alternative approach could be a single "Inbox" Type with a 'Type' field (e.g., External/Internal) for consolidated reporting and views.

| Field        | Type           | Description                                                                                                                                                                | Options / Formula                                     |
| ------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Source       | Enum           | Origin                                                                                                                                                                     | Email; Slack; API                                     |
| Received At  | DateTime       | Timestamp                                                                                                                                                                  | `createdAt`                                           |
| Raw Text     | Rich text      | Full message                                                                                                                                                               | n/a                                                   |
| Labels       | Multi-select   | AI classification (e.g., Type, Urgency). This is typically performed by an external n8n workflow (triggered by WebhookTriageToken) integrated with a 3rd party AI service. | e.g. Type: Bug/Idea/Request; Urgency: Low/Normal/High |
| Processed    | Checkbox       | Triage completed                                                                                                                                                           | default: False                                        |
| Created Task | Relation (TSK) | Linked Task                                                                                                                                                                | optional                                              |
| Created At   | DateTime       | Auto                                                                                                                                                                       | `createdAt`                                           |
| Updated At   | DateTime       | Auto                                                                                                                                                                       | `updatedAt`                                           |

---

#### 2.17 Scorecard (SCB)

| Field      | Type     | Description                                                | Options / Formula                                                            |
| ---------- | -------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Week_Start | Date     | The start date of the week the scorecard entry pertains to | e.g. "YYYY-MM-DD"                                                            |
| KPI Name   | Text     | Metric name                                                | e.g. Sell hrs %; Ship cycle time                                             |
| Value      | Number   | Measured value                                             | n/a                                                                          |
| Target     | Number   | Goal value                                                 | n/a                                                                          |
| Owner      | User     | Person responsible for the KPI                             | Default: Founder                                                             |
| Color      | Formula  | Health indicator based on Value vs Target                  | `if(Value >= Target, 'Green', if(Value >= (Target * 0.8), 'Yellow', 'Red'))` |
| Created At | DateTime | Auto                                                       | `createdAt`                                                                  |
| Updated At | DateTime | Auto                                                       | `updatedAt`                                                                  |

---

#### 2.18 Time Log (TM)

| Field          | Type            | Description                  | Options / Formula                            |
| -------------- | --------------- | ---------------------------- | -------------------------------------------- |
| Name           | Text            | Name/description of time log | optional                                     |
| Task           | Relation (TSK)  | Parent Task                  | required                                     |
| Project        | Relation (PRJ)  | Parent Project (from Task)   | Lookup: Task.Project                         |
| User           | Relation (User) | User who logged the time     | required                                     |
| Date           | Date            | Date the time was logged for | required                                     |
| Start          | DateTime        | Start timestamp              | from Toggl                                   |
| Stop           | DateTime        | Stop timestamp               | from Toggl                                   |
| Time Spent     | Formula         | Hours (formerly Duration)    | `round(dateDiff(Stop,Start,'minutes')/60,2)` |
| Notes (if any) | Text            | Additional notes for the log | optional                                     |
| Toggl Entry ID | Text            | External reference           | n/a                                          |
| Created At     | DateTime        | Auto                         | `createdAt`                                  |
| Updated At     | DateTime        | Auto                         | `updatedAt`                                  |

---

#### 2.19 Config (CFG)

| Field       | Type     | Description                | Options / Formula                               |
| ----------- | -------- | -------------------------- | ----------------------------------------------- |
| Key         | Text     | Config identifier          | e.g. WIP\_CAP; SELL\_RATIO\_MIN; Webhook tokens |
| Value       | Text     | Config value               | numeric or URL/text                             |
| Description | Text     | Human-readable explanation | n/a                                             |
| Created At  | DateTime | Auto                       | `createdAt`                                     |
| Updated At  | DateTime | Auto                       | `updatedAt`                                     |

---

#### 2.20 Comment (CMT) - Placeholder

| Field         | Type            | Description               | Options / Formula |
| ------------- | --------------- | ------------------------- | ----------------- |
| Author        | Relation (User) | User who made the comment | required          |
| Content       | Rich text       | The comment text          | required          |
| Parent Entity | Relation (*/*)  | Entity being commented on | required          |
| Created At    | DateTime        | Auto                      | `createdAt`       |
| Updated At    | DateTime        | Auto                      | `updatedAt`       |

---

#### 2.21 File (File) - Placeholder

| Field         | Type           | Description                   | Options / Formula |
| ------------- | -------------- | ----------------------------- | ----------------- |
| Name          | Text           | Name of the file              | required          |
| File Size     | Number         | Size in bytes                 | calculated        |
| Mime Type     | Text           | Type of file                  | calculated        |
| URL/Secret    | Text           | Link or identifier for access | calculated        |
| Parent Entity | Relation (*/*) | Entity file is attached to    | required          |
| Created At    | DateTime       | Auto                          | `createdAt`       |
| Updated At    | DateTime       | Auto                          | `updatedAt`       |

---

### Space: Support

#### 2.22 Issue (ISC)

| Field       | Type           | Description                                         | Options / Formula                      |
| ----------- | -------------- | --------------------------------------------------- | -------------------------------------- |
| Rock        | Relation (RCK) | Associated Rock                                     | optional                               |
| Description | Rich text      | Issue details                                       | n/a                                    |
| Category    | Enum           | Classification of the issue                         | Sell; Ship; Strategy; Systems; Support |
| Severity    | Enum           | Impact level                                        | Low; Medium; High                      |
| Owner       | User           | Person responsible for resolving the issue          | Default: Founder                       |
| Next_Step   | Text           | Immediate next action required to address the issue | n/a                                    |
| Root_Cause  | Rich text      | Analysis of the underlying cause of the issue       | n/a                                    |
| Status      | Enum           | Lifecycle state                                     | Open; Closed                           |
| Created At  | DateTime       | Auto                                                | `createdAt`                            |
| Resolved At | DateTime       | On closing                                          | auto-populated when Status=Closed      |

---

## 3  Fibery Buttons

...  Fibery Buttons

| Button       | Entity  | Action                              | Config Key         |
| ------------ | ------- | ----------------------------------- | ------------------ |
| Start Focus  | Task    | POST to webhook (from Config Key)   | WebhookStartToken  |
| Stop Focus   | Task    | POST to webhook                     | WebhookStopToken   |
| Decompose    | Project | POST Project ID & Method to webhook | WebhookDecompToken |
| Retry Triage | Inbox   | POST Inbox ID to webhook            | WebhookTriageToken |

---

## 4  Fibery Automations

### 4.1  Scorecard Color Alert
**Trigger**: `Scorecard.Color` field changes (or is set) to `Red` or `Yellow`.
**Action**: Send Slack notification to `#ops-alerts` (or a channel defined in Config entity).

### 4.2  Auto-Create Task from Issue
**Trigger**: New `Issue` entity is created.
**Action**: Automatically generate a `Task`. Task `Title` set to "Follow up on Issue: [Issue.Name/ID]". Task `Description` pre-filled with `Issue.Next_Step`. Link Task to the source `Issue`. Assign to `Issue.Owner` if set, otherwise Founder.

### 4.3  Auto-Inherit on Task
**On create:**
  • `Task.DecompMethod` is copied from the parent `Project.DecompMethod`.
  • `Task.Mode` should be set based on other logic (e.g. a default value, or inferred from `Project.Type`, or manually set) as the `Project` entity does not have a directly mappable `Mode` field.
  (Note: `Task.Rock` is a direct lookup from `Project.Rock` as per field definition in 2.6).

### 4.4  WIP Guard

**Trigger:** Task.Status → In Progress; **Condition:** owner has >3 In Progress; **Action:** revert status & Slack DM.

### 4.5  Priority Due Alert

**Hourly scheduled:** send Slack DM for High Priority tasks due ≤24h.

### 4.6  Rock Issue Spawn

**Daily scheduled:** for Rocks past Due & not Done, create Issue.

### 4.7  Time Log Data Flow
`Time Log` (TM) entities are created/updated in Fibery by an external automation (e.g., n8n workflow A3 in OPS-Systems-Overview.md) triggered by Toggl events (via Start/Stop Focus webhooks). The `Task.Time Tracked` field is a formula field in Fibery that automatically sums the `Duration` from these `Time Log` records. Therefore, a separate Fibery automation rule to 'update Task.Time Tracked sum' is not required.

---

## 5  Views & Dashboards

1. **Task Kanban** (Tasks by Status, swimlanes by Mode).
2. **Daily Focus** (Tasks Ready/In Progress sorted by Priority).
3. **Sell vs Ship Chart** (Weekly hours by Mode).
4. **Key Results Table** (Key Results table, filterable by current year, grouped by Primary_S and Support_S).
5. **Rocks Progress Board** (Rocks Kanban, grouped by Status: Proposed; Active; Blocked; Done).
6. **OKR Board** (Objectives → KRs → Rocks progress).
7. **Capacity Planner** (Task estimates vs tracked by Week).
8. **Inbox Manager** (Inbox unprocessed).
9. **Issue Log** (Open issues by Severity).
10. **Weekly Scorecard Dashboard** (Visual summary of Scorecard entities, showing KPI Name, Value, Target, and Color).
11. **Company Interaction Log** (Table view of Interactions, filterable by Company, showing Date, Category, Subtype, Modality, User, and a snippet of Content).

---

## 6  Seed Data & Setup Steps

1. **Config** rows:

   * `WIP_CAP`: 3
   * `SELL_RATIO_MIN`: 60
   * `SHIP_RATIO_MIN`: 30
   * `WebhookStartToken`, `WebhookStopToken`, `WebhookDecompToken`, `WebhookTriageToken` (values to be set)
2. Define Enums exactly as listed.
3. Create sample Q2 Objectives, KRs, Rocks.
4. Create top‑10 SOP Link records.
5. Invite Bot user with API token.
6. Define standard values and schemas for `Interaction.Category`, `Interaction.Subtype`, `Interaction.Direction`, and `Interaction.Modality` enums/fields.

---

## 7  Acceptance Criteria

1. Entities & fields exactly match spec; no missing fields or relations.
2. Buttons visible and bound to Config keys.
3. Automations fire correctly in test scenarios.
4. Views display sample data accurately.
5. Config data present and secured to Owner.
6. The `Interaction` type and its fields are implemented as specified.
7. Roll-up fields on `Company` and `Deal` (e.g., `LastInteractionDate`) correctly calculate values based on linked `Interaction` records.
8. Fields intended for future automation (e.g., `Sentiment`) are present but understood to not be functional initially.

---

## UI/UX Considerations (New Section)

*   **Manual Interaction Logging:** Consider enabling manual logging of `Interactions` directly from `Company` and `Deal` entity views for quick ad-hoc entries. While most interactions are expected to be logged via automation from external sources (e.g., email sync, call logging tools), manual entry should be supported.
*   **Interaction Templates:** Future enhancements could include 'Interaction Templates' selectable within Fibery to pre-fill common interaction types and content, potentially triggered via a button on the `Company` or `Deal` entity.

