Story C4S-S2-001-CLISubmitBatch: Add 'submit-batch' CLI Subcommand
As a developer/user, I want a new CLI subcommand `submit-batch` that accepts a file path containing URLs, so that I can easily initiate crawl jobs for multiple URLs listed in a file.

Acceptance Criteria:
- A new subcommand `submit-batch` is added to the CLI structure (`cli.py` using `argparse`).
- The `submit-batch` command accepts a required argument `--file <path>`.
- Code implementing the handler function for `submit-batch` is added.
- The handler includes logic to check if the specified file exists and is readable.
- **Verification (on target server):** Running `cli.py submit-batch --file path/to/urls.txt` parses correctly. Running without `--file` or with a non-existent file path produces an appropriate error.

Dependencies: C4S-009-CLI (CLI Skeleton Prepared).
Relevant Resources: CLI Layer (`cli.py`).
Estimated Effort: [Optional]

---

Story C4S-S2-002-BatchJobCreate: Implement Batch Job Creation Logic
As a developer, I want the `submit-batch` command handler to read URLs from the specified file and create individual crawl jobs for each URL using the existing `CrawlManagerService`, so that batch submissions are correctly recorded for later processing.

Acceptance Criteria:
- The `submit-batch` handler reads the file specified by `--file`, expecting one URL per line.
- The handler iterates through the list of URLs read from the file.
- For each URL, the handler calls the existing `CrawlManagerService.submit_job` method (prepared in Iteration 1).
- The handler prints the submitted URL and the corresponding Job ID returned by `submit_job` to the console for each submission.
- Basic error handling for invalid URL format during iteration can be included (e.g., log a warning and skip).
- **Verification (on target server):** Running `cli.py submit-batch --file path/to/urls.txt` creates multiple 'PENDING' job records (one per valid URL) in the PostgreSQL database and prints the URL/Job ID pairs to the console.

Dependencies: C4S-S1-001-CLI (Job Creation Logic Prepared), C4S-S2-001-CLISubmitBatch (New subcommand structure).
Relevant Resources: CLI Layer (`cli.py`), Application Layer (`CrawlManagerService`), Infrastructure Layer (`database.py`), PostgreSQL.
Estimated Effort: [Optional]

---

Story C4S-S2-003-StatusOutput: Enhance CLI 'status' Command to Save Output
As a developer/user, I want the CLI `status` command to have an option to save the crawl result (markdown or error message) to a file in the shared output volume, so that I can easily access the full crawl output.

Acceptance Criteria:
- The existing `status` subcommand in `cli.py` is modified to accept an optional argument `--output-file <filename>`.
- The handler function for `status` fetches the job details (including result/error) using `CrawlManagerService.get_job_status`.
- If `--output-file <filename>` is provided:
    - The handler checks if markdown content or an error message is available in the job result.
    - The handler constructs the full path within the container's mapped output volume (e.g., `/app/output/<filename>`).
    - The handler writes the available markdown content or error message to the specified file path.
    - A confirmation message (e.g., "Result saved to output/<filename>") is printed to the console.
- If `--output-file` is *not* provided, the handler prints the status details and result/error to the console as it did previously.
- **Verification (on target server):** Running `cli.py status <job_id>` works as before. Running `cli.py status <job_id> --output-file my_result.md` creates `my_result.md` in the host's mapped `./output` directory containing the job's result/error, and prints a confirmation.

Dependencies: C4S-S1-003-RES (Result Persistence Logic Prepared).
Relevant Resources: CLI Layer (`cli.py`), Application Layer (`CrawlManagerService`), Docker Volume (`./output`), Filesystem I/O.
Estimated Effort: [Optional]

---

Story C4S-S2-004-DocUpdate: Update README Documentation
As a developer, I want to update the project's README file to document the new `submit-batch` command and the `--output-file` option for the `status` command, so that users understand how to use the new features.

Acceptance Criteria:
- The `technology/crawl4ai-setup/README.md` file is updated.
- The documentation clearly explains the usage of `cli.py submit-batch --file <path>`.
- The documentation clearly explains the usage of `cli.py status <job_id> --output-file <filename>`.
- Examples are provided for both commands.

Dependencies: C4S-S2-001-CLISubmitBatch, C4S-S2-003-StatusOutput.
Relevant Resources: `README.md`.
Estimated Effort: [Optional] 