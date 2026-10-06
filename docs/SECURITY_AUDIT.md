# Security Audit Checklist — FoodSafe v0.1.0

## OWASP Top 10 Coverage

| # | Vulnerability | Status | Implementation |
|---|--------------|--------|----------------|
| A01 | Broken Access Control | ✅ | RBAC + tenant isolation on every query |
| A02 | Cryptographic Failures | ✅ | Bcrypt (12 rounds) + JWT HS256 + TLS 1.3 |
| A03 | Injection | ✅ | SQLAlchemy ORM parameterized queries |
| A04 | Insecure Design | ⚠️ | Missing threat modeling — schedule STRIDE review |
| A05 | Security Misconfiguration | ⚠️ | Hardcoded defaults in `.env.example` — rotate in production |
| A06 | Vulnerable Components | ⚠️ | No SBOM generated yet — run `pip-audit` |
| A07 | Auth Failures | ✅ | JWT expiry + refresh rotation + bcrypt |
| A08 | Data Integrity | ✅ | Audit logs + entity versioning for conflict detection |
| A09 | Logging Failures | ✅ | Structured logging with request IDs |
| A10 | SSRF | ⚠️ | Object storage URL validation pending |

## Authentication Tests

- [x] Password complexity enforced (uppercase + lowercase + digit, min 8 chars)
- [x] Bcrypt hashing with configurable rounds
- [x] JWT access token expiry (default 1440 min = 24h)
- [x] JWT refresh token expiry (default 7 days)
- [x] Token verification on protected endpoints
- [x] Account disabled check on login
- [x] Organization status check on login

## Authorization Tests

- [x] Role-based permission checks (OWNER, ADMIN, MANAGER, SUPERVISOR, STAFF)
- [x] Tenant-scoped queries (organization_id filter)
- [x] Explicit permission enum (incident:create, capa:verify, etc.)

## Data Protection Tests

- [x] Soft delete pattern (deleted_at column)
- [x] File upload extension/MIME/size validation
- [x] Object storage signed URLs
- [x] Encryption hooks in place (AES-256-GCM pending implementation)

## Infrastructure Tests

- [x] Docker Compose for reproducible local env
- [x] PostgreSQL connection pooling (QueuePool, size 20)
- [x] Health + readiness endpoints
- [x] CORS origin whitelist

## Gaps to Close Before Production

1. **Threat model** (STRIDE) for incident reporting + traceability flows
2. **SBOM** generation (`pip-audit` or `cyclonedx-bom`)
3. **Secrets rotation** — rotate `JWT_SECRET`, `DATABASE_URL` credentials
4. **Rate limiting** middleware — currently config-only, not enforced
5. **SSRF protection** on object storage URLs
6. **WAF** rules for SQL injection / XSS pattern blocking
7. **Backup encryption** for PostgreSQL dumps
8. **VPN / private link** for database access in cloud deployment
