# TL;DR – Quick Start & Success Criteria

**This is a high-level summary for experienced devs. See full guide below for details.**

---

## 🚀 Quick Start

1. **Clone or Bootstrap Project**
   - If starting from scratch: Follow Phase 0 to create all required files and directories.
   - If using a template: `git clone <repo> marketing-site-factory && cd marketing-site-factory`
   - `pnpm install`

2. **Setup Environment**
   - Copy `.env.example` to `.env.local` and fill in required values (DB, Redis, API keys, etc).
   - Start Docker: `pnpm dev:db:start`

3. **Develop**
   - Start dev server: `pnpm dev` (from root or client project)
   - Use AI tools (loveable/21st.dev) and provided prompts to scaffold components.
   - Customize business-type components and content in `clients/client-<slug>-website/`.

4. **Test**
   - Run all tests: `pnpm test` (unit), `pnpm test:e2e` (E2E), `pnpm type-check`, `pnpm test:perf` (Lighthouse)
   - Lint/format: `pnpm lint`, `pnpm format`

5. **Create New Client**
   - `./scripts/new-client.sh "Business Name" "city-state" "business-type"`
   - Update `.env.local` and `src/config/client.ts` in the new client directory.
   - Start dev: `cd clients/client-<slug>-website && pnpm dev`

6. **Deploy**
   - Staging: `./scripts/deploy-staging.sh` (from client dir)
   - Production: `./scripts/deploy-prod.sh` (from client dir)
   - Configure Vercel project, domains, and environment variables as needed.

7. **Handoff & Support**
   - Transfer repo, Vercel, and documentation to client.
   - Provide training and 30-day support.

---

## 🎯 Success Criteria
- **2-3 hour client deployment** (from intake to live site)
- **95%+ deployment success rate** (even for junior devs)
- **Lighthouse 90+ scores** (performance, accessibility, SEO)
- **Zero accessibility violations** (critical paths)
- **<$20/month per client** (hosting, infra)
- **99.9% uptime**
- **>4.5/5 client satisfaction** (post-handoff survey)

---

# Marketing Site Factory & Client Launch: Implementation Guide

This guide provides a comprehensive, step-by-step process for setting up the Marketing Site Factory and launching new client websites based on the principles and tools outlined in the `DEV_HANDBOOK.md`.

## I. Prerequisites

Before starting any development, ensure your local Debian server and development environment have the following tools installed and at the correct versions as specified in the `DEV_HANDBOOK.md`:

1.  **Node.js**:
    *   Verify: `node --version` (Target: v20.x.x)
2.  **pnpm**:
    *   Verify: `pnpm --version` (Target: v8.6+)
3.  **Docker**:
    *   Verify: `docker --version` (Target: Latest)
4.  **Vercel CLI**:
    *   Verify: `vercel --version` (Target: Latest)

---

## II. Phase 0: Foundation Creation (NEW PHASE - 45 minutes)

**Goal**: Establish the core infrastructure of the Marketing Site Factory template from scratch.

### 0.1 Project Bootstrap Structure
**Goal**: Create the foundational project structure.

**File Creation:**
- `marketing-site-factory/package.json` - Root monorepo configuration
- `marketing-site-factory/pnpm-workspace.yaml` - PNPM workspace definition
- `marketing-site-factory/turbo.json` - Turborepo configuration
- `marketing-site-factory/.env.example` - Environment variable template
- `marketing-site-factory/.gitignore` - Git ignore patterns
- `marketing-site-factory/README.md` - Project documentation

**Root `package.json` Content:**
```json
{
  "name": "marketing-site-factory",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev",
    "lint": "turbo run lint",
    "format": "biome check --apply ./",
    "test": "turbo run test",
    "test:e2e": "turbo run test:e2e",
    "type-check": "turbo run type-check",
    "dev:db": "docker-compose up -d postgres && sleep 3 && pnpm --filter website db:studio",
    "dev:db:start": "docker-compose up -d",
    "dev:db:stop": "docker-compose down",
    "dev:db:reset": "docker-compose down -v && docker-compose up -d && sleep 5 && pnpm --filter website db:push",
    "new-client": "./scripts/new-client.sh",
    "deploy:staging": "./scripts/deploy-staging.sh",
    "deploy:prod": "./scripts/deploy-prod.sh"
  },
  "devDependencies": {
    "@biomejs/biome": "^1.4.1",
    "turbo": "^1.11.2"
  },
  "packageManager": "pnpm@8.6.0"
}
```

**PNPM Workspace Configuration (`pnpm-workspace.yaml`):**
```yaml
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"
  - "clients/*"
```

**Turborepo Configuration (`turbo.json`):**
```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", "dist/**"]
    },
    "lint": {},
    "type-check": {},
    "dev": {
      "cache": false,
      "persistent": true
    },
    "test": {},
    "test:e2e": {}
  }
}
```

### 0.2 Core Application Structure
**Directory Creation:**
```
marketing-site-factory/
├── apps/
│   └── website/                 # Template Next.js app
├── packages/
│   ├── ui/                      # Component library
│   ├── utils/                   # Shared utilities
│   └── config/                  # Shared configurations
├── scripts/                     # Automation scripts
├── templates/                   # Client template files
├── clients/                     # Generated client projects
└── docs/                       # Documentation
```

### 0.3 Template Next.js Application
**Create:** `apps/website/package.json`
```json
{
  "name": "@marketing-factory/website",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "build": "next build",
    "dev": "next dev",
    "lint": "biome lint ./src",
    "start": "next start",
    "type-check": "tsc --noEmit",
    "db:push": "prisma db push",
    "db:studio": "prisma studio",
    "db:generate": "prisma generate"
  },
  "dependencies": {
    "next": "14.0.4",
    "react": "^18",
    "react-dom": "^18",
    "@prisma/client": "^5.7.1",
    "tailwindcss": "^3.3.6",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "typescript": "^5",
    "prisma": "^5.7.1"
  }
}
```

### 0.4 Environment Variables Template
**Create:** `.env.example`
```env
# Database
DATABASE_URL="postgresql://dev:dev_password@localhost:5432/marketing_sites"

# Redis
UPSTASH_REDIS_REST_URL="your_upstash_redis_url"
UPSTASH_REDIS_REST_TOKEN="your_upstash_redis_token"

# Email
RESEND_API_KEY="your_resend_api_key"

# Client Configuration
NEXT_PUBLIC_CLIENT_NAME="Template Client"
NEXT_PUBLIC_CLIENT_SLUG="template-client"
NEXT_PUBLIC_SITE_URL="http://localhost:3000"

# Analytics
NEXT_PUBLIC_GA_ID="G-XXXXXXXXXX"

# Third-party Services
VERCEL_PROJECT_ID="your_vercel_project_id"
VERCEL_ORG_ID="your_vercel_org_id"
VERCEL_TOKEN="your_vercel_token"

# Testing
CHROMATIC_PROJECT_TOKEN="your_chromatic_token"

# Development
NODE_ENV="development"
```

---

## III. Phase 1: Enhanced Foundation Setup (30 minutes)

**Goal**: Establish the core infrastructure of the Marketing Site Factory template. This phase mirrors the "Foundation Setup" section of the `DEV_HANDBOOK.md`\'s Implementation Checklist.

1.  **Next.js Application Configuration**
    **Create:** `apps/website/next.config.js`
    ```javascript
    /** @type {import('next').NextConfig} */
    const withBundleAnalyzer = require('@next/bundle-analyzer')({
      enabled: process.env.ANALYZE === 'true',
    });

    const nextConfig = {
      reactStrictMode: true,
      swcMinify: true,
      images: {
        formats: ['image/webp', 'image/avif'],
        remotePatterns: [
          {
            protocol: 'https',
            hostname: '**',
          },
        ],
      },
      experimental: {
        optimizeCss: true,
      },
    };

    module.exports = withBundleAnalyzer(nextConfig);
    ```

2.  **Tailwind Configuration**
    **Create:** `apps/website/tailwind.config.js`
    ```javascript
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
        './src/components/**/*.{js,ts,jsx,tsx,mdx}',
        './src/app/**/*.{js,ts,jsx,tsx,mdx}',
        '../../packages/ui/src/**/*.{js,ts,jsx,tsx,mdx}',
      ],
      theme: {
        extend: {
          colors: {
            primary: {
              50: '#f0fdf4',
              500: '#22c55e',
              600: '#16a34a',
              700: '#15803d',
              900: '#14532d',
            },
            neutral: {
              50: '#fafafa',
              100: '#f4f4f5',
              200: '#e4e4e7',
              300: '#d4d4d8',
              400: '#a1a1aa',
              500: '#71717a',
              600: '#52525b',
              700: '#3f3f46',
              800: '#27272a',
              900: '#18181b',
            },
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
          },
          screens: {
            'xs': '475px',
          },
        },
      },
      plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
      ],
    };
    ```

