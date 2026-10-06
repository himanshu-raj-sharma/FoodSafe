# FoodSafe Architecture Decision Records (ADR)

## ADR-001: Offline-First Architecture

**Status:** Accepted

**Context:** Food operations must work regardless of connectivity conditions in commercial kitchens.

**Decision:** Room database as local source of truth with WorkManager-based sync.

**Consequences:** 
- Positive: Uninterrupted operations, data security in isolated environments.
- Negative: Increased complexity in conflict resolution, sync logic.

## ADR-002: Multi-Tenant Database Design

**Status:** Accepted

**Context:** Organizations must never access each other's data.

**Decision:** Each organization table includes organization_id with foreign keys and database-level checks.

**Consequences:**
- Positive: Strong isolation, scalable organization support.
- Negative: All queries must include organization filters.

## ADR-003: Evidence Storage

**Status:** Accepted

**Context:** Photos and documents must be stored securely.

**Decision:** PostgreSQL for metadata, object storage for files with signed URLs.

**Consequences:**
- Positive: Scalable storage, secure access control.
- Negative: Additional infrastructure dependency (object storage).

## ADR-004: AI Safety

**Status:** Accepted

**Context:** AI must assist but never independently decide regulatory compliance.

**Decision:** Human-verification gateway for all AI-generated actions with structured output logging.

**Consequences:**
- Positive: Regulatory protection, user accountability.
- Negative: Additional UI complexity for approval flows.

## ADR-005: Technology Stack Selection

**Status:** Accepted

**Context:** Production-grade SaaS for food businesses.

**Decision:** Kotlin/Android (UI) + Python/FastAPI (Backend) + PostgreSQL.

**Consequences:**
- Positive: Industry-standard, well-supported, maintainable.
- Negative: Two language runtimes to maintain.