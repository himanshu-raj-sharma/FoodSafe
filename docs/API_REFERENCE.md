# FoodSafe API Reference

Base URL: `https://<your-domain>/api/v1`

## Authentication

### Register
```
POST /auth/register
Body: { "email", "username", "password", "first_name", "last_name", "organization_id" }
Returns: { "message": "User registered successfully" }
```

### Login
```
POST /auth/login
Body: { "email", "password" }
Returns: { "access_token", "refresh_token", "token_type", "user", "expires_in" }
```

## Organizations

### Create Organization
```
POST /organizations/
Body: { "name", "slug", "description", "tier" }
Returns: OrganizationRead
```

## Outlets

### Create Outlet
```
POST /outlets/{org_id}
Body: { "name", "code", "address", "latitude", "longitude" }
Returns: OutletRead
```

## Incidents

### Create Incident
```
POST /incidents/
Body: { "title", "description", "type", "severity", "outlet_id", "evidence_urls" }
Returns: IncidentRead
```

## CAPA

### Create CAPA
```
POST /capa/
Body: { "incident_id", "title", "description", "assignee_id", "due_date" }
Returns: CAPARead
```

## Suppliers

### Create Supplier
```
POST /suppliers/
Body: { "name", "category", "risk_score", "outlet_id" }
Returns: SupplierRead
```

## Batches

### Create Batch
```
POST /batches/
Body: { "supplier_id", "product_name", "production_date", "expiry_date" }
Returns: BatchRead
```

## Analytics

### Organization Risk Score
```
GET /analytics/risk/{org_id}
Returns: { "risk_score", "critical_incidents", "overdue_capas", "temperature_deviations" }
```

## Sync

### Upload Offline Operations
```
POST /sync/upload
Body: { "operations": [{ "type", "entity_type", "entity_id", "data" }] }
Returns: { "synced": [...], "conflicts": [...] }
```
