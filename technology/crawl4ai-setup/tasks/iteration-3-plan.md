# Iteration 3 Plan: API Layer and Advanced Features

**Goal:** Implement a comprehensive API layer for Crawl4AI, supporting single and batch submissions, specific extraction parameters, authenticated access, and enhanced callback functionality, including features initially deemed out-of-scope.

**Project:** [Crawl4AI API Layer Setup](<AIRTABLE_PROJECT_LINK_IF_AVAILABLE - currently recC8GeAaCgM7cWyd>)

---

## Stories / Tasks

**[ ] C4S-S3-001-APIInit: Initialize and Configure API Layer**
*   **Description:** As a developer, I want to initialize the Flask/FastAPI application structure, configure its basic settings, and ensure it runs within the Docker service, building upon the scaffolding task (C4S-010).
*   **Acceptance Criteria:**
    *   Flask/FastAPI app instance created in `api.py`.
    *   Basic configuration (e.g., from environment variables) is loaded.
    *   A `/health` endpoint exists and returns 200 OK.
    *   The API application runs successfully within the `crawl4ai_service` container using a production server (like `gunicorn` or `uvicorn`).
    *   `docker-compose.yml` correctly exposes the API port.
    *   **Code changes are tested locally (e.g., basic run, health check test) and committed to Git.**
    *   **Verification (on target server):** API starts and health endpoint is accessible after deployment.
*   **Dependencies:** C4S-010-API (API Skeleton Prepared).
*   **Relevant Resources:** `api.py`, `docker-compose.yml`, `Dockerfile` (add API server dependency).
*   **Airtable Task:** [Link to C4S-S3-001](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recQl04qFdJjunSzy>)

---

**[ ] C4S-S3-002-APISubmitSingle: Implement API Endpoint for Single URL Submission**
*   **Description:** As a developer, I want to implement a `/submit` API endpoint that accepts a JSON payload with a single URL and an optional callback URL, so external workflows can initiate individual crawl jobs.
*   **Acceptance Criteria:**
    *   A POST `/submit` endpoint is created in the API (`api.py`).
    *   Endpoint accepts JSON body like `{"url": "http://example.com", "callback_url": "http://optional/callback"}`.
    *   Endpoint validates the presence and basic format of the `url`.
    *   Endpoint calls `CrawlManagerService.submit_job` to create a 'PENDING' job record in the DB, storing the `callback_url` if provided.
    *   Endpoint immediately returns a JSON response like `{"job_id": "rec..."}`.
    *   **Code changes are tested locally (e.g., unit tests for endpoint logic, mock service calls) and committed to Git.**
    *   **Verification (on target server):** Calling the endpoint successfully creates a job in the DB and returns a job ID. Invalid requests return appropriate errors (e.g., 400) after deployment.
*   **Dependencies:** C4S-S3-001-APIInit, C4S-S1-001-CLI (Job Creation Logic).
*   **Relevant Resources:** `api.py`, `CrawlManagerService`.
*   **Airtable Task:** [Link to C4S-S3-002](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recqhC8EUivbGpCu4>)

---

**[ ] C4S-S3-003-APISubmitBatchList: Implement API Endpoint for Batch URL List Submission**
*   **Description:** As a developer, I want to implement a `/submit-batch` API endpoint that accepts a JSON payload with a list of URLs and an optional callback URL, so external workflows can initiate multiple crawl jobs efficiently.
*   **Acceptance Criteria:**
    *   A POST `/submit-batch` endpoint is created in the API (`api.py`).
    *   Endpoint accepts JSON body like `{"urls": ["http://a.com", "http://b.com"], "callback_url": "http://optional/callback"}`.
    *   Endpoint validates the presence and format of the `urls` list.
    *   Endpoint calls `CrawlManagerService` (using logic similar to C4S-S2-002) to create individual 'PENDING' job records for each valid URL, storing the `callback_url` with each.
    *   Endpoint immediately returns a JSON response like `{"job_ids": ["rec...", "rec..."]}`.
    *   **Code changes are tested locally (e.g., unit tests for endpoint logic) and committed to Git.**
    *   **Verification (on target server):** Calling the endpoint successfully creates multiple jobs in the DB and returns their IDs after deployment.
*   **Dependencies:** C4S-S3-001-APIInit, C4S-S2-002-BatchJobCreate (Batch Job Creation Logic).
*   **Relevant Resources:** `api.py`, `CrawlManagerService`.
*   **Airtable Task:** [Link to C4S-S3-003](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recXVWOaVfaAhtexe>)

---