3.  **TypeScript Configuration**
    **Create:** `apps/website/tsconfig.json`
    ```json
    {
      "extends": "../../packages/config/tsconfig.json",
      "compilerOptions": {
        "baseUrl": ".",
        "paths": {
          "@/*": ["./src/*"],
          "@/ui/*": ["../../packages/ui/src/*"],
          "@/utils/*": ["../../packages/utils/src/*"]
        }
      },
      "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
      "exclude": ["node_modules"]
    }
    ```
    **Create:** `packages/config/tsconfig.json` (base TypeScript config)
    ```json
    {
      "compilerOptions": {
        "target": "esnext",
        "lib": ["dom", "dom.iterable", "esnext"],
        "allowJs": true,
        "skipLibCheck": true,
        "strict": true,
        "forceConsistentCasingInFileNames": true,
        "noEmit": true,
        "esModuleInterop": true,
        "module": "esnext",
        "moduleResolution": "node",
        "resolveJsonModule": true,
        "isolatedModules": true,
        "jsx": "preserve",
        "incremental": true,
        "plugins": [
          {
            "name": "next"
          }
        ]
      },
      "exclude": ["node_modules"]
    }
    ```

4.  **Biome Linting Configuration**
    **Create:** `biome.json`
    ```json
    {
      "$schema": "https://biomejs.dev/schemas/1.4.1/schema.json",
      "organizeImports": {
        "enabled": true
      },
      "linter": {
        "enabled": true,
        "rules": {
          "recommended": true,
          "complexity": {
            "noExcessiveCognitiveComplexity": "warn"
          },
          "style": {
            "useImportType": "error"
          }
        }
      },
      "formatter": {
        "enabled": true,
        "indentStyle": "space",
        "indentWidth": 2
      },
      "javascript": {
        "formatter": {
          "quoteStyle": "single",
          "trailingComma": "es5"
        }
      }
    }
    ```
    *Instruction: Add Biome scripts to the root `package.json` (already covered in Phase 0).*
    *Run `pnpm format` and `pnpm lint` to ensure Biome is configured correctly.*

5.  **Basic App Structure**
    *Instruction: Create the following directory structure and placeholder files in `apps/website/src/app/`:*
    ```
    apps/website/src/app/
    ├── layout.tsx         # Root layout
    ├── page.tsx           # Homepage
    ├── globals.css        # Global styles
    ├── about/
    │   └── page.tsx
    ├── contact/
    │   └── page.tsx
    └── services/
        └── page.tsx
    ```
    **`apps/website/src/app/layout.tsx`**:
    ```typescript
    import type { Metadata } from 'next';
    import { Inter } from 'next/font/google';
    import './globals.css';

    const inter = Inter({ subsets: ['latin'] });

    export const metadata: Metadata = {
      title: 'Marketing Site Factory',
      description: 'Generated by create next app',
    };

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode;
    }) {
      return (
        <html lang="en">
          <body className={inter.className}>{children}</body>
        </html>
      );
    }
    ```
    **`apps/website/src/app/page.tsx` (Homepage Placeholder):**
    ```typescript
    export default function HomePage() {
      return (
        <main className="flex min-h-screen flex-col items-center justify-center p-24">
          <h1 className="text-4xl font-bold">Welcome to the Marketing Site Factory</h1>
          <p className="mt-4 text-lg">This is the homepage for your template website.</p>
        </main>
      );
    }
    ```
    *Instruction: Ensure Tailwind CSS directives (`@tailwind base; @tailwind components; @tailwind utilities;`) are imported in `apps/website/src/app/globals.css`.*

---

## IV. Phase 2: AI-Integrated Component Library Development (90 minutes)

**Goal**: Build a library of reusable UI components, categorized by business type, leveraging AI for faster prototyping.

1.  **Component Library Package Structure**
    **Create:** `packages/ui/package.json`
    ```json
    {
      "name": "@marketing-factory/ui",
      "version": "0.1.0",
      "private": true,
      "main": "./src/index.ts",
      "types": "./src/index.ts",
      "scripts": {
        "lint": "biome lint ./src",
        "type-check": "tsc --noEmit"
      },
      "dependencies": {
        "react": "^18",
        "react-dom": "^18",
        "tailwindcss": "^3.3.6",
        "clsx": "^2.0.0",
        "tailwind-merge": "^2.2.0"
      },
      "devDependencies": {
        "@types/react": "^18",
        "@types/react-dom": "^18",
        "typescript": "^5"
      }
    }
    ```
    **Create:** `packages/ui/tsconfig.json`
    ```json
    {
      "extends": "../../packages/config/tsconfig.json",
      "compilerOptions": {
        "baseUrl": ".",
        "paths": {
          "@/*": ["./src/*"]
        }
      },
      "include": ["**/*.ts", "**/*.tsx"],
      "exclude": ["node_modules"]
    }
    ```
    **Instruction:** Create directory structure `packages/ui/src/components/base/`, `packages/ui/src/business-types/`, `packages/ui/src/types/`, `packages/ui/src/templates/`.

2.  **Core Component Types and Interfaces**
    **Create:** `packages/ui/src/types/index.ts`
    ```typescript
    export interface BusinessComponentProps {
      clientSlug: string;
      content?: ContentBlock;
      settings?: ClientSettings;
      className?: string;
    }

    export interface ContentBlock {
      id: string;
      type: 'hero' | 'services' | 'testimonials' | 'gallery' | 'contact' | 'about';
      title?: string;
      subtitle?: string;
      description?: string;
      image?: string;
      images?: string[];
      cta?: {
        text: string;
        href: string;
        variant?: 'primary' | 'secondary' | 'outline';
      };
      items?: Array<{
        id: string;
        title: string;
        description?: string;
        image?: string;
        price?: string;
        features?: string[];
      }>;
    }

    export interface ClientSettings {
      businessName: string;
      businessType: 'landscaping' | 'hvac' | 'roofing' | 'plumbing' | 'general';
      primaryColor: string;
      secondaryColor: string;
      phone: string;
      email: string;
      address: {
        street: string;
        city: string;
        state: string;
        zip: string;
      };
      serviceAreas: string[];
      logo?: string;
      socialMedia?: {
        facebook?: string;
        instagram?: string;
        twitter?: string;
        linkedin?: string;
      };
    }

    export interface BusinessType {
      id: string;
      name: string;
      description: string;
      heroVariants: string[];
      serviceCategories: string[];
      ctaTemplates: string[];
    }
    ```

3.  **AI Component Templates**
    **Create:** `packages/ui/src/templates/ai-prompts.ts`
    ```typescript
    export const componentPrompts = {
      landscaping: {
        hero: `Create a React component for a landscaping company hero section with:\n- Professional outdoor background image\n- Bold headline about landscape transformation\n- Subheadline about local expertise and quality\n- Two CTAs: "Get Free Quote" and "View Our Work"\n- Trust indicators (years experience, projects completed)\n- Responsive design with Tailwind CSS`,
        
        services: `Create a landscaping services grid component with:\n- Service cards for: Lawn Care, Landscape Design, Irrigation, Tree Service\n- Each card has icon, title, brief description, "Learn More" button\n- Hover effects and responsive grid (1-2-3-4 columns)\n- Use green color scheme consistent with nature theme`,
        
        gallery: `Create a before/after image gallery component for landscaping:\n- Grid layout with before/after image pairs\n- Smooth transitions and hover effects\n- Modal/lightbox functionality for full-size viewing\n- Filtering by project type (residential, commercial, maintenance)\n- Lazy loading for performance`
      },
      
      hvac: {
        hero: `Create an HVAC company hero section with:\n- Indoor comfort/temperature control theme\n- Emphasis on emergency service availability\n- Seasonal messaging (heating/cooling)\n- Emergency hotline prominently displayed\n- Service area coverage map or list`,
        
        services: `Create HVAC services component featuring:\n- Emergency Repair, Installation, Maintenance, Inspection\n- 24/7 availability badges\n- Seasonal service highlights\n- Energy efficiency messaging\n- Financing options display`
      },
      
      roofing: {
        hero: `Create a roofing company hero with:\n- Professional rooftop/construction imagery\n- Storm damage and insurance claim messaging\n- Free inspection offers\n- Weather-resistant, quality craftsmanship themes\n- Local licensing and insurance information`,
        
        services: `Create roofing services showcase:\n- Repair, Replacement, New Construction, Emergency Services\n- Material showcases (shingles, metal, tile)\n- Storm damage assessment tools\n- Insurance claim assistance messaging`
      },
      // Add plumbing and general prompts here
    };
    ```

