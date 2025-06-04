# Gruntworks Project Management System – Blueprint

## 1. Core Problem

Current project handling is ad‑hoc; tool decisions have oscillated (Airtable → Fibery → Airtable). Lack of a standard, end‑to‑end framework throttles throughput and clarity.

## 2. Key Insights

* **Standardisation beats improvisation at scale.** Flexibility feels faster short‑term but compounds inefficiency.
* Projects originate from many triggers (client requests, research, internal pain points, etc.)—intake must accept multiple entry points.
* Tooling must serve the *process*, not dictate it; Airtable is the chosen single source of truth for now.
* Everything must ladder up to **Ship** or **Sell** (2S). Support, Strategy, Systematise (3S) exist only to accelerate 2S.

## 3. Guiding Principles (2S‑3S Applied)

1. **Ship & Sell Focus** – No project proceeds unless it clearly supports shipping deliverables or generating revenue.
2. **Lean but Documented** – Minimum viable process, fully written; nothing lives only in someone’s head.
3. **Single Source of Truth** – Airtable holds canonical project data; other tools integrate but do not store decisions.
4. **Modular Intake** – Unified intake schema that can be triggered from IDE, browser extension, email, or form.
5. **Lifecycle Transparency** – Every project moves through identical stage gates; status is always unambiguous.

## 4. Objectives (90‑Day)

| #   | Objective                        | Definition of Done                                                    |
| --- | -------------------------------- | --------------------------------------------------------------------- |
| O1  | Finalise Airtable "GruntOS" base | Tables, views, automations live; tested with two active projects.     |
| O2  | Document Project Lifecycle SOP   | 1‑page flowchart + checklist stored in knowledge base; team sign‑off. |
| O3  | Deploy Multi‑Entry Intake        | Browser bookmarklet + IDE snippet + client form all feed Ideas table. |
| O4  | Train Team                       | 2× 30‑min sessions recorded; quiz score ≥90%.                         |

## 5. Standard Project Lifecycle

1. **Trigger / Idea Capture** – Anything that could become a project enters *Ideas* table with minimal fields.
2. **Triage & Scoring** – Weekly review scores against 2S impact, effort, urgency. Pass → Project.
3. **Definition** – Draft PRD or brief; identify owner, success metric, dependencies.
4. **Planning** – Break into tasks, set deadlines, allocate resources.
5. **Execution** – Work tracked via Tasks & Sub‑tasks linked to source repos/boards.
6. **QA & Demo** – Internal QA or client review; accept/iterate.
7. **Delivery / Close** – Ship to client or internal deploy; mark metrics.
8. **Retrospective** – 15‑min template; lessons captured in *Retros* table.

## 6. Airtable "GruntOS" Schema (v1)

### Tables & Fields

| Table              | Primary Field             | Core Fields                                                                                                                                     | Relationships                       |
| ------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Ideas              | `Idea Name` (single line) | Source (single select), Quick Desc (long text), Creator (user), 2S Tag (multi‑select), Effort (number), Impact (number), Created (created time) | links → Projects (optional)         |
| Projects           | `Project Name`            | Status (stage select), Owner (user), Start, Target End, Actual End (formula), 2S Tag, ROI Score (formula), Idea Link, Client (link)             | links → Tasks, Deliverables, Retros |
| Tasks              | `Task`                    | Project (link), Assignee, Status, Priority, Due, Estimate Hrs (number), Actual Hrs (rollup), Blocked By (link to Dependencies)                  | links → Sub‑tasks                   |
| Sub‑tasks          | `Sub‑task`                | Parent Task (link), Status, Assignee, Due                                                                                                       | –                                   |
| Deliverables       | `Deliverable Name`        | Project (link), File/URL (attachment/url), Delivered Date, Accepted? (checkbox)                                                                 | –                                   |
| Dependencies       | `Dependency`              | Blocks (link to Tasks), Type (single select: ext/internal), Notes                                                                               | –                                   |
| Retros             | `Retro`                   | Project (link), Wins (long text), Fails, Action Items, Owner, Follow‑up Date                                                                    | –                                   |
| Clients (optional) | `Client`                  | Contact, Tier, Active Projects (rollup)                                                                                                         | –                                   |

