# GDPR Compliance — FoodSafe

## Data Controller

**FoodSafe** (Himanshu Raj)
Email: himanshu.raj@example.com
Address: [Your Business Address]

## Lawful Basis for Processing

- **Contract performance**: User account management, incident reporting
- **Legal obligation**: Food safety record retention (varies by jurisdiction)
- **Legitimate interest**: Audit logging, security monitoring

## Data Subject Rights

### Right to Access
Users can export all their data via:
```
GET /api/v1/users/me/export
```
Returns: JSON archive of all user data within the organization.

### Right to Rectification
Users can update their profile:
```
PUT /api/v1/users/me
Body: { "first_name", "last_name", "phone" }
```

### Right to Erasure ("Right to be Forgotten")
Users can request account deletion:
```
DELETE /api/v1/users/me
```
This triggers soft delete (deleted_at = now()) for audit trail compliance.

### Right to Data Portability
```
GET /api/v1/organizations/{org_id}/export
Returns: JSON + CSV exports
```

## Data Retention

| Data Type | Retention Period | Legal Basis |
|-----------|-----------------|-------------|
| Audit logs | 7 years | Food safety regulation |
| Incident records | 7 years | HACCP requirement |
| User data | Until account deletion | Consent / contract |
| Evidence files | 7 years | Legal hold |
| Sync records | 1 year | Operational |

## Data Protection Measures

- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Access control**: RBAC with permission checks
- **Audit logging**: All state changes logged
- **Breach notification**: Within 72 hours per GDPR Article 33

## Data Processing Agreement (DPA)

This document serves as the DPA between FoodSafe (processor) and the organization (controller).

### Processor Obligations
1. Implement technical/organizational measures per Article 32
2. Assist controller with data subject requests (Articles 15-22)
3. Notify controller of breaches within 24 hours
4. Delete data upon contract termination
5. Sub-processor transparency

### Controller Obligations
1. Provide lawful basis for processing
2. Ensure consent where required
3. Notify data subjects about processing

## Cross-Border Transfers

Data stored in [region] only. No transfers to third countries unless:
- Adequacy decision in place
- Standard Contractual Clauses executed
- Binding Corporate Rules approved

## Contact

Data Protection Officer: dpo@foodsafe.example.com
Breach Notification: security@foodsafe.example.com
Owner: Himanshu Raj