4.  **Base Component Library**
    **Create:** `packages/ui/src/components/base/Button.tsx`
    ```typescript
    import type { ButtonHTMLAttributes, ReactNode } from 'react';
    import { clsx } from 'clsx';

    interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
      variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
      size?: 'sm' | 'md' | 'lg';
      children: ReactNode;
      isLoading?: boolean;
    }

    export function Button({
      variant = 'primary',
      size = 'md',
      className,
      children,
      isLoading,
      disabled,
      ...props
    }: ButtonProps) {
      return (
        <button
          className={clsx(
            'inline-flex items-center justify-center font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
            {
              'bg-primary-600 text-white hover:bg-primary-700 focus-visible:ring-primary-500': variant === 'primary',
              'bg-neutral-100 text-neutral-900 hover:bg-neutral-200 focus-visible:ring-neutral-500': variant === 'secondary',
              'border border-neutral-300 bg-transparent hover:bg-neutral-50 focus-visible:ring-neutral-500': variant === 'outline',
              'bg-transparent hover:bg-neutral-100 focus-visible:ring-neutral-500': variant === 'ghost',
              'h-9 px-3 text-sm': size === 'sm',
              'h-11 px-8': size === 'md',
              'h-12 px-8 text-lg': size === 'lg',
            },
            className
          )}
          disabled={disabled || isLoading}
          {...props}
        >
          {isLoading ? 'Loading...' : children}
        </button>
      );
    }
    ```
    *Instruction: Develop other base components (Card, Layout, etc.) similarly. Use AI tools (loveable/21st.dev) with prompts from `ai-prompts.ts` to generate initial versions of business-specific components.*

5.  **Business-Specific Component Templates**
    **Create:** `packages/ui/src/business-types/landscaping/LandscapingHero.tsx`
    ```typescript
    import type { BusinessComponentProps } from '../../types';
    import { Button } from '../../components/base/Button';

    export function LandscapingHero({ clientSlug, content, settings, className }: BusinessComponentProps) {
      const businessName = settings?.businessName || 'Professional Landscaping';
      const phone = settings?.phone || '(555) 123-4567';
      
      return (
        <section className={`relative min-h-screen flex items-center justify-center bg-gradient-to-br from-green-800 to-green-600 ${className}`}>
          <div className="absolute inset-0 bg-black/40" />
          <div className="relative z-10 max-w-4xl mx-auto text-center px-4 text-white">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              {content?.title || `Transform Your Landscape with ${businessName}`}
            </h1>
            <p className="text-xl md:text-2xl mb-8 max-w-2xl mx-auto">
              {content?.description || 'Professional landscaping services that bring your outdoor vision to life. Serving your community with quality and expertise.'}
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="bg-primary-500 hover:bg-primary-600">
                Get Free Quote
              </Button>
              <Button size="lg" variant="outline" className="border-white text-white hover:bg-white hover:text-green-800">
                Call {phone}
              </Button>
            </div>
            <div className="mt-12 grid grid-cols-3 gap-8 max-w-md mx-auto text-center">
              <div>
                <div className="text-3xl font-bold">15+</div>
                <div className="text-sm">Years Experience</div>
              </div>
              <div>
                <div className="text-3xl font-bold">500+</div>
                <div className="text-sm">Projects Completed</div>
              </div>
              <div>
                <div className="text-3xl font-bold">100%</div>
                <div className="text-sm">Satisfaction Guaranteed</div>
              </div>
            </div>
          </div>
        </section>
      );
    }
    ```
    **Instruction:** Create `index.ts` files in each business type directory (e.g., `packages/ui/src/business-types/landscaping/index.ts`) to export components:
    ```typescript
    export * from './LandscapingHero';
    // export * from './SeasonalServices';
    // export * from './BeforeAfterGallery';
    ```
    **Create:** `packages/ui/src/index.ts` (root export for the UI package)
    ```typescript
    // Base Components
    export * from './components/base/Button';
    // ... other base components

    // Types
    export * from './types';
    ```

---

## V. Phase 3: Database & API Implementation (45 minutes)

1.  **Prisma Schema**
    **Create:** `apps/website/prisma/schema.prisma`
    ```prisma
    generator client {
      provider = "prisma-client-js"
    }

    datasource db {
      provider = "postgresql"
      url      = env("DATABASE_URL")
    }

    model Contact {
      id          String   @id @default(cuid())
      name        String
      email       String
      phone       String?
      message     String
      service     String?
      clientSlug  String
      source      String?  // 'website', 'phone', 'referral'
      status      String   @default("new") // 'new', 'contacted', 'quoted', 'closed'
      createdAt   DateTime @default(now())
      updatedAt   DateTime @updatedAt

      @@map("contacts")
    }

    model Client {
      id            String   @id @default(cuid())
      slug          String   @unique
      businessName  String
      businessType  String
      email         String
      phone         String
      address       Json
      settings      Json     // Store ClientSettings interface from packages/ui/src/types
      isActive      Boolean  @default(true)
      createdAt     DateTime @default(now())
      updatedAt     DateTime @updatedAt

      @@map("clients")
    }

    model Analytics {
      id         String   @id @default(cuid())
      clientSlug String
      event      String   // 'page_view', 'form_submit', 'phone_click'
      page       String?
      data       Json?
      userAgent  String?
      ip         String?
      createdAt  DateTime @default(now())

      @@map("analytics")
    }
    ```
    *Instruction: Run `pnpm --filter website db:generate` after defining schema.*

2.  **Contact Form API Route**
    **Create:** `apps/website/src/app/api/contact/route.ts`
    ```typescript
    import { NextRequest, NextResponse } from 'next/server';
    import { PrismaClient } from '@prisma/client';
    import { Resend } from 'resend';

    const prisma = new PrismaClient();
    const resendApiKey = process.env.RESEND_API_KEY;
    const resend = resendApiKey ? new Resend(resendApiKey) : null;

    export async function POST(request: NextRequest) {
      try {
        const body = await request.json();
        const { name, email, phone, message, service, clientSlug } = body;

        if (!name || !email || !message || !clientSlug) {
          return NextResponse.json(
            { error: 'Missing required fields' },
            { status: 400 }
          );
        }

        const contact = await prisma.contact.create({
          data: {
            name,
            email,
            phone: phone || null,
            message,
            service: service || null,
            clientSlug,
            source: 'website',
          },
        });

        if (resend) {
          try {
            await resend.emails.send({
              from: 'website@yourdomain.com', // Replace with your domain
              to: ['leads@yourdomain.com'], // Replace with your lead receiving email
              subject: `New Contact Form Submission - ${clientSlug}`,
              html: `
                <h2>New Contact Form Submission</h2>
                <p><strong>Client:</strong> ${clientSlug}</p>
                <p><strong>Name:</strong> ${name}</p>
                <p><strong>Email:</strong> ${email}</p>
                <p><strong>Phone:</strong> ${phone || 'Not provided'}</p>
                <p><strong>Service:</strong> ${service || 'Not specified'}</p>
                <p><strong>Message:</strong></p>
                <p>${message}</p>
                <hr>
                <p><em>Submitted at: ${new Date().toISOString()}</em></p>
              `,
            });
          } catch (emailError) {
            console.error('Failed to send email notification:', emailError);
          }
        }

        await prisma.analytics.create({
          data: {
            clientSlug,
            event: 'form_submit',
            page: '/contact', // Or get from request headers if more dynamic
            data: { service, hasPhone: !!phone },
            userAgent: request.headers.get('user-agent'),
            ip: request.headers.get('x-forwarded-for') || request.ip || 'unknown',
          },
        });

        return NextResponse.json(
          { message: 'Contact form submitted successfully', id: contact.id },
          { status: 201 }
        );
      } catch (error) {
        console.error('Contact form submission error:', error);
        return NextResponse.json(
          { error: 'Internal server error' },
          { status: 500 }
        );
      }
    }
    ```

3.  **Client Configuration API**
    **Create:** `apps/website/src/app/api/client/[slug]/route.ts`
    ```typescript
    import { NextRequest, NextResponse } from 'next/server';
    import { PrismaClient } from '@prisma/client';

    const prisma = new PrismaClient();

    export async function GET(
      request: NextRequest,
      { params }: { params: { slug: string } }
    ) {
      try {
        const client = await prisma.client.findUnique({
          where: { slug: params.slug },
        });

        if (!client || !client.isActive) {
          return NextResponse.json(
            { error: 'Client not found or inactive' },
            { status: 404 }
          );
        }
        
        // Assuming 'settings' field in Client model stores ClientSettings JSON
        const clientSettings = client.settings as any; // Cast to any or define proper type

        return NextResponse.json({
          businessName: client.businessName,
          businessType: client.businessType,
          settings: clientSettings, // Send the whole settings object
        });
      } catch (error) {
        console.error('Client fetch error:', error);
        return NextResponse.json(
          { error: 'Internal server error' },
          { status: 500 }
        );
      }
    }
    ```
    *Instruction: Seed initial client data into the `Client` table for testing.*

