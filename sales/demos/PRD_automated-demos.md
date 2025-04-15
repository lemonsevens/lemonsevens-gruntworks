# PRD: Personalized Demo Template Workflow (Updated)

## 1. Introduction
**Project Name:** Personalized Demo Template Workflow (e.g., "The [Your Brand] Opportunity Briefing")  
**Objective:** Automate the creation of highly personalized demo templates triggered by either website needs assessment submissions or CRM status changes, using prospect data from needs assessments, CRM, web scraping, and AI to deliver a curated, insightful presentation that articulates the prospect's specific challenges and the tailored solution.

## 2. Key Features
- **Multiple Entry Points:**
  - **Website Entry:** Workflow initiates when a prospect completes a needs assessment form on the website.
  - **CRM Entry:** Workflow initiates when a contact's status in the CRM changes from "Prospect" to "Demo/Opportunity" via cold outreach.
- **Needs Assessment Integration:** For cold outreach prospects, automatically sends needs assessment form to be completed before demo.
- **Scheduled Demo Generation:** Creates demo content shortly before scheduled meeting time to ensure most up-to-date information.
- **Automated Data Collection:** Pulls company name, website URL, and other available data from needs assessment and/or CRM contact record.
- **Intelligent Data Source Management:** Checks for existing needs assessment data before initiating web scraping to avoid redundant operations.
- **Web Scraping (When Needed):** Extracts prospect details from their website, Google Business Profile, search results, and social profiles using Firecrawl AI only when this data hasn't already been collected via needs assessment.
- **AI-Powered Content Generation:** Uses OpenAI API to summarize available data and create personalized demo content.
- **Interactive Demo Template:** Delivers a customized presentation via Google Slides, structured as a premium offering.
- **Adaptive Demo Structure:** Automatically adjusts demo content and structure based on whether needs assessment data is available.

## 3. User Stories
- As a sales representative, I want a demo template automatically generated when a prospect is ready, using their CRM, needs assessment, and online data, so I can present a tailored solution without manual research.
- As a prospect, I want a demo that reflects my company's specific challenges and goals, making it feel uniquely relevant and valuable.
- As a sales manager, I want demo generation to be scheduled shortly before the meeting to ensure the most current data is used.
- As a sales representative, I want the system to create an appropriate demo regardless of whether the prospect completed the needs assessment.
- As a system administrator, I want to avoid redundant data collection operations to optimize system performance and resources.

## 4. Functional Requirements
### Entry Points and Triggers:
- **Website Needs Assessment Entry:**
  - Workflow initiates when prospect completes the needs assessment form on website.
  - System captures comprehensive data from assessment to inform personalized demo.
  - Demo generation is scheduled for 1 hour before the calendared meeting time.

