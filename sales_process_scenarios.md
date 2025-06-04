# Sales Process Scenarios

This document outlines the various scenarios and paths a company can take as it moves through our sales system, from initial targeting to post-conversion and potential churn. Our goal is a simplified yet comprehensive process aligning with Gruntworks' productized offerings and full-funnel client management. While this document details all possible states, the specific path a company/deal takes will often be guided by its assigned "Deal Type" in the CRM (e.g., `New Client Acquisition (Productized)`, `New Client Acquisition (Custom/Enterprise)`, or `Upsell/Cross-Sell (Existing Client)`).

## 0. Pre-Engagement & Targeting

### 1. Identified Target
   - **Trigger:** Proactive identification of a potential mid-size landscaping company aligning with Gruntworks' Ideal Customer Profile (ICP) through market research, list building, or other strategic sourcing. This is the first point of entry into the CRM for such proactively sourced potentials, representing a company that appears promising but requires further internal review or strategic planning before active outreach begins.
   - **Initial State:** `Sales/ClientWorkflowState` = "Identified Target"
   - **Category:** Pre-Engagement (Signifying it's on the radar but not yet in active sales pursuit)
   - **Company Attributes Recorded (Minimum):**
     - `Sales/Default Next State`: "New Lead (Raw)"
     - `Sales/Default Previous States`: (None)
     - `Sales/Name` (Company Name)
     - `Sales/Website` (if readily available)
     - `Sales/Status`: "Pre-Engagement" (Initial status for a targeted company)
     - Initial notes on ICP fit.
   - **Next Action:** Detailed Data Enrichment and first contact strategy planning. Once a decision is made to actively pursue, it transitions to "New Lead (Raw)".

## I. Lead Intake & Data Enrichment

### 2. New Raw Lead Identified (Renamed from "1. New Raw Lead Identified")
   - **Trigger:** Company data formally enters the active sales pipeline within the system. This occurs when:
     - An "Identified Target" is approved for active pursuit and transitioned from the Pre-Engagement stage.
     - A lead arrives via other channels (e.g., web form, list import where immediate prospecting is intended, manual entry by sales for an immediate opportunity, referral).
   - **Initial State:** `Sales/ClientWorkflowState` = "New Lead (Raw)"
   - **Category:** Prospecting (Signifying the start of active efforts to enrich, contact, and qualify)
   - **Company Attributes Recorded (Minimum, if not already from "Identified Target"):**
     - `Sales/Default Next State`: "Enriching"
     - `Sales/Default Previous States`: "Identified Target"
     - `Sales/Name` (Company Name)
     - `Sales/Source` (Lead Source)
     - `Sales/Status`: "Prospecting"
     - `Sales/Contact Name` (if available)
     - `Sales/Email` (if available)
     - `Sales/Contact Phone` (if available)
   - **Next Action:** Data Enrichment.

### 3. Data Enrichment Process (Renamed from "2. Data Enrichment Process")
   - **Trigger:** "New Lead (Raw)" status or progression from "Identified Target."
   - **Current State:** `Sales/ClientWorkflowState` = "Enriching"
   - **Category:** Prospecting
   - **Default Next State:** "Lead - Verified"
   - **Default Previous States:** "New Lead (Raw)", "Contact Failed (Delivery Issue)"
   - **Actions:**
     - Automated and/or manual processes to verify and augment company and contact data.
     - Fill in missing fields like `Sales/Industry`, `Sales/Employees`, `Sales/Website`, confirm contact details, identify key decision-makers for outreach.
     - Populate `Sales/Short description` with a concise company overview.
     - Assign initial `Sales/Sales person` if not already assigned.
     - Determine and set `Sales/Company.Tier` if criteria are available (e.g., based on employee count, industry, potential segment).
   - **If Enrichment Successful (key data verified/found):**
     - **Next State:** `Sales/ClientWorkflowState` = "Lead - Verified"
     - **Category:** Prospecting
     - **Next Action:** Proceed to Outreach.
   - **If Enrichment Fails (critical data missing, cannot verify contact):**
     - **Option A: Manual Review:** Flag for manual review and further research.
     - **Option B: Discard/Archive:**
       - **Next State:** `Sales/ClientWorkflowState` = "Enrichment Failed - Unusable"
       - **Category:** Closed
       - **IsFinal (for state):** true
       - Update `Sales/Status`: "Closed - Unusable"

## II. Outreach & Initial Contact

### 4. Outreach Attempt (Renamed from "3. Outreach Attempt")
   - **Trigger:** "Lead - Verified" status.
   - **Current State:** `Sales/ClientWorkflowState` = "Lead - Verified"
   - **Category:** Prospecting
   - **Default Next State:** "Contacted (Delivery Confirmed)"
   - **Default Previous States:** "Enriching"
   - **Actions:** Sales team initiates first contact sequence using approved Gruntworks methods (e.g., cold email, cold phone call, targeted LinkedIn/Twitter/Instagram/Facebook DM). Log `Last Outreach Method`.
   - **Outcome 1: Contact Delivery Successful**
     - (e.g., Email delivered to inbox, phone number connects, LinkedIn message sent successfully)
     - **Next State:** `Sales/ClientWorkflowState` = "Contacted (Delivery Confirmed)"
     - **Category:** Prospecting
     - **Next Action:** Monitor for engagement/response.
   - **Outcome 2: Contact Delivery Failed**
     - (e.g., Email bounced, phone number invalid/unreachable, LinkedIn profile not found/message fails)
     - **Next State:** `Sales/ClientWorkflowState` = "Contact Failed (Delivery Issue)"
     - **Category:** Prospecting
     - **Actions:**
       - Flag for re-enrichment to find correct contact information.
       - If re-enrichment is not immediately possible or fails, consider `Sales/ClientWorkflowState` = "Nurturing - Awaiting Response (Initial Outreach)" with a note about delivery issues.
     - **If re-enrichment/nurture exhausted without successful delivery:**
       - **Next State:** `Sales/ClientWorkflowState` = "Unreachable"
       - **Category:** Closed
       - **IsFinal (for state):** true
       - Update `Sales/Status`: "Closed - Unreachable"

## III. Engagement & Qualification

### 5. Engagement & Response Handling (Renamed from "4. Engagement & Response Handling")
   - **Trigger:** Lead is in "Contacted (Delivery Confirmed)" state.
   - **Current State:** `Sales/ClientWorkflowState` = "Contacted (Delivery Confirmed)"
   - **Category:** Prospecting
   - **Default Next State:** "Qualified"
   - **Default Previous States:** "Lead - Verified"
   - **Actions:** Monitor for response to outreach (e.g., email reply, returned call, LinkedIn message response).
   - **Outcome 1: Engagement Received (Response from Prospect)**
     - **Action:** Proceed to Qualification (Step 6). The nature of the response will determine qualification status.
     - (Company is now actively engaged)
   - **Outcome 2: No Response (after N attempts over X days via defined outreach cadence)**
     - **Next State:** `Sales/ClientWorkflowState` = "Nurturing - Awaiting Response (Initial Outreach)" (This is a more specific state than the previous "Nurturing - No Response")
     - **Category:** Nurturing
     - **Action:** Add to a "No Response Cold Nurture Campaign."
     - **If nurture campaign exhausted without response:**
       - **Next State:** `Sales/ClientWorkflowState` = "Unresponsive (Initial Outreach)"
       - **Category:** Closed
       - **IsFinal (for state):** true
       - Update `Sales/Status`: "Closed - Unresponsive"
   - **Outcome 3: Explicit Negative Response (e.g., "Not interested", "Unsubscribe request")**
     - **Next State:** `Sales/ClientWorkflowState` = "Not Interested (Initial Contact)"
     - **Category:** Closed
     - **IsFinal (for state):** true
     - **Action:** Record reason, honor unsubscribe if requested. Update to "Do Not Contact" if explicitly requested.
     - Update `Sales/Status`: "Closed - Not Interested"

### 6. Qualification Process (Renamed from "5. Qualification Process")
   - **Trigger A: Engagement Received (from Step 5, Outcome 1).**
     - **Current State (implicit):** Engaged, pending qualification.
   - **Trigger B: Inbound Lead with Engagement**
     - (e.g., Filled out web form with details, sent direct inquiry, warm referral showing clear interest)
     - **Initial State for Inbound:** `Sales/ClientWorkflowState` = "Inbound Lead - Auto Qualified" (if criteria met via form) or "Inbound Lead - Pending Qualification Review"
     - **Default Next State (for Auto Qualified):** "Qualified"
     - **Default Previous States (for Auto Qualified):** (None - Entry Point)
     - **Default Next State (for Pending Review):** "Qualified"
     - **Default Previous States (for Pending Review):** (None - Entry Point)
     - **Category:** Prospecting
   - **Actions:**
     - Sales rep assesses needs, budget, authority, timeline (BANT or similar).
     - Evaluate response sentiment and fit with `Sales/ClientSegment`.
     - Update company record with new details.
     - Confirm/update `Sales/Company.Tier` based on qualification details.
     - Confirm/update `Sales/Sales person` assignment.
   - **Outcome 1: Qualified**
     - **Next State:** `Sales/ClientWorkflowState` = "Qualified"
     - **Category:** Prospecting (or Active Sales if demo intent is immediate)
     - **Next Action:** Schedule a Demo.
     - Update `Sales/Status`: "Qualified Lead" (or similar)
   - **Outcome 2: Not Qualified**
     - **Next State:** `Sales/ClientWorkflowState` = "Not Qualified"
     - **Category:** Closed
     - **IsFinal (for state):** true
     - **Action:** Provide reasoning for disqualification.
     - Update `Sales/Status`: "Closed - Not Qualified"
   - **Outcome 3: Qualified but Goes Cold (Fails to engage for Demo Scheduling)**
     - **Next State:** `Sales/ClientWorkflowState` = "Nurturing - Qualified Gone Cold (Pre-Demo)"
     - **Category:** Nurturing
     - **Action:** Add to a "Qualified Nurture Campaign" aimed at booking a demo.

## IV. Demo Process

### 7. Demo Scheduling & Management (Renamed from "6. Demo Scheduling & Management")
   - **Trigger:** Lead is "Qualified" and demo is the next step.
   - **Current State:** `Sales/ClientWorkflowState` = "Qualified"
   - **Category:** Active Sales (Transition to Active Sales funnel stage)
   - **Default Next State:** "Demo Scheduled"
   - **Default Previous States:** "Contacted (Delivery Confirmed)", "Inbound Lead - Auto Qualified", "Inbound Lead - Pending Qualification Review", "Nurturing - Churned Client Re-engagement"
   - **Actions:**
     - Sales team works to schedule the demo for Local SEO (or Website) productized offers.
     - A `Sales/Deal` entity should be created or activated at this stage to track the opportunity, reflecting the commitment shown by scheduling a demo. Assign a relevant `Sales/Deal.Stage` like "Demo Scheduled" and initial `Sales/Deal.Probability %`.
   - **Path A: Demo Scheduled**
     - **Next State:** `Sales/ClientWorkflowState` = "Demo Scheduled"
     - **Category:** Active Sales
     - **Next Action:** Conduct the demo.
   - **Path B: Unable to Schedule Demo (Qualified lead becomes unresponsive/disengaged at this point)**
     - (This scenario is covered by "Nurturing - Qualified Gone Cold (Pre-Demo)" - see Step 6, Outcome 3)
   - **Path C: Client Eager to Sign Up (Skips Demo - Rare for cold outreach, more common for high-intent inbound or referrals)**
     - **Trigger:** "Qualified" lead expresses strong desire to move to sign up directly.
     - **Next Stage:** `Sales/ClientWorkflowState` = "Tier Selection & Agreement"
     - **Category:** Active Sales
     - **Next Action:** Guide client to private sign-up page for chosen tier.

### 8. Demo Conducted & Outcomes (Renamed from "7. Demo Conducted & Outcomes")
   - **Trigger:** Demo has been conducted.
   - **Current State:** `Sales/ClientWorkflowState` = "Demo Scheduled"
   - **Category:** Active Sales
   - **Default Next State:** "Tier Selection & Agreement"
   - **Default Previous States:** "Qualified"
   - **Actions:** Sales team conducts demo (primarily for Local SEO, can include Website), presents tiered productized offerings, gathers feedback, aims to close or move to tier selection. The specific Deal Type (e.g., `New Client Acquisition (Productized)` vs. `New Client Acquisition (Custom/Enterprise)`) will influence emphasis and next steps.
   - **Post-Demo Outcome 1: Positive Interest / Ready for Tier Selection (Primary Goal for `New Client Acquisition (Productized)` Deal Type)**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Tier Selection & Agreement"
     - **Category:** Active Sales
     - **Next Action:** Guide to private sign-up page, assist with tier choice, address final questions. Create/update `Sales/Deal`.
       - `Sales/Deal.Client` = Link to `Sales/Company`
       - `Sales/Deal.Amount` = Tiered Product Value
       - `Sales/Deal.Probability %` = (e.g., 75%)
       - `Sales/Deal.Stage` = "Tier Selection"
       - `Sales/Deal.Owner` = Link to Sales Rep/User(s) (Can be one or more users)
   - **Post-Demo Outcome 2: Positive Interest / Buys without Proposal (Primarily for `New Client Acquisition (Custom/Enterprise)` or specific `Upsell/Cross-Sell` Deal Types)**
     - This path is now reserved for Automation cross-sells or unique custom deals, typically not for initial SEO/Website. Applicable Deal Types will determine if this is a valid next step.
     - **Next Stage (if applicable for Custom/Automation):** `Sales/ClientWorkflowState` = "Contract - Custom/Automation"
     - **Category:** Active Sales
     - **Next Action:** Prepare and send contract. Create/update `Sales/Deal`.
   - **Post-Demo Outcome 3: Positive Interest / Needs Proposal (Primarily for `New Client Acquisition (Custom/Enterprise)` or specific `Upsell/Cross-Sell` Deal Types)**
     - This path is now reserved for Automation cross-sells or unique custom deals. Applicable Deal Types will determine if this is a valid next step.
     - **Next Stage (if applicable for Custom/Automation):** `Sales/ClientWorkflowState` = "Proposal - Custom/Automation"
     - **Category:** Active Sales
     - **Next Action:** Prepare and send proposal. Create/update `Sales/Deal` entity.
   - **Post-Demo Outcome 4: Undecided / Needs Follow-up (Nurturing)**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Nurturing - Post Demo Follow-up"
     - **Category:** Nurturing
     - **Action:** Add to post-demo nurture campaign. Schedule follow-up tasks.
     - Update `Sales/Deal.Probability %` (e.g., 25%)
     - Update `Sales/Deal.Stage` = "Nurturing" (or more specific `Sales/Deal.Stage` like "Post-Demo Nurture")
   - **Post-Demo Outcome 5: Not Interested**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Closed Lost - Post Demo"
     - **Category:** Closed
     - **IsFinal (for state):** true
     - Update `Sales/Deal.Stage` = "Closed Lost"
     - `Sales/Deal.Probability %` = 0%
     - Update `Sales/Status`: "Closed - Lost (Post-Demo)"
   - **Post-Demo Outcome 6: Demo No Show**
     - **Next State:** `Sales/ClientWorkflowState` = "Demo No Show"
     - **Category:** Active Sales (or Nurturing if multiple no-shows)
     - **Action:** Initiate demo rescheduling sequence. If persistent, move to a specific "Nurturing - Demo No Show" or "Nurturing - Qualified Gone Cold (Pre-Demo)".
     - Update `Sales/Deal.Stage` to reflect "Demo No Show" and adjust `Sales/Deal.Probability %` accordingly.

## V. Closing & Onboarding (Simplified for Productized Offers)

### 9. Tier Selection & Agreement (New Section replacing "Proposal Stage" for standard offers)
   - **Trigger:** Positive demo outcome for Local SEO/Website, client ready to proceed.
   - **Current Stage:** `Sales/ClientWorkflowState` = "Tier Selection & Agreement"
   - **Category:** Active Sales
   - **Default Next State:** "Onboarding"
   - **Default Previous States:** "Demo Scheduled", "Nurturing - Post Demo Follow-up"
   - **Associated Entity:** `Sales/Deal` is active.
     - `Sales/Deal.Stage` = "Tier Selection" (or "Pending Sign-up")
   - **Actions:**
     - Guide client to private sign-up page.
     - Confirm chosen productized tier (Basic, Average, Enterprise for Local SEO/Website).
     - Assist with online sign-up process and payment if applicable.
     - Follow up if sign-up is not completed promptly.
   - **If Sign-up & Payment Completed:**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Onboarding" (This is a "Closed Won" scenario for productized offer)
     - **Category:** Active Client
     - Update `Sales/Deal.Stage` = "Closed Won"
     - Update `Sales/Deal.Probability %` = 100%
     - Update `Sales/Deal.Close Date` = Date of sign-up/payment.
     - **This company is now an "Active Client".**
     - Update `Sales/Status`: "Active Client"
   - **If Sign-up Stalled / Client Goes Cold:**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Nurturing - Stalled Tier Selection"
     - **Category:** Nurturing
     - **Action:** Add to specific nurture campaign for stalled sign-ups.
     - Update `Sales/Deal.Stage` = "Nurturing - Stalled Tier Selection"
     - Update `Sales/Deal.Probability %` (e.g., 10-20%)

### 10. Proposal & Contract Stages (for Custom/Automation & Enterprise Deals ONLY) - (Formerly Sections 8 & 9)
   - **Context:** These stages are now primarily for non-productized, custom Automation service engagements (often as a cross-sell to existing clients) or highly tailored Enterprise-level package deals that require formal documentation beyond the standard tier sign-up. They are typically not part of the initial Local SEO/Website client acquisition flow. These stages are primarily navigated by deals classified as `New Client Acquisition (Custom/Enterprise)` or `Upsell/Cross-Sell (Existing Client)` Deal Types.
   - **Trigger for "Proposal - Custom/Automation":**
     - Existing client ("Managing" or "Max Impact" stage) identified for Automation upsell and requires a detailed proposal (typically an `Upsell/Cross-Sell (Existing Client)` Deal Type).
     - New high-value lead with complex needs explicitly requiring a custom proposal for a non-standard package (typically a `New Client Acquisition (Custom/Enterprise)` Deal Type).
   - **Current Stage:** `Sales/ClientWorkflowState` = "Proposal - Custom/Automation"
   - **Category:** Active Sales
   - **Associated Entity:** `Sales/Deal` (potentially a new deal for cross-sell) is active.
   - **Default Next State:** "Contract - Custom/Automation"
   - **Default Previous States:** (None - Manual Trigger)
     - `Sales/Deal.Stage` = "Proposal Sent (Custom/Automation)"
   - **Actions:** Prepare and send detailed proposal, follow up, negotiations.
   - **If Proposal Accepted:**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Contract - Custom/Automation"
     - Update `Sales/Deal.Stage` = "Contract Sent (Custom/Automation)"
     - Update `Sales/Deal.Probability %` (e.g., 75%)
   - **If Proposal Rejected / Stalled:**
     - **Option A: Re-Nurture:**
       - **Next Stage:** `Sales/ClientWorkflowState` = "Nurturing - Stalled Proposal (Custom/Automation)"
       - **Action:** Add to specific nurture campaign.
     - **Option B: Closed Lost:**
       - **Next Stage:** `Sales/ClientWorkflowState` = "Closed Lost - Proposal Rejected (Custom/Automation)"
       - **IsFinal (for state):** true
       - Update `Sales/Status`: "Closed - Lost (Proposal)"
   - **Trigger for "Contract - Custom/Automation":** Proposal accepted.
   - **Current Stage:** `Sales/ClientWorkflowState` = "Contract - Custom/Automation"
   - **Actions:** Send contract, address legal points.
   - **If Contract Signed & Payment (if applicable) Received:**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Onboarding" (or a specific "Onboarding - Automation" if process differs significantly)
     - **Category:** Active Client
     - Update `Sales/Deal.Stage` = "Closed Won"
     - Update `Sales/Deal.Probability %` = 100%
     - Update `Sales/Status`: "Active Client"
     - Consider creating/linking `Ship/Project` via `Sales/Company.Projects` for custom work.
   - **If Contract Stalled / Client Backs Out:**
     - **Next Stage:** `Sales/ClientWorkflowState` = "Closed Lost - Contract Stage (Custom/Automation)"
     - **IsFinal (for state):** true
     - Update `Sales/Status`: "Closed - Lost (Contract)"

## VI. Post-Conversion: Active Client Lifecycle (Retained for Full Funnel View)

### 11. Onboarding (Renamed from "10. Onboarding")
   - **Trigger:** Contract signed/Tier selection completed & payment confirmed, deal "Closed Won".
   - **Current Stage:** `Sales/ClientWorkflowState` = "Onboarding"
   - **Category:** Active Client
   - **Default Next State:** "First Impact"
   - **Default Previous States:** "Tier Selection & Agreement", "Contract - Custom/Automation", "Nurturing - Stalled Tier Selection"
   - **IsFinal (for state):** false
   - **Actions:**
     - Welcome new client.
     - Kick-off call.
     - System setup, user provisioning for Local SEO/Website services.
     - If applicable, create and link a new `Ship/Project` via `Sales/Company.Projects` for tracking onboarding or initial service delivery.
     - Initial training.
   - **Next Stage (upon completion of onboarding milestones):** `Sales/ClientWorkflowState` = "First Impact"

### 12. First Impact (Renamed from "11. First Impact")
   - **Trigger:** Onboarding successfully completed.
   - **Current Stage:** `Sales/ClientWorkflowState` = "First Impact"
   - **Category:** Active Client
   - **Default Next State:** "Managing"
   - **Default Previous States:** "Onboarding"
   - **IsFinal (for state):** false
   - **Actions:**
     - Client starts actively using the product/service (Local SEO/Website).
     - Focus on achieving initial value and success milestones.
     - Regular check-ins by Customer Success/Account Management.
   - **Next Stage (upon achieving initial value metrics):** `Sales/ClientWorkflowState` = "Managing"

### 13. Managing (Renamed from "12. Managing")
   - **Trigger:** Client has achieved initial value and is in a steady state of usage.
   - **Current Stage:** `Sales/ClientWorkflowState` = "Managing"
   - **Category:** Active Client
   - **Default Next State:** "Max Impact"
   - **Default Previous States:** "First Impact", "Max Impact"
   - **IsFinal (for state):** false
   - **Actions:**
     - Ongoing support and account management.
     - Proactive check-ins.
     - Identify upsell/cross-sell opportunities (e.g., Website if they only have SEO, Automation services). This involves creating a new `Sales/Deal` record, assigning the `Upsell/Cross-Sell (Existing Client)` Deal Type, and potentially proceeding to stages like "Proposal - Custom/Automation".
     - QBRs (Quarterly Business Reviews).
     - Gather feedback.
   - **Next Stage (when client is fully utilizing and deriving significant value):** `Sales/ClientWorkflowState` = "Max Impact"

### 14. Max Impact (Renamed from "13. Max Impact")
   - **Trigger:** Client is a power user, advocate, and deriving maximum possible value from initial services.
   - **Current Stage:** `Sales/ClientWorkflowState` = "Max Impact"
   - **Category:** Active Client
   - **Default Next State:** "Managing"
   - **Default Previous States:** "Managing"
   - **IsFinal (for state):** false
   - **Actions:**
     - Maintain high satisfaction.
     - Seek testimonials, case studies, referrals.
     - Explore partnership opportunities.
     - Continue to provide excellent support and strategic guidance.
     - Actively work on cross-selling Automation services if not already adopted. This involves creating a new `Sales/Deal` record, assigning the `Upsell/Cross-Sell (Existing Client)` Deal Type, and potentially leading to "Proposal - Custom/Automation".
   - **Possible Transitions from here:**
     - Renewal (continues in "Managing" or "Max Impact" or a specific "Renewed" state if desired)
     - Churn

## VII. Churn

### 15. Churn (Renamed from "14. Churn")
   - **Trigger:** Client indicates intent to cancel, or non-renewal of contract.
   - **Current Stage (from any Active Client stage):** Transitions to `Sales/ClientWorkflowState` = "Churned" (or a more specific "Churn - At Risk" followed by "Churned - Confirmed" if desired for internal process)
   - **Category:** Closed
   - **IsFinal (for state):** true
   - **Actions:**
     - Understand reasons for churn (exit interview/survey).
     - Attempt retention efforts if applicable and timely.
     - Offboard the client if retention fails.
     - Mark `Sales/Deal` (if applicable to the churn event, or a related "Subscription" entity) as "Churned" or "Cancelled".
   - **Default Next State:** (None - Final State)
   - **Default Previous States:** (Any Active Client State)
   - Update `Sales/Status`: "Churned"

## VIII. Other Scenarios & Considerations

### A. Re-Engagement, Nurturing "Lost" Deals, & "Do Not Contact" Policies

This section outlines how to handle entities that are not actively progressing, including those who should not be contacted further, those who stalled but might be re-engaged, and churned clients with varying potential for future business.

1.  **"Do Not Contact" (DNC) Status:**
    *   **Trigger:**
        *   A prospect or client explicitly requests no further contact.
        *   Internal decision based on strong disinterest, consistent unresponsiveness after multiple outreach cycles, or other factors deeming future contact inappropriate.
    *   **Action:** The entity's `Sales/ClientWorkflowState` is updated to "Do Not Contact".
    *   **Category:** Closed
    *   **IsFinal (for state):** true
    - **Default Next State:** (None - Final State)
    - **Default Previous States:** (Various, not explicitly tracked via default)
    *   **Policy:** These entities must be excluded from all future sales and marketing outreach.
    - Update `Sales/Status`: "Do Not Contact"

2.  **"Nurturing - Long Term (Lost Deal)" Status:**
    *   **Context:** This applies to deals where a prospect showed initial or continued interest (e.g., completed a demo, was qualified) but did not proceed to close, and *has not* requested "Do Not Contact".
    *   **Examples of Previous Specific Nurturing States that might lead here after time:** "Nurturing - Post Demo Follow-up," "Nurturing - Stalled Tier Selection," "Nurturing - Qualified Gone Cold (Pre-Demo)."
    *   **Action:** Entities can be moved to `Sales/ClientWorkflowState` = "Nurturing - Long Term (Lost Deal)"
    *   **Category:** Nurturing
    *   **IsFinal (for state):** false
    *   **Next Action:**
        *   Placed in targeted long-term nurture campaigns.
        *   Periodically reviewed for potential re-engagement triggers.
    *   **Re-Engagement Trigger:** Significant time elapsed, new relevant offerings, observed changes.
    *   **If Interest Rekindled:**
        *   **Next Stage:** Can re-enter the active pipeline at "Qualified," "Demo Scheduled," or "Tier Selection & Agreement," depending on context. A new or updated `Sales/Deal` would be created/re-opened.

3.  **Churned Client Re-Engagement & DNC Policy:**
    *   **Context:** When a client churns (as per Section VII, Step 15).
    *   **Scenario 1: Churned - Do Not Re-engage / DNC**
        *   **Trigger:** Client was highly dissatisfied, explicitly requested no future contact.
        *   **Action:** `Sales/ClientWorkflowState` is updated/confirmed as "Churned - DNC".
        *   **Category:** Closed
        *   **IsFinal (for state):** true
        - Update `Sales/Status`: "Churned - DNC"
    *   **Scenario 2: Churned - Eligible for Re-engagement Nurture**
        *   **Trigger:** Client churned for reasons not indicating permanent dissatisfaction.
        *   **Action:** `Sales/ClientWorkflowState` is updated to "Nurturing - Churned Client Re-engagement".
        *   **Category:** Nurturing
        *   **IsFinal (for state):** false
        *   **Next Action:** Specialized nurture campaign for former clients.
        *   **If Interest Rekindled:** Re-enter pipeline ("Qualified," etc.). New `Sales/Deal`.
    - **Default Next State:** "Qualified"
    - **Default Previous States:** "Churned" (if eligible)

### B. Direct Inbound - High Intent
   - **Trigger:** Client directly contacts sales with high intent to purchase or evaluate.
   - **Action:** Can bypass earliest stages. The lead should be assigned an appropriate Deal Type upon creation (e.g., `New Client Acquisition (Productized)` if fitting standard tiers, or `New Client Acquisition (Custom/Enterprise)` if needs are clearly complex).
   - A `Sales/Deal` record should be created immediately for these high-intent leads, reflecting their advanced stage in the buying process.
   - **Possible Entry Stages:** `Sales/ClientWorkflowState` = "Qualified", `Sales/ClientWorkflowState` = "Demo Scheduled", or even directly to "Tier Selection & Agreement" if intent and understanding are exceptionally clear.
   - **Important Clarification:** Must still undergo necessary evaluation.

### C. Lead Source Specific Flows
   - Some lead sources might have slightly varied initial steps. These should be noted if significantly different but generally flow into this main process.

---
*This document aims to be comprehensive. Specific internal processes or tool configurations might necessitate adjustments or further granularity. The `Sales/ClientWorkflowState` names used here should align with the `Specific State Name` in the Fibery CRM setup, and these roll up to a `State Category` for high-level reporting.* 