---

## VI. Phase 4: Automation Scripts Creation (60 minutes)

1.  **New Client Script**
    **Create:** `scripts/new-client.sh` (Make it executable: `chmod +x scripts/new-client.sh`)
    ```bash
    #!/bin/bash

    # Marketing Site Factory - New Client Setup Script
    # Usage: ./scripts/new-client.sh "Business Name" "city-state" "business-type"

    set -e # Exit immediately if a command exits with a non-zero status.

    # Colors for output
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color

    # Function to print colored output
    print_status() { echo -e "${GREEN}[INFO]${NC} $1"; }
    print_warning() { echo -e "${YELLOW}[WARN]${NC} $1"; }
    print_error() { echo -e "${RED}[ERROR]${NC} $1"; }
    print_step() { echo -e "\n${BLUE}➡️  $1${NC}"; }

    # Validate arguments
    if [ $# -ne 3 ]; then
        print_error "Usage: $0 \"Business Name\" \"city-state\" \"business-type\""
        print_error "Example: $0 \"Acme Landscaping\" \"phoenix-az\" \"landscaping\""
        print_error "Valid business types: landscaping, hvac, roofing, plumbing, general"
        exit 1
    fi

    BUSINESS_NAME_RAW="$1"
    CITY_STATE_SLUG="$2" # e.g., phoenix-az
    BUSINESS_TYPE="$3"

    # Validate business type
    VALID_TYPES=("landscaping" "hvac" "roofing" "plumbing" "general")
    if [[ ! " ${VALID_TYPES[@]} " =~ " ${BUSINESS_TYPE} " ]]; then
        print_error "Invalid business type: $BUSINESS_TYPE. Valid types: ${VALID_TYPES[*]}"
        exit 1
    fi

    # Generate client slug from business name
    CLIENT_SLUG=$(echo "${BUSINESS_NAME_RAW,,}" | tr -cs 'a-z0-9' '-' | sed 's/--\+/-/g; s/^-//; s/-$//')
    PROJECT_NAME="client-${CLIENT_SLUG}-website"
    CLIENT_DIR_RELATIVE="clients/${PROJECT_NAME}"
    CLIENT_DIR_ABSOLUTE="$(pwd)/${CLIENT_DIR_RELATIVE}"

    print_step "Creating New Client Project"
    echo "-------------------------------------"
    print_status "Business Name: $BUSINESS_NAME_RAW"
    print_status "Location Slug: $CITY_STATE_SLUG"
    print_status "Business Type: $BUSINESS_TYPE"
    print_status "Generated Client Slug: $CLIENT_SLUG"
    print_status "Target Project Directory: $CLIENT_DIR_RELATIVE"
    echo "-------------------------------------"

    # Check if directory already exists
    if [ -d "$CLIENT_DIR_ABSOLUTE" ]; then
        print_error "Directory $CLIENT_DIR_ABSOLUTE already exists!"
        exit 1
    fi

    print_step "Scaffolding Project Directory..."
    mkdir -p "$CLIENT_DIR_ABSOLUTE"
    cp -r apps/website/* "$CLIENT_DIR_ABSOLUTE/"
    # Remove any potentially conflicting files like .git if apps/website was a git repo
    rm -rf "$CLIENT_DIR_ABSOLUTE/.git"
    print_status "Template files copied to $CLIENT_DIR_ABSOLUTE"

    print_step "Updating package.json..."
    # Use a temporary file for sed to avoid issues with in-place editing on different systems
    tmp_file=$(mktemp)
    sed "s/@marketing-factory\/website/@marketing-factory\/${PROJECT_NAME}/g" "$CLIENT_DIR_ABSOLUTE/package.json" > "$tmp_file" && mv "$tmp_file" "$CLIENT_DIR_ABSOLUTE/package.json"
    print_status "package.json updated with project name: @marketing-factory/${PROJECT_NAME}"

    print_step "Creating Client-Specific Configuration..."
    # .env.local
    cat > "$CLIENT_DIR_ABSOLUTE/.env.local" << EOF
# Client Configuration
NEXT_PUBLIC_CLIENT_NAME="$BUSINESS_NAME_RAW"
NEXT_PUBLIC_CLIENT_SLUG="$CLIENT_SLUG"
NEXT_PUBLIC_BUSINESS_TYPE="$BUSINESS_TYPE"
NEXT_PUBLIC_SITE_URL="http://localhost:3000" # Update this for production

# Database (shared or client-specific, adjust as needed)
DATABASE_URL="${DATABASE_URL:-postgresql://dev:dev_password@localhost:5432/marketing_sites}"

# Redis (shared or client-specific)
UPSTASH_REDIS_REST_URL="${UPSTASH_REDIS_REST_URL:-your_upstash_redis_url}"
UPSTASH_REDIS_REST_TOKEN="${UPSTASH_REDIS_REST_TOKEN:-your_upstash_redis_token}"

# Email
RESEND_API_KEY="${RESEND_API_KEY:-your_resend_api_key}"

# Analytics (Placeholder - get from client)
NEXT_PUBLIC_GA_ID="G-XXXXXXXXXX"

# Development
NODE_ENV="development"
EOF
    print_status "Created .env.local"

    # Client settings TypeScript file
    mkdir -p "$CLIENT_DIR_ABSOLUTE/src/config"
    # Extract city and state from city-state-slug
    CITY_NAME_FORMATTED=$(echo "$CITY_STATE_SLUG" | cut -d'-' -f1 | sed -e "s/\b\(.\)/\u\1/g")
    STATE_ABBR_UPPER=$(echo "$CITY_STATE_SLUG" | cut -d'-' -f2 | tr 'a-z' 'A-Z')

    cat > "$CLIENT_DIR_ABSOLUTE/src/config/client.ts" << EOF
// This file is auto-generated by new-client.sh
// Customize it with the client's actual details.
import type { ClientSettings } from '@marketing-factory/ui'; // Adjusted import path

export const clientConfig: ClientSettings = {
  businessName: "$BUSINESS_NAME_RAW",
  businessType: "$BUSINESS_TYPE" as const,
  primaryColor: "#22c55e", // Default Green, customize as needed
  secondaryColor: "#16a34a", // Default Darker Green
  phone: "(555) 123-4567", // Placeholder
  email: "info@${CLIENT_SLUG}.com", // Placeholder
  address: {
    street: "123 Main Street", // Placeholder
    city: "$CITY_NAME_FORMATTED",
    state: "$STATE_ABBR_UPPER",
    zip: "12345" // Placeholder
  },
  serviceAreas: ["$CITY_NAME_FORMATTED", "Surrounding Areas"], // Placeholder
  logo: "/logo-placeholder.png", // Placeholder logo path
  socialMedia: { // Placeholders
    // facebook: "https://facebook.com/${CLIENT_SLUG}",
    // instagram: "https://instagram.com/${CLIENT_SLUG}"
  }
};
EOF
    print_status "Created src/config/client.ts"

    print_step "Generating Business-Specific Homepage..."
    # Capitalize first letter of business type for component name
    COMPONENT_NAME_PREFIX=$(echo "$BUSINESS_TYPE" | sed -e "s/\b\(.\)/\u\1/g")
    
    cat > "$CLIENT_DIR_ABSOLUTE/src/app/page.tsx" << EOF
// This file is auto-generated by new-client.sh
import { ${COMPONENT_NAME_PREFIX}Hero } from '@marketing-factory/ui/business-types/${BUSINESS_TYPE}'; // Adjusted import path
import { clientConfig } from '@/config/client'; // '@/' should resolve to src/

export default function HomePage() {
  return (
    <main>
      <${COMPONENT_NAME_PREFIX}Hero 
        clientSlug="$CLIENT_SLUG"
        settings={clientConfig}
        // Add content prop if needed, e.g., from a local MDX or CMS
      />
      {/* TODO: Add other relevant business-specific components here */}
      {/* Example: <${COMPONENT_NAME_PREFIX}Services settings={clientConfig} /> */}
      {/* Example: <Testimonials clientSlug="$CLIENT_SLUG" /> */}
      {/* Example: <ContactForm clientSlug="$CLIENT_SLUG" /> */}
    </main>
  );
}
EOF
    print_status "Created src/app/page.tsx with ${COMPONENT_NAME_PREFIX}Hero component"

    print_step "Creating Vercel Configuration..."
    cat > "$CLIENT_DIR_ABSOLUTE/vercel.json" << EOF
{
  "buildCommand": "pnpm build",
  "devCommand": "pnpm dev",
  "installCommand": "pnpm install --force", 
  "framework": "nextjs",
  "outputDirectory": ".next",
  "regions": ["iad1"] 
}
EOF
    print_status "Created vercel.json"

    print_step "Installing Dependencies for New Client..."
    # Navigate to client directory to run pnpm install
    (cd "$CLIENT_DIR_ABSOLUTE" && pnpm install --force) # --force might be needed if copying node_modules isn't perfect
    print_status "Dependencies installed."

    print_step "Initializing Git Repository for Client..."
    (cd "$CLIENT_DIR_ABSOLUTE" && git init && git add . && git commit -m "Initial commit - ${BUSINESS_NAME_RAW} website scaffolded from Marketing Site Factory")
    print_status "Git repository initialized."

    echo "-------------------------------------"
    print_status "✅ Client project '$PROJECT_NAME' created successfully!"
    print_status ""
    print_status "Next steps:"
    print_status "1. cd $CLIENT_DIR_RELATIVE"
    print_status "2. Update .env.local with REAL API keys and production URLs."
    print_status "3. Update src/config/client.ts with client's actual business information."
    print_status "4. Run 'pnpm dev' to start the development server for this client."
    print_status "5. Open http://localhost:3000 (or assigned port) to view the site."
    print_status ""
    print_status "For deployment:"
    print_status "1. Create a new GitHub repository for this client project."
    print_status "2. (cd $CLIENT_DIR_RELATIVE && git remote add origin <YOUR_GITHUB_REPO_URL> && git push -u origin main)"
    print_status "3. Connect the GitHub repository to Vercel and deploy."
    print_status "4. Configure domain and environment variables in Vercel project settings."
    echo "-------------------------------------"
    ```

