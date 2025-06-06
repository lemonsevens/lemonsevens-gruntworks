# Gruntworks Operating System – Comprehensive Operational Guide v1.0

> *A practical, clock‑level guide to how 2S‑3S, OKRs and automation drive every hour, day, week, quarter and year at Gruntworks.*

---

## 1. Introduction & Core Purpose

This document serves as the single‑source specification for Gruntworks' end‑to‑end Operating System (OS). It outlines how the 2S‑3S methodology, OKR/Rock execution, AI‑assisted automation, and knowledge operations are combined into a scalable, low‑maintenance platform.

**Core Goals:**

*   **Uniﬁed Work Hub:** A central Airtable Base housing Objectives → Key Results → Rocks → Tasks, with connected CRM, Issues, and knowledge links, visually segmented using Airtable Interfaces.
*   **Automated Flow:** n8n workflows for daily/weekly digests, intake triage, focus timers, WIP enforcement, and capacity reports interacting with the Airtable Base.
*   **AI Augmentation:** A suite of AI agents including Taskmaster (large internal projects), RIPER‑5 (small projects), Triage Agent, Next‑Action Agent, and Focus Buddy to enhance productivity and decision-making, all interacting with data in Airtable.
*   **Knowledge Ops:** GitHub/MkDocs as the canonical SOP repository, with semantic search capabilities and links back to tasks in Airtable.
*   **Low Cognitive Load:** Minimized manual status updates and cognitive overhead through Slack DMs for internal prompts and priority alerts.

### 1.1 Time‑Budget North Star

| Mode                                         | Target % of Founder Hours | Why                                                 |
| -------------------------------------------- | ------------------------- | --------------------------------------------------- |
| **Sell** (new revenue)                       | **60 %**                  | Pipeline is oxygen; keep top of funnel full.        |
| **Ship** (client value)                      | **30 %**                  | Deliver promises quickly, maintain quality.         |
| **Strategy / Systems / Support** (the "3 S") | **10 %**                  | Keep compass true, processes sharp, engine healthy. |

Hours tracked in Toggl per Task roll up to these modes; weekly scorecard flags drift.

### 1.2 Core Operational Philosophy and Terminology

The Gruntworks Operating System is built upon the "2S-3S" framework, which emphasizes two primary modes of operation supported by three key pillars. This structure ensures that all activities are aligned with core business objectives.

*   **Primary Modes**:
    *   **Sell**: Encompasses all revenue-generating activities, including marketing, sales, and customer acquisition. The primary goal is to keep the top of the funnel full and drive new business.
    *   **Ship**: Includes all fulfillment, delivery, and production activities. This mode focuses on delivering on promises to clients quickly and maintaining high quality.

*   **Supporting Pillars**:
    *   **Strategy**: Involves planning, setting Objectives and Key Results (OKRs), ensuring roadmap alignment, and making high-level decisions to guide the company's direction.
    *   **Systems**: Pertains to the technical infrastructure, automation, Standard Operating Procedures (SOPs), and process design that form the backbone of operations.
    *   **Support**: Focuses on issue resolution for both internal team members and external clients, ensuring smooth operations and client satisfaction.

Every record, task, or metric within the Gruntworks OS should ideally map to one Primary S (Sell or Ship). The Strategy, Systems, and Support pillars exist to accelerate the performance and efficiency of the Sell and Ship modes.

**Key Terminology:**

*   **OKRs (Objectives and Key Results)**: A goal-setting framework used to define and track objectives and their outcomes. Objectives are ambitious goals, and Key Results are measurable metrics that track the achievement of those objectives.
*   **Rocks**: Significant, clearly defined priorities or projects, typically with a quarterly cadence, derived from Key Results. The term is borrowed from the Entrepreneurial Operating System (EOS)/Traction methodology.
*   **L10 (Level 10 Meeting)**: A structured weekly leadership or team meeting format, also from EOS/Traction, designed for efficient review, problem-solving, and accountability.
*   **Scorecard**: A weekly metrics dashboard that provides a visual representation (often red/yellow/green status) of key performance indicators (KPIs) to track progress and identify issues quickly, often built as an Airtable Interface.
*   **Airtable Base/Tables/Interfaces**: The foundational data structure in Airtable. Gruntworks will use a single primary Base. Within this Base, different types of information (e.g., Objectives, Tasks, Clients) are organized into Tables. Airtable Interfaces will be used to create customized visual dashboards and logical groupings that simulate "Spaces" for different functions or areas of the business.
*   **SOPs (Standard Operating Procedures)**: Documented, step-by-step instructions for executing recurring tasks or processes to ensure consistency, efficiency, and quality.

---

## 2. Core Systems Architecture

The Gruntworks OS integrates several key platforms and data structures to streamline operations.

### 2.1 System Overview Diagram

```
+-------------------------+        webhooks          +------------------+
|  External Emails        |  -->  Postmark Inbound  |  External Inbox   |
|  Client/Partner Slack   |                          |  (Airtable Table) |
+-------------------------+                          +------------------+
           |                                                         |
           v                                                         v
+-------------------------+  internal slash cmds   +------------------+
|   Slack (Workspace)     |  <-------------------  |  Internal Inbox  |
+-------------------------+                          |  (Airtable Table) |
           |                                                         |
           |  triage agent (n8n + OpenAI) assigns Priority, Type, S  |
           +---------------------------------------------------------+
           v
+-------------------+   API    +-----------------------+
|     n8n (Docker)  | <------> |   Airtable Cloud      |
+-------------------+          | (Single Base, Tables) |
           |                   +-----------------------+
           | calls                    | contains OKRs, Rocks, Tasks,...
           v                           v
+-------------------+          +-------------------+
| LangGraph Agents  |          | GitHub + MkDocs   |
|  (Taskmaster etc) |          |   (SOP repo)      |
+-------------------+          +-------------------+
```

