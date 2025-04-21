# 🛠️ TASK MASTER: PROJECT PLANNING WORKFLOW

This document gives the step-by-step workflow for how to plan a new project using interactive prompts.

### Overall Commands:
- `#start` – Starts a new project by executing Phase 1.
- `#continue` – Continues existing project by asking for the project directory and then launching the next appropriate phase.
- `#project-summary` – Generates/updates a `PROJECT_README.md` summary file in the project root (Phase 11).

### Phase-Specific Commands:
- `#generate-<phase>` – Starts the workflow for a specific phase (e.g., `#generate-vision`, `#generate-risks`).
- `#modify-<phase>` – Modifies the output of a specific phase (e.g., `#modify-requirements`).
- `#<phase>-status` – Shows the status within a specific phase workflow (e.g., `#requirements-status`).
- `#implement-story [ID]`, `#implement-next-step [ID]`, `#implementation-status [ID]` – Commands for Phase 9.
- `#push-to-airtable`, `#modify-airtable-task [ID]`, `#airtable-sync-status` – Commands for Phase 8 (Airtable Sync).
- `#generate-next-ideas`, `#retrospective-status` - Commands for Phase 10.

---

## 1. Vision & Goals Definition
- **Action**: Execute the interactive prompt located in `TASK-MASTER/1_vision-statement-generator.md`
- **Purpose**: Guide the creation of a clear, structured, and compelling vision statement.
- **Goal**: Clarify what success looks like for the project.
- **Output**: Vision Statement Document (`vision-statement.md`)
- **Commands**:
  - `#generate-vision` – Starts new vision statement generation
  - `#modify-vision` – Modify an existing vision statement
  - `#vision-status` – Show current progress in vision workflow

---

## 2. Scope & Requirements Gathering
- **Action**: Execute the interactive prompt located in `TASK-MASTER/2_requirements-gathering.md`
- **Purpose**: Define and document core project requirements based on the vision.
- **Goal**: Document essential features, needs, and stakeholder expectations.
- **Output**: Requirements Document (`requirements.md`)
- **Commands**:
  - `#generate-requirements` - Starts new project requirements generation
  - `#modify-requirements` - Allows modification of existing requirements
  - `#requirements-status` - Shows current progress in requirements workflow

---

## 3. Resource Selection
- **Action**: Execute the interactive prompt located in `TASK-MASTER/3_resource-selection.md`
- **Purpose**: Define and document compatible resources (tools, materials, standards, etc.) tailored to the specific project type.
- **Goal**: Establish the resources that best suit the project requirements and granular project type.
- **Output**: Resource Plan Documentation (`resource-plan.md`), Configuration/Specification Files (e.g., `resources/config.yaml`)
- **Commands**:
  - `#generate-resources` - Starts new resource plan generation
  - `#modify-resources` - Allows modification of existing resource plan
  - `#resources-status` - Shows current progress in resource planning workflow

---

## 3.5. Risk Assessment & Mitigation Planning
- **Action**: Execute the interactive prompt located in `TASK-MASTER/3.5_risk-assessment.md`
- **Purpose**: Identify, analyze, and plan mitigations for potential project risks.
- **Goal**: Proactively manage risks that could impact project success.
- **Output**: Risk Register (`risk-register.md`)
- **Commands**:
  - `#generate-risks` - Starts new risk assessment process
  - `#modify-risks` - Allows modification of the existing risk register
  - `#risk-status` - Shows current progress in risk assessment workflow

---

## 4. Methodology Selection
- **Action**: Execute the interactive prompt located in `TASK-MASTER/4_methodology-selection.md`
- **Purpose**: Select and document an appropriate project management methodology.
- **Goal**: Establish the methodology (Agile, Waterfall, Lean, etc.) that best suits the project type and characteristics.
- **Output**: Methodology Documentation (`methodology.md`)
- **Commands**:
  - `#generate-methodology` - Starts new methodology selection process
  - `#modify-methodology` - Allows modification of the selected methodology
  - `#methodology-status` - Shows current progress in methodology selection workflow

---

## 5. Architecture Design Generation
- **Action**: Execute the interactive prompt located in `TASK-MASTER/5_architecture-generator.md`
- **Purpose**: Define core architectural components using a template relevant to the specific project type.
- **Goal**: Outline fundamental structures, patterns, and relationships tailored to the project archetype.
- **Output**: Architecture Documentation (`architecture.md`), Diagram Source (`architecture/architecture.mmd`), Diagram Image (`architecture/architecture.png`)
- **Commands**:
  - `#generate-architecture` - Starts or resumes architecture design generation
  - `#architecture-status` - Shows current progress in architecture workflow

---

## 6. Initial Scaffolding Story Generation (Sprint 0)
- **Action**: Execute the interactive prompt located in `TASK-MASTER/6_initial-scaffolding-generator.md`
- **Purpose**: Generate focused user stories or tasks for the initial project setup (Sprint/Iteration 0) using project-type-specific templates. Includes defining mandatory verification criteria (e.g., unit tests, success metrics).
- **Goal**: Ensure all foundational elements (environment, core structures, tooling) are properly sequenced and verifiable.
- **Output**: Scaffolding Stories (`scaffolding-stories.md`)
- **Commands**:
  - `#generate-scaffold-stories` - Starts or resumes scaffolding story generation
  - `#scaffold-stories-status` - Shows current progress in story generation workflow

