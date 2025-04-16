Story C4S-001-GIT: Establish Project Directory Structure and Git Initialization
As a developer, I want to set up the standard project directory structure and initialize Git so that code and configuration can be managed effectively under version control.

Acceptance Criteria:
- Standard directories (`src/`, `tests/`, `config/`, `output/`, `scripts/`) are created at the root level (`technology/crawl4ai-setup/`).
- A `.gitignore` file is created with common Python and environment-specific exclusions (e.g., `*.pyc`, `__pycache__/`, `.env`, `output/*`).
- The project is initialized as a Git repository (`git init` if not already done, though our project seems to be part of a larger repo).
- A basic `README.md` file is created at the project root (`technology/crawl4ai-setup/README.md`).

Dependencies: None

Developer Notes:
- Ensure directories align with common Python project layouts.
- The `planning/` directory already exists from previous steps.

---

Story C4S-002-DKR: Define Docker Environment Configuration Artifacts
As a developer, I want to prepare the `Dockerfile`, `docker-compose.yml`, and initial `.env` files, so that the service and database containers can be built and orchestrated on the target DigitalOcean server.

Acceptance Criteria:
- `technology/crawl4ai-setup/Dockerfile` is created in the repository, based on `planning/resources/Dockerfile.example`.
- `technology/crawl4ai-setup/docker-compose.yml` is created in the repository, based on `planning/resources/docker-compose.yml.example`.
- `technology/crawl4ai-setup/.env.template` (renamed from `.env`) is created by copying `planning/resources/.env.example` to serve as a template for the target server.
- The actual `.env` file (containing secrets) is added to `.gitignore`.
- **Verification (on target server):** Docker containers can be successfully built using `docker-compose build` after deploying these files and creating a `.env` file from the template.

Dependencies: C4S-001-GIT

Developer Notes:
- Ensure paths in `docker-compose.yml` are suitable for the target server deployment context.
- The `.env` file itself will be created and populated on the target server, not committed.

---

Story C4S-003-DEP: Define Core Python Dependencies and Update Dockerfile
As a developer, I want to define project dependencies in `requirements.txt` and update the `Dockerfile` to install them, so that the application image built on the target server includes necessary libraries.

Acceptance Criteria:
- `technology/crawl4ai-setup/requirements.txt` is created listing core dependencies (pinned versions recommended): `crawl4ai==0.5.0`, `asyncpg`, `Flask` or `FastAPI`, `python-dotenv`, `PyYAML`.
- The prepared `Dockerfile` is updated to copy `requirements.txt` and run `pip install -r requirements.txt`.
- **Verification (on target server):** The Docker image builds successfully using the updated `Dockerfile`.

Dependencies: C4S-002-DKR

Developer Notes:
- Pin dependency versions in `requirements.txt` for reproducibility on the target server.

---

Story C4S-004-CFG: Prepare Basic Configuration Loading Code
As a developer, I want to prepare the Python code for loading configuration from environment variables and YAML/JSON files, so that the application running on the target server can access settings.

Acceptance Criteria:
- A configuration loading module (e.g., `src/config.py`) is created in the repository.
- The module contains code using `python-dotenv` to load variables from the `.env` file (which will exist on the target server).
- The module contains code providing functions to load YAML/JSON files from the `config/` directory (mounted via volume on the target server).
- **Verification (on target server):** Basic access to DB credentials (from `.env`) and placeholder crawl parameters (from a sample config file) works when the application runs.

Dependencies: C4S-003-DEP

Developer Notes:
- Code prepares for loading; actual loading happens on the target server.

---

Story C4S-005-LOG: Prepare Basic Logging Framework Code
As a developer, I want to prepare the Python code for basic application logging configuration, so that logs can be captured effectively when running on the target server.

Acceptance Criteria:
- Python's standard `logging` module is configured within the prepared application code (e.g., `src/config.py` or main entry point).
- Configuration specifies formatting (timestamp, level, module) and directs logs to `stdout/stderr`.
- Configuration allows log level to be set via an environment variable (e.g., `LOG_LEVEL` loaded via `src/config.py`).
- **Verification (on target server):** Basic log messages are emitted to Docker logs when the application starts.

Dependencies: C4S-004-CFG

Developer Notes:
- Ensure code prepares logging suitable for Docker log collection on the target server.

---

