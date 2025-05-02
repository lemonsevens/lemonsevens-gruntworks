# Gruntworks Brand Documentation System: Relationship Map

```mermaid
flowchart TB
    classDef main fill:#1C1C1C,stroke:#F2EEDB,color:#F2EEDB,stroke-width:2px
    classDef product fill:#7B8448,stroke:#F2EEDB,color:#F2EEDB,stroke-width:1px
    classDef application fill:#4A6B8A,stroke:#F2EEDB,color:#F2EEDB,stroke-width:1px
    classDef management fill:#8B5A2B,stroke:#F2EEDB,color:#F2EEDB,stroke-width:1px
    
    %% Main brand directory centered at top
    BRAND["/marketing/brand/"]
    
    %% Core documents below brand directory
    BRAND --> BSG["/brand-system.md"]
    
    %% Management directories on left and right for balance
    BRAND --> VOICE_DIR["/voice/"]
    BRAND --> ASSET_DIR["/asset-management/"]
    
    %% Add subcategory connectors
    BSG --> PROD_HEAD[Product Documents]
    BSG --> APP_HEAD[Application Guides]
    
    %% Product documentation on left side
    PROD_HEAD --> SW
    PROD_HEAD --> SITEW
    PROD_HEAD --> FLOW
    
    %% Application guides on right side
    APP_HEAD --> SOCIAL
    APP_HEAD --> WEB
    APP_HEAD --> EMAIL
    APP_HEAD --> SALES
    
    %% Management documents in their directories
    VOICE_DIR --> VOICE["/voice-messaging-guide.md"]
    ASSET_DIR --> DAM["/dam-handbook.md"]
    
    %% Product documents with shortened labels
    SW["/product/seo/\nSEEDWORKS_PLAYBOOK.md"]
    SITEW["/product/site/\nSITEWORKS_PLAYBOOK.md"]
    FLOW["/product/automation/\nFLOWWORKS_PLAYBOOK.md"]
    
    %% Application guides with shortened labels
    SOCIAL["/marketing/social/\nsocial-media-playbook.md"]
    WEB["/marketing/web/\nwebsite-style-guide.md"]
    EMAIL["/marketing/email/\nemail-marketing-handbook.md"]
    SALES["/sales/resources/\nsales-presentation-guide.md"]
    
    %% Style assignments
    class BRAND,BSG main
    class SW,SITEW,FLOW product
    class SOCIAL,WEB,EMAIL,SALES application
    class VOICE,DAM,VOICE_DIR,ASSET_DIR management
    
    %% Link styling
    linkStyle default stroke-width:1.5px
```

## Document System Overview

The Gruntworks brand documentation system is organized with the marketing/brand directory as the central hub, containing the Brand System Guide and specialized subdirectories. The Brand System Guide establishes core identity principles, while specialized documents provide detailed guidance for specific applications.

### Core Documents
- **Brand Directory** (`/marketing/brand/`) - Central hub for all brand documentation
- **Brand System Guide** (`/marketing/brand/brand-system.md`) - Foundational reference establishing brand identity, strategy, and standards

### Brand Management Documents
- **Voice & Messaging Guide** (`/marketing/brand/voice/voice-messaging-guide.md`) - Detailed guidelines for content creation and messaging across contexts
- **Digital Asset Management Handbook** (`/marketing/brand/asset-management/dam-handbook.md`) - Protocols for managing, accessing, and maintaining brand assets

### Product Documentation
- **SeedWorks Playbook** (`/product/seo/SEEDWORKS_PLAYBOOK.md`) - Comprehensive guide for local SEO & GBP optimization service
- **SiteWorks Playbook** (`/product/site/SITEWORKS_PLAYBOOK.md`) - Detailed specifications for website development service
- **FlowWorks Playbook** (`/product/automation/FLOWWORKS_PLAYBOOK.md`) - Complete framework for automation & CRM implementation service

### Application-Specific Guides
- **Social Media Playbook** (`/marketing/social/social-media-playbook.md`) - Platform strategies, content frameworks, and management protocols
- **Website Style Guide** (`/marketing/web/website-style-guide.md`) - Component specifications, UX patterns, and content guidelines
- **Email Marketing Handbook** (`/marketing/email/email-marketing-handbook.md`) - Template systems, campaign frameworks, and optimization approaches
- **Sales & Presentation Guide** (`/sales/resources/sales-presentation-guide.md`) - Pitch materials, proposal frameworks, and client journey mapping

## Document Locations

| Document | File Path |
|----------|-----------|
| Brand System Guide | `/marketing/brand/brand-system.md` |
| SeedWorks Playbook | `/product/seo/SEEDWORKS_PLAYBOOK.md` |
| SiteWorks Playbook | `/product/site/SITEWORKS_PLAYBOOK.md` |
| FlowWorks Playbook | `/product/automation/FLOWWORKS_PLAYBOOK.md` |
| Brand Voice & Messaging Guide | `/marketing/brand/voice/voice-messaging-guide.md` |
| Digital Asset Management Handbook | `/marketing/brand/asset-management/dam-handbook.md` |
| Social Media Playbook | `/marketing/social/social-media-playbook.md` |
| Website Style Guide | `/marketing/web/website-style-guide.md` |
| Email Marketing Handbook | `/marketing/email/email-marketing-handbook.md` |
| Sales & Presentation Guide | `/sales/resources/sales-presentation-guide.md` |

## Usage Guidelines

1. **Start with the Brand System Guide** for foundational understanding of the Gruntworks brand
2. **Reference specific documents** when working on specialized projects or content types
3. **Maintain consistency** by aligning all materials with the principles in the Brand System Guide
4. **Report inconsistencies** to the brand team at brand@gruntworks.com 