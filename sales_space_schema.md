# Fibery Workspace Schema: Sales Space

This document outlines the structure of the **Sales** space in your Fibery workspace.

## Space: Sales

### Types and Fields:

#### 1. Type: `Sales/ClientSegment`
   - **Description:** Represents different segments of clients (e.g., Enterprise, SMB).
   - **Fields:**
     - `fibery/id`: ID (Read-only, System Generated)
     - `fibery/public-id`: Text (Read-only, System Generated)
     - `fibery/creation-date`: Date (Read-only, System Generated)
     - `fibery/modification-date`: Date (Read-only, System Generated)
     - `fibery/rank`: Number (Read-only, System Generated)
     - `Sales/Name`: Text
     - `Sales/Icon`: Text (Stores an icon identifier or URL)
     - `Sales/Description`: Rich Text
     - `Sales/Companies`: Relation (One-to-Many with `Sales/Company`) - *Note: This represents the companies belonging to this segment.*
   - **Default/Queried Entities:**
     - Name: Enterprise, Icon: (icon_value_if_known_or_NA)
     - Name: SMB, Icon: (icon_value_if_known_or_NA)
     - Name: Startup, Icon: (icon_value_if_known_or_NA)
     - Name: Mid-Size, Icon: (icon_value_if_known_or_NA)
     *(Actual icon values were present in the query but are generalized here for brevity)*

#### 2. Type: `Sales/ClientWorkflowState`
   - **Description:** Defines the stages in a client's lifecycle or a deal's progression, aligning with the revised sales process.
   - **Fields:**
     - `fibery/id`: ID (Read-only, System Generated)
     - `fibery/public-id`: Text (Read-only, System Generated)
     - `fibery/creation-date`: Date (Read-only, System Generated)
     - `fibery/modification-date`: Date (Read-only, System Generated)
     - `fibery/rank`: Number (Read-only, System Generated)
     - `Sales/Name`: Text (e.g., "New Lead (Raw)", "Nurturing - Post Demo Follow-up") - *This is the granular name of the state (SDL: name: String).*
     - `Sales/StateCategory`: Single-Select (related to `SalesCategorySalesClientWorkflowState`, e.g., "Prospecting," "Active Sales," "Nurturing," "Closed") - *For high-level grouping. Options: "Pre-Engagement," "Prospecting," "Active Sales," "Active Client," "Nurturing," "Closed".*
     - `Sales/IsFinal`: Checkbox (Boolean - True if this is a terminal state for a typical flow).
     - `Sales/DefaultNextState`: Relation (Many-to-One with `Sales/ClientWorkflowState` - Optional) - *Can help guide users or automate transitions.*
     - `Sales/DefaultPreviousStates`: Relation (One-to-Many with `Sales/ClientWorkflowState`) - *Represents states for which this state is the default next state (auto-generated back-relation).*
     - `Sales/DescriptionPurpose`: Rich Text (SDL: description: RichField) - *To clarify the meaning and criteria for each state.*
     - `Sales/Companies`: Relation (One-to-Many with `Sales/Company`) - *Note: This represents the companies currently in this workflow state.*
   - **Default/Queried Entities (This is the complete list of states to be created/updated based on the Work Order):**
     - **Pre-Engagement Category:**
       - SpecificStateName: "Identified Target", StateCategory: "Pre-Engagement", IsFinal: false
     - **Prospecting Category:**
       - SpecificStateName: "New Lead (Raw)", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Enriching", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Lead - Verified", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Contacted (Delivery Confirmed)", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Contact Failed (Delivery Issue)", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Inbound Lead - Auto Qualified", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Inbound Lead - Pending Qualification Review", StateCategory: "Prospecting", IsFinal: false
       - SpecificStateName: "Qualified", StateCategory: "Prospecting", IsFinal: false
     - **Active Sales Category:**
       - SpecificStateName: "Demo Scheduled", StateCategory: "Active Sales", IsFinal: false
       - SpecificStateName: "Demo No Show", StateCategory: "Active Sales", IsFinal: false
       - SpecificStateName: "Tier Selection & Agreement", StateCategory: "Active Sales", IsFinal: false
       - SpecificStateName: "Proposal - Custom/Automation", StateCategory: "Active Sales", IsFinal: false
       - SpecificStateName: "Contract - Custom/Automation", StateCategory: "Active Sales", IsFinal: false
     - **Nurturing Category:**
       - SpecificStateName: "Nurturing - Awaiting Response (Initial Outreach)", StateCategory: "Nurturing", IsFinal: false
       - SpecificStateName: "Nurturing - Qualified Gone Cold (Pre-Demo)", StateCategory: "Nurturing", IsFinal: false
       - SpecificStateName: "Nurturing - Post Demo Follow-up", StateCategory: "Nurturing", IsFinal: false
       - SpecificStateName: "Nurturing - Stalled Tier Selection", StateCategory: "Nurturing", IsFinal: false
       - SpecificStateName: "Nurturing - Stalled Proposal (Custom/Automation)", StateCategory: "Nurturing", IsFinal: false
       - SpecificStateName: "Nurturing - Long Term (Lost Deal)", StateCategory: "Nurturing", IsFinal: false
       - SpecificStateName: "Nurturing - Churned Client Re-engagement", StateCategory: "Nurturing", IsFinal: false
     - **Active Client Category:**
       - SpecificStateName: "Onboarding", StateCategory: "Active Client", IsFinal: false
       - SpecificStateName: "First Impact", StateCategory: "Active Client", IsFinal: false
       - SpecificStateName: "Managing", StateCategory: "Active Client", IsFinal: false
       - SpecificStateName: "Max Impact", StateCategory: "Active Client", IsFinal: false
     - **Closed Category:**
       - SpecificStateName: "Enrichment Failed - Unusable", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Unreachable", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Unresponsive (Initial Outreach)", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Not Interested (Initial Contact)", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Not Qualified", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Closed Lost - Post Demo", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Closed Lost - Proposal Rejected (Custom/Automation)", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Closed Lost - Contract Stage (Custom/Automation)", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Do Not Contact", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Churned", StateCategory: "Closed", IsFinal: true
       - SpecificStateName: "Churned - DNC", StateCategory: "Closed", IsFinal: true