Story C4S-006-DBI: Prepare Database Schema and Connection Code
As a developer, I want to prepare the initial PostgreSQL schema script and the Python code for async database connections, so that the database can be initialized and accessed by the application on the target server.

Acceptance Criteria:
- A SQL script (e.g., `scripts/init_db.sql`) defining initial tables (`crawl_jobs`, etc.) is created in the repository.
- A Python module (e.g., `src/database.py`) containing code for async DB connections (`asyncpg`) is created in the repository.
- The `src/database.py` module loads connection details from the configuration prepared in C4S-004-CFG.
- **Verification (on target server):** The `init_db.sql` script runs successfully against the PostgreSQL container. The application running in the `crawl4ai_service` container can establish a connection to the `postgres_db` container.

Dependencies: C4S-002-DKR, C4S-003-DEP, C4S-004-CFG

Developer Notes:
- Prepare scripts and code; execution and connection testing occur on the target server.

---

Story C4S-007-DOM: Define Core Domain Entities Code
As a developer, I want to prepare the Python data classes/models for core domain entities (`CrawlRequest`, `CrawlResult`), so that data structures are defined for use in the application code.

Acceptance Criteria:
- Python files defining `CrawlRequest` and `CrawlResult` (e.g., `src/domain/models.py`) are created in the repository.
- Classes include fields identified in the architecture with type hinting.

Dependencies: C4S-001-GIT

Developer Notes:
- This defines the structures; their usage is tested later.

---

Story C4S-008-APP: Create Skeleton Application Services & Interfaces Code
As a developer, I want to prepare the skeleton Python files/classes for core application services and interfaces, so that the application's structural foundation is present in the codebase.

Acceptance Criteria:
- Python files for services (e.g., `src/services/crawl_manager.py`, `src/services/crawl_executor.py`) containing skeleton classes/methods are created in the repository.
- Python file(s) defining interfaces (`ICrawler`, `IDataExporter`) (e.g., `src/domain/interfaces.py`) are created in the repository.

Dependencies: C4S-007-DOM

Developer Notes:
- Creates the code structure; implementation follows in later iterations.

---

Story C4S-009-CLI: Prepare Basic CLI Structure Code
As a developer, I want to prepare the basic CLI structure code using `argparse` or similar, so that a command-line interface is available for testing and interaction on the target server.

Acceptance Criteria:
- A main CLI script (e.g., `technology/crawl4ai-setup/cli.py`) defining basic subcommands (`submit`, `status`) using `argparse` is created in the repository.
- Placeholder functions are linked to subcommands.
- **Verification (on target server):** The script can be executed within the Docker container (e.g., `docker-compose exec crawl4ai_service python cli.py --help`) without errors.

Dependencies: C4S-001-GIT, C4S-003-DEP

Developer Notes:
- Prepares the CLI script; execution testing occurs on the target server.

---

Story C4S-010-API: Prepare Basic API Structure Code (Optional)
As a developer, I want to prepare the basic Flask/FastAPI application structure code with a health check endpoint, so that the foundation for webhook integration is ready for deployment.

Acceptance Criteria:
- A basic Flask/FastAPI application file (e.g., `technology/crawl4ai-setup/api.py`) defining a `/health` endpoint is created in the repository.
- `docker-compose.yml` prepared in C4S-002-DKR includes port exposure for the API service.
- **Verification (on target server):** The API application runs within the Docker container, and the `/health` endpoint is reachable and returns `200 OK`.

Dependencies: C4S-001-GIT, C4S-003-DEP

Developer Notes:
- Prepares the API script; execution and endpoint testing occur on the target server.

---

Story C4S-011-KAN: Setup Airtable Kanban Board
As a project member, I want to set up the Kanban board structure within Airtable for this project, so that scaffolding tasks can be tracked according to the chosen methodology.

Acceptance Criteria:
- A new Project record is created in the Airtable 'Projects' table (Base ID: `app9cv9ob4Qt0A8C0`) for "crawl4ai Setup".
- The Kanban view is configured for the 'Tasks' table, filtered for the "crawl4ai Setup" project.
- Columns representing workflow stages (e.g., ToDo, Doing, Done - mapped from Status field) are defined.
- Initial WIP limits are discussed and potentially set in the view or documented policy.
- Policies for 'Definition of Ready' and 'Definition of Done' for tasks are drafted.

Dependencies: None (Process task, can be done in parallel)

Developer Notes:
- This task involves configuring Airtable as described in the Methodology document. Requires Airtable access. 