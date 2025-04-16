Story C4S-S1-001-CLI: Implement CLI 'submit' Command and Job Creation
As a developer/user, I want to use the CLI `submit` command to provide a URL and initiate a crawl job, so that jobs can be created and tracked in the system via the command line.

Acceptance Criteria:
- CLI `submit` subcommand accepts a target URL argument.
- Calling `submit <url>` interacts with `CrawlManagerService`.
- `CrawlManagerService` creates a new record in the `crawl_jobs` table in PostgreSQL.
- The new job record has a unique ID, the provided URL, an initial status of 'PENDING', and a creation timestamp.
- The CLI command outputs the unique Job ID upon successful creation.
- Basic input validation exists (e.g., checking if a URL is provided).

Dependencies: C4S-006-DBI (DB Schema/Connection), C4S-008-APP (Service Skeletons), C4S-009-CLI (CLI Skeleton).
Relevant Resources: CLI Layer (`cli.py`), Application Layer (`CrawlManagerService`), Infrastructure Layer (`database.py`), PostgreSQL.
Estimated Effort: [Optional]

---

Story C4S-S1-002-EXE: Execute Single-URL Crawl and Update Job Status
As the system, I want to process a 'PENDING' job by executing a crawl using `crawl4ai` and updating the job status, so that crawl jobs are actively processed and their lifecycle (Running, Completed, Failed) is tracked.

Acceptance Criteria:
- `CrawlExecutorService` picks up a 'PENDING' job (initial trigger mechanism can be simple, e.g., integrated into the `submit` flow for now).
- Job status is updated to 'RUNNING' in the PostgreSQL `crawl_jobs` table before starting the crawl.
- `CrawlExecutorService` uses `crawl4ai.AsyncWebCrawler.arun` with the job's target URL.
- Upon successful completion of `arun`, the job status is updated to 'COMPLETED' in the DB.
- If `arun` raises an exception, the job status is updated to 'FAILED' in the DB.
- Basic logging indicates job start, completion, or failure.

Dependencies: C4S-S1-001-CLI (Job creation), C4S-003-DEP (`crawl4ai` installed), C4S-005-LOG (Logging), C4S-006-DBI (DB Connection), C4S-008-APP (Service Skeletons).
Relevant Resources: Application Layer (`CrawlExecutorService`), Infrastructure Layer (`crawl4ai`, `database.py`, `logging`), PostgreSQL.
Estimated Effort: [Optional]

---

Story C4S-S1-003-RES: Persist Basic Crawl Result or Error to Database
As the system, I want to store the markdown content from a successful crawl or the error message from a failed crawl in the database, so that the fundamental output or failure reason for each crawl job is persisted.

Acceptance Criteria:
- If a crawl completes successfully (status 'COMPLETED'), the markdown content from the `crawl4ai` result is stored in the `crawl_jobs` table (e.g., in a `result_markdown` text column) or a linked `crawl_results` table.
- If a crawl fails (status 'FAILED'), the error message/details are stored in the `crawl_jobs` table (e.g., in an `error_message` text column).
- Database schema (`init_db.sql`) is updated if necessary to include columns for results/errors.
- Data is successfully persisted and can be retrieved (e.g., via a simple DB query or CLI status check).

Dependencies: C4S-S1-002-EXE (Crawl execution and status update).
Relevant Resources: Application Layer (`CrawlExecutorService`), Infrastructure Layer (`database.py`), PostgreSQL (`crawl_jobs` table schema).
Estimated Effort: [Optional] 