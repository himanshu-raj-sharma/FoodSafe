# FoodSafe - Food Safety SaaS Platform

> Production-grade food safety operations platform for QSRs, cloud kitchens, and restaurant groups.

## Overview

FoodSafe is a multi-tenant SaaS platform designed to streamline food safety operations for modern food businesses. It combines offline-first mobile capabilities with intelligent backend services to ensure compliance, track incidents, and maintain audit-ready documentation.

## Key Features

### Core Functionality
- **Multi-Tenant Architecture** — Organization → Outlet → User hierarchy with full data isolation
- **Offline-First Mobile App** — Full operations without internet via Room database + WorkManager sync
- **HACCP Compliance** — Documented workflows with evidence chain for audits
- **Incident Management** — Report, track, and resolve food safety incidents
- **CAPA System** — Corrective and preventive action workflow with verification
- **Batch Traceability** — Supplier → Outlet traceability for recall readiness
- **Risk Scoring Engine** — Deterministic risk assessment without black-box AI
- **AI Copilot** — AI-assisted suggestions with human gate for safety-critical decisions

### Security & Compliance
- JWT authentication with refresh token rotation
- Role-Based Access Control (RBAC) with 5 permission levels
- AES-256 encryption for sensitive data at rest
- TLS 1.3 enforced in transit
- Comprehensive audit logging
- GDPR-compliant data handling

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | FastAPI, Python 3.11, SQLAlchemy 2.0 |
| **Database** | PostgreSQL with connection pooling |
| **Mobile** | Android (Kotlin), Room Database |
| **File Storage** | MinIO (S3-compatible) |
| **Task Queue** | Background tasks with scheduling |
| **Security** | JWT, Bcrypt, CORS whitelisting |

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Android App    │────▶│   FastAPI       │────▶│   PostgreSQL    │
│  (Offline-First)│     │   Backend       │     │   (Multi-Tenant)│
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                │
                                ▼
┌─────────────────┐     ┌─────────────────┐
│    MinIO        │     │  AI Services    │
│   (Storage)     │     │   (Copilot)     │
└─────────────────┘     └─────────────────┘
```

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 14+
- Android Studio (for mobile app)

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env with your PostgreSQL credentials

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

Access the API documentation at `http://localhost:8000/docs`

### Mobile App Setup

Open the Android project in Android Studio and build/run on your device or emulator.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/auth/login` | User login |
| `POST` | `/api/v1/auth/register` | User registration |
| `GET` | `/api/v1/organizations/` | List organizations |
| `POST` | `/api/v1/organizations/` | Create organization |
| `GET` | `/api/v1/outlets/` | List outlets |
| `POST` | `/api/v1/incidents/` | Report incident |
| `POST` | `/api/v1/capa/` | Create CAPA |
| `GET` | `/api/v1/batches/` | Batch traceability |
| `POST` | `/api/v1/copilot/analyze` | AI risk analysis |

## Deployment

### Render.com (Free Tier)

```bash
# Push to GitHub
git push origin main

# On Render:
# 1. Create PostgreSQL service
# 2. Create Web Service from GitHub repo
# 3. Set environment variables
# 4. Add build command: cd backend && pip install -r requirements.txt
# 5. Add start command: gunicorn app.main:app -w 2
```

### Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access services:
# Backend: http://localhost:8000
# pgAdmin: http://localhost:5050
# MinIO: http://localhost:9000
```

## Revenue Model

| Plan | Price | Features |
|------|-------|----------|
| **Starter** | $49/month | 1 outlet, 5 users |
| **Growth** | $149/month | 5 outlets, 25 users |
| **Enterprise** | Custom | 20+ outlets, unlimited users |

## Market

- **TAM**: $12B food safety software market
- **SAM**: $2B QSR/kitchen groups in APAC
- **SOM**: 500 outlets in Year 1

## Owner

**Himanshu Raj**
- Email: rajhimanshu5522@gmail.com
- GitHub: @himanshu-raj-sharma

---

**FoodSafe © 2026 Himanshu Raj. All rights reserved.**
