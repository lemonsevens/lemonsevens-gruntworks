# Fibery API Interaction Guide

This document provides examples and guidelines for interacting with the Fibery API, primarily using `curl` for creating schema (Databases/Types, Fields) and managing data (Entities).

**Source of Truth:** Always refer to the official Fibery API Documentation (e.g., `https://the.fibery.io/@public/User_Guide/Guide/Schema-API-261`) for the most accurate and up-to-date details. The examples below are based on common API patterns and may need adjustment.

**Complementary Tools:** For gathering prerequisite information like exact `Space` names/IDs, existing `Type` names, or detailed schema which are often needed for constructing the `curl` commands below, consider using the Fibery GraphQL tools available within environments like Cursor (e.g., `list_spaces_and_types`, `get_schema_sdl`). This can help ensure accuracy before making direct API calls.

### Domain:
`https://gruntworks.fibery.io`

### API Token:
`605bbbb5.d08eb70695e6c8d455faff55ae72d2dbf9c`

## 1. API Basics

### Base Endpoint
All API commands are typically sent to a common endpoint:
`POST [https://gruntworks.fibery.io/api/commands`


### Authentication
Authentication is done via an API Token from the `fibery-bot` user, include in the `Authorization` header:
`Authorization: f78d2ff3.c598f4e87f56393c665a5df4bc61743c314`


### Content-Type
Requests with a JSON body should include the `Content-Type` header:
`Content-Type: application/json`

## 2. Schema Manipulation

### 2.1. Creating a New Database (Type)
To create a new Database (referred to as a "Type" in the API), the recommended approach is to use a batch command that includes the type creation and necessary mixin installations. This ensures all standard fields and configurations are correctly applied.

*   **Command:** `fibery.schema/batch`
*   **Nested Commands within Batch:**
    *   `schema.type/create`: Defines the new type, its name (e.g., `SpaceName/TypeName`), primary field, custom fields, and critically, all standard Fibery system fields with their precise `fibery/meta` properties.
    *   `fibery.app/install-mixins`: Installs necessary mixins, such as `fibery/rank-mixin`.

**Example `curl` command (creating "SpaceName/MyNewDatabase"):**

```bash
curl -X POST \
  https://YOUR_WORKSPACE_NAME.fibery.io/api/commands \
  -H 'Authorization: Token YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '[{
    "command": "fibery.schema/batch",
    "args": {
      "commands": [
        {
          "command": "schema.type/create",
          "args": {
            "fibery/name": "SpaceName/MyNewDatabase", // Use "SpaceName/TypeName" format
            "fibery/meta": {
              "fibery/domain?": true, // Marks it as a main database type
              "ui/color": "#32CD32"  // Optional: sets a UI color for the type
            },
            "fibery/fields": [
              // 1. Primary Field (e.g., a Text field named "Title")
              {
                "fibery/name": "SpaceName/Title", // Field names also use "SpaceName/FieldName"
                "fibery/type": "fibery/text",
                "fibery/meta": { "ui/title?": true } // Designates this as the primary display field
              },
              // 2. Custom Fields (add as needed)
              {
                "fibery/name": "SpaceName/Description",
                "fibery/type": "fibery/text"
              },
              {
                "fibery/name": "SpaceName/DueDate",
                "fibery/type": "fibery/date"
              },
              // 3. Standard Fibery System Fields (Essential for type integrity)
              {
                "fibery/name": "fibery/id",
                "fibery/type": "fibery/uuid",
                "fibery/meta": { "fibery/id?": true, "fibery/readonly?": true }
              },
              {
                "fibery/name": "fibery/public-id",
                "fibery/type": "fibery/text",
                "fibery/meta": { "fibery/public-id?": true, "fibery/readonly?": true }
              },
              {
                "fibery/name": "fibery/creation-date",
                "fibery/type": "fibery/date-time",
                "fibery/meta": { "fibery/creation-date?": true, "fibery/readonly?": true, "fibery/default-value": "$now" }
              },
              {
                "fibery/name": "fibery/modification-date",
                "fibery/type": "fibery/date-time",
                "fibery/meta": { "fibery/modification-date?": true, "fibery/required?": true, "fibery/readonly?": true, "fibery/default-value": "$now" }
              }
            ]
          }
        },
        {
          "command": "fibery.app/install-mixins",
          "args": {
            "types": {
              "SpaceName/MyNewDatabase": ["fibery/rank-mixin"] // Ensures ranking functionality
            }
          }
        }
      ]
    }
  }]'
```

**Important Notes on Type Creation:**
*   **Naming Convention:** Always use the `SpaceName/TypeName` format for the `fibery/name` of the type and `SpaceName/FieldName` for its fields (e.g., `Admin/Config`, `Admin/Key`).
*   **Standard Fields:** Meticulously include all standard Fibery fields (`fibery/id`, `fibery/public-id`, `fibery/creation-date`, `fibery/modification-date`) with their correct `fibery/meta` properties as shown in the example. This is crucial for proper type functioning.
*   **Verification (Silent Success):** The API might return a successful HTTP status code (e.g., 200) without a detailed JSON body in the response, indicating a "silent success." Always verify the successful creation of the Type by listing types in the space (e.g., using GraphQL `list_spaces_and_types` or another query command) or checking the Fibery UI.
*   **Permissions:** Ensure the API token used has full schema manipulation permissions for the target space. Issues in restricted spaces (like "Admin") can often be permission-related.
*   **Workspace Name & Token:** Replace `YOUR_WORKSPACE_NAME.fibery.io` and `YOUR_API_TOKEN` with your actual workspace domain and API token.

