Story C4S-S1-001-CLI: Implement CLI 'submit' Command Logic and Prepare for Deployment
As a developer, I want to implement the core logic for the CLI `submit` command and its interaction with the `CrawlManagerService` for job creation, preparing the code for deployment to the target server.

Acceptance Criteria:
- Code implementing the CLI `submit` subcommand to accept a target URL argument is added to `cli.py`.
- Code implementing the interaction with `CrawlManagerService` is added.
- Code implementing the `CrawlManagerService` logic to create a new record in the `crawl_jobs` table (using the DB connection prepared in C4S-006) is added.
- The code ensures the new job record includes necessary details (ID, URL, 'PENDING' status, timestamp).
- The code ensures the CLI command returns the unique Job ID upon successful creation.
- Code includes basic input validation (e.g., checking if a URL is provided).
- **Verification (on target server):** After deployment, running `cli.py submit <url>` successfully creates a 'PENDING' job record in the PostgreSQL database and outputs the Job ID.

Dependencies: C4S-006-DBI (DB Schema/Connection Prepared), C4S-008-APP (Service Skeletons Prepared), C4S-009-CLI (CLI Skeleton Prepared).
Relevant Resources: CLI Layer (`cli.py`), Application Layer (`CrawlManagerService`), Infrastructure Layer (`database.py`), PostgreSQL.
Estimated Effort: [Optional]

---

Story C4S-S1-002-EXE: Implement Single-URL Crawl Execution Logic and Prepare for Deployment
As a developer, I want to implement the core logic for the `CrawlExecutorService` to process a 'PENDING' job, execute a single-URL crawl using `crawl4ai`, and update job status, preparing the code for deployment.

Acceptance Criteria:
- Code implementing the `CrawlExecutorService` logic to handle a job (e.g., accept a job ID or object) is added.
- Code implementing the job status update to 'RUNNING' before the crawl is added.
- Code implementing the use of `crawl4ai.AsyncWebCrawler.arun` with the job's target URL is added.
- Code implementing the job status update to 'COMPLETED' (on success) or 'FAILED' (on exception) is added.
- Code implementing basic logging for job start, completion, or failure is added.
- **Verification (on target server):** After deployment and job submission via CLI, the job status transitions correctly in the database ('PENDING' -> 'RUNNING' -> 'COMPLETED'/'FAILED'), and logs reflect execution.

Dependencies: C4S-S1-001-CLI (Job creation logic prepared), C4S-003-DEP (`crawl4ai` installed in image), C4S-005-LOG (Logging code prepared), C4S-006-DBI (DB Connection code prepared), C4S-008-APP (Service Skeletons prepared).
Relevant Resources: Application Layer (`CrawlExecutorService`), Infrastructure Layer (`crawl4ai`, `database.py`, `logging`), PostgreSQL.
Estimated Effort: [Optional]

---

Story C4S-S1-003-RES: Implement Basic Result/Error Persistence Logic and Prepare for Deployment
As a developer, I want to implement the logic to store the basic markdown result or error message from a crawl in the database, preparing the code for deployment.

Acceptance Criteria:
- Code is added to `CrawlExecutorService` to extract markdown content or error message from the `crawl4ai` result/exception.
- Code is added to interact with the database (via `database.py`) to store the extracted markdown or error message in the appropriate `crawl_jobs` table column (or related table).
- The prepared database schema script (`scripts/init_db.sql`) includes the necessary columns for storing results/errors.
- **Verification (on target server):** After deployment and a job completes/fails, the corresponding result markdown or error message is correctly stored in the PostgreSQL database.

Dependencies: C4S-S1-002-EXE (Crawl execution logic prepared).
Relevant Resources: Application Layer (`CrawlExecutorService`), Infrastructure Layer (`database.py`), PostgreSQL (`crawl_jobs` table schema).
Estimated Effort: [Optional] 