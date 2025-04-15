# Interactive Project Planning Workflow

This document provides instructions on how to use the interactive project planning workflow facilitated by specialized AI prompts. The workflow guides you through defining, planning, and setting up a project step-by-step.

## Overview

The workflow consists of several phases, each managed by a specific prompt file located in the `operations/project-planning/` directory. You interact with the workflow by issuing commands (hashtags) in your chat interface. Each phase builds upon the outputs of the previous ones, creating a comprehensive set of planning documents.

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

---

**Phase 1: Vision & Goals Definition**
- **Purpose**: Define a clear and compelling vision statement for the project.
- **Prompt File**: `operations/project-planning/1_vision-statement-generator.md`
- **Output**: `vision-statement.md`
- **Commands**:
    - `#generate-vision`: Start creating a new vision statement.
    - `#modify-vision`: Change an existing vision statement.
    - `#vision-status`: Check progress on the vision statement.

---

**Phase 2: Scope & Requirements Gathering**
- **Purpose**: Document the core project requirements based on the vision.
- **Prompt File**: `operations/project-planning/2_requirements-gathering.md`
- **Output**: `requirements.md`
- **Commands**:
    - `#generate-requirements`: Start gathering requirements.
    - `#modify-requirements`: Change existing requirements.
    - `#requirements-status`: Check progress on requirements.

---

**Phase 3: Resource Selection**
- **Purpose**: Identify and document necessary resources (tools, standards, materials).
- **Prompt File**: `operations/project-planning/3_resource-selection.md`
- **Output**: `resource-plan.md`, Configuration/Specification files (e.g., `resources/config.yaml`)
- **Commands**:
    - `#generate-resources`: Start defining the resource plan.
    - `#modify-resources`: Change the existing resource plan.
    - `#resources-status`: Check progress on resource planning.

---

**Phase 4: Methodology Selection**
- **Purpose**: Choose and document an appropriate project management methodology.
- **Prompt File**: `operations/project-planning/4_methodology-selection.md`
- **Output**: `methodology.md`
- **Commands**:
    - `#generate-methodology`: Start the methodology selection process.
    - `#modify-methodology`: Change the selected methodology.
    - `#methodology-status`: Check progress on methodology selection.

---

**Phase 5: Architecture Design Generation**
- **Purpose**: Define the core architectural components for initial project scaffolding.
- **Prompt File**: `operations/project-planning/5_architecture-generator.md`
- **Output**: `architecture.md`, Diagram Source (`architecture/architecture.mmd`), Diagram Image (`architecture/architecture.png`)
- **Commands**:
    - `#generate-architecture`: Start or resume architecture design.
    - `#architecture-status`: Check progress on architecture design.

---

**Phase 6: Initial Scaffolding Story Generation (Sprint 0)**
- **Purpose**: Create tasks/stories for the foundational project setup (environment, core structures).
- **Prompt File**: `operations/project-planning/6_initial-scaffolding-generator.md`
- **Output**: `scaffolding-stories.md`
- **Commands**:
    - `#generate-scaffold-stories`: Start generating initial setup stories/tasks.
    - `#scaffold-stories-status`: Check progress on scaffolding story generation.

---

**Phase 7: Iteration Planning & Story Generation (Sprint 1+)**
- **Purpose**: Generate tasks/stories for subsequent work iterations based on requirements and architecture.
- **Prompt File**: `operations/project-planning/7_full-scaffolding-generator.md`
- **Output**: `iteration-{N}-plan.md`
- **Commands**:
    - `#generate-iteration-plan`: Start planning stories/tasks for the next iteration.
    - `#iteration-plan-status`: Check progress on iteration planning.

---

**Phase 8: Project Management Synchronization (Optional - Airtable)**
- **Purpose**: Synchronize project tasks/stories with a designated Airtable base.
- **Prompt File**: `operations/project-planning/8_project-manager.md`
- **Output**: Updated Airtable records.
- **Requires**: Airtable integration configured.
- **Commands**:
    - `#push-to-airtable`: Push project and tasks to Airtable.
    - `#modify-airtable-task [Task Unique ID]`: Update a specific task in Airtable and the local file.
    - `#airtable-sync-status`: Check Airtable synchronization status.

---

**Phase 9: Execution & Implementation (Story/Task Level)**
- **Purpose**: Guide the step-by-step implementation of individual stories or tasks.
- **Prompt File**: `operations/project-planning/9_implementor.md`
- **Output**: Implemented code/deliverables, Step Plan (`[Story/Task ID]-steps.md`).
- **Commands**:
    - `#implement-story [Story/Task ID]`: Analyze a story/task and break it into implementation steps.
    - `#implement-next-step [Story/Task ID]`: Plan and execute the next pending implementation step.
    - `#implementation-status [Story/Task ID]`: Show implementation progress for a story/task.

---

**Phase 10: Quality Assurance & Testing**
- **Purpose**: Verify deliverables meet requirements and acceptance criteria.
- **Process**: Typically manual or tool-assisted, following the defined methodology.
- **Output**: Test results, bug reports, feedback.

---

**Phase 11: Evaluation & Continuous Improvement**
- **Purpose**: Assess project outcomes against goals and document lessons learned.
- **Process**: Manual review and retrospective meetings.
- **Output**: Project evaluation reports, lessons learned documentation.

---

Follow the phases sequentially using the provided commands to structure your project planning process.

© 2025 Gruntworks. All rights reserved.
