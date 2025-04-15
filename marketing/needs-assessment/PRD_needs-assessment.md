# PRD: Need Assessment Landing Page + Workflow (Updated)

## 1. Introduction
**Project Name:** Need Assessment Landing Page and Workflow (e.g., "Your [Industry] Growth Scorecard")  
**Objective:** Deliver an interactive needs assessment tool via a landing page that provides prospects with valuable insights, qualifies leads, and drives engagement through progressive profiling and gated full-report delivery tied to demo scheduling.

**Value Proposition:** Provide landscaping business owners with a clear understanding of their marketing and operational strengths and gaps, benchmarked against industry standards, with actionable recommendations to drive growth.

## 2. Key Features
- **Value-Focused Introduction:** Clear explanation of assessment purpose, time investment (5 minutes), and specific benefits/deliverables before users begin
- **Sample Report Preview:** Interactive preview of the assessment report format with sample data to demonstrate value before starting
- **Mobile-First Interactive Landing Page:** React/Vite-built page with a structured assessment tool optimized for smartphone interaction
- **Multi-Stage Form Assessment:** Typeform-style interactive form experience with mobile-optimized question display and touch-friendly controls
- **Needs Assessment Tool:** Guided questions delivering an initial summary and gated full report
- **Data Processing Workflow:** n8n analyzes responses and generates insights/scores
- **Automated Follow-Ups:** Triggers demo scheduling and report delivery based on assessment completion
- **Progress Saving Functionality:** Allows users to save their progress and return to complete the assessment later
- **Intuitive Mobile User Experience:** Touch-optimized UI with logically grouped questions, clear instructions, and contextual help accessible via thumb-friendly zones
- **Engaging Micro-interactions:** Visual feedback and animations that maintain user interest throughout the assessment, designed for mobile interaction patterns

## 3. User Stories
- As a prospect, I want to clearly understand what I'll gain from completing the assessment before I start, so I can determine if it's worth my time investment.
- As a prospect, I want to see examples of the insights I'll receive, so I can visualize the value of completing the assessment.
- As a prospect, I want an assessment that gives me immediate insights and a clear next step, so I feel informed and motivated to engage further.
- As a sales team, I want a tool that qualifies leads and schedules demos automatically, so I can prioritize high-potential prospects efficiently.
- As a busy prospect, I want to save my progress and return later, so I can complete the assessment at my convenience.
- As a user unfamiliar with industry terminology, I want contextual help available, so I can accurately answer all questions.

## 4. Functional Requirements
- **Landing Page:** Built with React and Vite, featuring:
  - A mobile-first design prioritizing smartphone user experience
  - Fast-loading performance with minimal data usage for mobile networks
  - Clean, minimalist design with touch-friendly controls and appropriate tap target sizes
  - Strategic use of imagery and icons that display well on smaller screens
  - Responsive design that scales up to tablet and desktop rather than down to mobile
- **Pre-Assessment Value Communication:**
  - Clear headline communicating the specific value proposition (e.g., "Discover Your Landscaping Business's Growth Potential in 5 Minutes")
  - Bullet points highlighting key takeaways users will receive from the assessment
  - Interactive sample report snippet showing the format and depth of insights
  - Brief explanation of the assessment process and time investment
  - Trust indicators (number of businesses assessed, testimonials from completers)
- **Assessment Tool (Multi-Stage Form):**
  - **Mobile-First Form Interface:**
    - Typeform-style experience with single questions optimized for smartphone screens
    - Touch-friendly input controls (large tap targets, swipe navigation where appropriate)
    - Minimal keyboard entry requirements to reduce mobile typing friction
    - Various mobile-optimized input types (toggle switches, sliders, tap-to-select options)
    - Portrait orientation optimization with minimal horizontal scrolling
  - **Question Structure:**
    - Logical grouping into thematic sections with clear headers and introductions
    - Mobile-friendly navigation between sections with prominent progress indicators
    - Input validation with friendly error messages optimized for small screens
  - **Content Delivery:**
    - **Initial Summary:** After completion, prospects receive a mobile-friendly report with:
      - A score representing readiness for [your solution].
      - 2-3 key challenges identified from responses.
      - A comparison to other companies in their industry.
    - **Full Report Gating:** Clear messaging that the full report is available after scheduling a 15-minute demo.
- **Data Management:**
  - Progressive data persistence using client-side storage (localStorage) for pre-email submission
  - Supabase database integration for permanent storage of assessment data
  - Real-time syncing for responses after email capture
  - See Data Architecture and Flow (Section 6) for detailed technical specifications