- **Cold Outreach Entry:**
  - n8n monitors the CRM and detects when a contact's status updates to "Demo/Opportunity."
  - System automatically sends needs assessment form to prospect with request to complete before scheduled demo.
  - System sets a reminder to check for needs assessment completion 2 hours before scheduled demo.
  - Demo generation proceeds only after either:
    - Needs assessment is completed, or
    - 1 hour before demo time (using available CRM and web-scraped data if assessment wasn't completed).

### Data Input and Management:
- **CRM Data Collection:** n8n retrieves company name, website URL, scheduled demo time, and any additional fields (e.g., industry) from the CRM contact record.
- **Needs Assessment Data Verification:** System checks if a completed needs assessment exists for the prospect:
  - If exists: Retrieves all needs assessment data, including previously scraped website and online presence data
  - If not exists: Proceeds to web scraping workflow
- **Web Scraping and Data Extraction:** Only performed when needs assessment data is unavailable. Firecrawl AI scrapes:
  - Company website (description, services, etc.)
  - Google Business Profile (location, reviews, etc.)
  - Search results positioning
  - Social media presence
  - Relevant business details (e.g., size, offerings)

### Demo Generation Paths
The system will follow one of two paths depending on whether needs assessment data is available:

#### Path A: With Needs Assessment Data
- **Data Sources Priority:**
  1. Needs assessment responses (primary source)
  2. Needs assessment web scraping results (already collected during assessment)
  3. CRM data (supplementary)
  
- **Demo Structure:**
  - **Introduction:** Personalized greeting referencing specific company challenges identified in the needs assessment
  - **Challenge Section:** Direct quotes or paraphrased content from needs assessment highlighting pain points
  - **Solution Section:** Tailored recommendations addressing specific needs from assessment
  - **ROI Section:** Customized calculations based on metrics provided in the needs assessment
  - **Implementation Timeline:** Detailed plan addressing timeline concerns from the assessment
  - **Testimonials:** Industry-specific customer stories matching prospect's sector
  - **Online Presence Analysis:** Insights from existing web scraped data collected during needs assessment

#### Path B: Without Needs Assessment Data
- **Data Sources Priority:**
  1. CRM data (primary source)
  2. Newly web-scraped data (critical for insight generation)
  3. Industry benchmarks and general market data (filling gaps)
  
- **Demo Structure:**
  - **Introduction:** Broader greeting highlighting industry trends relevant to prospect's sector
  - **Challenge Section:** Common industry pain points identified from competitor analysis and market research
  - **Solution Section:** More generalized but still industry-specific solutions
  - **ROI Section:** Industry-standard ROI calculations with ranges rather than specifics
  - **Implementation Timeline:** Standard implementation plan with flexible options
  - **Testimonials:** Broader set of success stories from similar companies
  - **Online Presence Analysis:** Insights from freshly scraped web data

### Content Generation:
- **AI-Powered Summarization:** OpenAI API processes all available data to produce:
  - A concise summary of the company's business and services.
  - Key customer pain points derived from needs assessment (Path A) or from reviews and website content (Path B).
- **Personalized Content Creation:** OpenAI API generates demo content, including:
  - A problem statement specific to the prospect's challenges.
  - Data/research highlights supporting the solution.
  - Tailored features, advantages, and benefits of the product/service.
  - An emotional story linking the prospect's situation to the solution.
- **Template Integration:** Google Slides API populates the appropriate pre-designed template (Path A or Path B) with the AI-generated content.
- **Automation Workflow:** n8n orchestrates:
  - Entry point detection (needs assessment submission or CRM status change).
  - Demo generation scheduling based on meeting time.
  - Needs assessment form delivery for cold outreach prospects.
  - Data collection from needs assessment and/or CRM.
  - Data source determination (checking for existing needs assessment data).
  - Web scraping via Firecrawl AI (only if needed).
  - Path determination (A or B) based on data availability.
  - Data summarization and content generation via OpenAI API.
  - Template creation and customization in Google Slides.
  - Delivery of the demo link or file to the sales rep.

## 5. Non-Functional Requirements
- **Speed:** Entire process from trigger to demo delivery completes within 5 minutes once initiated.
- **Timing:** Demo generation occurs approximately 1 hour before scheduled meeting time.
- **Accuracy:** Data and AI content must be relevant and error-free for at least 90% of cases.
- **Reliability:** Workflow must handle CRM updates, needs assessment submissions, and scraping failures gracefully (e.g., fallback to CRM data if scraping fails).
- **Path Detection:** System must accurately determine whether to use Path A or Path B based on data availability.
- **Template Quality:** Both Path A and Path B templates must maintain high quality standards despite different data inputs.
- **Resource Efficiency:** System must avoid redundant operations by properly checking for existing data before initiating new data collection.

## 6. Success Metrics
- **Automation Rate:** Percentage of demos generated without manual intervention.
- **Needs Assessment Completion Rate:** Percentage of cold outreach prospects who complete the needs assessment before demo.
- **Demo Quality by Path:** Comparison of demo quality and conversion rates between Path A and Path B demos.
- **Prospect Relevance:** Positive feedback from prospects on demo accuracy and personalization.
- **Conversion Rate:** Increase in prospects advancing from demo to purchase, reflecting trust and engagement.
- **Path B Effectiveness:** Measure of how effective the Path B demos are relative to Path A demos despite having less input data.
- **System Efficiency:** Reduction in redundant operations and processing time.