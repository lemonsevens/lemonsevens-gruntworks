# Implementation Steps for Task LOS-002-b: Verify and Configure Airtable CRM for Landscaping Outreach

1.  Confirm Airtable Base ID and Table IDs: Verify the Base ID (`app9cv9ob4Qt0A8C0`) and identify the Table IDs for 'Accounts' and 'Contacts' using `mcp_airtable_tools_list_tables`.
2.  List Existing Fields in 'Accounts' Table: Use `mcp_airtable_tools_list_tables` (or its detailed output if already available) to retrieve the current schema/fields for the 'Accounts' table.
3.  Identify Missing 'Accounts' Fields: Compare the existing fields from Step 2 with the required list: 'Target Profile Match Status', 'Region', 'Company Size Est.', 'Data Source Notes'. Document which ones are missing.
4.  Create Missing 'Accounts' Fields: For each missing field identified in Step 3, use `mcp_airtable_tools_create_field` to add it to the 'Accounts' table. Choose appropriate field types (e.g., singleSelect, singleLineText, number).
5.  List Existing Fields in 'Contacts' Table: Use `mcp_airtable_tools_list_tables` (or its detailed output) to retrieve the current schema/fields for the 'Contacts' table.
6.  Identify Missing 'Contacts' Fields: Compare the existing fields from Step 5 with the required list: 'Decision Maker Role', 'Outreach Status', 'Last Tactic Used', 'Best Contact Method', 'Gatekeeper Notes'. Document which ones are missing.
7.  Create Missing 'Contacts' Fields: For each missing field identified in Step 6, use `mcp_airtable_tools_create_field` to add it to the 'Contacts' table. Choose appropriate field types.
8.  Verify Field Creation: Briefly re-list tables/fields or use `mcp_airtable_tools_list_tables` again to confirm all required fields now exist in both tables.

## Dependencies between steps:
*   Step 3 depends on Step 2.
*   Step 4 depends on Step 3.
*   Step 6 depends on Step 5.
*   Step 7 depends on Step 6.
*   Step 8 depends on Step 4 and Step 7.
*   Steps 2-4 (Accounts) can run in parallel with Steps 5-7 (Contacts) after Step 1 is complete. 