2.  **Deployment Scripts**
    **Create:** `scripts/deploy-staging.sh` (Make executable)
    ```bash
    #!/bin/bash
    set -e
    GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
    print_status() { echo -e "${GREEN}[INFO]${NC} $1"; }
    print_warning() { echo -e "${YELLOW}[WARN]${NC} $1"; }

    if [ ! -f "src/config/client.ts" ]; then
        print_warning "Not in a client project directory. Run this from a client's root."
        exit 1
    fi
    CLIENT_SLUG=$(grep -o 'clientSlug: "[^"]*"' src/config/client.ts | cut -d'"' -f2 || echo "unknown-client")
    print_status "Deploying $CLIENT_SLUG to Vercel staging..."
    print_status "Running tests..."
    pnpm test || { print_warning "Tests failed. Aborting staging deployment."; exit 1; }
    pnpm type-check || { print_warning "Type check failed. Aborting staging deployment."; exit 1; }
    print_status "Building application..."
    pnpm build || { print_warning "Build failed. Aborting staging deployment."; exit 1; }
    print_status "Deploying to Vercel (staging environment)..."
    vercel --target staging --yes
    print_status "✅ Staging deployment initiated for $CLIENT_SLUG."
    ```
    **Create:** `scripts/deploy-prod.sh` (Make executable)
    ```bash
    #!/bin/bash
    set -e
    GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
    print_status() { echo -e "${GREEN}[INFO]${NC} $1"; }
    print_warning() { echo -e "${YELLOW}[WARN]${NC} $1"; }
    print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

    if [ ! -f "src/config/client.ts" ]; then
        print_error "Not in a client project directory. Run this from a client's root."
        exit 1
    fi
    CLIENT_SLUG=$(grep -o 'clientSlug: "[^"]*"' src/config/client.ts | cut -d'"' -f2 || echo "unknown-client")
    print_warning "⚠️  PRODUCTION DEPLOYMENT for $CLIENT_SLUG"
    print_warning "This will deploy to the live client domain."
    read -p "Are you absolutely sure you want to continue? (yes/N) " -r
    echo
    if [[ ! "$REPLY" =~ ^[Yy][Ee][Ss]$ ]]; then
        print_status "Production deployment cancelled."
        exit 0
    fi
    print_status "Running full test suite (unit, e2e, type-check)..."
    pnpm test || { print_error "Unit tests failed. Aborting production deployment."; exit 1; }
    # pnpm test:e2e || { print_error "E2E tests failed. Aborting production deployment."; exit 1; } # Uncomment when E2E is stable
    pnpm type-check || { print_error "Type check failed. Aborting production deployment."; exit 1; }
    print_status "Building production application..."
    pnpm build || { print_error "Build failed. Aborting production deployment."; exit 1; }
    print_status "Deploying to Vercel (production environment)..."
    vercel --prod --yes
    print_status "✅ Production deployment initiated for $CLIENT_SLUG."
    ```

---

## VII. Phase 5: Testing & Development Workflow (45 minutes)

1.  **Vitest Configuration**
    **Create:** `packages/config/vitest.config.ts`
    ```typescript
    import { defineConfig } from 'vitest/config';
    import react from '@vitejs/plugin-react';
    import path from 'path';

    export default defineConfig({
      plugins: [react()],
      test: {
        globals: true,
        environment: 'jsdom',
        setupFiles: [path.resolve(__dirname, './vitest.setup.ts')], // Corrected path
        coverage: {
          provider: 'v8', // or 'istanbul'
          reporter: ['text', 'json', 'html'],
        },
      },
      resolve: {
        alias: {
          // Alias configuration might be needed if testing components from apps/website
          // For packages/ui tests, direct imports should work.
          // Example for an app: '@/': path.resolve(__dirname, '../../apps/website/src'),
        },
      },
    });
    ```
    **Create:** `packages/config/vitest.setup.ts`
    ```typescript
    // vitest.setup.ts
    import '@testing-library/jest-dom/vitest';
    ```
    *Instruction: Ensure Vitest and related dependencies are added to the root `package.json` devDependencies (already covered in Phase 0 for `turbo run test`). Add test scripts to individual packages as needed.*

2.  **Playwright Configuration**
    **Create:** `playwright.config.ts` (at the root of the monorepo)
    ```typescript
    import { defineConfig, devices } from '@playwright/test';
    import path from 'path';

    // Define a base URL, assuming client projects run on different ports or paths during E2E
    // For simplicity, we'll target the template app. Adjust for multi-client E2E.
    const baseURL = 'http://localhost:3000'; // Default for template app

    export default defineConfig({
      // Look for test files in the "tests/e2e" directory, relative to the project root.
      testDir: './apps/website/tests/e2e', // Or make this configurable per client
      fullyParallel: true,
      forbidOnly: !!process.env.CI,
      retries: process.env.CI ? 2 : 0,
      workers: process.env.CI ? 1 : undefined,
      reporter: 'html',
      use: {
        baseURL,
        trace: 'on-first-retry',
      },
      projects: [
        { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
        // { name: 'firefox', use: { ...devices['Desktop Firefox'] } }, // Uncomment as needed
        // { name: 'webkit', use: { ...devices['Desktop Safari'] } },  // Uncomment as needed
        // { name: 'Mobile Chrome', use: { ...devices['Pixel 5'] } }, // Uncomment as needed
      ],
      // Example webServer config for the template app. This needs to be adapted
      // if running E2E against dynamically started client apps.
      webServer: {
        command: 'pnpm --filter @marketing-factory/website dev', // Target the template app
        url: baseURL,
        reuseExistingServer: !process.env.CI,
        timeout: 120 * 1000, // 2 minutes
        // stdout: 'pipe',
        // stderr: 'pipe',
      },
    });
    ```
    *Instruction: Add Playwright to root devDependencies: `pnpm add -D @playwright/test`. Initialize Playwright: `pnpm playwright install --with-deps`. Write sample E2E tests in `apps/website/tests/e2e/`. Example: `apps/website/tests/e2e/homepage.spec.ts`*
    ```typescript
    // apps/website/tests/e2e/homepage.spec.ts
    import { test, expect } from '@playwright/test';

    test('homepage has title', async ({ page }) => {
      await page.goto('/');
      await expect(page).toHaveTitle(/Marketing Site Factory/);
    });
    ```