### 2.2 Airtable Data Model (Unified Work Hub)

Airtable is the central hub for all strategic and operational data at Gruntworks, organized within a single primary Base. This Base contains multiple Tables, each tailored to a specific type of data. Airtable Interfaces are then used to create logical "Spaces" or dashboards that provide focused views for different functional areas and align with the 2S-3S operational methodology. This structure ensures that data related to Selling, Shipping, Strategy, Systems, and Support is managed effectively, with clear workflows and connections between Tables.

#### 2.2.1 Airtable Tables, Interfaces and 2S-3S Alignment

The Gruntworks Airtable setup utilizes a single Base, with Tables and Interfaces structured as follows:

*   **Strategy Interface & Associated Tables (🟣 `Objectives`, 🟣 `Key Results`, 🟣 `Rocks`, 🟣 `Scorecard` Tables):**
    *   **2S-3S Pillar**: Strategy
    *   **Purpose**: Manages the company's high-level strategic planning and execution via an "Strategy" Interface. This Interface draws data from the 🟣 `Objectives`, 🟣 `Key Results (KRs)`, 🟣 `Rocks`, and 🟣 `Scorecard` Tables to provide a clear view of strategic goals and progress.
    *   **Key Tables**: 🟣 `Objectives Table`, 🟣 `Key Results Table`, 🟣 `Rocks Table`, 🟣 `Scorecard Table`.
    *   **Flow**: Feeds strategic priorities (Rocks from the 🟣 `Rocks Table`) into execution Tables (e.g., 🔴 `Projects Table`). Performance data from other Tables (e.g., 🔴 `Projects Table`, 🟢 Sales-related Tables) flows back to update KRs and Scorecards (in the 🟣 `Scorecard Table` or via Interface calculations).

*   **Sales Interface & Associated Tables (e.g., 🟢 `Clients`, 🟢 `Deals`, 🟢 `Leads`, 🟢 `Contacts`, 🟢 `Campaigns`, 🟢 `Personas`, 🟢 `Competitors`, 🟢 `Channels`, 🟢 `Partnerships` Tables):**
    *   **2S-3S Pillar**: Sell (Primary Mode)
    *   **Purpose**: Manages all client interactions, sales pipeline, customer data, and revenue-generating activities through a "Sales" Interface. This Interface pulls from Tables like 🟢 `Clients`, 🟢 `Deals`, 🟢 `Leads`, and other sales-related tables. Essential for tracking leads, deals, and maintaining client relationships.
    *   **Key Tables**: 🟢 `Clients Table`, 🟢 `Deals Table`, 🟢 `Leads Table`, 🟢 `Contacts Table`, 🟢 `Campaigns Table`, 🟢 `Personas Table`, 🟢 `Competitors Table`, 🟢 `Channels Table`, 🟢 `Partnerships Table`.
    *   **Flow**: Information about new clients or won deals typically triggers the creation of records in the 🔴 `Projects Table` for service delivery. Data from these Tables informs strategic Scorecards in the 🟣 `Scorecard Table`.

*   **Ship Interface & Associated Tables (🔴 `Projects`, 🔴 `Tasks`, 🔴 `Jobs`, 🔴 `Products` Tables):**
    *   **2S-3S Pillar**: Ship (Primary Mode)
    *   **Purpose**: The core execution engine for all projects and tasks related to delivering value to clients and fulfilling commitments, visualized through a "Ship" Interface. It also handles internal projects that support Sell, Strategy, Systems, and Support pillars when they are structured as projects.
    *   **Key Tables**: 🔴 `Projects Table`, 🔴 `Tasks Table`, 🔴 `Jobs Table`, 🔴 `Products Table`.
    *   **Flow**: The 🔴 `Projects Table` receives projects derived from 🟣 `Rocks` (linked from 🟣 `Rocks Table`) or new client engagements (linked from 🟢 Sales-related Tables). Task progress and time log data are generated here (in 🔴 `Tasks` and 🔵 `Timesheets` Tables), feeding into 🟣 `Scorecard` views (in an Interface or 🟣 `Scorecard Table`) and potentially 🔵 finance-related tables like 🔵 `Income`. Issues identified during execution can be escalated by creating records in the 🟡 `Issues Table`.

*   **Support Interface & Associated Tables (🟡 `Issues`, 🟡 `External Inbox`, 🟡 `Internal Inbox`, 🟡 `Interactions` Tables):**
    *   **2S-3S Pillar**: Support (Supporting Pillar)
    *   **Purpose**: Manages client and internal support requests, issue tracking, and resolution workflows via a "Support" Interface drawing from the 🟡 `Issues`, 🟡 `External Inbox`, 🟡 `Internal Inbox`, and 🟡 `Interactions` Tables. Ensures smooth operations by addressing problems and maintaining stakeholder satisfaction.
    *   **Key Tables**: 🟡 `Issues Table`, 🟡 `External Inbox Table`, 🟡 `Internal Inbox Table`, 🟡 `Interactions Table`.
    *   **Flow**: 🟡 `Issues` can be generated from client communications (via 🟡 `External Inbox`), internal flags (via 🟡 `Internal Inbox`), complications in 🔴 `Projects Table` execution, or system monitoring. Resolution might involve creating 🔴 `Tasks` (in 🔴 `Tasks Table`) for fixes, updating SOPs (in 🔵 `SOPs Table`), tracking client 🟡 `Interactions`, or direct communication.