**[ ] C4S-S3-004-APIStatus: Implement API Endpoint for Job Status and Results**
*   **Description:** As a developer, I want to implement a `/status/{job_id}` API endpoint that returns the current status and, if completed/failed, the persisted results (markdown or error), so external workflows can poll for job outcomes.
*   **Acceptance Criteria:**
    *   A GET `/status/{job_id}` endpoint is created in the API (`api.py`).
    *   Endpoint retrieves job details from `CrawlManagerService` (or DB).
    *   If job not found, returns 404.
    *   If job pending/running, returns JSON like `{"job_id": "...", "status": "RUNNING"}`.
    *   If job completed/failed, returns JSON like `{"job_id": "...", "status": "COMPLETED", "result": "...", "error": null}` or `{"job_id": "...", "status": "FAILED", "result": null, "error": "..."}`.
    *   **Code changes are tested locally (e.g., unit tests with mock data for different job statuses) and committed to Git.**
    *   **Verification (on target server):** Calling the endpoint with different job IDs returns the correct status and data based on the job's state in the DB after deployment.
*   **Dependencies:** C4S-S3-001-APIInit, C4S-S1-003-RES (Result Persistence Logic).
*   **Relevant Resources:** `api.py`, `CrawlManagerService`.
*   **Airtable Task:** [Link to C4S-S3-004](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recUtvyrRZ7rNrh3f>)

---

**[ ] C4S-S3-005-CallbackBasic: Implement Basic Webhook Callback on Job Completion**
*   **Description:** As the system, I want to attempt sending a POST request to a job's specified `callback_url` when the job finishes (Completed or Failed), so the originating workflow can be notified without polling.
*   **Acceptance Criteria:**
    *   `CrawlExecutorService` (or a new dedicated service) checks if a `callback_url` exists for the job upon completion/failure.
    *   If a URL exists, the service makes an asynchronous HTTP POST request to that URL.
    *   The POST request body contains JSON payload with `job_id`, `status`, `result` (if completed), and `error` (if failed).
    *   The callback is "fire-and-forget" for this story (no complex error handling or retries yet).
    *   **Code changes are tested locally (e.g., mock the callback trigger, check logged request attempt) and committed to Git.**
    *   **Verification (on target server):** A job submitted via API with a valid `callback_url` triggers a POST request to that URL upon completion/failure (verified using a mock receiver) after deployment.
*   **Dependencies:** C4S-S1-002-EXE (Job Execution Logic), C4S-S3-002-APISubmitSingle (Storing callback_url).
*   **Relevant Resources:** `CrawlExecutorService` (or new callback service), HTTP client library (e.g., `aiohttp`).
*   **Airtable Task:** [Link to C4S-S3-005](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently reckP0boaBlbMOSXR>)

---