3.  **GitHub Actions Workflow**
    **Create:** `.github/workflows/ci.yml`
    ```yaml
    name: CI

    on:
      push:
        branches: [main, develop] # Adjust to your main branches
      pull_request:
        branches: [main, develop]

    jobs:
      lint-and-type-check:
        name: Lint & Type Check
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: pnpm/action-setup@v2
            with:
              version: 8.6.0 # Match your local pnpm version
          - uses: actions/setup-node@v4
            with:
              node-version: 20 # Match your local Node.js version
              cache: 'pnpm'
          
          - name: Install dependencies
            run: pnpm install --frozen-lockfile
          
          - name: Lint
            run: pnpm lint # Relies on turbo to run lint in all packages
          
          - name: Type check
            run: pnpm type-check # Relies on turbo to run type-check in all packages

      unit-tests:
        name: Unit Tests
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: pnpm/action-setup@v2
            with:
              version: 8.6.0
          - uses: actions/setup-node@v4
            with:
              node-version: 20
              cache: 'pnpm'
          
          - name: Install dependencies
            run: pnpm install --frozen-lockfile
          
          - name: Run Vitest tests
            run: pnpm test --coverage # Ensure your test script generates coverage
          
          - name: Upload coverage reports to Codecov
            uses: codecov/codecov-action@v3
            with:
              # token: ${{ secrets.CODECOV_TOKEN }} # Optional: for private repos
              fail_ci_if_error: true

      e2e-tests:
        name: E2E Tests
        runs-on: ubuntu-latest
        # Optional: if your tests need a display server
        # services:
        #   xvfb:
        #     image: রবি/xvfb
        #     options: --shm-size=1g
        steps:
          - uses: actions/checkout@v4
          - uses: pnpm/action-setup@v2
            with:
              version: 8.6.0
          - uses: actions/setup-node@v4
            with:
              node-version: 20
              cache: 'pnpm'
          
          - name: Install dependencies
            run: pnpm install --frozen-lockfile
          
          - name: Install Playwright browsers
            run: pnpm playwright install --with-deps
          
          - name: Run Playwright tests
            # env:
            #   DISPLAY: :99 # If using xvfb
            run: pnpm test:e2e # This should trigger Playwright via turbo
          
          - uses: actions/upload-artifact@v3
            if: failure()
            with:
              name: playwright-report
              path: playwright-report/ # Default Playwright report output
              retention-days: 30

      # build: # Example build job, adjust as needed
      #   name: Build All Apps & Packages
      #   runs-on: ubuntu-latest
      #   needs: [lint-and-type-check, unit-tests] # Optional: wait for other jobs
      #   steps:
      #     - uses: actions/checkout@v4
      #     - uses: pnpm/action-setup@v2
      #       with:
      #         version: 8.6.0
      #     - uses: actions/setup-node@v4
      #       with:
      #         node-version: 20
      #         cache: 'pnpm'
            
      #     - name: Install dependencies
      #       run: pnpm install --frozen-lockfile
            
      #     - name: Build applications and packages
      #       run: pnpm build # Relies on turbo to run build in all relevant packages
    ```

---
## VIII. Phase 6A: Docker Development Environment Setup (20 minutes)

1.  **Create Docker Compose Configuration**
    **Create:** `docker-compose.yml` in the root:
    ```yaml
    version: '3.8'
    services:
      postgres:
        image: postgres:15
        container_name: marketing_factory_postgres
        environment:
          POSTGRES_DB: marketing_sites
          POSTGRES_USER: dev
          POSTGRES_PASSWORD: dev_password
        ports:
          - "5432:5432"
        volumes:
          - postgres_data:/var/lib/postgresql/data
        restart: unless-stopped

      redis: # Optional: if Upstash is not used for local dev
        image: redis:7-alpine
        container_name: marketing_factory_redis
        ports:
          - "6379:6379"
        volumes:
          - redis_data:/data
        restart: unless-stopped

    volumes:
      postgres_data:
      redis_data:
    ```
    *Instruction: Update root `package.json` scripts for `dev:db` (already covered in Phase 0).*

---
## IX. Phase 6B: Comprehensive SEO Implementation (90 minutes)

1.  **Implement Business Schema Templates**
    **Create:** `packages/utils/src/seo/schemas.ts`
    ```typescript
    // packages/utils/src/seo/schemas.ts
    import type { ClientSettings } from '@marketing-factory/ui'; // Adjust import if needed

    // Use ClientSettings for business data as it's comprehensive
    export function generateOrganizationSchema(settings: ClientSettings, siteUrl: string) {
      return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": settings.businessName,
        "url": siteUrl,
        "logo": settings.logo ? `${siteUrl}${settings.logo}` : undefined, // Assuming logo path is relative
        "contactPoint": {
          "@type": "ContactPoint",
          "telephone": settings.phone,
          "contactType": "customer service" // Or make this configurable
        },
        // Add other relevant Organization properties like address, sameAs (social media)
      };
    }

    export function generateLocalBusinessSchema(settings: ClientSettings, siteUrl: string) {
      // Basic GeoCoordinates from address (can be improved with actual lat/long)
      const geo = settings.address ? {
        "@type": "GeoCoordinates",
        // Placeholder: "latitude": "0", "longitude": "0" 
        // In a real app, you'd get this from an API or client input
      } : undefined;

      return {
        "@context": "https://schema.org",
        "@type": settings.businessType === 'general' ? 'ProfessionalService' : settings.businessType.charAt(0).toUpperCase() + settings.businessType.slice(1) + 'Service', // e.g., LandscapingService
        "name": settings.businessName,
        "url": siteUrl,
        "image": settings.logo ? `${siteUrl}${settings.logo}` : undefined,
        "telephone": settings.phone,
        "email": settings.email,
        "address": {
          "@type": "PostalAddress",
          "streetAddress": settings.address.street,
          "addressLocality": settings.address.city,
          "addressRegion": settings.address.state,
          "postalCode": settings.address.zip
        },
        "geo": geo,
        "priceRange": "$$", // Placeholder, make configurable
        "areaServed": settings.serviceAreas.map(area => ({
          "@type": "Place",
          "name": area
        })),
        // Potentially add openingHours, paymentAccepted, etc.
      };
    }

    // Example for a specific service page
    export interface ServicePageData {
      serviceName: string;
      serviceDescription: string;
      // Potentially category, offers, etc.
    }

    export function generateServiceSchema(serviceData: ServicePageData, settings: ClientSettings, siteUrl: string, servicePagePath: string) {
      return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": serviceData.serviceName, // Or a more specific category
        "name": serviceData.serviceName,
        "description": serviceData.serviceDescription,
        "url": `${siteUrl}${servicePagePath}`,
        "provider": {
          "@type": "Organization", // Or the specific LocalBusiness type
          "name": settings.businessName,
          "url": siteUrl,
        },
        "areaServed": settings.serviceAreas.map(area => ({
          "@type": "Place",
          "name": area
        })),
        // Add offers, serviceOutput, etc.
      };
    }
    ```

2.  **Implement Geographic Targeting Page Structure**
    **Example for:** `apps/website/src/app/[service-type]/[city-slug]/page.tsx`
    ```typescript
    // apps/website/src/app/[service-type]/[city-slug]/page.tsx
    import { Metadata, ResolvingMetadata } from 'next';
    import { generateLocalBusinessSchema, generateServiceSchema } from '@/utils/seo/schemas'; // Adjust path
    import { clientConfig } from '@/config/client'; // This would be client specific
    import { notFound } from 'next/navigation';

    interface Props {
      params: {
        'service-type': string;
        'city-slug': string;
      };
    }
    
    // This function would fetch dynamic data for the service and city
    async function getServicePageContent(serviceType: string, citySlug: string) {
      // In a real app, fetch this from a CMS or database based on params
      // For now, return mock data or check against clientConfig
      if (serviceType === 'landscaping' && clientConfig.businessType === 'landscaping') {
        return {
          serviceName: `Landscaping in ${citySlug.replace('-', ' ')}`,
          serviceDescription: `Expert landscaping services in ${citySlug.replace('-', ' ')} by ${clientConfig.businessName}.`,
          // other content for the page
        };
      }
      return null;
    }

    export async function generateMetadata({ params }: Props, parent: ResolvingMetadata): Promise<Metadata> {
      const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000';
      const pageContent = await getServicePageContent(params['service-type'], params['city-slug']);

      if (!pageContent) {
        return { title: 'Service Not Found' };
      }
      
      const title = `${pageContent.serviceName} | ${clientConfig.businessName}`;
      const description = pageContent.serviceDescription;
      const canonicalUrl = `/${params['service-type']}/${params['city-slug']}`;

      return {
        title,
        description,
        alternates: {
          canonical: canonicalUrl,
        },
        // OpenGraph and Twitter card metadata can also be added here
      };
    }

    export default async function ServiceLocationPage({ params }: Props) {
      const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000';
      const pageContent = await getServicePageContent(params['service-type'], params['city-slug']);

      if (!pageContent) {
        notFound(); // Or render a custom "not found" component
      }

      const localBusinessSchema = generateLocalBusinessSchema(clientConfig, siteUrl);
      const serviceSchema = generateServiceSchema(
        { serviceName: pageContent.serviceName, serviceDescription: pageContent.serviceDescription },
        clientConfig,
        siteUrl,
        `/${params['service-type']}/${params['city-slug']}`
      );

      return (
        <div>
          <h1>{pageContent.serviceName}</h1>
          <p>{pageContent.serviceDescription}</p>
          {/* Rest of the page content */}

          <script
            type="application/ld+json"
            dangerouslySetInnerHTML={{ __html: JSON.stringify(localBusinessSchema) }}
          />
          <script
            type="application/ld+json"
            dangerouslySetInnerHTML={{ __html: JSON.stringify(serviceSchema) }}
          />
        </div>
      );
    }
    ```