*   **Systems Interface & Associated Tables (🔵 `Team`, 🔵 `Config`, 🔵 `SOPs`, 🔵 `Schema`, 🔵 `Tools`, 🔵 `Agents`, 🔵 `Prompts`, 🔵 `Timesheets`, 🔵 `Invoices`, 🔵 `Payroll`, 🔵 `Expenses`, 🔵 `Income`, 🔵 `Vendors` Tables):**
    *   **2S-3S Pillar**: Systems (Supporting Pillar)
    *   **Purpose**: Manages the operational infrastructure via a "Systems" Interface. This Interface draws from Tables like 🔵 `SOPs` (for Standard Operating Procedures), 🔵 `Team`, 🔵 `Config`, 🔵 `Schema`, 🔵 `Tools`, 🔵 `Agents`, 🔵 `Prompts` for operational functionality, along with financial tables like 🔵 `Timesheets`, 🔵 `Invoices`, 🔵 `Payroll`, 🔵 `Expenses`, 🔵 `Income`, and 🔵 `Vendors`.
    *   **Key Tables**: 🔵 `Team Table`, 🔵 `Config Table`, 🔵 `SOPs Table`, 🔵 `Schema Table`, 🔵 `Tools Table`, 🔵 `Agents Table`, 🔵 `Prompts Table`, 🔵 `Timesheets Table`, 🔵 `Invoices Table`, 🔵 `Payroll Table`, 🔵 `Expenses Table`, 🔵 `Income Table`, 🔵 `Vendors Table`.
    *   **Flow**: 🔵 `SOPs` from this area provide guidance for tasks in the 🔴 `Tasks Table`. 🟡 `External Inbox` and 🟡 `Internal Inbox` items can be triaged into 🔴 `Tasks` or 🟡 `Issues`. This area also underpins all others by managing access, structural settings, and core configuration data. Financial information flows through the various finance-related tables for client billing and expense tracking.

*   **Company Documents (Attachment fields across various tables):**
    *   **2S-3S Pillar**: Strategy, Systems
    *   **Purpose**: A repository for important company-wide documents, including finalised strategic plans, formal SOP versions, and other key reference materials. This might use attachment fields in relevant Tables across all color categories.
    *   **Key Entities**: Integrated via Attachment fields in tables like 🟣 `Objectives`, 🔵 `SOPs`, 🔴 `Projects`, and other tables.
    *   **Flow**: Provides reference materials linked to records across various Tables (e.g., a strategic brief attached to a 🟣 `Objectives` record, documentation attached to 🔵 `SOPs`, client deliverables attached to 🔴 `Projects`).

*   **Finance Interface & Associated Tables (🔵 `Invoices`, 🔵 `Expenses`, 🔵 `Income`, 🔵 `Payroll`, 🔵 `Vendors`, 🔵 `Timesheets` Tables):**
    *   **2S-3S Pillar**: Support (Supporting Pillar)
    *   **Purpose**: Manages financial data, invoicing, and expense tracking via a "Finance" Interface within the Systems category.
    *   **Key Tables**: Financial Tables (🔵 `Invoices Table`, 🔵 `Expenses Table`, 🔵 `Income Table`, 🔵 `Payroll Table`, 🔵 `Vendors Table`) and utilizes time data (from 🔵 `Timesheets Table`) for billing and cost analysis.
    *   **Flow**: Aggregates timesheet data (from 🔵 `Timesheets Table`, linked to 🔴 `Tasks Table`) for client billing and project profitability analysis. Links to 🟢 `Clients` for client-related financial information.

#### 2.2.2 Airtable Table Details (within the single Base)

Key Tables within the single Airtable Base include:

