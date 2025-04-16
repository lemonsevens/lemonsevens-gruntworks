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

Story C4S-002-DKR: Define Docker Environment Configuration
As a developer, I want to define the `Dockerfile` and `docker-compose.yml` files based on the examples, and create the initial `.env` file, so that the service and database containers can be built and orchestrated.

Acceptance Criteria:
- `technology/crawl4ai-setup/Dockerfile` created, based on `planning/resources/Dockerfile.example`, specifying `python:3.11-slim` base image and initial dependencies.
- `technology/crawl4ai-setup/docker-compose.yml` created, based on `planning/resources/docker-compose.yml.example`, defining `crawl4ai_service` and `postgres_db` services, networks, and volumes (`config`, `output`, `postgres_data`).
- `technology/crawl4ai-setup/.env` created by copying `planning/resources/.env.example`, with placeholder values for database credentials.
- The `.env` file is added to `.gitignore`.
- Docker containers can be built using `docker-compose build`.

Dependencies: C4S-001-GIT

Developer Notes:
- Place `Dockerfile`, `docker-compose.yml`, and `.env` in the project root (`technology/crawl4ai-setup/`).
- Update context/paths in `docker-compose.yml` if necessary (e.g., volume paths relative to compose file).

---

Story C4S-003-DEP: Install Core Python Dependencies
As a developer, I want to define project dependencies in a `requirements.txt` file and ensure they are installed in the Docker image, so that the application has access to necessary libraries.

Acceptance Criteria:
- `technology/crawl4ai-setup/requirements.txt` created listing core dependencies: `crawl4ai==0.5.0`, `asyncpg` (or alternative async PG driver), `Flask` or `FastAPI`, `python-dotenv`, `PyYAML`.
- `Dockerfile` is updated to copy `requirements.txt` into the image and run `pip install -r requirements.txt`.
- The Docker image builds successfully with dependencies installed (`docker-compose build`).

Dependencies: C4S-002-DKR

Developer Notes:
- Pin dependency versions for reproducibility.
- Consider using virtual environments locally even though Docker handles deployment environment.

---

Story C4S-004-CFG: Implement Basic Configuration Loading
As a developer, I want to implement a basic mechanism to load configuration from environment variables (`.env`) and YAML/JSON files, so that the application can access settings like database credentials and crawl parameters.

Acceptance Criteria:
- A configuration loading module (e.g., `src/config.py`) is created.
- The module uses `python-dotenv` to load variables from the `.env` file.
- The module provides functions to load YAML/JSON files from the `config/` directory (mounted via volume).
- Basic access to DB credentials and placeholder crawl parameters is demonstrated (e.g., in a test script or CLI entry point).

Dependencies: C4S-003-DEP

Developer Notes:
- Use libraries like `PyYAML` for file loading.
- Structure configuration access clearly (e.g., via a config object or dedicated functions).

---

Story C4S-005-LOG: Setup Basic Logging Framework
As a developer, I want to configure basic application logging so that events, errors, and debug information can be captured and monitored, especially within the Docker environment.

Acceptance Criteria:
- Python's standard `logging` module is configured in the application (e.g., in `src/config.py` or `src/main.py`).
- Logs are formatted to include timestamp, level, and module name.
- Logs are directed to `stdout/stderr` by default.
- Log level is configurable via an environment variable (e.g., `LOG_LEVEL`).
- Basic log messages (e.g., application start, config loaded) are emitted.

Dependencies: C4S-004-CFG

Developer Notes:
- Ensure logs are easily consumable by Docker logging drivers.

---

Story C4S-006-DBI: Initialize Database Schema and Connection
As a developer, I want to define the initial PostgreSQL database schema and establish a basic async database connection capability, so that application services can persist and retrieve job data.

Acceptance Criteria:
- A SQL script (e.g., `scripts/init_db.sql`) is created defining tables for `crawl_jobs` (with columns for ID, status, request details, timestamps) and potentially `crawl_results`.
- A Python module (e.g., `src/database.py`) is created to handle async database connections using `asyncpg` (or chosen driver).
- A function exists to apply the `init_db.sql` script (potentially run manually initially or via an entrypoint script).
- Basic connection test succeeds within the running `crawl4ai_service` container connecting to the `postgres_db` container.

Dependencies: C4S-002-DKR, C4S-003-DEP, C4S-004-CFG

Developer Notes:
- Consider using a simple schema migration tool later if schema evolves significantly (e.g., Alembic).
- Ensure DB connection details are loaded from configuration.

---

Story C4S-007-DOM: Define Core Domain Entities
As a developer, I want to define the basic Python data classes or Pydantic models for core domain entities (`CrawlRequest`, `CrawlResult`) as outlined in the architecture, so that data can be structured consistently throughout the application.

Acceptance Criteria:
- Python files defining `CrawlRequest` and `CrawlResult` (e.g., `src/domain/models.py`) are created.
- Classes include basic fields identified in the architecture (URLs, status, data placeholder, timestamps, etc.).
- Type hinting is used for clarity.

Dependencies: C4S-001-GIT

Developer Notes:
- Pydantic can be useful for data validation if complex rules are anticipated.

---

Story C4S-008-APP: Create Skeleton Application Services & Interfaces
As a developer, I want to create the skeleton Python files and classes for the core application services (`CrawlManagerService`, `CrawlExecutorService`, `DataExportService`) and their interfaces (`ICrawler`, `IDataExporter`) as defined in the architecture, so that the application structure is established.

Acceptance Criteria:
- Python files for services (e.g., `src/services/crawl_manager.py`, `src/services/crawl_executor.py`) are created.
- Skeleton classes with placeholder methods (matching architecture use cases/interfaces) are defined.
- Interfaces (`ICrawler`, `IDataExporter`) are defined (e.g., using abstract base classes or protocols in `src/domain/interfaces.py`).

Dependencies: C4S-007-DOM

Developer Notes:
- Focus on structure and interfaces; implementation details come later.

---

Story C4S-009-CLI: Implement Basic CLI Structure
As a developer, I want to implement a basic command-line interface structure using `argparse` or similar in the main script (`cli.py`), so that manual job submission or status checks can be performed for testing.

Acceptance Criteria:
- A main script (`technology/crawl4ai-setup/cli.py` or similar) is created.
- `argparse` is used to define basic subcommands (e.g., `submit`, `status`).
- Placeholder functions are called for each subcommand.
- The script can be executed within the Docker container (e.g., `docker-compose exec crawl4ai_service python cli.py --help`).

Dependencies: C4S-001-GIT, C4S-003-DEP

Developer Notes:
- This provides an essential testing and interaction mechanism before the API layer.

---

Story C4S-010-API: Implement Basic API Structure (Optional)
As a developer, I want to set up a basic Flask/FastAPI application structure with a health check endpoint, so that the foundation for webhook integration is in place.

Acceptance Criteria:
- A basic Flask/FastAPI application file (e.g., `technology/crawl4ai-setup/api.py`) is created.
- A simple `/health` endpoint is implemented that returns a `200 OK` status.
- The API application can be run within the Docker container (e.g., using `gunicorn` or `uvicorn`).
- `docker-compose.yml` is updated to expose the necessary port (e.g., 5000).

Dependencies: C4S-001-GIT, C4S-003-DEP

Developer Notes:
- Choose either Flask or FastAPI consistently. This story focuses only on the basic app setup and health check.

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