3.  **Implement Automated Sitemap Generation**
    **Create:** `apps/website/src/app/sitemap.ts`
    ```typescript
    // apps/website/src/app/sitemap.ts
    import { MetadataRoute } from 'next';
    import { clientConfig } from '@/config/client'; // Client specific config

    // In a real app, fetch these from a CMS or database
    const dynamicServiceRoutes = [
      { serviceType: 'landscaping', citySlug: 'phoenix-az' },
      { serviceType: 'landscaping', citySlug: 'scottsdale-az' },
      // ... other routes based on services offered and areas served by the client
    ];

    export default function sitemap(): MetadataRoute.Sitemap {
      const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000';
      
      const staticPages: MetadataRoute.Sitemap = [
        { url: baseUrl, lastModified: new Date(), changeFrequency: 'weekly', priority: 1 },
        { url: `${baseUrl}/about`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.8 },
        { url: `${baseUrl}/contact`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.9 },
        { url: `${baseUrl}/services`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.9 },
      ];

      const locationServicePages: MetadataRoute.Sitemap = dynamicServiceRoutes
        .filter(route => route.serviceType === clientConfig.businessType) // Filter by current client's business type
        .map(route => ({
          url: `${baseUrl}/${route.serviceType}/${route.citySlug}`,
          lastModified: new Date(),
          changeFrequency: 'monthly',
          priority: 0.7,
        }));

      return [...staticPages, ...locationServicePages];
    }
    ```

4.  **Implement Image SEO Optimization Component**
    **Create:** `packages/ui/src/components/base/OptimizedImage.tsx`
    ```typescript
    // packages/ui/src/components/base/OptimizedImage.tsx
    import NextImage, { ImageProps as NextImageProps } from 'next/image';
    import { clsx } from 'clsx';

    interface OptimizedImageProps extends Omit<NextImageProps, 'alt'> {
      alt: string; // Make alt strictly required
      // Add any custom props if needed
    }

    export function OptimizedImage({
      src,
      alt,
      width,
      height,
      priority = false,
      className,
      loading = 'lazy',
      sizes = "(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw", // Default sizes
      ...props
    }: OptimizedImageProps) {
      return (
        <NextImage
          src={src}
          alt={alt} // Crucial for SEO and accessibility
          width={width}
          height={height}
          priority={priority}
          loading={loading}
          className={clsx(className)} // Apply any custom classes
          sizes={sizes}
          // Consider adding a default style for object-fit if common
          // style={{ objectFit: 'cover', objectPosition: 'center', ...props.style }}
          {...props}
        />
      );
    }
    ```
    *Instruction: Ensure all images used in components leverage this `OptimizedImage`.*

---

## X. Phase 6C: Additional Development Tools & Commands (30 minutes)

1.  **Add Bundle Analyzer**
    *Instruction: `pnpm add -D @next/bundle-analyzer` (if not already added for `next.config.js`).*
    *Instruction: Add script to root `package.json` (already covered in Phase 0).*
    ```json
    // In root package.json scripts
    // "analyze": "ANALYZE=true pnpm --filter @marketing-factory/website build" // Example for template
    // For a client: "analyze": "cd clients/client-acme-website && ANALYZE=true pnpm build"
    ```

2.  **Add Performance Testing Scripts**
    *Instruction: Add comprehensive test scripts to root `package.json` (already covered in Phase 0).*
    *Instruction: `pnpm add -D lighthouse @lhci/cli` (if not covered by other test setups).*
    **Create/Update:** `lighthouserc.js` (at the root)
    ```javascript
    // lighthouserc.js
    module.exports = {
      ci: {
        collect: {
          // This needs to be adaptable per client or run against a deployed preview
          // startServerCommand: 'pnpm --filter @marketing-factory/website dev', // Example for template
          // url: ['http://localhost:3000'],
          // For CI, better to run against static build or deployed URL
          staticDistDir: './apps/website/.next', // Example for template, if testing static export
          // Alternatively, use a script that deploys a preview and gets its URL
        },
        assert: {
          presets: 'lighthouse:recommended',
          assertions: {
            'categories:performance': ['warn', {minScore: 0.9}],
            'categories:accessibility': ['warn', {minScore: 0.95}], // Higher bar
            'categories:best-practices': ['warn', {minScore: 0.9}],
            'categories:seo': ['warn', {minScore: 0.9}],
            'cumulative-layout-shift': ['error', {maxNumericValue: 0.1}],
            'largest-contentful-paint': ['error', {maxNumericValue: 2500}],
            'interactive': ['error', {maxNumericValue: 3800}], // TTI
            // Consider INP when Lighthouse supports it fully in CI
          },
        },
        upload: {
          target: 'temporary-public-storage', // Or configure GitHub status checks, S3, etc.
        },
      },
    };
    ```
    *Add to root package.json scripts (if not already):*
    ```json
    // "test:perf": "lhci autorun", // This can be run in CI
    // "lighthouse:local": "lighthouse http://localhost:3000 --view --preset=desktop"
    ```

3.  **Add Debug and Development Scripts**
    *Instruction: Update root `package.json` with specific debug scripts if needed (some already covered).*
    ```json
    // "dev:debug:website": "pnpm --filter @marketing-factory/website exec -- next dev --inspect",
    // "build:debug:website": "pnpm --filter @marketing-factory/website exec -- next build --debug",
    // "db:seed": "pnpm --filter @marketing-factory/website exec -- tsx prisma/seed.ts" // if seed script is in website app
    ```

---
## XI. Phase 7: New Client Website Launch Process

**Goal**: Detail the end-to-end, repeatable process for launching a new client website using the Marketing Site Factory. This phase synthesizes various parts of the `DEV_HANDBOOK.md`.

**Overall Estimated Client Deployment Time**: 2-3 hours (as per handbook)

### A. Step 1: Client Intake & Initial Project Setup (Automated + 10-15 mins manual review/setup)

1.  **Gather Client Information**:
    *   Required: Full Business Name, Primary City & State (for slug, e.g., "Phoenix, AZ"), Business Type (`landscaping`, `hvac`, `roofing`, `plumbing`, `general`).
    *   Highly Recommended: Contact Info (Phone, Email, Physical Address if applicable), Logo files, Brand Colors (Hex codes), Key Services List, Primary Service Areas (list of cities/neighborhoods).
    *   Optional: Desired Domain Name, Social Media Links, Testimonials, Project Photos.

2.  **Run `new-client.sh` Script**:
    *   Navigate to the root `marketing-site-factory/` directory.
    *   Execute the script: `./scripts/new-client.sh "Client Business Name" "city-state-slug" "business-type"`
        *   Example: `./scripts/new-client.sh "Acme Landscaping Inc." "phoenix-az" "landscaping"`
    *   *Expected Outcome: New client project directory (e.g., `clients/client-acme-landscaping-inc-website/`) scaffolded.*

3.  **Manual Configuration & Verification (Inside new client directory `clients/client-...`)**:
    *   **Review & Update `.env.local`**:
        *   Crucially, update `NEXT_PUBLIC_SITE_URL` when a staging/production URL is known.
        *   Add real API keys for `RESEND_API_KEY`, `UPSTASH_...` if applicable for this client.
        *   Set client's `NEXT_PUBLIC_GA_ID`.
    *   **Review & Update `src/config/client.ts`**:
        *   Verify/Correct all business details (name, phone, email, address).
        *   Set `primaryColor`, `secondaryColor` based on client branding.
        *   Update `serviceAreas` with actual locations.
        *   Add real `logo` path (e.g., `/images/client-logo.png`) and social media links.
    *   **Database Record for Client**:
        *   Manually add a record to the `Client` table in your database (e.g., via Prisma Studio `pnpm dev:db`) for this new client. Include the `slug`, `businessName`, `businessType`, and the JSON from `client.ts` into the `settings` field.
        *   Manually add a record to the `Client` table in your database (e.g., via Prisma Studio `pnpm dev:db`) for this new client. Include the `slug`, `businessName`, `businessType`, and the JSON from `client.ts` into the `settings` field.
    *   **Start Development Server**: `pnpm dev`
    *   **Verify Locally**: Open `http://localhost:XXXX` (port shown in terminal). Check:
        *   Homepage loads with correct business name and basic styling.
        *   Relevant business-type hero component is displayed.
        *   Console has no major errors.