| Table Name         | Logical Grouping (Interface)                        | Key Fields / Purpose (Airtable Field Types)                                                                                                                                                                                                                                                                           | Key Relations (Linked Record Fields to other Tables)                      |
| ------------------ | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Objectives**     | `Strategy`                                          | `Objective` (Multiline Text, Primary Field), `Narrative` (Multiline Text), `Primary_S` (Single Select: Sell/Ship), `Year` (Number), `Total Number of Key Results` (Count), `Completed Key Results` (Count), `Percentage Completed` (Formula), `Quarters` (Single Line Text) (Defines strategic goals for the company) | ⇢ `Key Results`                                                           |
| **Key Results**    | `Strategy`                                          | `Metric` (Single Line Text), `Target` (Number), `Unit` (Single Line Text), `Primary_S` (Single Select), `Support_S` (Single Select: Strategy/Systems/Support), `Start_Date` (Date), `Due_Date` (Date), `Status` (Single Select) (Tracks measurable progress towards Objectives)                                       | ⇠ `Objectives`; ⇢ `Rocks`                                                 |
| **Rocks**          | `Strategy`                                          | `Title` (Single Line Text), `Description` (Long Text), `Phase` (Single Select: Sell/Ship), `Status` (Single Select), `Owner` (User), `Due_Date` (Date), `Figma_Link` (URL), ICE scores (Number fields) (Major quarterly projects derived from Key Results)                                                            | ⇠ `Key Results`; ⇢ `Projects`; ⇢ `Issues`                                 |
| **Projects**       | `Ship`                                              | `Name` (Single Line Text), `Project Type` (Single Select), `Status` (Single Select), `Decomp Method` (Single Select: RIPER-5/Taskmaster), `Primary_S` (Single Select), `Support_S` (Single Select). (Work containers for client/internal/ops initiatives)                                                             | ⇠ `Clients`; ⇠ `Rocks` (optional); ⇢ `Tasks`                              |
| **Tasks**          | `Ship`                                              | `Title` (Single Line Text), `Description` (Long Text), `Primary_S` (Single Select), `Support_S` (Single Select), `ETA` (Date), `Done_Date` (Date), `Owner` (User), `Priority` (Single Select), `Estimate hrs` (Number), `Status` (Single Select) (Actionable work units)                                              | ⇠ `Projects`; ⇠ `Rocks` (sometimes directly); ⇢ `Time Logs`; ⇢ `SOPs`     |
| **Clients**        | `Sales`                                             | `Name` (Single Line Text), `Verticals` (Multiple Select), `Tier` (Single Select) (Client information)                                                                                                                                                                                                                 | ⇢ `Projects`, `Tasks`                                                     |
| **External Inbox** | `Systems`                                           | `Source` (Single Line Text), `Raw Text` (Long Text), `Labels` (Multiple Select) (Initial capture for external communications)                                                                                                                                                                                         | ⇢ `Tasks` (if actioned); ⇢ `Issues` (if actioned)                         |
| **Internal Inbox** | `Systems`                                           | `Source` (Single Line Text), `Raw Text` (Long Text), `Labels` (Multiple Select) (Initial capture for internal requests)                                                                                                                                                                                               | ⇢ `Tasks` (if actioned); ⇢ `Issues` (if actioned)                         |
| **Issues**         | `Support`                                           | `Description` (Long Text), `Category` (Single Select: Support/Systems/Project), `Severity` (Single Select: Low/Med/High), `Owner` (User), `Next_Step` (Single Line Text), `Created_Date` (Date), `Status` (Single Select), `Root Cause` (Long Text) (Problem tracking)                                                | ⇠ `Rocks`; ⇠ `Projects`                                                   |
| **Scorecard**      | `Strategy`, `Systems`                               | `Metric` (Single Line Text), `Target` (Number), `Actual` (Number), `Week_Start` (Date), `Color` (Single Select: Green/Yellow/Red), `Owner` (User) (Performance metrics tracking, visualized via Interfaces)                                                                                                           | (Often linked to `Key Results` or specific System components via Lookups) |
| **Time Logs**      | `Ship` (primarily recorded), `Finance` (aggregated) | `Start` (Date/Time), `Stop` (Date/Time), `Duration` (Duration) (Time tracking per task)                                                                                                                                                                                                                               | ⇠ `Tasks`                                                                 |
| **SOPs**           | `Systems`, `Company Documents` (logical grouping)   | `Title` (Single Line Text), `Content` (Rich Text or Long Text), `Keywords` (Multiple Select), `Attachment` (Attachment) (Standard Operating Procedures, linked across the workspace)                                                                                                                                  | (Linked from `Tasks`, `Projects`, available via RAG)                      |
| **Config**         | `Systems`                                           | `SettingName` (Single Line Text), `Value` (Long Text/JSON), `Description` (Long Text) (Stores system-wide configurations, API keys, etc.)                                                                                                                                                                             |                                                                           |

> \*Airtable can perform roll-ups and aggregations from linked records (e.g., Task progress to Projects) using Rollup, Lookup, and Formula fields. These are then often visualized in Airtable Interfaces to create dashboards showing progress towards Rocks → KRs → Objectives.

### 2.2.3 Airtable Views and Interfaces

Key views within Airtable Tables and custom Interfaces will be configured to support the 2S-3S OS:

*   **Objectives View (within `Objectives Table` or Interface)**: Grouped by `Primary_S` (Sell/Ship) to visualize strategic alignment.
*   **Key Results View (within `Key Results Table` or Interface)**: Filtered by the current year and grouped by `Primary_S` for progress tracking.
*   **Rocks Kanban View (within `Rocks Table`)**: Grouped by `Status` (e.g., To Do, In Progress, Done) to manage quarterly project execution.
*   **Tasks Grid View (within `Tasks Table`)**: Filtered by `Owner` and `Due_Date` (e.g., ≤ 7 days) for individual workload management.
*   **Scorecard Interface**: An Airtable Interface designed to visualize weekly red/yellow/green counts of key performance indicators, pulling data from the `Scorecard Table` and other relevant Tables.
*   **Issues Backlog View (within `Issues Table`)**: Sorted by `Severity` (descending) and then `Created_Date` (ascending) for prioritized problem resolution.

### 2.2.4 Airtable-Native Automations

In addition to n8n-driven workflows, several automations will be configured directly within Airtable (in the single Base) to maintain system integrity and streamline processes:

1.  **Scorecard Alert**
    *   **Trigger:** When a record in the 🟣 `Scorecard Table` has its `Color` field updated to `Red`.
    *   **Action:** Airtable Automation: Send a Slack webhook notification to the `#ops-alerts` channel.

2.  **Rocks → Issues Linkage (Proactive Issue Creation)**
    *   **Trigger:** When a record in the 🟣 `Rocks Table` has its `Due_Date` pass and its `Status` is not 'Done'.
    *   **Action:** Airtable Automation: Create a new record in the 🟡 `Issues Table`, linking it to the overdue Rock record.

