# Marketing Site Factory - Developer Handbook

*(Version 2.0 - Streamlined for 2-3 Hour Deployment)*

---

## Quick Navigation

1. [Quick Start](#1-quick-start-5-minutes)
2. [Tech Stack Essentials](#2-tech-stack-essentials)
3. [Development Workflow](#3-development-workflow)
4. [Component Library Usage](#4-component-library-usage)
5. [Testing Strategy](#5-testing-strategy)
6. [Performance Requirements](#6-performance-requirements)
7. [SEO Implementation](#7-seo-implementation)
8. [Deployment Process](#8-deployment-process)
9. [Client Handoff](#9-client-handoff)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. Quick Start (5 minutes)

**Goal**: From zero to local development in 5 minutes

### Prerequisites
```bash
# Required tools
node --version    # v20.x.x
pnpm --version    # v8.6+
docker --version  # Latest
vercel --version  # Latest
```

### New Client Setup
```bash
# 🚀 Create new client project (automated)
./scripts/new-client.sh "Acme Landscaping" "phoenix-az" "landscaping"

# 🏗️ Start development
cd client-acme-landscaping-website
pnpm dev

# ✅ Verify setup
open http://localhost:3000
```

**Expected Result**: Fully functional local site with business-specific components in under 5 minutes.

---

## 2. Tech Stack Essentials

### Core Stack
| Component     | Tool                   | Purpose                              |
| ------------- | ---------------------- | ------------------------------------ |
| **Framework** | Next.js 14 App Router  | Hybrid SSG/SSR, optimal performance  |
| **Database**  | Neon Postgres + Prisma | Serverless database with type safety |
| **Hosting**   | Vercel Pro             | Global edge deployment               |
| **Caching**   | Upstash Redis          | Rate limiting and session management |
| **Styling**   | Tailwind CSS           | Utility-first styling                |
| **Monorepo**  | Turborepo              | Component sharing across clients     |

### Budget Target
- **Total Cost**: <$20/month per client
- Neon: $0-5/month (free tier scaling)
- Vercel: ~$5/month per client (shared Pro plan)
- Upstash: $0-3/month (free tier sufficient)
- Domain: $10-15/month (client responsibility)

### File Structure
```
marketing-site-template/
├── apps/website/           # Next.js client site
├── packages/
│   ├── ui/                # Reusable components
│   │   └── business-types/ # Industry-specific components
│   └── utils/             # Shared utilities
├── scripts/
│   ├── new-client.sh      # Client setup automation
│   └── deploy.sh          # Deployment automation
├── docs/                  # This handbook
└── docker-compose.yml     # Development environment
```

---

## 3. Development Workflow

### Factory-Line Process
```bash
# 1. Client Intake (automated)
./scripts/new-client.sh "Business Name" "city-state" "business-type"

# 2. Component Selection (automated)
# - Script detects business type
# - Scaffolds appropriate components
# - Generates initial content via AI

# 3. Local Development (90 minutes)
pnpm dev
# - Customize components
# - Add client-specific content
# - Configure integrations

# 4. Testing & Deploy (15 minutes)
pnpm test:all
pnpm deploy:staging

# 5. Client Review & Production (10 minutes)
pnpm deploy:prod
```

### Branch Strategy
| Branch Type    | Pattern                    | Purpose                   |
| -------------- | -------------------------- | ------------------------- |
| Main           | `main`                     | Template updates          |
| Client Staging | `staging`                  | Client review environment |
| Features       | `feat/client-slug/feature` | New development           |
| Hotfixes       | `hotfix/client-slug/issue` | Critical fixes            |

### Development Commands
```bash
# Development
pnpm dev              # Start Next.js dev server
pnpm dev:db           # Start database with Prisma Studio

# Testing
pnpm test             # Unit tests with Vitest
pnpm test:e2e         # Playwright E2E tests
pnpm test:perf        # Lighthouse performance tests

# Build & Deploy
pnpm build            # Production build
pnpm deploy:staging   # Deploy to staging
pnpm deploy:prod      # Deploy to production
```

---

## 4. Component Library Usage

### Business-Type Components

**Available Business Types:**
- `landscaping` - Seasonal services, before/after galleries
- `hvac` - Emergency services, maintenance plans
- `roofing` - Storm damage, material showcase
- `plumbing` - Emergency repairs, service callouts
- `general` - Multi-service contractors

### Component Import Pattern
```typescript
// Import business-specific components
import { 
  LandscapingHero,
  SeasonalServices,
  BeforeAfterGallery 
} from '@/ui/business-types/landscaping';

// Usage with client data
<LandscapingHero
  clientSlug="acme-landscaping"
  content={heroContent}
  settings={clientSettings}
/>
```

### Component Props Interface
```typescript
interface BusinessComponentProps {
  clientSlug: string;        // Client identifier
  content?: ContentBlock;    // CMS content
  settings?: ClientSettings; // Theme/config
  className?: string;        // Additional styling
}
```

### Responsive Design
- **Mobile-first**: All components built for mobile, enhanced for desktop
- **Breakpoints**: `sm:640px`, `md:768px`, `lg:1024px`, `xl:1280px`
- **Touch Targets**: Minimum 44x44px for mobile interactions

---

## 5. Testing Strategy

### Test Layers
| Type              | Tool          | Coverage             | Required for Deploy |
| ----------------- | ------------- | -------------------- | ------------------- |
| **Unit**          | Vitest        | Business logic       | ✅ 80% coverage      |
| **E2E**           | Playwright    | User journeys        | ✅ Critical paths    |
| **Performance**   | Lighthouse CI | Core Web Vitals      | ✅ 90+ scores        |
| **Visual**        | Chromatic     | Component regression | ✅ No regressions    |
| **Accessibility** | axe-core      | WCAG 2.2 AA          | ✅ Zero violations   |

### Critical Test Scenarios
1. **Contact Form Journey**: Homepage → Contact → Form Submit → Thank You
2. **Service Discovery**: Homepage → Services → Service Detail → Contact
3. **Mobile Navigation**: Menu → Pages → Contact Information
4. **Performance**: Page load times across device types

### Running Tests
```bash
# Run all tests
pnpm test:all

# Individual test suites
pnpm test              # Unit tests only
pnpm test:e2e          # E2E tests only
pnpm test:perf         # Performance tests only
pnpm test:visual       # Visual regression tests
```

### Performance Budgets
- **Lighthouse Scores**: 90+ for all categories
- **Core Web Vitals**: LCP <2.5s, INP <200ms, CLS <0.1
- **Bundle Size**: <500KB total page weight
- **Images**: WebP/AVIF with responsive sizing

---

## 6. Performance Requirements

### Core Web Vitals Targets
| Metric  | Mobile Target | Desktop Target | Business Impact                  |
| ------- | ------------- | -------------- | -------------------------------- |
| **LCP** | ≤ 2.0s        | ≤ 1.5s         | Contact info visible immediately |
| **INP** | ≤ 200ms       | ≤ 200ms        | Form interactions responsive     |
| **CLS** | ≤ 0.1         | ≤ 0.1          | Stable mobile contact forms      |

### Optimization Strategy
```typescript
// Image optimization
import Image from 'next/image';

<Image
  src="/hero-landscaping.jpg"
  alt="Professional landscaping services"
  width={1200}
  height={600}
  priority={true}  // Above-fold images
  sizes="(max-width: 768px) 100vw, 50vw"
/>

// Font optimization
import { Inter } from 'next/font/google';
const inter = Inter({ subsets: ['latin'], display: 'swap' });
```

### Performance Monitoring
- **Real-time**: Vercel Analytics for Core Web Vitals
- **Lab Testing**: Lighthouse CI on every deployment
- **Error Tracking**: Sentry for performance regressions
- **Uptime**: Simple HTTP monitoring

---

## 7. SEO Implementation

### Automatic SEO Features
- **Schema Markup**: Business-type specific JSON-LD
- **Meta Tags**: Generated from content management
- **Sitemap**: Auto-generated for all pages
- **Local SEO**: NAP consistency across pages

### Business Schema Example
```typescript
// Essential JSON-LD schemas for local service businesses
const schemas = {
  Organization: {
    "@type": "Organization",
    "name": "{Client Business Name}",
    "url": "{Website URL}",
    "logo": "{Logo URL}",
    "contactPoint": {
      "@type": "ContactPoint",
      "telephone": "{Phone Number}",
      "contactType": "customer service"
    }
  },
  
  LocalBusiness: {
    "@type": "LocalBusiness",
    "name": "{Business Name}",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "{Address}",
      "addressLocality": "{City}",
      "addressRegion": "{State}",
      "postalCode": "{ZIP}"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": "{Latitude}",
      "longitude": "{Longitude}"
    },
    "telephone": "{Phone}",
    "priceRange": "{Price Range}",
    "areaServed": ["{Service Areas}"]
  },
  
  Service: {
    "@type": "Service",
    "name": "{Service Name}",
    "description": "{Service Description}",
    "provider": {
      "@type": "LocalBusiness",
      "name": "{Business Name}"
    },
    "areaServed": "{Service Area}"
  }
};
```

### On-Page SEO Optimization

**Geographic Targeting Strategy**
* Individual landing pages for each service area (city/neighborhood)
* Location-specific content with local landmarks and references
* Service area radius mapping with schema markup
* Geo-targeted meta descriptions and titles

**Page Structure per Service Area**
```
/{service-type}/{city-slug}/
├── index.tsx (main service page)
├── gallery.tsx (local project portfolio)
├── reviews.tsx (area-specific testimonials)
└── contact.tsx (location-aware contact form)
├── seo.config.ts (location-specific SEO settings)
├── schema.ts (location-specific schema markup)
├── content/
│   ├── {city-slug}.mdx (location-specific content)
│   └── {city-slug}-gallery.mdx (local project portfolio)
│   └── {city-slug}-reviews.mdx (area-specific testimonials)
│   └── {city-slug}-contact.mdx (location-aware contact form)
├── images/
│   ├── {city-slug}.jpg (location-specific hero image)
│   └── {city-slug}-gallery/ (local project images)

```

**Meta Tag Strategy**
* Title tags: "{Service} in {City} | {Business Name}"
* Meta descriptions: Include service, location, and unique value proposition
* H1 tags: Service + location combination
* Header hierarchy: Proper H1-H6 structure for readability
* Alt text: Descriptive text for all images including location context

**Technical SEO Requirements**
* Canonical URLs to prevent duplicate content
* Structured URLs with location and service slugs
* 301 redirects for any URL changes
* Clean URL structure without parameters
* Breadcrumb navigation with schema markup

### Local Search Optimization (On-Site Only)

**Location Page Implementation**
* Individual pages for each major service area
* Unique, substantial content per location (minimum 500 words)
* Location-specific contact forms with area pre-population
* Embedded maps showing service area coverage
* Local testimonials and case studies per area

**Contact Information Consistency**
* NAP (Name, Address, Phone) consistency across all pages
* Click-to-call phone number implementation
* Contact information in website footer
* Structured data markup for contact details
* Location-aware contact forms

### Content Strategy for SEO

**Service Page Content Requirements**
* Comprehensive service descriptions (800+ words)
* FAQ sections with local context
* Before/after image galleries with alt text
* Process explanations and service benefits
* Call-to-action buttons optimized for conversions

**Blog Content Framework**
* Educational content relevant to services
* Seasonal content tied to local weather/needs
* Case studies featuring local projects
* Industry insights and tips
* Regular publishing schedule for freshness
**Image SEO Implementation**
* WebP/AVIF format with fallbacks
* Responsive image sizing
* Lazy loading for below-fold images
* Descriptive file names with keywords
* Optimized alt text for accessibility and SEO

**Mobile SEO Requirements**
* Mobile-first responsive design
* Touch-friendly navigation and buttons
* Fast mobile loading times
* Mobile-specific meta viewport
* Accelerated Mobile Pages (AMP) for blog content

### Analytics & Search Console Setup

**Google Search Console Configuration**
* Property verification and sitemaps submission
* URL inspection and indexing requests
* Performance monitoring for local keywords
* Manual action and penalty monitoring
* International targeting settings (if applicable)

**SEO Tracking Implementation**
```typescript
// SEO performance tracking
const seoMetrics = {
  organicTraffic: 'Google Analytics 4',
  keywordRankings: 'Search Console API',
  technicalIssues: 'Lighthouse CI',
  coreWebVitals: 'PageSpeed Insights API',
  localSearchVisibility: 'Search Console local queries'
};
```

### Content Management for SEO

**SEO Configuration**
* SEO fields for all content types (title, description, keywords)
* Automatic slug generation with SEO best practices
* Image alt text fields with validation
* Meta tag preview functionality
* Content freshness tracking

**Automated SEO Features**
* Automatic sitemap generation on content updates
* Schema markup injection based on content type
* Meta tag generation with fallbacks
* Internal linking suggestions
* Content length and readability scoring

This focused SEO strategy ensures technical excellence and local search optimization while staying within the website development scope.

---

## 8. Deployment Process

### Client Environment Strategy

| Env                   | Branch / Alias          | URL Pattern                             | Purpose             | Owner                 |
| --------------------- | ----------------------- | --------------------------------------- | ------------------- | --------------------- |
| **Development**       | feature branches        | `{pr-hash}-{client}.vercel.app`         | Developer testing   | Gruntworks            |
| **Client Staging**    | `client-staging-{name}` | `staging-{client}.gruntworksagency.com` | Client review & UAT | Gruntworks            |
| **Client Production** | `client-prod-{name}`    | `{client-domain}.com`                   | Live client site    | Client (post-handoff) |

**Multi-Client Deployment Architecture**:
- Each client gets isolated Vercel projects for staging and production
- Shared component library deployed as NPM package for consistency
- Environment variables managed per-client directly in Vercel
- DNS management transitions from Gruntworks to client during handoff

### Comprehensive Client Handoff Process

**Philosophy**: Successful handoff ensures clients can independently manage their website while maintaining performance and security standards established during development.

### Pre-Handoff Validation & Testing

**Technical Validation Checklist**
- [ ] **Performance Targets**: All Core Web Vitals meet or exceed targets
- [ ] **Mobile Optimization**: Responsive design validated across 10+ devices
- [ ] **SEO Implementation**: Local SEO strategy fully deployed and tested
- [ ] **Accessibility Compliance**: WCAG 2.2 AA compliance verified
- [ ] **Security Audit**: Complete security scan with zero critical vulnerabilities
- [ ] **Integration Testing**: All third-party services operational
- [ ] **Backup Systems**: Automated backups tested and documented
- [ ] **SSL Configuration**: Valid certificates with auto-renewal
- [ ] **Analytics Setup**: Google Analytics 4 and conversion tracking active
- [ ] **Performance Monitoring**: Real-time monitoring dashboards configured

**Business Function Validation**
- [ ] **Contact Forms**: All forms deliver to correct endpoints
- [ ] **Phone Tracking**: CallRail dynamic insertion working
- [ ] **Lead Management**: CRM integration and lead routing functional
- [ ] **Payment Processing**: Online payment systems tested (if applicable)
- [ ] **Booking Systems**: Appointment scheduling working (if applicable)
- [ ] **Review Management**: Review monitoring and response systems active
- [ ] **Email Marketing**: Newsletter signup and automation sequences
- [ ] **Emergency Features**: After-hours contact and emergency routing

### Client Training & Documentation Package

**Content Management Training**
```markdown
# Website Management Training (3-hour program)

<!-- ## Session 1: Sanity Studio Basics (1 hour)
- Content types overview and navigation
- Creating and editing services
- Managing team member profiles
- Uploading and optimizing images
- Publishing workflow and preview -->

## Session 2: Website Analytics & SEO (1 hour)  
- Google Analytics dashboard overview
- Understanding website traffic metrics
- Blog post creation and SEO basics
- Contact form and conversion tracking
- Content freshness and updates

## Session 3: Website Maintenance (1 hour)
- Common content issues and solutions
- Image optimization and management
- Website backup verification
- Security best practices
- When to request technical support
```

**Comprehensive Documentation Package**
- **Website Admin Guide** (50+ pages): Complete management instructions
- **Content Style Guide**: Brand voice, image requirements, SEO guidelines
- **Emergency Response Plan**: Step-by-step incident handling procedures
- **Vendor Contact Directory**: Support contacts for all integrated services
- **Performance Benchmarks**: Target metrics and monitoring procedures
- **Security Guidelines**: Password policies, access management, threat awareness
- **Legal Compliance**: GDPR/CCPA compliance procedures and documentation

### Technical Asset Transfer

**Code & Infrastructure Transfer**
```typescript
// Client handoff automation script
interface ClientHandoffAssets {
  // Repository access
  githubRepo: {
    url: string;
    adminAccess: string[];
    backupSchedule: 'daily' | 'weekly';
  };
  
  // Hosting and domains
  vercelProject: {
    transferTo: string;
    environmentVariables: Record<string, string>;
    deploymentSettings: object;
  };
  
  // // Content management
  // sanityProject: {
  //   adminUsers: string[];
  //   editorUsers: string[];
  //   backupProcedures: string;
  // };
  
  // Monitoring and analytics
  monitoringAccess: {
    vercelAnalytics: string[];
    googleAnalytics: string[];
    sentryAccess: string[];
  };
}
```

**Domain & DNS Management Transfer**
1. **DNS Record Documentation**: Complete record inventory and explanations
2. **SSL Certificate Transfer**: Auto-renewal setup with client account
3. **Email Configuration**: MX records and email service setup
4. **CDN Settings**: Cloudflare or equivalent service transfer
5. **Subdomain Management**: Staging and development environment access

**Third-Party Service Transitions**
- **CRM Systems**: Admin access transfer with data export
- **Email Marketing**: Account ownership transfer and list exports
- **Call Tracking**: CallRail account transfer and historical data
- **Review Management**: Platform access and automation setup
- **Payment Processing**: Merchant account connections and compliance
- **Backup Services**: Independent backup system establishment

### Client Support & Maintenance Framework

### Environment Variables
```bash
# Managed directly in Vercel dashboard per project
NEXT_PUBLIC_CLIENT_NAME="Acme Landscaping"
NEXT_PUBLIC_CLIENT_SLUG="acme-landscaping"
DATABASE_URL="postgresql://..."
RESEND_API_KEY="re_..."
UPSTASH_REDIS_REST_URL="https://..."
NEXT_PUBLIC_GA_ID="G-..."
```

### Deployment Checklist
- [ ] All tests passing
- [ ] Performance budgets met
- [ ] Environment variables configured
- [ ] Custom domain DNS configured
- [ ] SSL certificate active
- [ ] Analytics tracking verified

---

## 9. Client Handoff

### Handoff Package
1. **Repository Transfer**: GitHub repo ownership to client
2. **Hosting Transfer**: Vercel project ownership
3. **Documentation**: Client admin guide (50+ pages)
4. **Training**: 3-hour content management session
5. **Support**: 30-day technical support included

### Client Training Topics
- **Content Updates**: How to modify text and images
- **Contact Form Management**: Lead review and response
- **Performance Monitoring**: Understanding analytics
- **Basic Troubleshooting**: Common issues and solutions

### Post-Handoff Support
| Support Level | Response Time  | Availability   | Pricing          |
| ------------- | -------------- | -------------- | ---------------- |
| **Emergency** | 15 minutes     | 24/7           | Included 30 days |
| **Technical** | 2 hours        | Business hours | Hourly           |
| **Content**   | 1 business day | Business hours | Project-based    |

### Success Metrics (30 Days)
- [ ] **Uptime**: 99.9% availability
- [ ] **Performance**: Core Web Vitals maintained
- [ ] **SEO**: Local rankings maintained/improved
- [ ] **Client Satisfaction**: >4.5/5 survey score

---

## 10. Troubleshooting

### Common Issues & Solutions

**Build Errors**
```bash
# Error: Cannot resolve module
pnpm install --frozen-lockfile

# Error: Type checking failed
pnpm type-check --noEmit

# Error: Environment variables missing
cp .env.example .env.local
# Edit .env.local with actual values
```

**Performance Issues**
```bash
# Check bundle size
pnpm build
pnpm bundle-analyzer

# Optimize images
# Use Next.js Image component with proper sizing
# Convert to WebP/AVIF format
```

**Deployment Failures**
```bash
# Vercel deployment failed
vercel logs
# Check for environment variable issues

# Database connection issues
pnpm db:studio
# Verify DATABASE_URL in Vercel dashboard
```

### Debug Commands
```bash
# Local debugging
pnpm dev --debug          # Next.js debug mode
pnpm test --verbose       # Detailed test output
pnpm build --debug        # Build with debug info

# Performance debugging
pnpm lighthouse --view    # Open Lighthouse report
pnpm bundle-analyzer      # Analyze bundle size
```

### Support Escalation
1. **Level 1**: Check troubleshooting guide
2. **Level 2**: Review GitHub issues and documentation
3. **Level 3**: Contact development team via Slack
4. **Level 4**: Emergency support (clients only)

### Emergency Procedures
**Site Down**:
1. Check Vercel status dashboard
2. Verify custom domain DNS settings
3. Roll back to previous deployment if needed
4. Contact client within 15 minutes

**Performance Degradation**:
1. Check Core Web Vitals in Vercel Analytics
2. Review recent deployments for changes
3. Run performance tests to isolate issue
4. Implement quick fixes or rollback

---

## Implementation Checklist

**Foundation Setup** (30 minutes)
- [ ] Clone template repository
- [ ] Setup monorepo structure with Turborepo
- [ ] Configure Next.js 14 with App Router
- [ ] Install and configure Biome linting
- [ ] Setup Tailwind CSS with design tokens

**Component Library** (60 minutes)
- [ ] Create business-type component structure
- [ ] Build landscaping component set
- [ ] Build HVAC component set
- [ ] Build roofing component set
- [ ] Build plumbing component set
- [ ] Build general contractor components

**Testing & CI/CD** (45 minutes)
- [ ] Configure Vitest for unit testing
- [ ] Setup Playwright for E2E testing
- [ ] Configure Lighthouse CI
- [ ] Setup GitHub Actions workflows
- [ ] Configure Chromatic visual testing

**Database & APIs** (30 minutes)
- [ ] Setup Prisma schema
- [ ] Create contact form API routes
- [ ] Configure Upstash Redis rate limiting
- [ ] Setup environment variable templates

**Automation Scripts** (45 minutes)
- [ ] Create new-client.sh setup script
- [ ] Build deployment automation
- [ ] Setup N8N webhook integration
- [ ] Create client handoff templates

**Documentation** (30 minutes)
- [ ] Write streamlined handbook
- [ ] Create troubleshooting guides
- [ ] Build client training materials
- [ ] Document support procedures

**Total Setup Time**: ~4 hours
**Client Deployment Time**: 2-3 hours
**Target Success Rate**: 95% with junior developers

---

**End of Streamlined Handbook**
