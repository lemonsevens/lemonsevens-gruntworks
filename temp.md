```markdown
# n8n Reference Documentation for LLM Consumption

## Section 1.1: Introduction to n8n

**Purpose:**  
n8n is a workflow automation platform designed to facilitate the connection and automation of tasks across various software applications and services. It employs a visual, node-based interface, allowing users to construct complex automation sequences with potentially minimal direct coding. Workflows are built by arranging and connecting functional blocks, known as nodes, on a digital canvas.

**Core Paradigm:**  
The fundamental interaction model within n8n revolves around its visual workflow editor. Users select nodes, representing specific actions or logic constructs, and define the sequence of operations by drawing connections between them. This visual approach abstracts much of the underlying complexity, making automation accessible to a broader range of users. While specific documentation regarding its open-source status or deployment options (cloud vs. self-hosted) was not available in the provided materials, these are common characteristics of such platforms.

**Relevance for LLM:**  
This document serves as a foundational knowledge base for a Large Language Model (LLM). It details the core principles, structural components, operational logic, data handling mechanisms, and the specific JSON format used by n8n. Understanding these elements is essential for an LLM tasked with interpreting natural language descriptions of automation requirements and translating them into valid, functional n8n workflow definitions in JSON format.

---

## Section 1.2: Core n8n Concepts

The n8n platform is built upon several fundamental concepts that work together to enable automation.

### Workflows
At the heart of n8n lies the Workflow. A workflow represents the complete definition of an automated process or task, encompassing a sequence of operations visually arranged and connected on the n8n canvas. These can range from simple two-step automations, like transferring data between applications, to highly complex processes involving multiple integrations, conditional logic, data transformations, and error handling routines. Key lifecycle actions associated with workflows include creation, saving, activation (workflows must typically be activated to run automatically via triggers), manual execution for testing or on-demand tasks, and reviewing execution history to monitor performance and debug issues. Workflows can also be exported and imported, commonly using a JSON format, facilitating sharing and version control.

### Nodes
Nodes are the atomic units of operation within an n8n workflow; they are the building blocks that perform specific actions. n8n categorizes nodes to clarify their purpose:

- **Trigger Nodes:** These initiate workflow execution. They listen for specific events or conditions, such as a schedule being met (e.g., 'Schedule Trigger'), a webhook URL receiving data (e.g., 'Webhook Trigger'), or an event occurring in an external application. A workflow typically starts with one or more trigger nodes.
- **Core Nodes:** These provide fundamental workflow logic and data manipulation capabilities. Examples include nodes for conditional branching ('If', 'Switch'), data transformation ('Set', 'Edit Fields'), merging execution paths ('Merge'), controlling flow ('Wait', 'NoOp'), executing custom code ('Function'), or handling batches of data ('SplitInBatches').
- **Action/Integration Nodes:** These nodes interact with external applications, services, and APIs. They perform actions like sending emails, creating records in a CRM, querying databases, reading/writing files, or interacting with specific SaaS platforms (e.g., Google Sheets, Slack, Asana).
- **Custom Nodes:** The platform allows for the creation of custom nodes, extending its built-in capabilities to integrate with bespoke systems or perform specialized tasks. Generating custom nodes is generally outside the scope of automated workflow generation from natural language.

### Connections
Connections are the directed links drawn between nodes in the n8n editor. They serve two primary purposes: defining the order of execution and dictating the path along which data flows through the workflow. When a node completes its operation, the resulting data is passed via its output connection(s) to the input(s) of the next connected node(s). Most nodes have a primary output ('main') for successful execution, and some may have additional outputs for different logical paths (like the 'true' and 'false' outputs of an 'If' node) or for error handling.

### Data Flow
Data processing is central to n8n workflows. Data typically flows from the trigger node through the sequence of connected nodes. Each node receives input data, performs its designated operation on that data, and then produces output data, which is passed to the subsequent node(s). n8n represents data as a structured array of items, where each item is usually a JSON object. A node might receive multiple items from a preceding node and can process them individually or collectively, potentially outputting a modified set of items, a different number of items, or summarized information. Grasping how data is structured (as items) and how it moves and transforms between nodes is crucial for configuring nodes correctly and utilizing expressions effectively.

### Credentials
To interact securely with external services and APIs, n8n uses Credentials. Credentials provide a secure mechanism to store sensitive authentication information, such as API keys, OAuth2 tokens, usernames/passwords, or other secrets, required by action/integration nodes. Instead of embedding this sensitive data directly within the workflow definition, nodes are configured to reference pre-defined credentials stored securely within the n8n instance's dedicated Credentials section. This separation enhances security and manageability, allowing credentials to be updated centrally without modifying individual workflows. n8n supports various authentication types tailored to the requirements of different services. When generating workflow JSON, the LLM must reference the type or name/ID of the required credential, not the secret itself.

### Expressions
Expressions provide a powerful mechanism for dynamic data access and manipulation within n8n workflows. Written using a JavaScript-based syntax, expressions are embedded within node parameters to perform tasks such as:
- Accessing output data from previous nodes.
- Extracting specific values from JSON data structures.
- Performing calculations or data formatting.
- Implementing conditional logic within node parameters.
- Referring to environment variables or workflow metadata.

Expressions make workflows dynamic and adaptable, allowing them to respond to the specific data being processed at runtime. The typical syntax involves double curly braces, e.g., `{{ $json.someValue }}` or `{{ $node["Previous Node Name"].json.anotherValue }}`.

The effective generation of n8n workflows requires understanding that these core concepts are deeply intertwined. A workflow's structure is defined by its nodes and the connections between them. These connections dictate the data flow path. Nodes operate on the data received through this flow, often using expressions to dynamically access data produced by earlier nodes in the sequence. Action nodes frequently rely on stored credentials to authorize their operations. Therefore, generating a valid workflow necessitates a holistic approach, ensuring that the selected nodes, their configurations (including expressions), the connections defining the data path, and any referenced credentials form a coherent and functional automation pipeline.

Furthermore, it's important to recognize the different layers of abstraction involved. Users interact with a visual canvas, arranging nodes and connections graphically. This visual representation is translated into and stored as a structured JSON document. During execution, this JSON definition is interpreted, nodes run in sequence (or parallel branches), and data items are passed between them. Expressions within the JSON are evaluated dynamically based on the data available at each step. The primary task for an LLM generating n8n workflows is to bridge the gap between a high-level, natural language description of an automation goal and the precise, structured JSON representation required by the n8n platform.

---

## Section 1.3: Workflow Structure and Execution

**Visual Canvas Representation:**  
Workflows are visually constructed on a potentially infinite canvas or grid within the n8n editor. Nodes are placed on this canvas, and connections are drawn between their input/output ports. The JSON representation of the workflow typically includes position attributes ([x, y] coordinates) for each node, preserving the visual layout when the workflow is loaded back into the editor.

**Execution Modes:**
- **Manual Execution:** Initiated directly by the user from the n8n editor, typically for testing and debugging purposes. Data for trigger nodes might need to be provided manually or mocked.
- **Production Execution:** Triggered automatically based on the configuration of the starting Trigger node(s). This could be a time-based schedule (e.g., every hour), an incoming webhook request, an event from a connected service, or other defined conditions. Active workflows run automatically based on their triggers.

**Execution Log:**  
n8n maintains a log of past workflow executions. This log is invaluable for monitoring and debugging. It typically shows the execution path taken (highlighting which nodes ran), the input and output data for each executed node, the execution time per node, and any errors encountered during the run. Analyzing the execution log helps understand if the workflow behaved as expected and pinpoint issues.

**Data Structure within Workflows:**

- **Input/Output Data:** The fundamental unit of data passed between nodes is the 'item'. A node's input data is typically an array of items (JSON objects), and its output data is also an array of items. For example, a trigger node might produce one item containing webhook data, or multiple items if triggered by multiple events simultaneously. A database query node might output multiple items, one for each row returned.
- **Data Linking:** n8n internally tracks the relationship between input items and output items for each node. This relationship depends on the node's function:
  - **1:1:** Nodes like 'Set' or 'HTTP Request' (often) process each input item individually and produce one corresponding output item.
  - **N:1:** Aggregation nodes might consume multiple input items and produce a single output item summarizing them.
  - **1:N:** Nodes like 'SplitInBatches' take one input item (or batch) and produce multiple output items.
- **Filtering:** Nodes like 'If' or 'Filter' might pass only a subset of input items to their output.
- **Paired Items (Merging):** When using a 'Merge' node to combine data from different execution branches, n8n often pairs items based on criteria like their index in the respective input arrays or a common key value. This ensures related data from different sources is combined correctly into single items.

---

## Section 1.4: Key Node Reference

This section provides details on common n8n nodes, categorized by their function. It focuses on their purpose, typical parameters, and data handling characteristics. Note that due to inaccessible external resources, this list cannot be exhaustive, particularly regarding specific application integrations. Examples are based on core functionalities and common integration patterns likely documented within the main n8n documentation.

### Trigger Nodes
Trigger nodes are the starting points of workflows, initiating execution based on specific events or conditions. Selecting the correct trigger is the first step in defining how and when an automation runs.

**Table 1: Common Trigger Nodes**

| Node Name (Type)       | Description                                             | Trigger Type                      | Key Parameters                                              | Example Output Data Structure (Conceptual)                                 |
|------------------------|---------------------------------------------------------|-----------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------|
| **Manual Trigger**     | Starts workflow execution manually from editor.       | Manual                            | N/A                                                         | `[{ "json": {} }]` (empty unless test data added)                          |
| **Schedule Trigger**   | Triggers workflow on a defined time schedule.           | Schedule                          | `triggerTimes.mode` (e.g., 'everyHour'), `triggerTimes.custom` (Cron expression) | `[{ "json": { "timestamp": "...", "runIndex": 0 } }]`         |
| **Webhook Trigger**    | Triggers workflow when an HTTP request is received.     | Webhook                           | `path`, `httpMethod` (GET, POST, etc.), authentication       | `[{ "json": { "headers": {…}, "params": {…}, "query": {…}, "body": {…} } }]` |
| **Cron**               | Similar to Schedule, uses CRON expressions.             | Schedule (Cron)                   | `cronTime`                                                  | `[{ "json": { "ts": "...", … } }]`                                          |
| **Error Trigger**      | Starts a workflow when another workflow fails.          | Event (Error)                     | `workflows` (Specify source workflow(s))                    | `[{ "json": { "error": {…}, "execution": {…}, "workflow": {…} } }]`         |

### Core Logic Nodes
These nodes form the backbone of workflow logic, enabling data manipulation, conditional execution, flow control, and custom operations. They are essential for building workflows that go beyond simple data transfers.

**Table 2: Common Core Logic Nodes**

| Node Name (Type)      | Description                                                | Use Case               | Key Parameters                                                                                         | Input/Output Data Relationship Example                                |
|-----------------------|------------------------------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **If**                | Routes items based on conditions (True/False).           | Conditional Logic      | `conditions` (complex structure defining comparisons, logic gates AND/OR)                              | Filters items (1:1 for passed items)                                    |
| **Switch**            | Routes items based on matching a value.                  | Multi-way Branching    | `fieldToMatch`, `routingRules.rules` (value -> output index mapping), `fallbackOutput`                   | Routes items (1:1 per output)                                           |
| **Merge**             | Combines item streams from different inputs.             | Merging Flows          | `mode` ('Append', 'Merge By Index', 'Merge By Key'), `joinOn.field1`, `joinOn.field2`                     | Combines items (N:M, depends on mode)                                   |
| **Set**               | Adds or modifies fields on items.                        | Data Transformation    | `valuesToSet.values` (array of field name, value/expression pairs), `keepOnlySet`                         | Modifies items (1:1)                                                    |
| **Edit Fields**       | More advanced field manipulation (rename, delete).       | Data Transformation    | `options.fields` (array defining operations like set, unset, move, duplicate)                            | Modifies items (1:1)                                                    |
| **NoOp (No Operation)** | Does nothing; useful as a placeholder or join point.     | Flow Control, Placeholder | N/A                                                                                                    | Passes items through unchanged (1:1)                                    |
| **Function**          | Executes custom JavaScript code on each item.            | Custom Code, Complex Logic | `jsCode`                                                                                                | Modifies/Replaces items (1:1 or 1:N)                                    |
| **SplitInBatches**    | Splits incoming items into batches of a fixed size.       | Looping, Batch Processing | `options.batchSize`                                                                                     | Groups items (N:M, M=N/batchSize)                                       |
| **Execute Workflow**  | Calls another n8n workflow as a sub-routine.             | Modularization, Recursion | `workflowId`                                                                                           | Depends on called workflow (N:M)                                        |

### Action/Integration Nodes
These nodes perform operations involving external systems. Limitation Note: Due to the inability to access the comprehensive integrations list, this section provides conceptual examples and common parameters rather than an exhaustive directory. The LLM should be prepared to use generic nodes like 'HTTP Request' or infer parameters for specific services based on common patterns if a dedicated node isn't explicitly known or detailed in its reference data.

**Table 3: Example Action Nodes (Conceptual & Common)**

| Node Name (Conceptual Type) | Service Category     | Common Operations      | Key Parameters (Examples)                                                                                               | Credential Type Typically Required       |
|-----------------------------|----------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| **HTTP Request**            | Generic HTTP         | GET, POST, PUT, DELETE | `url`, `method`, `authentication` (e.g., 'basicAuth', 'headerAuth', 'oAuth2'), `bodyParameters`, `queryParameters`, `options` | Varies (None, Basic, Header, OAuth2)       |
| **Send Email (Generic)**    | Email                | Send                   | `to`, `subject`, `html/text`, `from`, `attachments`                                                                       | SMTP, OAuth2 (e.g., Gmail)                |
| **SQL Database (Generic)**  | Database (SQL)       | SELECT, INSERT, UPDATE | `operation` ('executeQuery', 'executeCommand'), `query`, `database` (type: MySQL, PostgreSQL etc.), `host`, `port`, `databaseName` | Database Credentials                      |
| **Google Sheets**           | Spreadsheet          | Read, Append, Update   | `operation` ('read', 'append', 'update'), `spreadsheetId`, `sheetName`, `range`, `options` (e.g., rawData), `columns`        | Google API (OAuth2)                       |
| **Read Binary File**        | File System          | Read                   | `fileSelector.path`, `options.propertyName`                                                                             | N/A (if local), Service specific          |
| **Write Binary File**       | File System          | Write                  | `fileSelector.path`, `binaryPropertyName`, `options.createDirectories`                                                   | N/A (if local), Service specific          |

---

## Section 1.5: Advanced Concepts

### Data Handling

**Working with Multiple Items:**  
Many triggers or nodes (e.g., database queries, reading file lines, 'SplitInBatches') can output multiple items. Subsequent nodes in the main execution path will typically process each of these items one by one. Understanding this sequential processing of item arrays is key to correctly applying logic or transformations to each item individually.

**Merging Data:**  
The 'Merge' node is crucial for workflows with multiple branches (e.g., after an 'If' node). It allows combining the items produced by these different branches back into a single stream. Key modes include:
- **Append:** Simply concatenates the item lists from all inputs.
- **Merge By Index:** Pairs items based on their position (index) in the input arrays.
- **Merge By Key:** Pairs items based on matching values in specified fields.

### Looping and Branching

**Looping:**  
While n8n doesn't have a dedicated 'Loop' node like some programming languages, iteration is commonly achieved using patterns like:
- **SplitInBatches:** Processing items in manageable chunks. The 'SplitInBatches' node emits batches, and subsequent nodes process each batch. If processing needs to happen per item within the batch, a 'Function' node or further decomposition might be needed.
- **Execute Workflow:** For complex iterations or recursive patterns, a workflow can call itself or another workflow, passing data back and forth. This requires careful design to avoid infinite loops.
- **Function Node:** Custom JavaScript within a 'Function' node can implement loops over data within a single item.

**Branching:**  
Conditional execution paths are primarily handled by:
- **If Node:** Creates two branches (True, False) based on whether items meet specified conditions.
- **Switch Node:** Creates multiple branches based on the value of a specific field in the input items, routing items to different outputs accordingly.

### Error Handling

Robust workflows must anticipate and handle potential errors gracefully.

- **Error Triggers:** A dedicated 'Error Trigger' node can initiate a specific error-handling workflow whenever a designated source workflow fails. This allows for centralized error logging, notification, or remediation logic.
- **Node Settings ('Continue On Fail'):** Many nodes have an option (often found under 'Settings') like 'Continue On Fail'. If enabled, a failure in that specific node won't halt the entire workflow execution. Instead, the workflow might continue, potentially routing the error information via a dedicated error output.
- **Error Output:** Some nodes provide a dedicated error output connection (often red). If 'Continue On Fail' is enabled, data related to the failed execution (including the error details and the original input item) can be routed through this connection to a separate error-handling branch within the same workflow.

### Using Expressions Effectively

Expressions are fundamental for dynamic workflows. Mastering their syntax and capabilities is essential.

#### Syntax Deep Dive:

- **Accessing Data:**  
  - `{{ $json.key }}`: Accesses key in the JSON data of the current item being processed by the node.
  - `{{ $node["Node Name"].json.key }}`: Accesses key in the JSON data of the first item output by the node named "Node Name". Use with caution if the referenced node outputs multiple items.
  - `{{ $items("Node Name")[index].json.key }}`: Accesses key in the JSON data of the item at a specific index from the output of "Node Name".
  - `{{ $item[index].json.key }}`: Accesses data from a specific item index when merging or iterating.
- **Environment Variables:**  
  - `{{ $env.VARIABLE_NAME }}` accesses environment variables configured in the n8n instance.
- **Workflow Static Data:**  
  - `{{ $workflow.staticData.key }}` accesses data defined in the workflow's static data section.
- **JavaScript Methods:**  
  Standard JavaScript string, array, math, and date methods can often be used within expressions (e.g., `{{ $json.email.split('@') }}`, `{{ new Date().toISOString() }}`).

**Table 4: Common Expression Use Cases**

| Use Case                          | Example Expression Syntax                                    | Explanation                                                                    |
|-----------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------|
| Accessing Trigger Data            | `{{ $json.body.orderId }}` (Webhook)                         | Extracts orderId from the JSON body of an incoming webhook request.            |
| Extracting Value from JSON        | `{{ $json.customer.address.city }}`                          | Navigates a nested JSON object to get the city.                                |
| Conditional Logic (in If node)    | `{{ $json.amount > 100 }}`                                   | Evaluates to true if the 'amount' field is greater than 100.                   |
| String Formatting                 | `Order {{ $json.orderId }} received from {{ $json.customerName }}` | Concatenates static text with dynamic data values.                           |
| Basic Math                        | `{{ $json.price * $json.quantity }}`                         | Performs multiplication using values from the current item.                    |
| Accessing Loop Index (Function)   | `{{ $itemIndex }}` (Inside Function node code)               | Gets the index of the current item being processed by the Function node.       |
| Referencing Previous Node Data    | `{{ $node["Get User Data"].json.email }}`                    | Retrieves the 'email' field from the output of the "Get User Data" node.       |
| Using Environment Variable        | `{{ $env.API_ENDPOINT }}/resource`                           | Constructs a URL using a configured environment variable.                    |

Generating workflows based on user requests often involves translating high-level goals into a sequence of concrete n8n operations. A request like "Fetch new orders from Shopify, and if the order value is over $100, add the customer email to a Mailchimp list" implicitly requires several steps: a Trigger node (Shopify Trigger), potentially a node to fetch order details (HTTP Request or Shopify node), an 'If' node to check the value, and an Action node (Mailchimp node). Data must flow correctly, the condition in the 'If' node needs an appropriate expression, and the Mailchimp node requires credentials and the email extracted from the order data (likely using another expression). The LLM must be capable of inferring these necessary intermediate steps and data transformations, structuring them logically within the workflow JSON, even if not explicitly detailed in the initial user request.

---

## Section 1.6: n8n Workflow JSON Structure

Workflows created in the n8n visual editor are fundamentally represented, stored, imported, and exported as JSON objects. Understanding this structure is critical for any system aiming to generate n8n workflows programmatically, including an LLM.

### Overview:
The entire workflow definition is contained within a single JSON object. This object contains keys that define the nodes, the connections between them, workflow-level settings, and potentially static data.

### Top-Level Keys:
The primary keys at the root of the workflow JSON object are typically:

- **nodes:** An array (`[]`) where each element is an object representing a single node in the workflow.
- **connections:** An object (`{}`) defining the links between nodes. The keys of this object are the source node IDs, and the values describe the target nodes and ports for each output of the source node.
- **settings:** An object (`{}`) containing workflow-level settings (e.g., execution timezone, error workflow configuration).
- **staticData:** An object (`{}`) holding static data accessible throughout the workflow via expressions (e.g., `{{ $workflow.staticData.myValue }}`).

### Node JSON Structure:
Each object within the nodes array represents one node and contains several key fields:

- **parameters:** An object (`{}`) containing the specific configuration settings for that node type. The keys and values within parameters vary significantly depending on the node's function (e.g., URL for HTTP Request, conditions for If, code for Function). Expressions are often used as values here.
- **name:** A string representing the display name of the node in the editor (e.g., "Get User Data").
- **type:** A string identifying the node type (e.g., `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-google.sheets`). This is crucial for n8n to instantiate the correct node logic.
- **typeVersion:** An integer (1, 2, etc.) specifying the version of the node type being used.
- **position:** An array (`[x, y]`) containing two numbers representing the node's X and Y coordinates on the visual editor canvas.
- **id:** A unique string identifier (UUID format typically) for this specific node instance within the workflow. This ID is used in the connections object.
- **credentials:** An object (`{}`) used to reference stored credentials needed by the node. The structure often involves nesting the credential type as a key (e.g., `googleApi`, `httpBasicAuth`) whose value is an object containing the id and name of the credential stored in the n8n instance.  
  Example:  
  ```json
  { "googleApi": { "id": "15", "name": "My Google Credential" } }
  ```  
  Crucially, secret values are never stored here.

### Connection JSON Structure:
The connections object defines how nodes are linked. It uses the unique id of the source node as a key.

- **Format:** The value associated with a source node ID is typically an object where keys represent the output port names of the source node (e.g., `main`, `output_0`, `output_true`).
- **Targets:** The value associated with an output port name is an array (`[]`) of connections originating from that port. Each connection within this array is itself an object containing one or more target objects.
- **Target Object:** Each target object specifies the destination node and input port:  
  ```json
  { "node": "TARGET_NODE_ID", "input": "INPUT_PORT_NAME" }
  ```  
  `INPUT_PORT_NAME` is typically `main` but can vary for nodes with multiple inputs (like 'Merge').

**Example:**  
To connect the main output of node `START_NODE_ID` to the main input of node `NEXT_NODE_ID`:

```json
"connections": {
  "START_NODE_ID": {
    "main": [
      {
        "node": "NEXT_NODE_ID",
        "input": "main"
      }
    ]
  }
}
```

**Branching Example (If Node):**  
An 'If' node (`IF_NODE_ID`) might have connections like:

```json
"connections": {
  "IF_NODE_ID": {
    "output_true": [ /* connections */ ],
    "output_false": [ /* connections */ ]
  }
}
```

**Table 5: Key Elements of n8n Workflow JSON**

| JSON Path                             | Description                                                          | Data Type / Structure          | Example Value (Conceptual)                                          |
|---------------------------------------|----------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------|
| `/nodes`                              | Array containing all node objects in the workflow.                 | Array `[]`                     | `[ {node1_object}, {node2_object} ]`                                |
| `/nodes/[index]/id`                   | Unique identifier for the node instance.                            | String (UUID)                  | `"a1b2c3d4-e5f6-7890-abcd-ef0123456789"`                            |
| `/nodes/[index]/name`                 | Display name of the node in the editor.                              | String                         | `"Fetch Orders"`                                                    |
| `/nodes/[index]/type`                 | Identifier for the type of node (logic, integration).                | String                         | `"n8n-nodes-base.httpRequest"`                                      |
| `/nodes/[index]/typeVersion`          | Version of the node type implementation.                             | Integer                        | `1`                                                                 |
| `/nodes/[index]/position`             | Coordinates `[x, y]` for placing the node on the visual canvas.      | Array `[Number, Number]`       | `[860, 340]`                                                        |
| `/nodes/[index]/parameters`           | Object containing node-specific settings and configurations.         | Object `{}`                    | `{ "url": "https://...", "method": "GET", "options": {} }`           |
| `/nodes/[index]/parameters/...`       | Specific parameter value (static or an expression).                  | Varies (String, Number, etc.)  | `"{{ $json.id }}"`                                                  |
| `/nodes/[index]/credentials`          | Object referencing stored credentials by type and ID/name.           | Object `{}`                    | `{ "httpBasicAuth": { "id": "22", "name": "My API Auth" } }`          |
| `/connections`                        | Object defining all connections between nodes.                       | Object `{}`                    | `{ "SourceNodeID": { "outputPort": [ {target_object} ] } }`           |
| `/connections/[nodeId]/[outputPort]/[idx]/node` | The ID of the target node for a specific connection.             | String (UUID)                  | `"TARGET_NODE_ID"`                                                  |
| `/connections/[nodeId]/[outputPort]/[idx]/input`| The name of the input port on the target node for the connection.    | String                         | `"main"`                                                            |

**Example: Simple Two-Node Workflow (Manual Trigger -> Set Node)**

```json
{
  "nodes": [
    {
      "parameters": { },
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [820, 300],
      "id": "f1b7c3d4-e5f6-7890-abcd-ef0123456789"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "message",
              "value": "Hello World!"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [820, 400],
      "id": "a9b8c7d6-e5f4-3210-fedc-ba9876543210"
    }
  ],
  "connections": {
    "f1b7c3d4-e5f6-7890-abcd-ef0123456789": {
      "main": [
        {
          "node": "a9b8c7d6-e5f4-3210-fedc-ba9876543210",
          "input": "main"
        }
      ]
    }
  },
  "settings": {},
  "staticData": null
}
```
```