3.  **Issue → Task Stub (Initial Action Prompt)**
    *   **Trigger:** When a new record is created in the 🟡 `Issues Table`.
    *   **Action:** Airtable Automation: Create a preliminary record in the 🔴 `Tasks Table`. The `Description` of this Task can be pre-filled with the `Issue.Next_Step` field content.

### 2.3 Key Infrastructure Components

The OS relies on the following technical infrastructure:

*   **n8n:** Hosted on DigitalOcean (Docker) – Serves as the primary Workflow Automation Engine.
*   **LangGraph services:** Hosted on DigitalOcean (Docker compose) – Powers various AI Agent Services.
*   **Vector store:** Utilizes LiteLLM JSON or SQLite – Stores SOP embeddings for Retrieval Augmented Generation (RAG).
*   **Airtable:** Cloud-based – Acts as the central Work Hub & Database (organized as a single Base with multiple Tables, and Interfaces for segmented views).
*   **Toggl Track:** SaaS – Used for all time tracking, API v9 integration. Workspace: `gruntworks-prod`.
*   **Postmark:** Inbound email server (`grunt-inbox`) – Manages email intake, webhook to n8n (`/webhooks/postmark`).
*   **GitHub & MkDocs:** Repository for SOPs, enabling version control and documentation site generation.

Security basics include environment variables in Docker secrets, UFW for ports 22 & 443, Fail2Ban, and nightly off-site snapshots.

### 2.4 Figma Workspace for Operational Visualization

Figma is utilized for creating and maintaining visual assets that support the 2S-3S Operating System, including process maps, organizational charts, and system diagrams. These visuals aid in understanding and communication.

**Team File: "2S-3S Ops Maps"**

A central Figma team file, named "2S-3S Ops Maps" or similar, houses key operational visualizations. This file is organized into the following pages:

*   **Org Chart Page**: Contains an auto-layout tree representing the organizational structure and roles. Annotations should specify the Primary S (Sell/Ship) focus for key roles or departments.
*   **Process Flows Page**: Includes diagrams illustrating core workflows for Sell, Ship, and Strategy processes. These visual maps help in identifying bottlenecks and areas for improvement.
*   **System Architecture Page**: Provides a visual representation of how different systems and tools integrate (e.g., Airtable → Slack → n8n → Airtable). This is crucial for understanding data flow and dependencies.
*   **Scorecard Mock Page**: Features a visual mock-up or template of the Scorecard (potentially an Airtable Interface design), illustrating how red/yellow/green metrics are displayed.

**Components & Templates**

To ensure consistency and efficiency in creating these visuals, a set of shared components and templates are maintained within Figma:

*   **Phase Tags**: Standardized visual tags (e.g., color-coded or labeled) for different operational phases: Sell (e.g., Orange), Ship (e.g., Blue), Strategy (e.g., Purple), Systems (e.g., Green), Support (e.g., Gray).
*   **Card Styles**: Pre-designed card styles for representing entities like Rocks, Tasks, and Issues in visual diagrams (conceptually, as these are now Airtable records).
*   **Connectors**: Standardized arrows, lines, and labels for creating clear and readable flowcharts and diagrams.

**Integration with Other Systems**

Figma frames from the "2S-3S Ops Maps" file are embedded into other systems to provide visual context where needed:

*   **Airtable**: Relevant Figma frames (e.g., a specific process flow for a Rock) can be embedded into Airtable records using URL fields, Rich Text fields with embed support, or within Airtable Interfaces.
*   **MKDocs**: Figma frames can be embedded into MKDocs pages (e.g., system architecture on a relevant SOP page) using `<iframe>` HTML tags.

---

## 3. Key Automations & AI Agents

Automation and AI are integral to the efficiency of the Gruntworks OS.

### 3.1 Automations & Workflows (n8n-centric)

| #   | Name                  | Trigger                                                                     | Function & Tools (n8n, OpenAI, Airtable, Toggl, Slack, GCal)                                                                                                              |
| --- | --------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A1  | **Intake Triage**     | Postmark or Slack event → 🟡 `External Inbox`/🟡 `Internal Inbox Table` entry | Classifies intent, priority; if actionable → creates record in 🔴 `Tasks Table` in Airtable (default status *Inbox*) (n8n + OpenAI)                                        |
| A2  | **Start Focus**       | Button on Airtable record (via script or n8n webhook)                       | Starts Toggl timer (tagged `task_<recordID>`), updates `Status` field in 🔴 `Tasks Table`, DMs user via Slack. 25-min blocks, break pings (n8n + Toggl + Slack).           |
| A3  | **Stop Focus**        | Button or WIP rule                                                          | Stops Toggl timer, writes `Time Tracked` to 🔴 `Tasks Table` record, prompts for completion notes (n8n + Toggl + Airtable). Webhook listener updates 🔵 `Timesheets Table`. |
| A4  | **Daily Scheduler**   | 17:00 daily cron                                                            | Queries 🔴 `Tasks Table` in Airtable for tomorrow's tasks, chunks into blocks, creates GCal events, DMs summary (n8n + Airtable + GCal + Slack).                           |
| A5  | **Morning Digest**    | 07:00 daily                                                                 | Gathers today's tasks/meetings from 🔴 `Tasks Table` (Airtable) & GCal, crafts Slack DM (n8n + OpenAI + Airtable + GCal + Slack).                                          |
| A6  | **Weekly Capacity**   | Friday 16:00                                                                | Rolls-up Planned vs Actual hrs from 🔴 `Tasks Table`/🔵 `Timesheets Table` (Airtable) & Toggl, overload check, Slack report (n8n + Airtable + Toggl + Slack).               |
| A7  | **WIP Enforcement**   | On record update in Airtable 🔴 `Tasks Table`                                | If user has >3 *In Progress* Tasks, reverts status + DMs user via Slack (Airtable Automation or n8n for DM).                                                              |
| A8  | **Priority Alert**    | Hourly check in Airtable (Scheduled Automation or n8n)                      | For 🔴 `Tasks Table` records with High Priority & Due ≤ 24h → Slack DM (Airtable Automation or n8n for DM).                                                                |
| A9  | **Taskmaster Decomp** | Airtable Button OR 🔴 `Project` record created with Decomp="Taskmaster"      | Multi-step scope → LLM → human approval doc → create sub-records in 🔴 `Tasks Table` (LangGraph + AgentOps + Airtable).                                                    |
| A10 | **RIPER-5 Decomp**    | Same, Decomp="RIPER"                                                        | One-shot LLM breakdown → return JSON → n8n creates records in 🔴 `Tasks Table` (Python FastAPI + GPT-3.5 + n8n + Airtable).                                                |

