# FoodSafe 🍽️🛡️

**Incident → Evidence → CAPA → Supplier/Batch Traceability → Recall Readiness → Risk Intelligence**

Food Safety Operations & Intelligence Platform for growing food businesses.

[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://www.docker.com/)

## Quick Links

| Document | Description |
|----------|-------------|
| [SECURITY.md](SECURITY.md) | Security policy & vulnerability disclosure |
| [LICENSE](LICENSE) | Proprietary license |
| [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) | Free deployment on Render/Railway/Oracle |
| [docs/API_REFERENCE.md](docs/API_REFERENCE.md) | API endpoint reference |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System architecture diagram |
| [docs/GDPR_COMPLIANCE.md](docs/GDPR_COMPLIANCE.md) | GDPR compliance documentation |
| [docs/SECURITY_AUDIT.md](docs/SECURITY_AUDIT.md) | OWASP security audit checklist |
| [docs/COMPETITIVE_ANALYSIS.md](docs/COMPETITIVE_ANALYSIS.md) | Market positioning |

## Quick Start (Free Deployment)

### Option 1: Render.com (Recommended)
```bash
# 1. Push code to GitHub
git push origin main

# 2. On render.com:
#    - New → PostgreSQL → Free
#    - New → Web Service → Connect repo
#    - Set env vars from .env.example
#    - Deploy
```

### Option 2: Docker Compose (Local)
```bash
docker-compose up -d
# Backend: http://localhost:8000
# MinIO: http://localhost:9001
# PostgreSQL: localhost:5432
```

### Option 3: Oracle Cloud Free Tier
- Always-free Autonomous PostgreSQL
- 20GB storage, 1 OCPU
- No expiration

See [DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) for detailed steps.

## Technology Stack

| Layer | Technology |
|-------|-----------|
| **Android** | Kotlin, Jetpack Compose, Room, WorkManager |
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy 2.0 |
| **Database** | PostgreSQL 16 |
| **Storage** | MinIO / S3 compatible |
| **Auth** | JWT + bcrypt (12 rounds) |
| **Sync** | Offline-first with conflict resolution |
| **Risk** | Deterministic scoring engine |
| **AI** | OpenAI/Anthropic with human verification gate |

## Security Features

- ✅ Bcrypt password hashing (12 rounds)
- ✅ JWT access + refresh tokens
- ✅ RBAC (OWNER/ADMIN/MANAGER/SUPERVISOR/STAFF)
- ✅ Tenant isolation (organization_id on every query)
- ✅ Audit logging for all state changes
- ✅ File upload validation (extension/MIME/size)
- ✅ Soft delete pattern (deleted_at)
- ✅ Rate limiting (configurable)
- ✅ SQL injection prevention (SQLAlchemy ORM)

## Project Structure

```
FoodSafe/
├── android/          # Kotlin Android app
├── backend/          # Python FastAPI backend
│   ├── app/
│   │   ├── core/     # Config, security, logging
│   │   ├── models/   # SQLAlchemy models
│   │   ├── schemas/  # Pydantic schemas
│   │   ├── api/v1/   # API routes
│   │   ├── repositories/  # Data access layer
│   │   └── services/      # Business logic
│   ├── alembic/      # Database migrations
│   └── tests/        # Test suite
├── docs/             # Documentation
├── infrastructure/   # Docker, CI/CD
└── scripts/          # Setup scripts
```

## Compliance

- HACCP documentation workflows
- ISO 22000 traceability
- GDPR data subject rights
- SOC 2 Type II (in progress)

## License

Proprietary — see [LICENSE](LICENSE)

## Contact

Security: security@foodsafe.example.com
Business: himanshu.raj@example.com
GitHub: @himanshu-raj (replace with actual username)
