# 🛠️ TASK MASTER: PROJECT PLANNER TOOL

This document provides instructions on how to use the interactive project planning workflow facilitated by specialized AI prompts. The workflow guides you through defining, planning, and setting up a project step-by-step.

## Overview

The workflow consists of several phases, each managed by a specific prompt file located in the `TASK-MASTER` directory. You interact with the workflow by issuing commands (hashtags) in your chat interface. Each phase builds upon the outputs of the previous ones, creating a comprehensive set of planning documents.

## Getting Started

To begin planning a new project, use the `#start` command, which initiates the Vision & Goals Definition phase.

```
#start
```

To continue working on an existing project where some planning documents already exist, use the `#continue` command. You will be prompted for the project directory location.

```
#continue
```

## Workflow Phases & Commands

Below are the phases of the project planning workflow and the primary commands used to interact with each phase. Status commands (`#<phase>-status`) are generally available to check progress within a phase. Modification commands (`#modify-<phase>`) allow revisiting and changing outputs.

*Note: The tool now supports more granular project types (e.g., Web Application, Marketing Campaign) which tailor resource suggestions, architecture templates, and task generation.* 

**Overall Project Commands:**
- `#start`: Initiate planning for a new project (Starts Phase 1).
- `#continue`: Resume planning for an existing project.
- `#project-summary`: Generate/update a `PROJECT_README.md` file in the project root summarizing the status based on planning artifacts (Phase 11).

---

**Phase 1: Vision & Goals Definition**
- **Purpose**: Define a clear and compelling vision statement for the project.
- **Prompt File**: `TASK-MASTER/1_vision-statement-generator.md`
- **Output**: `vision-statement.md`
- **Commands**:
    - `#generate-vision`: Start creating a new vision statement.
    - `#modify-vision`: Change an existing vision statement.
    - `#vision-status`: Check progress on the vision statement.

---

**Phase 2: Scope & Requirements Gathering**
- **Purpose**: Document the core project requirements based on the vision.
- **Prompt File**: `TASK-MASTER/2_requirements-gathering.md`
- **Output**: `requirements.md`
- **Commands**:
    - `#generate-requirements`: Start gathering requirements.
    - `#modify-requirements`: Change existing requirements.
    - `#requirements-status`: Check progress on requirements.

---

**Phase 3: Resource Selection**
- **Purpose**: Identify and document necessary resources (tools, standards, materials) tailored to the specific project type.
- **Prompt File**: `TASK-MASTER/3_resource-selection.md`
- **Output**: `resource-plan.md`, Configuration/Specification files (e.g., `resources/config.yaml`)
- **Commands**:
    - `#generate-resources`: Start defining the resource plan.
    - `#modify-resources`: Change the existing resource plan.
    - `#resources-status`: Check progress on resource planning.

---

**Phase 3.5: Risk Assessment & Mitigation Planning**
- **Purpose**: Identify potential project risks, analyze their likelihood and impact, and plan mitigation strategies.
- **Prompt File**: `TASK-MASTER/3.5_risk-assessment.md`
- **Output**: `risk-register.md`
- **Commands**:
    - `#generate-risks`: Start identifying and analyzing risks.
    - `#modify-risks`: Change the existing risk register.
    - `#risk-status`: Check progress on risk assessment.

---

**Phase 4: Methodology Selection**
- **Purpose**: Choose and document an appropriate project management methodology.
- **Prompt File**: `TASK-MASTER/4_methodology-selection.md`
- **Output**: `methodology.md`
- **Commands**:
    - `#generate-methodology`: Start the methodology selection process.
    - `#modify-methodology`: Change the selected methodology.
    - `#methodology-status`: Check progress on methodology selection.

---

**Phase 5: Architecture Design Generation**
- **Purpose**: Define the core architectural components using a template relevant to the specific project type.
- **Prompt File**: `TASK-MASTER/5_architecture-generator.md`
- **Output**: `architecture.md`, Diagram Source (`architecture/architecture.mmd`), Diagram Image (`architecture/architecture.png`)
- **Commands**:
    - `#generate-architecture`: Start or resume architecture design.
    - `#architecture-status`: Check progress on architecture design.

---

**Phase 6: Initial Scaffolding Story Generation (Sprint 0)**
- **Purpose**: Create tasks/stories for the foundational project setup (environment, core structures) using templates specific to the project type. Tasks include mandatory verification criteria (e.g., unit tests, success metrics).
- **Prompt File**: `TASK-MASTER/6_initial-scaffolding-generator.md`
- **Output**: `scaffolding-stories.md`
- **Commands**:
    - `#generate-scaffold-stories`: Start generating initial setup stories/tasks.
    - `#scaffold-stories-status`: Check progress on scaffolding story generation.

---

**Phase 7: Iteration Planning & Story Generation (Sprint 1+)**
- **Purpose**: Generate tasks/stories for subsequent work iterations based on requirements, architecture, risks, and project type. Tasks include mandatory verification criteria.
- **Prompt File**: `TASK-MASTER/7_full-scaffolding-generator.md`
- **Output**: `iteration-{N}-plan.md`
- **Commands**:
    - `#generate-iteration-plan`: Start planning stories/tasks for the next iteration.
    - `#iteration-plan-status`: Check progress on iteration planning.

---

**Phase 8: Project Management Synchronization (Optional - Airtable)**
- **Purpose**: Synchronize project tasks/stories with a designated Airtable base.
- **Prompt File**: `TASK-MASTER/8_project-manager.md`
- **Output**: Updated Airtable records.
- **Requires**: Airtable integration configured.
- **Commands**:
    - `#push-to-airtable`: Push project and tasks to Airtable.
    - `#modify-airtable-task [Task Unique ID]`: Update a specific task in Airtable and the local file.
    - `#airtable-sync-status`: Check Airtable synchronization status.

---

**Phase 9: Execution & Implementation (Story/Task Level)**
- **Purpose**: Guide the step-by-step implementation of individual stories or tasks, ensuring verification criteria are met.
- **Prompt File**: `TASK-MASTER/9_implementor.md`
- **Output**: Implemented code/deliverables, Step Plan (`[Story/Task ID]-steps.md`).
- **Commands**:
    - `#implement-story [Story/Task ID]`: Analyze a story/task and break it into implementation steps.
    - `#implement-next-step [Story/Task ID]`: Plan and execute the next pending implementation step.
    - `#implementation-status [Story/Task ID]`: Show implementation progress for a story/task.

---

**Phase 10: Iteration Retrospective & Next Idea Generation**
- **Purpose**: Analyze the completed iteration or overall project state to generate suggestions for the next iteration's focus and improvements.
- **Prompt File**: `TASK-MASTER/10_retrospective_ideation.md`
- **Output**: Suggestions document (`iteration-{N+1}-ideas.md` or `project-retrospective-ideas.md`)
- **Commands**:
    - `#generate-next-ideas`: Start the retrospective and ideation process.
    - `#retrospective-status`: Check progress on this phase.

---

**Phase 11: Project Summary Reporter**
- **Purpose**: Generate a high-level summary report (`PROJECT_README.md`) in the project root, consolidating information from planning and task artifacts.
- **Prompt File**: `TASK-MASTER/11_reporter.md`
- **Output**: `PROJECT_README.md` in the project root directory.
- **Commands**:
    - `#project-summary`: Generate or update the project summary report.

---

Follow the phases sequentially using the provided commands to structure your project planning process. Use `#project-summary` periodically to get a high-level overview.

© 2025 Gruntworks. All rights reserved.