### Key Field Types

* Dates: date w/ time, same timezone
* Status fields: single select with colours
* Rollups & Formulas for burndown, ROI, completion %

## 7. Views

### Ideas

* **Intake Kanban** – group by Source, sorted Created desc.
* **Ready for Triage** – filter Effort & Impact blank.

### Projects

* **Active Timeline** – Gantt view; Start → Target End.
* **2S Matrix** – grid view with Kanban lanes Ship vs Sell.
* **Roadmap Calendar** – monthly calendar of Target End.

### Tasks

* **My Tasks** – current user filter Status ≠ Done, due ≤ 7d.
* **Sprint Board** – Kanban by Status (To‑Do / In‑Progress / Review / Done).
* **Gantt** – Parent Project grouping, dependency lines.

### Sub‑tasks

* **Nested List** – grid grouped by Parent Task.

### Deliverables

* **Client Hand‑Offs** – filter Accepted? = unchecked.

### Retros

* **Retro Backlog** – upcoming follow‑ups.

## 8. Interfaces (Airtable Interface Designer)

| Interface           | Audience          | Components                                                        |
| ------------------- | ----------------- | ----------------------------------------------------------------- |
| **Home Dashboard**  | Exec              | KPIs (projects shipped, sales \$, burndown), Active Projects list |
| **Idea Capture**    | All staff         | Form with minimal required fields, submission triggers automation |
| **Project Manager** | PMs               | Timeline element, task table, dependency viewer, status buttons   |
| **My Week**         | Individuals       | Personal task list, calendar, quick‑update checkboxes             |
| **Client Portal**   | External (future) | Read‑only status of deliverables, next milestones                 |

## 9. Automations

| #   | Trigger                           | Condition                       | Action                                               |
| --- | --------------------------------- | ------------------------------- | ---------------------------------------------------- |
| A1  | **Form submission** to Ideas      | Always                          | Post Slack #ideas + assign Effort & Impact default 1 |
| A2  | **Weekly (Mon 9am)**              | Ideas where Effort/Impact blank | Send Triage reminder to PM                           |
| A3  | **Idea Status set to "Approved"** | –                               | Create linked Project record + copy key fields       |
| A4  | **Project Status → "Planning"**   | –                               | Create default task set from template via script     |
| A5  | **Task Status → "Done"**          | All sub‑tasks done              | If all project tasks done → set Project Status "QA"  |
| A6  | **Project Status → "Delivered"**  | –                               | Post Slack #wins + move to Closed after 2 weeks      |
| A7  | **Retro Follow‑up Date arrives**  | –                               | Email owner a reminder                               |

> **Scripts** (where Automations lack power):
> ‑ Task template generator (JSON config of default tasks per project type).
> ‑ Burndown calculator to write %Complete to Projects.

## 10. Immediate Action Items (Next 2 Weeks)

1. Audit current Airtable base; map to schema above (Owner: Stacks, ½‑day).
2. Create blank tables/fields using CSV import or scripting block.
3. Build views listed; hide unused fields.
4. Draft and deploy Interfaces A1–A4.
5. Build Automations A1–A4 first; mock‑test with sample data.
6. Migrate two live initiatives into new flow; field‑test edge cases.

## 11. Risks & Mitigations

* **Scope Creep:** Enforce 1‑page PRD cap during Definition.
* **Tool Fatigue:** Hide non‑essential fields/views by default.
* **API Limits:** If Airtable API hits rate limits, queue writes via N8N.

## 12. Open Questions

* Separate *Goals/OKR* table or embed goals inside Projects?
* Reporting cadence that gives visibility without noise?
* Integration path for client‑facing dashboards?

---

**Next Checkpoint:** Review progress against O1–O4 in 14 days and adjust schema/process based on field feedback.
