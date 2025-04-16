# Architecture Documentation: crawl4ai Setup Service

## 1. Overview
A brief description of the overall architecture: A Dockerized Python service utilizing `crawl4ai` for web scraping, orchestrated via a CLI and/or a simple REST API (for webhooks). It uses PostgreSQL for job/result persistence and relies on Docker volumes for configuration and file exports. The core service leverages `asyncio` for efficient crawling.

## 2. Architectural Pattern
- **Pattern:** Simple Async Service with Layered Internal Structure
- **Rationale:** Balances simplicity, maintainability, and performance for the project scope. Leverages `asyncio` for I/O-bound tasks (crawling, DB interaction) and aligns with Docker deployment. Avoids premature complexity of microservices or full event-driven patterns.

## 3. Core Components / Services
- **`crawl4ai_service` (Docker Container):** The main service hosting the Python application.
  - **`CrawlManagerService`:** Handles job lifecycle (submission, status tracking).
  - **`CrawlExecutorService`:** Executes crawls using `crawl4ai.AsyncWebCrawler` (`arun`, `arun_many`).
  - **`DataExportService`:** Manages exporting results (DB, CSV, JSON).
  - **`(Optional) WebhookApiService` (Flask/FastAPI):** Exposes HTTP endpoints for job submission/status.
  - **`CLIService` (main script):** Provides command-line interface.
- **`postgres_db` (Docker Container):** Hosts the PostgreSQL database.
- **(External) Webhook Caller (e.g., N8N):** Triggers the service via the API Layer.
- **(External) User/Admin:** Interacts via CLI or triggers via Webhook Caller.

## 4. Layers (within `crawl4ai_service`)
- **API Layer:** Handles incoming HTTP requests (Flask/FastAPI).
- **CLI Layer:** Handles command-line arguments and execution.
- **Application Layer:** Contains core services (`CrawlManagerService`, `CrawlExecutorService`, `DataExportService`) coordinating use cases.
- **Domain Layer:** Defines core entities (`CrawlRequest`, `CrawlResult`), interfaces (`ICrawler`, `IDataExporter`), and business rules.
- **Infrastructure Layer:** Handles interactions with external systems (PostgreSQL via async driver, `crawl4ai` library for HTTP, file system via Docker volumes).

## 5. Data Flow & Component Interactions
- **Webhook Trigger:** N8N -> API Layer -> `CrawlManagerService` -> Persist Job (DB) -> Async Task Queue -> `CrawlExecutorService` -> `crawl4ai` -> Target Website -> `CrawlExecutorService` -> Update Job Status (DB) -> `DataExportService` -> Persist Results (DB/File).
- **CLI Trigger:** User -> CLI Layer -> `CrawlManagerService` -> ... (similar flow as above).
- **Data Persistence:** Services interact with PostgreSQL via async drivers. File exports written to Docker volumes.

## 6. Key Integration Points
- **`crawl4ai` Library:** Used by `CrawlExecutorService`.
- **PostgreSQL Database:** Accessed by multiple services for job state and results.
- **API Layer:** Interface for external webhook callers.
- **Docker Volumes:** Used for configuration (`config`), output files (`output`), and database persistence (`postgres_data`).
- **Docker Network:** Enables communication between `crawl4ai_service` and `postgres_db`.

## 7. Cross-cutting Concerns
- **Configuration:** `.env` file + YAML/JSON config files.
- **Logging:** Standard Python `logging` to container `stdout/stderr`.
- **Error Handling:** Service-level error handling, logging, status updates in DB.
- **Security:** SSH access, DB credentials, optional API key.

## 8. Deployment View
- Two Docker containers (`crawl4ai_service`, `postgres_db`) managed by `docker-compose.yml`.
- Runs on a DigitalOcean Droplet (Ubuntu LTS).
- Persistent data stored in Docker volumes.
- Access controlled via SSH and optional API security. 