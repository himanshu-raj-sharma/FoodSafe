# FoodSafe Security Policy

## Security Overview

FoodSafe implements production-grade security for food safety operations data. This document outlines our security measures, compliance posture, and vulnerability disclosure process.

## Authentication & Authorization

- **JWT-based authentication** with refresh token rotation
- **Bcrypt password hashing** (12 rounds work factor)
- **Role-Based Access Control (RBAC)** with granular permissions:
  - `OWNER` — Full organization control
  - `ADMIN` — Manage users, outlets, configuration
  - `MANAGER` — View reports, approve CAPA, manage incidents
  - `SUPERVISOR` — Create tasks, report incidents, verify CAPA
  - `STAFF` — Execute tasks, log observations
- **Permission checks** on every API endpoint (e.g., `incident:create`, `capa:verify`)
- **Tenant isolation** — Users can only access data within their organization

## Data Protection

- **Encryption at rest**: PostgreSQL with TDE-ready configuration
- **Encryption in transit**: TLS 1.3 enforced via reverse proxy
- **Sensitive data encryption**: `encrypt_sensitive_data` / `decrypt_sensitive_data` hooks (AES-256-GCM)
- **Object storage**: MinIO/S3-compatible with signed URLs for evidence files
- **File upload validation**: Extension whitelist (`jpg, jpeg, png, pdf`), MIME type check, 10MB size limit

## API Security

- **Rate limiting**: 100 requests/minute per client (configurable via `RATE_LIMIT_REQUESTS_PER_MINUTE`)
- **CORS**: Configured with explicit origin whitelist (`CORS_ORIGINS`)
- **Input validation**: Pydantic v2 schemas with strict type checking
- **SQL injection prevention**: SQLAlchemy 2.0 parameterized queries only (no raw SQL)
- **Error handling**: Generic error messages in production; detailed errors in development only

## Security Headers (Production)

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## Audit Logging

Every state change is logged via `AuditLog` model:
- **Who**: User ID
- **What**: Entity type + ID
- **How**: Action type (CREATE, UPDATE, DELETE)
- **When**: Timestamp with timezone
- **Why**: Change reason (optional)

## Vulnerability Disclosure

If you discover a security vulnerability, please report it responsibly:

1. **Email**: security@foodsafe.example.com
2. **PGP Key**: Available upon request
3. **Response time**: Within 48 hours
4. **Disclosure**: Coordinated release after fix

We reward responsible disclosure with public recognition.

## Compliance

- **GDPR**: Data residency support, right to erasure, audit trail
- **HACCP**: Documented food safety workflows with evidence chain
- **ISO 22000**: Traceability from supplier to outlet
- **SOC 2 Type II**: In progress (target Q2 2026)

## Penetration Testing

- External pentest: Quarterly
- Dependency scanning: Dependabot / GitHub Security Advisories
- SAST: GitHub CodeQL on every PR
- Secrets scanning: GitHub secret scanning enabled

## Incident Response

1. **Detect**: Audit logs + anomaly detection
2. **Contain**: Isolate affected tenant data
3. **Eradicate**: Patch vulnerability, rotate credentials
4. **Recover**: Restore from backups, verify integrity
5. **Lessons learned**: Post-mortem within 7 days

## Contact

Security Team: security@foodsafe.example.com
Owner: Himanshu Raj
