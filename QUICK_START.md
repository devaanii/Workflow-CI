# 🚀 Quick Start Guide

## TL;DR - Fast Setup (5 Steps)

Untuk setup cepat repository ini dan menjalankan workflow CI/CD:

---

## Step 1: Clone & Push Repository

```bash
cd Workflow-CI-Devani
git init
git add .
git commit -m "Initial commit: MLflow CI/CD Wine Quality"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/Workflow-CI-Devani.git
git push -u origin main
```

⚠️ **Ganti `<YOUR_USERNAME>` dengan GitHub username Anda**

---

## Step 2: Setup Docker Hub Secrets

### Get Docker Hub Token:
1. Login: https://hub.docker.com
2. Profile > Account Settings > Security
3. New Access Token
4. Name: `github-actions`, Permission: `Read, Write, Delete`
5. **COPY TOKEN!**

### Add to GitHub:
1. GitHub repo > Settings > Secrets > Actions
2. Add secret:
   - Name: `DOCKERHUB_USERNAME`
   - Value: Docker Hub username
3. Add secret:
   - Name: `DOCKERHUB_TOKEN`
   - Value: Token yang di-copy

---

## Step 3: Setup Google Drive Secrets

### Option A: Quick (Using Existing Credentials)
Jika sudah punya Google Drive credentials:
1. GitHub repo > Settings > Secrets > Actions
2. Add secret:
   - Name: `GOOGLE_DRIVE_CREDENTIALS`
   - Value: JSON credentials
3. Add secret:
   - Name: `GOOGLE_DRIVE_FOLDER_ID`
   - Value: Folder ID

### Option B: Generate New (Detailed)
Lihat **SETUP_GUIDE.md** untuk step-by-step lengkap.

Quick version:
```bash
pip install google-auth-oauthlib
python generate_token.py
# Follow browser prompts
# Copy output JSON
```

---

## Step 4: Trigger Workflow

### Auto-trigger:
Push ke main branch akan otomatis trigger workflow

### Manual trigger:
1. GitHub repo > Actions tab
2. Select "MLflow Wine Quality Training CI/CD"
3. Run workflow > Run workflow

---

## Step 5: Verify Results

### Check Workflow:
```
GitHub > Actions > Latest run
✅ All steps should be green
```

### Check Google Drive:
```
1. Open Google Drive
2. Go to target folder
3. Verify mlruns/ exists
```

### Check Docker Hub:
```
1. Login to hub.docker.com
2. Find <USERNAME>/wine-quality-model
3. Verify 'latest' tag exists
```

### Test Docker Image:
```bash
docker pull <YOUR_USERNAME>/wine-quality-model:latest
docker run -p 5000:8080 <YOUR_USERNAME>/wine-quality-model:latest

# In another terminal:
curl -X POST http://localhost:5000/invocations \
  -H 'Content-Type: application/json' \
  -d '{
    "dataframe_split": {
      "columns": ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"],
      "data": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
    }
  }'
```

Expected: `{"predictions": [1]}`

---

## ✅ Done!

Repository Anda sekarang:
- ✅ Running automated CI/CD
- ✅ Training model with MLflow
- ✅ Storing artifacts in Google Drive (Skilled)
- ✅ Building & pushing Docker images (Advance)

**Kriteria 3 - Advance (4 points)**: ✅ **COMPLETE**

---

## 📚 Need More Details?

- **README.md** - Full documentation
- **SETUP_GUIDE.md** - Detailed step-by-step
- **SUBMISSION_CHECKLIST.md** - Grading criteria
- **STRUCTURE.md** - Repository structure
- **COMPLETION_SUMMARY.md** - Final summary

---

## 🐛 Quick Troubleshooting

### Workflow failed at "Upload to Google Drive"
→ Check `GOOGLE_DRIVE_CREDENTIALS` secret is valid JSON

### Workflow failed at "Build Docker Model"
→ Verify model was logged with `mlflow.sklearn.log_model()` in modelling.py

### Workflow failed at "Push Docker Image"
→ Check `DOCKERHUB_TOKEN` is valid and has write permission

### "Permission denied" errors
→ Verify all 4 secrets are set correctly in GitHub

---

## 💡 Pro Tips

1. **Test Locally First**:
   ```bash
   cd MLProject
   python modelling.py wine-quality-white_preprocessing.csv 100 42 0.2
   mlflow ui
   ```

2. **Check Secrets**:
   ```
   Settings > Secrets > Actions
   Should see 4 secrets:
   - DOCKERHUB_USERNAME
   - DOCKERHUB_TOKEN
   - GOOGLE_DRIVE_CREDENTIALS
   - GOOGLE_DRIVE_FOLDER_ID
   ```

3. **Monitor First Run**:
   - Watch logs carefully
   - Check each step completes
   - Verify outputs

4. **Screenshot Everything**:
   - Workflow success
   - Google Drive artifacts
   - Docker Hub image
   - Prediction test

---

## 🎯 Success Criteria

Repository ini memenuhi **Advance (4 points)**:

| Kriteria | Status |
|----------|--------|
| Folder MLProject | ✅ |
| Workflow CI | ✅ |
| Training model | ✅ |
| Upload to Google Drive | ✅ |
| Build Docker with MLflow | ✅ |
| Push to Docker Hub | ✅ |

---

**Happy Submitting! 🎉**

For detailed guides, check other documentation files in this repository.