### 3.2 AI Agents

| Agent                 | Primary Purpose                                          | Key Technologies (Phase)           |
| --------------------- | -------------------------------------------------------- | ---------------------------------- |
| **Triage Agent**      | Classify inbound communications, assign labels           | n8n + GPT-4o (Phase 1)             |
| **Next-Action Agent** | Suggest next best task after completion, respecting mode | n8n + GPT-4o (Phase 2)             |
| **Focus Buddy**       | Pomodoro timer pings & encouragement via Slack           | n8n + GPT-3.5 (Phase 1)            |
| **Taskmaster**        | Decompose large internal projects (> 3 days WBS)         | LangGraph + GPT-4o (Phase 3)       |
| **RIPER-5**           | Breakdown small projects based on RIPER-5 protocol       | Python FastAPI + GPT-3.5 (Phase 2) |
| **Load Forecaster**   | Predict over/under-capacity for the next 2 weeks         | LangGraph + regression (Phase 4)   |

---

## 4. Knowledge Operations & SOPs

Standard Operating Procedures (SOPs) are the single source of truth for processes.

*   **Repository:** SOPs are maintained in Markdown format (`/sops/**.md`) within a GitHub repository and rendered via MkDocs. Some key SOP data might be synced or summarized in an `SOPs Table` within Airtable.
*   **Embeddings:** A nightly GitHub Action regenerates embeddings from SOP content and stores them as `sop_vectors.pkl` (e.g., on DigitalOcean).
*   **Retrieval:** The `/asksop <query>` Slack command triggers an n8n RAG workflow. This workflow uses OpenAI's models along with the vector store to find and return relevant SOP excerpts and links directly in Slack.
*   **Task Integration:** Airtable `Task` records (in the `Tasks Table`) can be linked to relevant SOPs (e.g., via a URL field to MkDocs or a linked record to an `SOPs Table` if it exists). The system may auto-suggest SOP links based on task keywords or type.

### 4.1 MKDocs Site Structure and Key Pages

The MKDocs site, which serves as the primary interface for the 2S-3S Operating System documentation and SOPs, is structured as follows:

**`mkdocs.yml` Navigation Structure:**

```yaml
site_name: 2S-3S Operating System
nav:
  - Home: index.md
  - Vision:
    - 3-Year Picture: vision.md
    - Core Values: values.md
  - OKRs:
    - Annual Objectives: okrs.md
    - Key Results: key-results.md
  - Rocks: rocks.md
  - Weekly L10 Review: weekly-l10.md
  - Daily Stand-Up: daily-standups.md
  - System Hygiene: system-hygiene.md
  - SOPs: sops.md
  - Playbooks: playbooks.md
theme: material
```

**Key Page Templates and Content:**

*   **`index.md`**: Provides an overview of the 2S-3S Operating System and links to each major section of the documentation.
*   **`vision.md`**: Contains the company's 3-Year Picture. Typically includes YAML front-matter for title and metadata.
*   **`values.md`**: Lists the Core Values that guide company culture and decision-making.
*   **`okrs.md`**: Embeds an Airtable view from the `Objectives Table` or an "Objectives" Airtable Interface to display current annual objectives.
*   **`key-results.md`**: Embeds an Airtable view from the `Key Results Table` or a "Key Results" Airtable Interface for detailed tracking.
*   **`rocks.md`**: Offers guidance on Rocks and embeds an Airtable Kanban view from the `Rocks Table` or a "Rocks" Airtable Interface.
*   **`weekly-l10.md`**: Serves as a template for the Weekly 2S Review meeting, including the agenda and an embedded Scorecard from an Airtable Interface.
*   **`daily-standups.md`**: Provides a template for daily stand-up meetings, outlining key discussion points.
*   **`system-hygiene.md`**: A checklist of recurring operational tasks necessary to keep systems running smoothly.
*   **`sops.md`**: Acts as an index for Standard Operating Procedures, linking to individual SOPs or playbooks.
*   **`playbooks.md`**: A library of detailed, longer-form how-to guides for complex or multi-step processes.

Each relevant page in MKDocs should ideally link back to corresponding records, views, or Interfaces in Airtable where applicable, using shared URLs to create a bi-directional connection.

### 4.2 Operational Cadences and Workflow Overview

The Gruntworks Operating System follows a structured rhythm across daily, weekly, monthly, quarterly, and annual cadences. The core operational flow emphasizes:

