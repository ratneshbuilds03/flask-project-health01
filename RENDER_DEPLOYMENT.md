# Render Deployment Guide

## Problem

Render pe MySQL connection nahi hai kyunki localhost MySQL available nahi hai.

## Solution: Use External Database (Railway Recommended)

### Step 1: Create Database on Railway.app

1. Go to [railway.app](https://railway.app)
2. Sign up/Login
3. Click "New Project"
4. Select "MySQL"
5. Wait for deployment (2-3 mins)
6. Go to "MySQL" tab
7. Copy the `DATABASE_URL` from connect section

Example URL format:

```
mysql://user123:pass456@containers.railway.app:12345/railway
```

### Step 2: Add Database URL to Render

1. Go to Render.com
2. Go to your web service
3. Click "Environment"
4. Add new variable:
   - **Key:** `DATABASE_URL`
   - **Value:** (paste Railway URL from step 1)

5. Add another variable:
   - **Key:** `JWT_SECRET_KEY`
   - **Value:** (any random secure string)

### Step 3: Update Requirements (if needed)

Make sure you have PyMySQL in `requirements.txt`:

```
PyMySQL==1.2.0
```

### Step 4: Redeploy

Click "Manual Deploy" or "Retry Deploy" in Render.

---

## Alternative: AWS RDS Free Tier

1. Go to [AWS RDS](https://aws.amazon.com/rds/)
2. Create MySQL database (free tier eligible)
3. Get endpoint (looks like: `mydb.xxxxx.us-east-1.rds.amazonaws.com`)
4. Create DATABASE_URL:
   ```
   mysql+pymysql://admin:yourpassword@mydb.xxxxx.us-east-1.rds.amazonaws.com:3306/taskdb
   ```
5. Add to Render environment variables

---

## How Config Works

```python
# Priority order:
1. DATABASE_URL (from Render env var) ← Use this for production
2. Docker host detection
3. Fallback to localhost (for local development)
```

---

## Test Connection

After deploying, check logs:

```
If you see: "Connected successfully" → ✅ Good
If you see: "Can't connect to MySQL" → ❌ Fix DATABASE_URL
```

---

## Common Issues

### ❌ "Can't connect to MySQL server on '12082003@localhost'"

**Fix:** Add `DATABASE_URL` environment variable

### ❌ "Connection refused"

**Fix:** Check MySQL host is correct, firewall rules allow connections

### ❌ "Access denied for user"

**Fix:** Check username/password in DATABASE_URL

### ❌ "Unknown database"

**Fix:** Database name in URL must exist

---

## Quick Deploy Checklist

- [ ] Create Railway/RDS MySQL database
- [ ] Copy DATABASE_URL
- [ ] Add DATABASE_URL to Render environment
- [ ] Add JWT_SECRET_KEY to Render environment
- [ ] Redeploy on Render
- [ ] Check deployment logs
- [ ] Test API endpoints

---

## Database Connection String Formats

### Railway MySQL

```
mysql://user:pass@containers.railway.app:port/dbname
```

### AWS RDS

```
mysql+pymysql://admin:password@db.region.rds.amazonaws.com:3306/taskdb
```

### Render MySQL

```
mysql+pymysql://user:pass@rds.render.com:3306/dbname
```

---

## After Getting Database Working

1. Test login: `/api/login`
2. Create task: `POST /api/tasks`
3. Get tasks: `GET /api/tasks`

If all working → ✅ Success!

For more help: Check Render logs → `Logs` tab in dashboard
