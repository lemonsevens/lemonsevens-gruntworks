# Gruntworks OS - Fibery Architecture

## 1. Architecture Overview

The Gruntworks Operating System (GWOS) architecture is centered around **Fibery** as the core platform for process management, data centralization, and workflow automation. It's designed to support a solo founder's operational cadences across Sell, Ship, Strategy, Systems, and Support modalities. The architecture emphasizes clear data relationships, automated information flow where possible, and integrated views for decision support, all as defined in the `Fibery-PRD.md v1.0`.

Supporting technologies like **n8n** (for external automation and complex integrations), **Slack** (for notifications), **Toggl Track** (for time logging), and **GitHub/MkDocs** (for SOPs) are integrated with Fibery to provide a comprehensive operational environment.

## 2. Core Architectural Principles

*   **Centralized Hub:** Fibery acts as the single source of truth for all operational data and process status.
*   **Process-Driven:** The system is structured around the core operational processes and cadences defined in the PRD.
*   **Data Interconnectivity:** Fibery databases are highly relational, ensuring data flows logically between strategic objectives (OKRs), projects, tasks, client management, and operational logs.
*   **Automation for Efficiency:** Fibery automations and n8n workflows are used to reduce manual effort and ensure process consistency.
*   **Transparency & Visibility:** Fibery views and dashboards provide clear insights into all aspects of the operation.
*   **Modularity & Adaptability:** While comprehensive, the PRD implies a modular setup (distinct Fibery databases for different functions) which can be adapted over time.

## 3. Key Architectural Components & Layers (Conceptual)

This isn't a traditional software layered architecture, but rather a conceptual layering of the operational system components:

### 3.1. Strategic Layer (Fibery)
*   **Components:** Objective (OBJ), Key Result (KR), Rock (RCK) databases.
*   **Purpose:** Defines and tracks long-term goals, quarterly targets, and major commitments.
*   **Interactions:** Objectives link to KRs, KRs link to Rocks. Progress is aggregated upwards.

### 3.2. Execution Layer (Fibery)
*   **Components:** Project (PRJ), Task (TSK) databases.
*   **Purpose:** Manages the day-to-day work required to achieve Rocks and KRs.
*   **Interactions:** Tasks roll up to Projects, Projects can be linked to Rocks. Time Logs (TM) are associated with Tasks.

### 3.3. Customer Relationship & Sales Layer (Fibery)
*   **Components:** Client (CLI), Deal (DLR) databases.
*   **Purpose:** Manages client information and sales pipeline.
*   **Interactions:** Deals link to Clients. Projects can link to Clients.

### 3.4. Ingestion & Issue Management Layer (Fibery)
*   **Components:** External Inbox (EIN), Internal Inbox (IIN), Issue (ISC) databases.
*   **Purpose:** Captures raw inputs, ideas, and problems for processing and potential task creation.
*   **Interactions:** Inbox items can be processed into Tasks. Issues can be linked to Rocks and can spawn Tasks.

### 3.5. Monitoring & Reporting Layer (Fibery)
*   **Components:** Scorecard (SCB) database, Time Log (TM) database, various custom Views and Dashboards.
*   **Purpose:** Tracks KPIs, time allocation, and overall system performance.
*   **Interactions:** Pulls data from multiple other entities to provide consolidated views.

### 3.6. Knowledge & Configuration Layer (Fibery & External)
*   **Components:** SOP Link (SOP) database (links to MkDocs/GitHub), Config (CFG) database.
*   **Purpose:** Manages links to procedural documentation and system configuration parameters (e.g., webhook tokens).
*   **Interactions:** SOPs are linked to Tasks. Config values are used by Fibery buttons and external automations.

### 3.7. External Automation & Integration Layer (n8n, APIs)
*   **Components:** n8n workflows, Slack integration, Toggl Track integration, Fibery API.
*   **Purpose:** Handles processes that occur outside Fibery or require complex logic/inter-service communication.
*   **Interactions:**
    *   Fibery buttons trigger n8n webhooks (via URLs in CFG).
    *   n8n workflows interact with Toggl Track API, Slack API, and Fibery API (read/write).
    *   Fibery automations can directly post to Slack or trigger internal actions.

## 4. Cross-cutting Concerns

*   **Configuration Management:** Primarily handled by the `Config (CFG)` database in Fibery, storing webhook URLs and key operational parameters. API keys for n8n integrations with external services (Toggl, Slack) are managed within n8n itself.
*   **Authentication & Authorization:**
    *   Fibery: Managed by Fibery's user roles (Owner, Bot User, Contractor) as defined in PRD.
    *   n8n & other services: Standard API key/token-based authentication.
*   **Data Integrity & Consistency:** Enforced by Fibery's relational structure, required fields, and data validation where possible. Automations aim to maintain consistency.
*   **Backup & Recovery:** Weekly data/schema backup via Fibery API (as per PRD). n8n workflows should be version controlled if self-hosted, or rely on cloud provider backups.

## 5. Core Integration Patterns

*   **Webhook-Driven (Fibery -> n8n):** Fibery buttons (Start/Stop Focus, Decompose, Retry Triage) trigger n8n workflows via webhooks.
*   **API-Driven (n8n <-> Fibery/Toggl/Slack):** n8n workflows use APIs to interact with Fibery (CRUD operations), Toggl (manage timers, get logs), and Slack (send messages).
*   **Native Integration (Fibery -> Slack):** Fibery's built-in Slack integration used for simpler notifications.
*   **URL Linking (Fibery -> SOPs):** Fibery `SOP Link` entities store URLs to MkDocs/GitHub pages.

## 6. Data Flow (High-Level Examples)

*   **Time Tracking:** User clicks "Start Focus" (Fibery) -> Webhook to n8n -> n8n starts Toggl timer & logs to Fibery (optional interim log) -> User clicks "Stop Focus" (Fibery) -> Webhook to n8n -> n8n stops Toggl timer -> n8n creates/updates `Time Log (TM)` in Fibery with full details. `Task.Time Tracked` updates via formula.
*   **Issue to Task:** New `Issue (ISC)` created in Fibery -> Fibery Automation creates `Task (TSK)`, links it to Issue, pre-fills details.
*   **Scorecard Alert:** `Scorecard (SCB)` value changes to Red/Yellow in Fibery -> Fibery Automation sends Slack notification. 