1.  **Plan (Strategy)**: Utilizing MKDocs for documentation and Airtable (Tables like `Objectives`, `Key Results`, `Rocks`, and relevant Interfaces) for OKRs and strategic alignment.
2.  **Execute (Sell/Ship)**: Managing daily tasks and progress within Airtable Tables (e.g., `Tasks`, `Projects`).
3.  **Review & Iterate**: Employing weekly L10 meetings (agenda in MKDocs, data from Airtable Interfaces/Tables) and continuous feedback loops to create `Issue` records and new `Task` records as needed.

**Cadence-Tool Snapshot:**

| Cadence        | Airtable Focus                                                                      | MKDocs Resource(s)                                 | Figma Visualization(s)      |
| -------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------- |
| **Annual**     | `Objectives Table` view or 'Strategy' Interface (for setting annual goals)          | `vision.md`, `okrs.md` (documentation & embedding) | Org Chart (strategic roles) |
| **Quarterly**  | `Rocks Table` Kanban view or 'Strategy' Interface (for tracking quarterly projects) | `rocks.md` (guidance & embedding)                  | Process Flows (for review)  |
| **Weekly L10** | 'Strategy'/'Systems' Interfaces (Scorecard), `Issues Table` view                    | `weekly-l10.md` (meeting agenda & embedding)       | Scorecard Mock (design ref) |
| **Daily**      | `Tasks Table` Grid view or 'Daily Tasks' Interface (for daily execution)            | `daily-standups.md` (stand-up template)            | —                           |
| **Hygiene**    | Specific views/records in `Config Table` or `Tasks Table` for System Hygiene        | `system-hygiene.md` (checklist)                    | System Architecture (ref)   |
| **SOPs**       | `SOPs Table` (if used) or links in other Tables to MKDocs                           | `sops.md`, `playbooks.md` (documentation)          | —                           |

## 5. Daily Cadence (Solo‑Founder)

| Time      | Action                                                                                                                                                                                  | System Touchpoints (Automations, Agents, Tools)                                                     | Mode    |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------- |
| **07:00** | Slack *Morning Digest* (A5) appears → skim agenda, choose top three priorities.                                                                                                         | n8n, OpenAI, Airtable (`Objectives Table`, `KRs Table`, `Tasks Table` for goals/tasks), GCal, Slack | Review  |
| 07:15     | `/startfocus` or Airtable button for first **Sell** task (e.g. Prospect list build).                                                                                                    | Focus Buddy (A2), Toggl, `Tasks Table` record status updated, Slack                                 | Sell    |
| 08:45     | 15‑min context switch ritual:*<br>• mark task done (A3 writes time)<br>• `/nexttask` (Next-Action Agent)<br>• quick stand‑stretch                                                       | n8n, Toggl, Airtable (`Tasks Table`), Next-Action Agent (n8n+OpenAI querying `Tasks Table`)         | —       |
| 09:00     | Second **Sell** block (cold‑email batch + CRM updates in Airtable `Clients`/`Deals` Tables).                                                                                            | Bulk actions in Airtable; Gmail via n8n (potential A)                                               | Sell    |
| 10:30     | **Ship** block #1 (client SEO audit).                                                                                                                                                   | `/startfocus` (A2) on Ship task (`Task` record in Airtable)                                         | Ship    |
| 12:00     | Lunch / walk – timers auto‑pause (manual or future A3 enhancement).                                                                                                                     | Toggl                                                                                               | —       |
| 13:00     | **Sales calls / demos** (calendar).                                                                                                                                                     | GCal events surfaced in Morning Digest (A5)                                                         | Sell    |
| 14:30     | **Ship** block #2 (implement Site fixes).                                                                                                                                               | Focus Buddy (A2) (`Task` record in Airtable)                                                        | Ship    |
| 16:00     | 20‑min **Systems** tune‑up:<br>check WIP alerts (A7), triage inbox (A1 - `Internal Inbox Table` → `Tasks Table` or `Issues Table`), capture lessons (to SOPs in MKDocs / `SOPs Table`). | Airtable Automations, n8n, OpenAI, Slack, GitHub/MkDocs, Airtable `SOPs Table`                      | Systems |
| 16:30     | **Support** – financial quickbooks, admin tasks.                                                                                                                                        | External SaaS                                                                                       | Support |
| 17:00     | Slack *Daily Shutdown* prompt (custom n8n workflow, similar to A4/A5 logic):<br>✔ capture wins<br>✔ set tomorrow's primary Sell target<br>✔ `/stopfocus` any running timers (A3).       | n8n, Airtable (`Tasks Table` for tasks/targets), Slack                                              | Review  |

> **Transition rule:** after each Focus block: *Mark task done* (triggers A3), *Log time*, *Ask `/nexttask`*. Keeps WIP ≤ 3 (enforced by A7) for `Task` records.
> **Scheduling:** Google Calendar "Work Blocks" (e.g., `Internal Deep Work`, `Client Execution`, `Sales/Calls`) are created daily by A4. Meetings are auto-pulled into Morning Digest (A5).

---

## 6. Weekly Cycle (Friday‑centric)

