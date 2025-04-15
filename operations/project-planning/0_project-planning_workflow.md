# 🛠️ PROJECT SCAFFOLDING & PLANNING WORKFLOW

This document gives the step-by-step workflow for how to plan a new project using interactive prompts.

### Commands:
- `#start` – Starts a new project by **executing the interactive prompt defined in** `operations/project-planning/vision-statement-generator.md`
- `#continue` – Continues existing project by asking the location of the project directory and then launching the requirements gathering prompt  
---

## 1. Vision & Goals Definition
- **Action**: Execute the interactive prompt located in `operations/project-planning/1_vision-statement-generator.md`
- **Purpose**: Guide the creation of a clear, structured, and compelling vision statement.
- **Goal**: Clarify what success looks like for the project.
- **Output**: Vision Statement Document (`vision-statement.md`)
- **Commands**:
  - `#generate-vision` – Starts new vision statement generation
  - `#modify-vision` – Modify an existing vision statement
  - `#vision-status` – Show current progress in vision workflow

---

## 2. Scope & Requirements Gathering
- **Action**: Execute the interactive prompt located in `operations/project-planning/2_requirements-gathering.md`
- **Purpose**: Define and document core project requirements based on the vision.
- **Goal**: Document essential features, needs, and stakeholder expectations.
- **Output**: Requirements Document (`requirements.md`)
- **Commands**:
  - `#generate-requirements` - Starts new project requirements generation
  - `#modify-requirements` - Allows modification of existing requirements
  - `#requirements-status` - Shows current progress in requirements workflow

---

## 3. Resource Selection
- **Action**: Execute the interactive prompt located in `operations/project-planning/3_resource-selection.md`
- **Purpose**: Define and document compatible resources (tools, materials, standards, etc.).
- **Goal**: Establish the resources that best suit the project requirements.
- **Output**: Resource Plan Documentation (`resource-plan.md`), Configuration/Specification Files (e.g., `resources/config.yaml`)
- **Commands**:
  - `#generate-resources` - Starts new resource plan generation
  - `#modify-resources` - Allows modification of existing resource plan
  - `#resources-status` - Shows current progress in resource planning workflow

---

## 4. Methodology Selection
- **Action**: Execute the interactive prompt located in `operations/project-planning/4_methodology-selection.md`
- **Purpose**: Select and document an appropriate project management methodology.
- **Goal**: Establish the methodology (Agile, Waterfall, Lean, etc.) that best suits the project type and characteristics.
- **Output**: Methodology Documentation (`methodology.md`)
- **Commands**:
  - `#generate-methodology` - Starts new methodology selection process
  - `#modify-methodology` - Allows modification of the selected methodology
  - `#methodology-status` - Shows current progress in methodology selection workflow

---

## 5. Architecture Design Generation
- **Action**: Execute the interactive prompt located in `operations/project-planning/5_architecture-generator.md`
- **Purpose**: Define core architectural components for initial project scaffolding.
- **Goal**: Outline fundamental structures, patterns, and relationships.
- **Output**: Architecture Documentation (`architecture.md`), Diagram Source (`architecture/architecture.mmd`), Diagram Image (`architecture/architecture.png`)
- **Commands**:
  - `#generate-architecture` - Starts or resumes architecture design generation
  - `#architecture-status` - Shows current progress in architecture workflow

---

## 6. Initial Scaffolding Story Generation (Sprint 0)
- **Action**: Execute the interactive prompt located in `operations/project-planning/6_initial-scaffolding-generator.md`
- **Purpose**: Generate focused user stories or tasks for the initial project setup (Sprint/Iteration 0).
- **Goal**: Ensure all foundational elements (environment, core structures, tooling) are properly sequenced.
- **Output**: Scaffolding Stories (`scaffolding-stories.md`)
- **Commands**:
  - `#generate-scaffold-stories` - Starts or resumes scaffolding story generation
  - `#scaffold-stories-status` - Shows current progress in story generation workflow

---

## 7. Iteration Planning & Story Generation (Sprint 1+)
- **Action**: Execute the interactive prompt located in `operations/project-planning/7_full-scaffolding-generator.md`
- **Purpose**: Generate focused user stories or tasks for subsequent work iterations (Sprint/Iteration 1+).
- **Goal**: Plan the next increment of work based on requirements, architecture, and dependencies.
- **Output**: Iteration Plan (`iteration-{N}-plan.md`)
- **Commands**:
  - `#generate-iteration-plan` - Starts or resumes sprint/iteration story/task generation
  - `#iteration-plan-status` - Shows current progress in story/task generation workflow

---

## 8. Project Management Synchronization (Optional - Airtable)
- **Action**: Execute the interactive prompt located in `operations/project-planning/8_project-manager.md`
- **Purpose**: Synchronize project tasks/stories with a designated Airtable base.
- **Goal**: Maintain project visibility and tracking in Airtable.
- **Output**: Updated Airtable records (`Projects` and `Tasks` tables).
- **Commands**:
  - `#push-to-airtable` - Pushes a new project and its initial tasks/stories to Airtable.
  - `#modify-airtable-task [Task Unique ID]` - Modifies a task locally and updates Airtable.
  - `#airtable-sync-status` - Shows the Airtable synchronization status.

---

## 9. Execution & Implementation (Story/Task Level)
- **Action**: Execute the interactive prompt located in `operations/project-planning/9_implementor.md`
- **Purpose**: Guide the step-by-step implementation of individual stories or tasks defined in `scaffolding-stories.md` or `iteration-{N}-plan.md`.
- **Goal**: Execute the planned work units.
- **Output**: Implemented code/deliverables, Step Plan (`[Story/Task ID]-steps.md`), Progress updates.
- **Commands**:
  - `#implement-story [Story/Task ID]` - Analyzes a story/task and breaks it into steps.
  - `#implement-next-step [Story/Task ID]` - Plans and executes the next pending step.
  - `#implementation-status [Story/Task ID]` - Shows implementation progress for a story/task.

---

## 10. Quality Assurance & Testing
- Verify that each component meets the requirements and acceptance criteria.
- Conduct appropriate testing (unit, integration, user acceptance) or quality checks.
- **Output**: QA/Testing reports, Bug fixes, Feedback logs

---

## 11. Evaluation & Continuous Improvement
- Assess project outcomes against the original vision and goals upon completion or at key milestones.
- Document lessons learned, successes, and areas for future improvement.
- **Output**: Project Evaluation Report, Retrospective notes

---

### Workflow Sequence:

Phase 1: Vision Statement Generation (`#generate-vision`)
↓ Output: `vision-statement.md`
Phase 2: Requirements Gathering (`#generate-requirements`)
↓ Output: `requirements.md`
Phase 3: Resource Selection (`#generate-resources`)
↓ Output: `resource-plan.md`, `resources/*`
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
Phase 10: Quality Assurance & Testing (Manual/Tool-Assisted)
↓ Output: Test Results, Feedback
Phase 11: Evaluation & Continuous Improvement (Manual)
↓ Output: Reports, Lessons Learned