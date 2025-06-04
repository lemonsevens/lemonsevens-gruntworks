# Marketing Site Factory – Implementation Checklist

**Purpose:** Use this checklist to track the actual implementation of all recommendations and requirements from the Implementation Guide. Assign team members, set due dates, and mark status for each item.

---

## Legend
- [ ] = Not started
- [~] = In progress
- [x] = Complete

| #   | Task/Requirement | Assignee | Due Date | Status | Notes |
| --- | ---------------- | -------- | -------- | ------ | ----- |


## Phase 0: Foundation Creation
| #   | Task                                                                                         | Assignee | Due Date | Status | Notes |
| --- | -------------------------------------------------------------------------------------------- | -------- | -------- | ------ | ----- |
| 0.1 | Create root directory structure (`apps/`, `packages/`, `clients/`, `scripts/`, `docs/`, etc) |          |          | [ ]    |       |
| 0.2 | Create and configure `package.json`, `pnpm-workspace.yaml`, `turbo.json`                     |          |          | [ ]    |       |
| 0.3 | Add `.env.example`, `.gitignore`, `README.md`                                                |          |          | [ ]    |       |
| 0.4 | Create initial `apps/website/` Next.js app and config files                                  |          |          | [ ]    |       |
| 0.5 | Add Biome config and scripts                                                                 |          |          | [ ]    |       |
| 0.6 | Add Docker Compose for Postgres/Redis                                                        |          |          | [ ]    |       |

## Phase 1: Component Library & Utilities
| #   | Task                                                          | Assignee | Due Date | Status | Notes |
| --- | ------------------------------------------------------------- | -------- | -------- | ------ | ----- |
| 1.1 | Create `packages/ui/` and base components (Button, Card, etc) |          |          | [ ]    |       |
| 1.2 | Create business-type component directories and templates      |          |          | [ ]    |       |
| 1.3 | Add AI prompt templates for component generation              |          |          | [ ]    |       |
| 1.4 | Create `packages/utils/` and add SEO/schema utilities         |          |          | [ ]    |       |

## Phase 2: Testing & CI/CD
| #   | Task                                          | Assignee | Due Date | Status | Notes |
| --- | --------------------------------------------- | -------- | -------- | ------ | ----- |
| 2.1 | Add Vitest config and sample tests            |          |          | [ ]    |       |
| 2.2 | Add Playwright config and E2E tests           |          |          | [ ]    |       |
| 2.3 | Add Lighthouse CI config                      |          |          | [ ]    |       |
| 2.4 | Add GitHub Actions workflow for CI            |          |          | [ ]    |       |
| 2.5 | Add Chromatic/Storybook for visual regression |          |          | [ ]    |       |
| 2.6 | Add accessibility testing (axe-core)          |          |          | [ ]    |       |

## Phase 3: Automation Scripts
| #   | Task                               | Assignee | Due Date | Status | Notes |
| --- | ---------------------------------- | -------- | -------- | ------ | ----- |
| 3.1 | Create `scripts/new-client.sh`     |          |          | [ ]    |       |
| 3.2 | Create `scripts/deploy-staging.sh` |          |          | [ ]    |       |
| 3.3 | Create `scripts/deploy-prod.sh`    |          |          | [ ]    |       |

## Phase 4: Database & API
| #   | Task                                  | Assignee | Due Date | Status | Notes |
| --- | ------------------------------------- | -------- | -------- | ------ | ----- |
| 4.1 | Add Prisma schema and generate client |          |          | [ ]    |       |
| 4.2 | Implement contact form API route      |          |          | [ ]    |       |
| 4.3 | Implement client config API route     |          |          | [ ]    |       |
| 4.4 | Add analytics/event tracking API      |          |          | [ ]    |       |

## Phase 5: SEO & Performance
| #   | Task                                      | Assignee | Due Date | Status | Notes |
| --- | ----------------------------------------- | -------- | -------- | ------ | ----- |
| 5.1 | Add schema generators and meta tag system |          |          | [ ]    |       |
| 5.2 | Implement dynamic sitemap generation      |          |          | [ ]    |       |
| 5.3 | Add image optimization component          |          |          | [ ]    |       |
| 5.4 | Add performance budgets and monitoring    |          |          | [ ]    |       |

## Phase 6: Client Launch & Handoff
| #   | Task                                 | Assignee | Due Date | Status | Notes |
| --- | ------------------------------------ | -------- | -------- | ------ | ----- |
| 6.1 | Run `new-client.sh` for first client |          |          | [ ]    |       |
| 6.2 | Update client config and content     |          |          | [ ]    |       |
| 6.3 | Test all features and run full CI    |          |          | [ ]    |       |
| 6.4 | Deploy to staging and production     |          |          | [ ]    |       |
| 6.5 | Complete documentation and handoff   |          |          | [ ]    |       |
| 6.6 | Provide training and 30-day support  |          |          | [ ]    |       |

## Phase 7: Success Metrics & Review
| #   | Task                               | Assignee | Due Date | Status | Notes |
| --- | ---------------------------------- | -------- | -------- | ------ | ----- |
| 7.1 | Achieve 2-3 hour client deployment |          |          | [ ]    |       |
| 7.2 | Meet Lighthouse 90+ scores         |          |          | [ ]    |       |
| 7.3 | Zero accessibility violations      |          |          | [ ]    |       |
| 7.4 | <$20/month infra per client        |          |          | [ ]    |       |
| 7.5 | 99.9% uptime                       |          |          | [ ]    |       |
| 7.6 | >4.5/5 client satisfaction         |          |          | [ ]    |       |

---

**Instructions:**
- Assign each task to a team member and set a due date.
- Update the status as you progress: [ ] Not started, [~] In progress, [x] Complete.
- Use the Notes column for blockers, links, or additional context.

--- 