#### 3. Type: `Sales/Company`
   - **Description:** Represents client companies or potential leads.
   - **Fields (based on schema and PRD, with Work Order updates):**
     - `fibery/id`: ID (Read-only, System Generated)
     - `fibery/public-id`: Text (Read-only, System Generated)
     - `fibery/creation-date`: Date (Read-only, System Generated)
     - `fibery/modification-date`: Date (Read-only, System Generated)
     - `fibery/rank`: Number (Read-only, System Generated)
     - `fibery/created-by`: User (Relation to `fibery/User`, System Generated)
     - `Sales/Name`: Text (Company Name)
     - `Sales/Description`: Rich Text
     - `Sales/Short description`: Text
     - `Sales/Industry`: Text (Fibery type: String)
     - `Sales/Website`: URL (Fibery type: String)
     - `Sales/Employees`: Number (Fibery type: Integer or Decimal/Float)
     - `Sales/ARR`: Number (Annual Recurring Revenue, Fibery type: Integer or Decimal/Float)
     - `Sales/Source`: Text (Lead Source, Fibery type: String)
     - `Sales/Segment`: Relation (Many-to-One with `Sales/ClientSegment`)
     - `Sales/WorkflowState`: Relation (Many-to-One with `Sales/ClientWorkflowState`) - *Salespeople select the `Sales/Name` (SpecificStateName) via this relation.*
     - `Sales/Tier`: Single-Select, options TBD
     - `Sales/Deals`: Relation (One-to-Many with `Sales/Deal`)
     - `Sales/Projects`: Relation (One-to-Many with `Ship/Project`)
     - `Sales/Contact Name`: Text
     - `Sales/Email`: Email (Fibery type: String)
     - `Sales/Contact Phone`: Phone (Fibery type: String)
     - `Sales/Address`: Text (Fibery type: String)
     - `Sales/LastOutreachMethod`: Single-Select (Related to `SalesLastOutreachMethodSalesCompany`) - *Options: "Cold Email," "Cold Call," "Social DM - LinkedIn," "Social DM - Twitter," "Social DM - Facebook," "Social DM - Instagram," "Other DM," "Referral," "Inbound Web Form," "Event."*
     - `Sales/Sales person`: Relation (Many-to-Many with `fibery/User`)
     - `Sales/ClientSegments`: Relation (Many-to-Many with `Sales/ClientSegment`) - *Auto-generated back-relation.*
     - `Sales/ClientWorkflowStates`: Relation (Many-to-Many with `Sales/ClientWorkflowState`) - *Auto-generated back-relation.*
   - **Default/Queried Entities:** (None explicitly queried for this type in the current context, beyond those created for deals)