- **Progress Management:**
  - Automatic progress saving using cookies before email submission
  - Email-based progress saving after email collection
  - "Continue Later" functionality with email link to resume
  - Session recovery for accidental browser closures
- **Help System:**
  - Tooltips for complex questions
  - "Why we ask" explanations for sensitive questions
- **Data Processing:** n8n workflow to:
  - Collect and process assessment responses from Supabase
  - Generate initial summary and score through predefined algorithms
  - Store processed data for full report generation
  - Trigger automated actions based on assessment stages
- **Automation:**
  - **Demo Scheduling Trigger:** After assessment completion, prospects are prompted to schedule a 15-minute demo to unlock the full report.
  - **CRM Integration:** Prospect data and assessment results synced to CRM system for sales follow-up.

## 5. Engagement and Gatekeeping
- **Value Communication:**
  - Clear upfront explanation of the value exchange at each step (what they'll receive for their input)
  - Visual preview of report format at assessment start to set expectations
  - Progress-based messaging highlighting proximity to valuable insights
- **Progressive Profiling & Initial Reward:**
  - Mobile-optimized question flow with minimal friction for smartphone users
  - Email capture via mobile-friendly input with optional autocomplete support
  - Benchmark report designed for easy viewing on smartphone screens
  - Progress continues seamlessly to the remaining assessment questions after email submission
- **Gamification:**
  - Progress indicators showing completion percentage and current position in the journey
  - **Points System:** 
    - Users earn points for each question answered, with bonus points for:
      - Completing sections without abandonment (persistence bonus)
      - Providing optional detailed answers (depth bonus)
      - Sharing industry-specific challenges (relevance bonus)
    - Point tallies displayed in mobile-friendly visualizations
    - Touch-responsive feedback and micro-animations when points are earned
  - **Tiered Rewards:**
    - **Tier 1 (Email Submission):** Unlock access to an industry benchmark report comparing the user's position to competitors
    - **Tier 2 (Complete Assessment):** Receive a downloadable toolkit with customized templates based on assessment responses (e.g., strategic planning templates, productivity tools, AI prompting guides) along with the initial assessment summary
    - The final tier maintains the main incentive of scheduling a demo to receive the comprehensive personalized report
    - Celebratory animations when unlocking each reward tier
  - **Achievement Badges:** Visual indicators for reaching milestones throughout the assessment, creating a sense of accomplishment
- **Social Proof:**
  - Mobile-friendly testimonial displays with appropriate text sizing
  - Touch-friendly links to case studies optimized for smartphone viewing
  - Strategically placed social proof elements within the assessment flow, designed for mobile scroll patterns
- **Personalized Recommendations:**
  - Initial summary includes 1-2 tailored recommendations based on responses.
  - Clear next steps presented after each major assessment milestone

## 6. Data Architecture and Flow
- **Client-Side Data Handling:**
  - **Form State Management:**
    - React state management (Redux or Context API) for real-time form state
    - Progressive form data stored in browser localStorage to preserve incomplete sessions
    - Form validation and conditional logic handled client-side for responsive UX
  - **Session Recovery:**
    - Automatic state persistence to localStorage after each question/section completion
    - Pre-email session identified by unique session ID stored in browser
    - Post-email session linked to user's email address

- **Data Storage Strategy:**
  - **Primary Database:** Supabase PostgreSQL database for structured data storage
  - **Storage Schema:**
    - `assessment_sessions` table tracking overall session metadata (status, completion, timestamps, device type)
    - `assessment_responses` table storing individual question responses
    - `assessment_reports` table containing generated reports and insights
    - Relational structure allowing for detailed analytics on response patterns and mobile vs. desktop comparisons
  
- **Data Persistence Patterns:**
  - **Progressive Persistence:**
    - Initial questions (pre-email): Stored temporarily in localStorage
    - At email capture: Session data pushed to Supabase, creating permanent record
    - Subsequent sections: Real-time syncing to database after each question/section
    - Form completion: Final status update triggering report generation
  - **Offline Capability:**
    - Limited offline form completion using localStorage/IndexedDB
    - Synchronization upon reconnection to network
    - Error handling for network interruptions

- **n8n Workflow Integration:**
  - **Trigger Mechanisms:**
    - Database webhooks fired on significant events (email capture, section completion, assessment completion)
    - API endpoints for direct form-to-workflow communication at critical milestones
  - **Data Processing Pipeline:**
    - n8n pulls complete response data from Supabase for processing
    - Scoring algorithms applied to categorize and weight responses
    - Website and online presence scraping for full report generation:
      - Website content and metadata extraction
      - Google Business Profile data collection
      - Search results analysis for competitive positioning
      - Social media presence evaluation
    - Template-based report generation using scored responses and scraped data
    - Tiered reward delivery based on completion stage
  - **Automation Hooks:**
    - Report storage in Supabase with secure access links
    - Email delivery of appropriate resources based on completion stage
    - CRM integration for lead qualification and tagging
    - Calendar integration for demo scheduling

- **Security Considerations:**
  - End-to-end encryption for sensitive response data
  - Role-based access control for internal team members
  - GDPR-compliant data storage with appropriate retention policies
  - Audit logging of all data access and modifications
  - **Supabase Security Implementation:**
    - Row-level security (RLS) policies restricting data access by user role and ownership
    - JWT authentication for secure API access to database resources
    - Encrypted environment variables for sensitive configuration
    - Database policy enforcement at the PostgreSQL level
  - **Form Security:**
    - CSRF token implementation to prevent cross-site request forgery
    - Rate limiting to prevent abuse and brute force attacks
    - Input sanitization and validation to prevent injection attacks
    - Secure HTTPS-only communication

## 7. UI/UX Considerations
- **Mobile-First Design Philosophy:**
  - Design for smartphones first, then scale up to larger screens
  - Touch as primary input method with appropriate tap target sizes (minimum 44x44px)
  - Portrait orientation optimization with minimal need for landscape viewing
  - Strategic positioning of UI elements for thumb-reach zones on smartphone screens

- **Progress Indicators:**
  - Touch-friendly progress bar at the top of the form showing completion percentage
  - Step indicators sized appropriately for mobile viewing
  - Visual cues indicating completed vs. remaining sections visible at a glance on small screens

- **Logical Grouping:**
  - Questions organized into mobile-friendly sections that minimize scrolling
  - Section headers with appropriate mobile text hierarchy
  - Single question per screen approach to maximize readability on small displays

- **Clear Instructions:**
  - Concise, action-oriented question phrasing optimized for mobile reading
  - Example answers with appropriate text sizing for smartphone screens
  - Mobile-friendly error messages positioned for visibility without obscuring content

- **Visual Appeal:**
  - Clean, minimalist design with touch-friendly interactive elements
  - Appropriate white space for mobile screens to prevent crowding
  - Strategic use of imagery or icons sized appropriately for mobile viewing
  - Mobile-optimized layout with consideration for various smartphone screen sizes

- **Micro-interactions:**
  - Subtle animations for transitions between questions/sections
  - Visual feedback when answering questions (checkmarks, color changes)
  - Celebratory animations when completing sections or earning rewards
  - Interactive elements that respond to user hover/click

- **Save Progress:**
  - Automatic progress saving (cookie-based for pre-email submission)
  - Email-based progress saving after email collection
  - "Continue Later" option with email link to resume
  - Session recovery if browser is closed accidentally

- **Contextual Help:**
  - Tooltips for complex questions or industry terminology
  - "Why we ask" explanations for sensitive or detailed questions
  - Live chat support option for immediate assistance
  - FAQ section accessible throughout the assessment

## 8. Non-Functional Requirements
- **Mobile Performance:**
  - Page load time under 1.5 seconds on 4G mobile connections
  - Optimized assets for minimal mobile data usage
  - Form transitions/animations optimized for mobile processors
  - Battery-efficient operation to minimize power consumption

- **Mobile Responsiveness:** 
  - Mobile-first design prioritizing smartphone experience (320px-428px widths)
  - Progressive enhancement for tablet (768px+) and desktop (1024px+) experiences
  - Touch-first interface elements with appropriate sizing and spacing
  - No horizontal scrolling on mobile devices in portrait orientation

- **Security:** 
  - Data Encryption: Encrypt prospect data in transit and at rest
  - Authentication: Secure admin access with multi-factor authentication
  - Authorization: Implement Supabase row-level security for granular access control
  - Security Headers: Configure appropriate HTTP security headers (CSP, HSTS, etc.)
  - Regular Updates: Maintain dependencies to address security vulnerabilities
  - Backups: Implement automated database backups with secure storage
  - Security Testing: Conduct periodic security assessments and penetration testing
  - GDPR/CCPA Compliance: Implement data subject access and deletion capabilities if applicable

- **Reliability:**
  - 99.9% uptime for the assessment landing page and form
  - Automatic error recovery for network interruptions
  - Graceful degradation of features in case of service disruptions
  - Regular data backups with point-in-time recovery capability

- **Scalability:** 
  - Support for 500+ concurrent users without performance degradation
  - Database architecture designed for efficient scaling of assessment data
  - Optimized resource utilization during peak traffic periods
  - Content delivery network (CDN) implementation for static assets

- **Maintainability:**
  - Comprehensive code documentation following industry standards
  - Modular architecture allowing independent updates to components
  - Automated testing with minimum 80% code coverage
  - Continuous integration/continuous deployment (CI/CD) pipeline

- **Accessibility:**
  - WCAG 2.1 AA compliance for all user interfaces
  - Screen reader compatibility for assessment questions and summaries
  - Appropriate color contrast ratios for all text and interactive elements
  - Keyboard navigation support throughout the entire assessment

## 9. Success Metrics
- **User Engagement Metrics:**
  - **Start Rate:** Percentage of landing page visitors who begin the assessment
  - **Completion Rate (Mobile vs. Desktop):** Comparative completion rates across device types
  - **Average Completion Time:** Time taken to complete the assessment
  - **Abandonment Points:** Identification of questions/sections with highest drop-off
  - **Return Rate:** Percentage of users who return to complete a saved assessment

- **Conversion Metrics:**
  - **Email Capture Rate:** Percentage of users providing email address
  - **Reward Claim Rate:** Percentage of users unlocking each tier of rewards
  - **Demo Scheduling Rate:** Percentage of completions resulting in demo bookings
  - **Demo Show Rate:** Percentage of scheduled demos that actually occur
  - **Conversion to Sale:** Percentage of demos that convert to customers

- **Assessment Quality Metrics:**
  - **Scoring Accuracy:** Correlation between assessment scores and actual customer fit
  - **Report Usefulness:** User feedback on value of insights provided
  - **Sales Team Feedback:** Rating of lead quality from assessment completions
  - **Content Effectiveness:** Identification of questions that best predict customer success

- **Technical Performance Metrics:**
  - **Page Load Speed (Mobile vs. Desktop):** Comparative load times across device types
  - **Form Responsiveness:** Average transition time between questions
  - **Mobile Network Resilience:** Success rate of form submissions on varying mobile connection qualities
  - **Error Rates:** Frequency of technical issues during assessment completion
  - **Data Integrity:** Accuracy and completeness of captured assessment data

- **Business Impact Metrics:**
  - **Cost per Lead:** Acquisition cost compared to other lead generation methods
  - **Mobile vs. Desktop Lead Value:** Comparison of sales outcomes by originating device type
  - **Sales Cycle Impact:** Reduction in sales cycle length for assessment-qualified leads
  - **Deal Size:** Average revenue from customers acquired through assessment
  - **ROI:** Overall return on investment from the assessment tool implementation

## 10. Implementation Approach
- **Development Phases:**
  - **Phase 1:** Core assessment form with basic data storage 
  - **Phase 2:** Initial summary generation and scoring algorithm (1 week)
  - **Phase 3:** Demo scheduling integration and email capture (1 week)
  - **Phase 4:** Visual polish, gamification, and mobile optimization (1 week)
  - **Phase 5:** Testing, refinement, and launch preparation (1 week)

- **Testing Strategy:**
  - User testing with target audience representatives
  - Cross-device compatibility testing
  - Performance testing on various network conditions
  - A/B testing of key conversion points
  - Security and penetration testing

## Appendix A: Assessment Questions

### Section 1: Business Profile (Initial Questions - Pre-Email)
1. **What industry does your business primarily serve?** [Radio Buttons]
   - Residential Landscaping
   - Commercial Landscaping
   - Both Residential and Commercial
   - Other (please specify) [Text field appears if selected]

2. **What is your company's annual revenue range?** [Radio Buttons]
   - Under $100,000
   - $100,000 - $500,000
   - $500,000 - $1 million
   - $1 million - $5 million
   - Over $5 million
   - Prefer not to say

3. **How many employees does your company have?** [Radio Buttons]
   - Just me (solo)
   - 2-5 employees
   - 6-15 employees
   - 16-50 employees
   - 50+ employees

### Section 2: Marketing Assessment (Post-Email Capture)
4. **Which marketing channels are you currently using?** [Checkboxes - Multiple Selection]
   - Website
   - Google Business Profile
   - Social Media
   - Email Marketing
   - Direct Mail/Print
   - Paid Advertising (Google, Facebook, etc.)
   - Referrals/Word of Mouth
   - Other (please specify) [Text field appears if selected]

5. **How satisfied are you with your current marketing results?** [Slider]
   (1 = Very Dissatisfied, 5 = Very Satisfied)

6. **How many new leads does your business generate in a typical month?** [Radio Buttons]
   - 0-5 leads
   - 6-15 leads
   - 16-30 leads
   - 31-50 leads
   - 50+ leads

7. **What is your biggest marketing challenge right now?** [Radio Buttons]
   - Finding new customers
   - Converting leads into customers
   - Standing out from competitors
   - Measuring marketing effectiveness
   - Creating content/marketing materials
   - Having enough time for marketing
   - Other (please specify) [Text field appears if selected]

### Section 3: Operations & Efficiency
8. **What are your biggest operational challenges?** [Checkboxes - Select up to 2]
   - Scheduling and dispatching crews
   - Customer communication
   - Estimating and bidding
   - Invoicing and payments
   - Inventory management
   - Employee management
   - Other (please specify) [Text field appears if selected]

9. **How do you currently manage customer information?** [Radio Buttons]
   - Paper records/filing system
   - Spreadsheets (Excel, Google Sheets)
   - Basic CRM software
   - Industry-specific software
   - Comprehensive business management software
   - Other (please specify) [Text field appears if selected]

10. **How efficiently do you feel your business currently operates?** [Slider]
    (1 = Very Inefficient, 5 = Extremely Efficient)

### Section 4: Technology & AI Adoption
11. **Which technologies are you currently using in your business?** [Checkboxes - Multiple Selection]
    - Customer relationship management (CRM) software
    - Scheduling/dispatching software
    - Estimating/proposal software
    - Accounting software
    - Marketing automation
    - Mobile apps for field crews
    - None of the above

12. **What is your familiarity with AI tools for business?** [Radio Buttons]
    - Using multiple AI tools currently
    - Experimenting with one or two AI tools
    - Interested but haven't started using AI
    - Not familiar with AI for business
    - Not interested in AI for business

13. **Which business areas would you most like to automate or improve with technology?** [Checkboxes - Select up to 2]
    - Lead generation
    - Customer communication
    - Scheduling and dispatching
    - Proposal creation
    - Invoicing and payments
    - Marketing content creation
    - Reporting and analytics
    - Other (please specify) [Text field appears if selected]

### Section 5: Growth Goals
14. **What are your primary business goals for the next 12 months?** [Checkboxes - Select up to 2]
    - Increase revenue
    - Improve profit margins
    - Expand service offerings
    - Enter new markets/locations
    - Improve operational efficiency
    - Build a stronger team
    - Other (please specify) [Text field appears if selected]

15. **What percentage growth in revenue are you targeting this year?** [Radio Buttons]
    - 0-10%
    - 11-25%
    - 26-50%
    - 51-100%
    - Over 100%
    - Not focused on revenue growth right now

16. **What do you believe is the biggest obstacle to achieving your growth goals?** [Text Area - Short Answer]

## Appendix B: Sample Assessment Report Outline

### Initial Summary Report (Email Capture Reward)
- **Industry Benchmark Comparison:** Visual graph showing how the prospect's business compares to peers in key metrics
- **Current Marketing Health Score:** Summary gauge visualization with simple explanation
- **Key Opportunities:** 1-2 specific opportunities based on initial questions

### Complete Assessment Summary (Assessment Completion Reward)
- **Growth Readiness Score:** Overall score with breakdown by category (Marketing, Operations, Technology)
- **Top 3 Challenges:** Specific challenges identified from responses with brief context
- **Quick Wins:** 2-3 immediately actionable recommendations
- **Next Steps:** Clear call-to-action to schedule demo for comprehensive report, explicitly highlighting what the full report will include:
  - Comprehensive scorecard with detailed analysis across all categories
  - Website & online presence analysis (website performance evaluation, Google Business Profile review, search results positioning, social media presence)
  - Current state analysis of marketing and operations
  - Competitive gap analysis compared to industry leaders
  - Detailed opportunity roadmap with implementation guidance
  - Custom 90-day growth strategy tailored to business goals
  - Resource toolkit with templates and guides