| When          | Ritual                                                                                                                                              | Outcome / System Touchpoints (Automations)                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Mon 07:05** | *Weekly Kickoff Digest* (custom n8n, like A5/A6) – tasks tagged *This Week*, meetings, capacity graph.                                              | Clear runway. (n8n, Airtable [`Tasks Table`], GCal, Slack) |
| **Wed 13:00** | Mid‑week KPI snapshot in Slack (`#ops`) (custom n8n, from Airtable `Scorecard Table` / Interface).                                                  | Early drift detection. (n8n, Airtable, Slack)              |
| **Fri 15:30** | *Scorecard Review* (Sell leads, Ship cycle‑time, Utilisation, Cash in) – manual review of Airtable Scorecard Interface / n8n report (A6 part).      | Red/Green indicators.                                      |
| **Fri 16:00** | *Sprint Retro* auto‑draft by n8n/OpenAI → founder edits 5 min → saved to Airtable record (e.g., `Retro Notes Table`).                               | Lessons captured. (n8n, OpenAI, Airtable)                  |
| **Fri 16:15** | Plan next week:<br> • update `Rock` records in Airtable for *This Week*<br> • set Estimates<br> • Weekly Capacity (A6) checker highlights overload. | Tasks scheduled; Calendar blocks created by A4.            |

---

## 7. Monthly / Quarterly / Annual Cadence

| Interval                | Key Meeting                                                       | Tool / Output                                                                    |
| ----------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Monthly (First Mon)** | 3S Systems Day – one hour to improve/automate one bottleneck.     | SOP update PR (Knowledge Ops), new n8n node (Automation), Airtable schema tweak. |
| **Quarterly (Q‑Day)**   | 2S‑3S *Rocks Reset*: grade last Rocks, define new, align to OKRs. | Airtable `OKRs Table` view / Interface; `Rocks Table` records ICE scored.        |
| **Annual (Dec)**        | Vision refresh, revenue targets, capacity modelling.              | Strategy doc + high‑level `Objective` records seeded in Airtable.                |

---

## 8. Essential Checklists by Mode

### 8.1 Sell (Daily)

1.  **Prospect generation** (10 new ICP leads via Clay/Crawl4AI).
2.  **Outbound touch** – 50 personalised emails/X DMs.
3.  **Pipeline hygiene** – update Deal stages in Airtable (`Deals Table`), next‑action set.
4.  **Follow‑ups** – min 15 warm leads pinged.

### 8.2 Ship (Daily)

1.  Review client queue in Airtable (`Tasks` or `Projects Table` views) – SLA clock check.
2.  Execute top Ship task with Focus timer (A2, A3).
3.  Push deliverables, notify client.
4.  Log time + brief note in Airtable (`Tasks Table` or `Time Logs Table`) (goal: <24 h response window).

### 8.3 Strategy / Systems / Support (Weekly‑mini)

*   **Mon 30‑min macro‑review** – metrics trend (Airtable Scorecard Interface).
*   **Fri Retro action item** – one SOP (Knowledge Ops) or automation improvement (Automations).
*   **Finance Friday** – send invoices, reconcile spend (External SaaS).

---

## 9. Flow Diagram – Daily Ops Pulse

```mermaid
graph LR
A[07:00 Morning Digest (A5)] --> B{Select Top 3 Priorities}
B --> C1[Sell Block 1 (A2 Start on Airtable Task)]
C1 --> D{Mark Done (A3 Stop), /nexttask (NextAction Agent)}
D --> C2[Sell Block 2 (A2 Start on Airtable Task)]
C2 --> E[Ship Block 1 (A2 Start on Airtable Task)]
E --> F[Sales Calls (GCal)]
F --> G[Ship Block 2 (A2 Start on Airtable Task)]
G --> H[Systems Review (A1 Triage Airtable Inbox, A7 WIP)]
H --> I[Shutdown Prompt (n8n)]
```

---

## 10. Enforcement Mechanisms

*   **WIP Guard (A7):** Airtable Automation + n8n blocks >3 concurrent *In Progress* tasks in the `Tasks Table`.
*   **Time Allocation Report:** Weekly pie chart from Toggl data (part of A6 or separate n8n report); alarm if Sell <55 %.
*   **Priority Drift Alert (A8):** Hourly Airtable Automation or n8n DM for High Priority tasks (in `Tasks Table`) due soon. Also, if >20 % hours spent on Support in a week (from Toggl/Airtable data), Slack DM.

---

## 11. Glue Commands (Slack)

| Command                                  | Purpose                                                          | System Interaction                                                                                                |
| ---------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `/addtask Fix landing‑page form`         | Quick capture to `Internal Inbox Table` in Airtable.             | n8n webhook → Airtable `Internal Inbox Table` record                                                              |
| `/triage`                                | Forces AI triage run (A1) on all unprocessed Inbox items.        | n8n → OpenAI → Airtable `Internal Inbox Table` / `External Inbox Table` → `Task` or `Issue` record in Airtable    |
| `/nexttask`                              | Suggests highest‑value task, respecting Sell≥Ship ratio.         | Next-Action Agent (n8n + OpenAI + Airtable query of `Tasks Table`)                                                |
| `/focus <taskID_or_name>`                | Shortcut to Start Focus (A2) on a specific Airtable Task record. | n8n → Airtable query (`Tasks Table`) → A2 logic (Toggl, Slack, Airtable)                                          |
| `/asksop GBP suspension`                 | Returns SOP excerpt + link from Knowledge Ops.                   | n8n → Vector Store (RAG from SOPs in GitHub/MKDocs, potentially linked in Airtable `SOPs Table`) → OpenAI → Slack |
| `/startfocus <optional_task_name_or_id>` | Alias for `/focus` or starts generic timer if no task specified. | (Similar to /focus - involves Airtable `Tasks Table`)                                                             |
| `/stopfocus`                             | Stops current Toggl timer, prompts for log (A3).                 | n8n → Toggl → Airtable (`Tasks Table` or `Time Logs Table`)                                                       |