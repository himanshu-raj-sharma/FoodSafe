# FoodSafe Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      ANDROID APP                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Dashboard│  │ Incidents│  │   CAPA   │  │  Supplier│   │
│  │  (MVVM)  │  │  (MVVM)  │  │  (MVVM)  │  │  (MVVM)  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Batch   │  │  Recall  │  │  Audit   │  │  Analytics│   │
│  │  (MVVM)  │  │  (MVVM)  │  │  (MVVM)  │  │  (MVVM)  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Sync    │  │  AI      │  │ Notifications│  │ Settings│   │
│  │ (WorkMgr)│  │  Copilot │  │  (FCM)     │  │  (MVVM)  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTPS / WebSocket
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     FASTAPI BACKEND                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Auth    │  │  Incidents│  │   CAPA   │  │ Suppliers│   │
│  │  (JWT)   │  │  (RBAC)  │  │ (RBAC)   │  │  (RBAC)  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Batches │  │  Recalls │  │  Audit   │  │ Analytics│   │
│  │  (RBAC)  │  │  (RBAC)  │  │  (RBAC)  │  │ (RBAC)   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Sync    │  │  AI      │  │ Notifications│  │  Risk   │   │
│  │ Engine   │  │  Copilot │  │  (FCM)     │  │Service  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────┬───────────────────────────────────────┘
                      │ SQLAlchemy 2.0
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    PostgreSQL 16                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │organizations││ outlets  │  │   users  │  │  roles   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │incidents │  │   capa   │  │ suppliers│  │  batches │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │audit_logs│  │ sync_ops │  │ notifications│  │  tasks  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Multi-Tenant Isolation

- Every query filters by `organization_id`
- JWT contains `org_id` claim
- Middleware validates tenant membership
- No cross-tenant data leakage possible

## Offline-First Sync

1. Room database stores all operations locally
2. WorkManager queues sync operations
3. SyncEngine uploads when connectivity resumes
4. Conflict detection via entity versioning
5. Idempotent operations for safe retries

## Risk Engine

Deterministic scoring algorithm:
- Critical incident: +30 points
- Temperature deviation: +20 points
- Hygiene issue: +15 points
- Overdue CAPA: +10 points
- Capped at 100 (critical)

## AI Copilot

- Human-verification safety gate
- Mock provider for demo
- OpenAI/Anthropic provider for production
- Generates suggestions only, never auto-approves