4.  **Version Control Setup (Inside new client directory)**:
    *   The `new-client.sh` script initializes a git repository.
    *   Create a new **private** repository on GitHub (or your provider) named (e.g., `acme-landscaping-website`).
    *   `git remote add origin <URL_OF_NEW_GITHUB_REPO>`
    *   `git branch -M main`
    *   `git push -u origin main`

5.  **Vercel Project Setup & Initial Staging Deployment**:
    *   In Vercel dashboard, create a new project. Import the GitHub repository created above.
    *   **Configure Project Settings on Vercel**:
        *   Framework Preset: Next.js.
        *   Root Directory: Should be the root of the client project.
        *   Build Command: `pnpm build` (or `turbo build --filter=<client-project-name>...` if deploying from monorepo root in Vercel).
        *   Install Command: `pnpm install --force` (or as per `vercel.json`).
    *   **Add Environment Variables on Vercel (for Staging/Production)**:
        *   `DATABASE_URL` (from your Neon project for this client or shared).
        *   `RESEND_API_KEY`, `UPSTASH_...` (if applicable, use production keys).
        *   `NEXT_PUBLIC_CLIENT_NAME`, `NEXT_PUBLIC_CLIENT_SLUG`, `NEXT_PUBLIC_BUSINESS_TYPE` (these should match `.env.local` and `client.ts`).
        *   `NEXT_PUBLIC_SITE_URL` (Vercel's preview URL for staging, custom domain for production).
        *   `NEXT_PUBLIC_GA_ID` (client's production GA ID).
    *   Vercel will automatically deploy on the first push to `main` (or the configured production branch). This becomes the initial staging/preview link.

### B. Step 2: Local Development & Customization (90-120 minutes)
*(Inside client project directory, on a new feature branch)*

1.  **Branching**: `git checkout -b feat/initial-content-and-styling`
2.  **Content Implementation**:
    *   Populate all pages (Homepage, About, Services, Contact) with client-provided text, actual images (using `<OptimizedImage />`).
    *   Create dynamic service pages if applicable (e.g., `/[service-slug]/page.tsx`).
    *   Ensure consistent NAP (Name, Address, Phone) across the site, especially footer and contact page.
3.  **Component Customization & Creation**:
    *   Use/customize components from `packages/ui/business-types/<type>/`.
    *   If AI tools (loveable/21st.dev) are used:
        *   Generate component variations using prompts from `packages/ui/src/templates/ai-prompts.ts`.
        *   Refine and integrate generated components.
        *   Ensure responsiveness and accessibility.
    *   Place new client-specific components in `src/components/` of the client project if they are not reusable for the factory.
4.  **Styling**:
    *   Adjust Tailwind theme in `tailwind.config.js` if client has very specific branding not covered by `client.ts` color settings.
    *   Ensure all components adhere to client branding.
5.  **SEO Configuration (Detailed Pass)**:
    *   Update `generateMetadata` in each page/layout for unique titles, descriptions.
    *   Implement schema markup (`generateLocalBusinessSchema`, `generateServiceSchema`, etc.) in relevant pages, ensuring data is from `clientConfig` or page content.
    *   Verify `sitemap.ts` generates correct URLs for this client.
    *   Create `robots.txt` if custom rules needed (usually Next.js default is fine).
6.  **Integrations**:
    *   Test contact form thoroughly. Ensure emails are sent (via Resend) and data saved to DB.
    *   Integrate Google Analytics using `NEXT_PUBLIC_GA_ID`.
    *   Implement CallRail/other tracking if required.
7.  **Commit & Push Regularly**: `git add . && git commit -m "feat: Implement about page and service details" && git push`

### C. Step 3: Testing & Staging Deployment (30 minutes + Review Time)

1.  **Run All Local Tests**: `pnpm test` (unit), `pnpm test:e2e` (if feasible locally), `pnpm type-check`. Address failures.
2.  **Accessibility & Visual Checks**: Manually use browser dev tools (Axe) or integrate into E2E. If Chromatic is setup for `packages/ui`, ensure component changes are approved.
3.  **Deploy to Staging**:
    *   Merge feature branch to `main` (or a dedicated `staging` branch).
    *   Vercel auto-deploys from the connected Git branch. Or use `./scripts/deploy-staging.sh` (if configured to point to this client's Vercel project).
    *   URL will be Vercel's preview URL (e.g., `project-name-git-branch-org.vercel.app`).

4.  **Internal QA on Staging**: Full site walkthrough: links, forms, responsiveness, integrations, console errors. Use `DEV_HANDBOOK.md` checklists.

### D. Step 4: Client Review & Iteration (Time varies)

1.  Share staging link with client.
2.  Collect feedback (structured).
3.  Implement revisions on new feature branches, merge, redeploy to staging. Repeat.

### E. Step 5: Production Deployment & Go-Live (30 minutes + DNS propagation)

1.  **Final Checks**: All tests pass, performance budgets met (Lighthouse on staging), production environment variables in Vercel are correct and final.
2.  **Branching**: Merge approved staging version (e.g., `main` or `staging` branch) into the production branch (e.g., `prod` or `main` if `main` is production).
3.  **Configure Custom Domain in Vercel**:
    *   Add client's custom domain(s) (e.g., `www.clientdomain.com`, `clientdomain.com`) in Vercel project settings.
    *   Vercel provides DNS records (A, CNAME).
4.  **Update DNS Records**: At client's domain registrar, update DNS. Propagation: minutes to 48 hours.
5.  **Deploy to Production**:
    *   Push to the production branch in Git. Vercel auto-deploys.
    *   Or use `./scripts/deploy-prod.sh` (if configured for this client's Vercel project).
    *   Vercel handles SSL.
6.  **Verify Production Site**: Thoroughly test live site. Check analytics. Use `DEV_HANDBOOK.md` Deployment Checklist.

### F. Step 6: Client Handoff & Post-Launch (Ongoing for 30 days support)
*(As per `DEV_HANDBOOK.md` Handoff Package, Training, Support, Success Metrics)*

1.  **Documentation & Asset Transfer**: GitHub access, Vercel project access (or transfer ownership), all handoff documents.
2.  **Training Sessions**: Conduct content management, analytics, and basic maintenance training.
3.  **Finalize Analytics & Search Console**: Ensure client owns/has access to GA4. Submit sitemap to GSC.
4.  **Provide 30-Day Support**: Adhere to agreed SLAs.
5.  **Monitor Success Metrics**: Uptime, Core Web Vitals, local rankings, client satisfaction survey.

### G. Step 7: Ongoing Maintenance & Support (Post 30 days - Optional/Contractual)
*(As per `DEV_HANDBOOK.md` for software updates, security, performance, content support)*

---
## XII. Summary of Key Files and Scripts to Create

*   **Monorepo Root:**
    *   `package.json`
    *   `pnpm-workspace.yaml`
    *   `turbo.json`
    *   `.env.example`
    *   `.gitignore`
    *   `README.md`
    *   `biome.json`
    *   `docker-compose.yml`
    *   `playwright.config.ts`
    *   `lighthouserc.js`
    *   `.github/workflows/ci.yml`
*   **`apps/website/` (Template App):**
    *   `package.json`
    *   `next.config.js`
    *   `tailwind.config.js`
    *   `tsconfig.json`
    *   `prisma/schema.prisma`
    *   `src/app/layout.tsx`, `src/app/page.tsx`, `src/app/globals.css`
    *   `src/app/api/contact/route.ts`
    *   `src/app/api/client/[slug]/route.ts`
    *   `src/app/sitemap.ts`
    *   `tests/e2e/homepage.spec.ts` (example)
*   **`packages/ui/`:**
    *   `package.json`
    *   `tsconfig.json`
    *   `src/index.ts` (exports)
    *   `src/types/index.ts` (interfaces)
    *   `src/templates/ai-prompts.ts`
    *   `src/components/base/Button.tsx`, `OptimizedImage.tsx`, etc.
    *   `src/business-types/<type>/<Component>.tsx` and `index.ts` for each type
*   **`packages/utils/`:**
    *   (Initially, `src/seo/schemas.ts` will be here. May add more utils later)
    *   `package.json`, `tsconfig.json`
*   **`packages/config/`:**
    *   `tsconfig.json` (base for other tsconfigs)
    *   `vitest.config.ts`
    *   `vitest.setup.ts`
*   **`scripts/`:**
    *   `new-client.sh`
    *   `deploy-staging.sh`
    *   `deploy-prod.sh`
*   **`docs/`:**
    *   `SETUP_WSL2.md`
    *   (Other handbook sections like `COMPONENT_GUIDELINES.md`, `API_REFERENCE.md` can be added later)

This implementation guide aims to provide a clear, actionable path to build the Marketing Site Factory.
---
**End of Implementation Guide** 