#### 4. Type: `Sales/DealType`
   - **Description:** Defines distinct types of deals to manage different sales processes.
   - **Fields:**
     - `fibery/id`: ID (Read-only, System Generated)
     - `fibery/public-id`: Text (Read-only, System Generated)
     - `fibery/creation-date`: Date (Read-only, System Generated)
     - `fibery/modification-date`: Date (Read-only, System Generated)
     - `fibery/rank`: Number (Read-only, System Generated)
     - `Sales/Name`: Text (e.g., "New Client Acquisition (Productized)")
   - **Default/Queried Entities (Examples based on Work Order):**
     - Name: "New Client Acquisition (Productized)"
     - Name: "New Client Acquisition (Custom/Enterprise)"
     - Name: "Upsell/Cross-Sell (Existing Client)"

#### 5. Type: `Sales/Deal`
   - **Description:** Represents sales opportunities.
   - **Fields (based on schema and PRD, with Work Order updates):**
     - `fibery/id`: ID (Read-only, System Generated)
     - `fibery/public-id`: Text (Read-only, System Generated)
     - `fibery/creation-date`: Date (System field, likely read-only)
     - `fibery/modification-date`: Date (System field, likely read-only)
     - `fibery/rank`: Number (Read-only, System Generated)
     - `Sales/Name`: Text (Deal Name)
     - `Sales/Client`: Relation (Many-to-One with `Sales/Company`) - *Primary company for the deal.*
     - `Sales/DealTypeRelation`: Relation (Many-to-One with `Sales/DealType`) - *Specifies the type of deal (SDL: dealTypeRelation: SalesDealType).*
     - `Sales/Amount`: Number (Currency, SDL: amount: Float)
     - `Sales/Probability %`: Number (Percent, SDL: probability: Int)
     - `Sales/Stage`: Single-Select (Related to `SalesStageSalesDeal`, e.g., Proposal, Contract. Options TBD) - *Review if its purpose is covered by `Sales/ClientWorkflowState` on Company. May represent sub-stages or be deprecated if `Sales/WorkflowState` on Deal was intended.*
     - `Sales/Close Date`: Date (SDL: closeDate: String)
     - `Sales/Owner`: Users (Relation Many-to-Many with `fibery/User`)
     - `Sales/Notes`: Rich Text (SDL: notes: RichField)
     - `Sales/Next Action`: Text (SDL: nextAction: String)
     - *Note: `Sales/WorkflowState` was previously documented for `Sales/Deal` but is not present in the current Fibery SDL for this type.*
   - **Default/Queried Entities:** (The four deals created previously would be listed here if we re-queried them, e.g., "Enterprise Website Redesign", "SMB E-commerce Integration", etc.)

### Views:

Information on specific Views within the Sales space (e.g., Kanban boards, tables, lists) is best obtained by inspecting the Fibery UI for the Sales space. The API methods used so far primarily detail the data schema (types and fields) rather than the UI configurations of views.

---

*This document is based on the schema information retrieved programmatically, the work order, and discussions about intended structure. Some field types or relations might have been manually adjusted in Fibery by the user, or may require specific Fibery configurations (e.g. setting up Single-Select options).* 