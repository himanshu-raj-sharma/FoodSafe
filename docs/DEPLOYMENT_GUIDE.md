# FoodSafe Deployment Guide

## Free Cloud Platforms

| Platform | Backend | Database | Storage | Monthly Cost |
|----------|---------|----------|---------|--------------|
| **Render.com** | ✅ | ✅ (PostgreSQL) | ✅ (S3-compatible) | Free tier available |
| **Railway.app** | ✅ | ✅ (PostgreSQL) | ✅ | $5 free credit/month |
| **Fly.io** | ✅ | ✅ (PostgreSQL) | ❌ | Free tier available |
| **Oracle Cloud** | ✅ | ✅ (Autonomous DB) | ✅ | Always free tier |
| **Vercel** | ✅ | ❌ | ❌ | Free tier available |

## Recommended: Render.com (Free Tier)

### Step 1: Create Account
1. Go to https://render.com
2. Sign up with GitHub
3. Verify email

### Step 2: Deploy PostgreSQL
1. Dashboard → New → PostgreSQL
2. Name: `foodsafe-db`
3. Plan: Free (90-day limit, then $7/mo)
4. Click "Create Database"
5. Copy `Internal Database URL`

### Step 3: Deploy Backend
1. Dashboard → New → Web Service
2. Connect GitHub repo: `FoodSafe`
3. Build command: `cd backend && pip install -r requirements.txt`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
5. Environment variables:
   ```
   DATABASE_URL=<from step 2>
   JWT_SECRET=<generate with: openssl rand -hex 32>
   ENVIRONMENT=production
   ```
6. Click "Create Web Service"

### Step 4: Run Migrations
```bash
# SSH into Render instance or use build hook
alembic upgrade head
```

### Step 5: Verify Deployment
```bash
curl https://foodsafe-backend.onrender.com/health
curl https://foodsafe-backend.onrender.com/docs  # Swagger UI
```

## Alternative: Railway.app

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway init
railway up
```

## Oracle Cloud Free Tier (Permanent Free)
- Always-free Autonomous PostgreSQL database
- 20GB storage, 1 OCPU
- No expiration

### Setup
```bash
# Install OCI CLI
pip install oci-cli

# Configure
oci setup config

# Create database
oci db autonomous-database create --compartment-id <id> --display-name FoodSafeDB --db-workload DW
```

## Environment Variables (Production)

```env
DATABASE_URL=postgresql+psycopg2://user:password@host:5432/foodsafe
JWT_SECRET=<32-char-random-string>
BCRYPT_ROUNDS=12
RATE_LIMIT_REQUESTS_PER_MINUTE=100
CORS_ORIGINS=https://your-frontend-domain.com
ENVIRONMENT=production
LOG_LEVEL=WARNING
OBJECT_STORAGE_ENDPOINT=https://your-minio-endpoint
OBJECT_STORAGE_BUCKET=foodsafe-evidence
OBJECT_STORAGE_ACCESS_KEY=<key>
OBJECT_STORAGE_SECRET_KEY=<secret>
ENCRYPTION_KEY=<32-byte-key>
```

## Backup Strategy

### PostgreSQL Backups
- Render: Automatic daily backups (paid tier)
- Railway: Automatic weekly backups
- Manual: `pg_dump` cron job

### Evidence Files
- MinIO: Enable versioning + lifecycle rules
- S3: Cross-region replication

## SSL/TLS
- Render: Auto-HTTPS on custom domain
- Railway: Auto-HTTPS
- Oracle: Configure in load balancer

## Monitoring
- Render: Built-in logs + metrics
- Railway: Built-in metrics
- Oracle: Cloud Monitoring dashboard