### 2.2. Adding a Field to an Existing Database (Type)
If fields (especially non-primitive like relations, or complex ones) are added after Type creation:

*   **Command (Example):** `fibery.schema.internal/create-field` (Verify exact command name)
*   **Required `args`:**
    *   `type-name`: The name of the Database to add the field to.
    *   `field-definition`: An object defining the new field's name, type, and options.

**Example `curl` command (adding a Text field):**
```bash
curl -X POST \
  https://{YOUR_WORKSPACE_NAME}.fibery.io/api/commands \
  -H 'Authorization: Token YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "command": "fibery.schema.internal/create-field",
    "args": {
      "type-name": "MyNewDatabase",
      "field-definition": {
        "name": "Status",
        "type": "fibery/text" // Or "fibery/single-select" with options
        // Potentially include options for select lists, etc.
      }
    }
  }'
```
*Note: Creating relation fields often involves defining both ends of the relation and can be more complex. Refer to API docs for `relation` field types.*

## 3. Data (Entity) Manipulation

### 3.1. Creating a New Record (Entity)
To create a new record (or multiple records in a batch) within an existing Database, it's highly recommended to use a temporary JSON file for the `curl` payload. This method avoids complex shell escaping issues, especially with string values, and improves command clarity.

*   **Command:** `fibery.entity/create`
*   **Payload Structure:** The API expects each creation operation to have the target `type` (e.g., "SpaceName/TypeName") and an `entity` object containing the field-value pairs (e.g., `"SpaceName/FieldName": "value"`).

**Recommended Approach (using a temporary payload file):**

1.  **Prepare the JSON payload:** Create a file (e.g., `entity_payload.json`) containing an array of one or more `fibery.entity/create` commands.

    *Example `entity_payload.json` for creating two records in "MySpace/MyDatabase":*
    ```json
    [
      {
        "command": "fibery.entity/create",
        "args": {
          "type": "MySpace/MyDatabase",
          "entity": {
            "MySpace/Title": "First Record Title",
            "MySpace/Description": "Details for the first record.",
            "MySpace/Status": "To Do"
          }
        }
      },
      {
        "command": "fibery.entity/create",
        "args": {
          "type": "MySpace/MyDatabase",
          "entity": {
            "MySpace/Title": "Second Record Title",
            "MySpace/AnotherField": 123
          }
        }
      }
    ]
    ```

2.  **Execute `curl`:** Use the `-d @filename` option to pass the JSON payload from the file.

    *Example `curl` command:*
    ```bash
    curl -X POST \
      https://{YOUR_WORKSPACE_NAME}.fibery.io/api/commands \
      -H 'Authorization: Token YOUR_API_TOKEN' \
      -H 'Content-Type: application/json' \
      -d @entity_payload.json
    ```

**Key Considerations for Entity Creation:**
*   **Field Naming:** Ensure field names in your payload (`"SpaceName/FieldName"`) exactly match your Fibery schema.
*   **Data Types:** Values provided must match the field's expected data type (e.g., strings for text fields, numbers for numeric fields, ISO 8601 for dates if applicable).
*   **Required Fields:** If your Fibery Type has required fields, ensure they are included in the `entity` object for each record.
*   **Batching:** You can include multiple `fibery.entity/create` objects within the main JSON array in your payload file to create several entities in a single API call, as shown in the example.
*   **Error Checking:** The API response will typically be an array of objects, each corresponding to a command in your batch, indicating `"success": true` or `"success": false` with error details.

### 3.2. Querying Records (Entities)
To retrieve records from a Database:

*   **Command (Example):** `fibery.entity/query` (Verify exact command name from your `mcp_fibery-mcp-server_query_database` tool's underlying API)
*   **Required `args` (example structure):**
    *   `from`: The name of the Database to query.
    *   `select`: An array or object defining which fields to retrieve.
    *   `where`: (Optional) A filter expression.
    *   `limit`: (Optional) Number of records to return.

**Example `curl` command:**
```bash
curl -X POST \
  https://{YOUR_WORKSPACE_NAME}.fibery.io/api/commands \
  -H 'Authorization: Token YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "command": "fibery.entity/query",
    "args": {
      "from": "MyNewDatabase",
      "select": [
        "Title",
        "Description",
        "DueDate",
        "fibery/id" // To get the Fibery ID
      ],
      "where": ["=", ["Title"], "My First Record via API"], // Example filter
      "limit": 10
    }
  }'
```

## 4. Important Considerations
*   **Error Handling:** Check API responses for status codes and error messages.
*   **Rate Limiting:** Be aware of any API rate limits.
*   **Field Names:** Ensure field names in your API calls exactly match the names in your Fibery schema (these are often `Namespace/FieldName` like `YourSpace/Status`). The `mcp_fibery-mcp-server_describe_database` tool can help get correct field names.
*   **Data Types:** Ensure data provided matches the expected type for each field (e.g., ISO format for dates, correct structure for relation updates).

This guide should provide a good starting point. Remember to cross-reference with the official Fibery documentation for precision. 