---

## 7. Iteration Planning & Story Generation (Sprint 1+)
- **Action**: Execute the interactive prompt located in `TASK-MASTER/7_full-scaffolding-generator.md`
- **Purpose**: Generate focused user stories or tasks for subsequent work iterations (Sprint/Iteration 1+) based on requirements, architecture, risks, and project type. Includes defining mandatory verification criteria.
- **Goal**: Plan the next increment of verifiable work based on requirements, architecture, dependencies, and risks.
- **Output**: Iteration Plan (`iteration-{N}-plan.md`)
- **Commands**:
  - `#generate-iteration-plan` - Starts or resumes sprint/iteration story/task generation
  - `#iteration-plan-status` - Shows current progress in story/task generation workflow

---

## 8. Project Management Synchronization (Optional - Airtable)
- **Action**: Execute the interactive prompt located in `TASK-MASTER/8_project-manager.md`
- **Purpose**: Synchronize project tasks/stories with a designated Airtable base.
- **Goal**: Maintain project visibility and tracking in Airtable.
- **Output**: Updated Airtable records (`Projects` and `Tasks` tables).
- **Commands**:
  - `#push-to-airtable` - Pushes a new project and its initial tasks/stories to Airtable.
  - `#modify-airtable-task [Task Unique ID]` - Modifies a task locally and updates Airtable.
  - `#airtable-sync-status` - Shows the Airtable synchronization status.

---

## 9. Execution & Implementation (Story/Task Level)
- **Action**: Execute the interactive prompt located in `TASK-MASTER/9_implementor.md`
- **Purpose**: Guide the step-by-step implementation of individual stories or tasks defined in `scaffolding-stories.md` or `iteration-{N}-plan.md`, ensuring mandatory verification criteria are planned for and met.
- **Goal**: Execute the planned work units and verify their completion against defined standards.
- **Output**: Implemented code/deliverables, Step Plan (`[Story/Task ID]-steps.md`), Progress updates.
- **Commands**:
  - `#implement-story [Story/Task ID]` - Analyzes a story/task and breaks it into steps.
  - `#implement-next-step [Story/Task ID]` - Plans and executes the next pending step.
  - `#implementation-status [Story/Task ID]` - Shows implementation progress for a story/task.

---

## 10. Iteration Retrospective & Next Idea Generation
- **Action**: Execute the interactive prompt located in `TASK-MASTER/10_retrospective_ideation.md`.
- **Purpose**: Analyze the project state or last iteration's outcomes and generate suggestions for the next iteration or overall improvements.
- **Goal**: Facilitate continuous improvement and inform future planning.
- **Output**: Suggestions Document (`iteration-{N+1}-ideas.md` or `project-retrospective-ideas.md`).
- **Commands**:
    - `#generate-next-ideas` - Starts the retrospective and ideation process.
    - `#retrospective-status` - Shows current progress.

---

## 11. Project Summary Reporter
- **Action**: Execute the interactive prompt located in `TASK-MASTER/11_reporter.md`.
- **Purpose**: Generate a high-level summary report (`PROJECT_README.md`) in the project root.
- **Goal**: Provide a quick overview of project status based on generated artifacts.
- **Output**: `PROJECT_README.md` file.
- **Commands**:
    - `#project-summary` - Generates or updates the summary report.

---

### Workflow Sequence:

Phase 1: Vision Statement Generation (`#generate-vision`)
↓ Output: `vision-statement.md`
Phase 2: Requirements Gathering (`#generate-requirements`)
↓ Output: `requirements.md`
Phase 3: Resource Selection (`#generate-resources`)
↓ Output: `resource-plan.md`, `resources/*`
Phase 3.5: Risk Assessment (`#generate-risks`)
↓ Output: `risk-register.md`
Phase 4: Methodology Selection (`#generate-methodology`)
↓ Output: `methodology.md`
Phase 5: Architecture Design Generation (`#generate-architecture`)
↓ Output: `architecture.md`, `architecture/architecture.mmd`, `architecture/architecture.png`
Phase 6: Initial Scaffolding Story Generation (`#generate-scaffold-stories`)
↓ Output: `scaffolding-stories.md`
Phase 7: Iteration Planning & Story Generation (`#generate-iteration-plan`)
↓ Output: `iteration-{N}-plan.md`
Phase 8: Project Management Synchronization (Optional - `#push-to-airtable`, `#modify-airtable-task`)
↓ Output: Updated Airtable Records
Phase 9: Implementation (`#implement-story`, `#implement-next-step`)
↓ Output: Progress, Code/Deliverables, `[Story/Task ID]-steps.md`
Phase 10: Retrospective & Ideation (`#generate-next-ideas`)
↓ Output: `planning/iteration-{N+1}-ideas.md`
Phase 11: Project Summary (`#project-summary`)
↓ Output: `PROJECT_README.md`