**[ ] C4S-S3-006-APIExtractionParams: Allow Specific Extraction Config via API**
*   **Description:** As a developer, I want to modify the API submit endpoints (`/submit`, `/submit-batch`) to accept an optional `extraction_config` object, so workflows can request specific data extraction beyond the default markdown.
*   **Acceptance Criteria:**
    *   `/submit` and `/submit-batch` endpoints are updated to accept an optional `extraction_config` field in the JSON payload (structure mirroring `crawl4ai`'s config).
    *   `CrawlManagerService` is updated to store this `extraction_config` with the job record in the DB.
    *   `CrawlExecutorService` is updated to retrieve the `extraction_config` for a job and pass it to `crawl4ai.AsyncWebCrawler.arun` or `arun_many`.
    *   If `extraction_config` is not provided in the API request, the default `crawl4ai` behavior (markdown extraction) is used.
    *   **Code changes are tested locally (e.g., unit tests verifying config is passed correctly) and committed to Git.**
    *   **Verification (on target server):** Submitting a job via API with a valid `extraction_config` (e.g., a simple CSS selector schema) results in the specifically extracted data being stored (per C4S-S1-003) after deployment.
*   **Dependencies:** C4S-S3-002-APISubmitSingle, C4S-S3-003-APISubmitBatchList, C4S-S1-002-EXE (Job Execution Logic).
*   **Relevant Resources:** `api.py`, `CrawlManagerService`, `CrawlExecutorService`, `crawl4ai`, PostgreSQL (schema potentially needs update for config storage).
*   **Airtable Task:** [Link to C4S-S3-006](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recS6T5Tsf1V9umMg>)

---

**[ ] C4S-S3-007-CallbackRobust: Enhance Webhook Callback Reliability**
*   **Description:** As the system, I want the webhook callback mechanism to include basic retry logic and improved error logging, so notification delivery is more reliable.
*   **Acceptance Criteria:**
    *   The callback sending logic (from C4S-S3-005) is enhanced.
    *   If the initial POST request fails (e.g., timeout, non-2xx response), the system attempts a configurable number of retries (e.g., 2 retries) with a short delay (e.g., 10 seconds).
    *   Errors during callback attempts (including final failure after retries) are logged clearly with job ID and target callback URL.
    *   **Code changes are tested locally (e.g., unit tests simulating callback failures) and committed to Git.**
    *   **Verification (on target server):** Test with a temporarily unavailable callback receiver; verify retries occur and errors are logged. Test with a working receiver; verify successful delivery after deployment.
*   **Dependencies:** C4S-S3-005-CallbackBasic.
*   **Relevant Resources:** Callback sending logic (in `CrawlExecutorService` or dedicated service), `logging`, async HTTP client.
*   **Airtable Task:** [Link to C4S-S3-007](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recyxtc3bR38exrOH>)

---

**[ ] C4S-S3-008-APISubmitBatchFile: Implement API Endpoint for Batch File Upload**
*   **Description:** As a developer, I want to implement a `/submit-batch-file` API endpoint that accepts a file upload containing URLs, providing an alternative to submitting a JSON list for batch jobs.
*   **Acceptance Criteria:**
    *   A POST `/submit-batch-file` endpoint is created in the API (`api.py`).
    *   Endpoint accepts `multipart/form-data` including a file field (e.g., `url_file`) and an optional `callback_url` field.
    *   Endpoint reads the uploaded file content, expecting one URL per line.
    *   Endpoint calls `CrawlManagerService` (using logic similar to C4S-S2-002) to create individual 'PENDING' job records for each valid URL, storing the `callback_url`.
    *   Endpoint returns a JSON response like `{"job_ids": ["rec...", "rec..."]}`.
    *   **Code changes are tested locally (e.g., unit tests simulating file uploads) and committed to Git.**
    *   **Verification (on target server):** Uploading a text file with URLs via this endpoint successfully creates multiple jobs in the DB and returns their IDs after deployment.
*   **Dependencies:** C4S-S3-001-APIInit, C4S-S2-002-BatchJobCreate (Batch Job Creation Logic).
*   **Relevant Resources:** `api.py` (requires handling file uploads in Flask/FastAPI), `CrawlManagerService`.
*   **Airtable Task:** [Link to C4S-S3-008](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently rec2nALRmUxpXmrUu>)

---

**[ ] C4S-S3-009-APIAuth: Implement API Key Authentication**
*   **Description:** As a developer, I want to secure the API endpoints using a simple API key mechanism, so that only authorized clients can submit jobs or check status.
*   **Acceptance Criteria:**
    *   API requires clients to send an API key in a specific HTTP header (e.g., `X-API-Key`).
    *   A list of valid API keys is stored securely (e.g., in the `.env` file on the target server, loaded via `config.py`).
    *   Middleware or a decorator is implemented in the API (`api.py`) to check for the presence and validity of the API key on incoming requests to protected endpoints (`/submit`, `/submit-batch`, `/submit-batch-file`, `/status`).
    *   If the key is missing or invalid, the API returns a 401 Unauthorized or 403 Forbidden error.
    *   The `/health` endpoint remains accessible without authentication.
    *   **Code changes are tested locally (e.g., unit tests for auth middleware/decorator) and committed to Git.**
    *   **Verification (on target server):** Calls to protected endpoints without/with invalid API keys fail. Calls with valid keys succeed. `/health` remains open after deployment.
*   **Dependencies:** C4S-S3-001-APIInit, C4S-004-CFG (Config loading prepared).
*   **Relevant Resources:** `api.py` (middleware/decorators), `config.py`, `.env` file on server.
*   **Airtable Task:** [Link to C4S-S3-009](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently reclLCtHxX0HiD8og>)

---

**[ ] C4S-S3-010-DocUpdate: Update README for API and Advanced Features**
*   **Description:** As a developer, I want to significantly update the project's README file to document all Iteration 3 features, including all API endpoints, authentication, parameters, callback mechanism, and usage examples, so users and integrators have comprehensive documentation.
*   **Acceptance Criteria:**
    *   The `technology/crawl4ai-setup/README.md` file is updated in the repository.
    *   Documents all new API endpoints (`/submit`, `/submit-batch`, `/submit-batch-file`, `/status/{job_id}`, `/health`).
    *   Explains request/response formats for each endpoint, including `extraction_config` parameter.
    *   Details the API key authentication mechanism (`X-API-Key` header).
    *   Explains the optional `callback_url` parameter and the callback behavior.
    *   Provides clear examples using tools like `curl` to interact with the API.
    *   Includes notes on how an external tool like N8N or Cursor Agent could potentially consume the API.
    *   **Documentation changes are committed to Git.**
*   **Dependencies:** All other C4S-S3-* stories.
*   **Relevant Resources:** `README.md`.
*   **Airtable Task:** [Link to C4S-S3-010](<AIRTABLE_TASK_LINK_IF_AVAILABLE - currently recmZWNDtCFdhf54H>) 