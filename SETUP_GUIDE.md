# Setup Guide - Workflow CI untuk Kriteria 3

Panduan lengkap untuk setup dan deploy Workflow CI dengan kriteria **Advance (4 points)**.

## 🎯 Tujuan

Setup workflow CI/CD yang otomatis melakukan:
1. ✅ Training model dengan MLflow Project
2. ✅ Upload artifacts ke Google Drive
3. ✅ Build Docker image dengan MLflow
4. ✅ Push Docker image ke Docker Hub

---

## 📝 Checklist Persiapan

Sebelum mulai, pastikan Anda memiliki:

- [ ] Akun GitHub (untuk repository)
- [ ] Akun Docker Hub (untuk push image)
- [ ] Akun Google Cloud (untuk Google Drive API)
- [ ] Git terinstall di komputer
- [ ] Python 3.9+ terinstall

---

## 🚀 Step-by-Step Setup

### Step 1: Buat Repository GitHub

1. Login ke [GitHub](https://github.com)
2. Klik tombol **New repository**
3. Isi detail:
   - Repository name: `Workflow-CI-Devani`
   - Description: `MLflow CI/CD for Wine Quality Classification`
   - Visibility: **Public** ⚠️ (penting untuk reviewer)
   - ✅ Add README file (atau uncheck jika mau push existing)
4. Klik **Create repository**

### Step 2: Setup Docker Hub

#### 2.1 Buat Akun Docker Hub

1. Pergi ke [Docker Hub](https://hub.docker.com)
2. Sign up atau login
3. Catat username Anda (misal: `devaniuser`)

#### 2.2 Buat Access Token

1. Klik profile icon > **Account Settings**
2. Pilih **Security**
3. Klik **New Access Token**
4. Isi:
   - Access Token Description: `github-actions-wine-quality`
   - Access permissions: **Read, Write, Delete**
5. Klik **Generate**
6. **⚠️ COPY TOKEN SEKARANG** (tidak akan ditampilkan lagi!)
7. Simpan di notepad sementara

### Step 3: Setup Google Drive API

#### 3.1 Buat Project di Google Cloud Console

1. Pergi ke [Google Cloud Console](https://console.cloud.google.com/)
2. Klik **Select a project** > **New Project**
3. Isi project name: `mlflow-wine-quality`
4. Klik **Create**

#### 3.2 Enable Google Drive API

1. Di dashboard, klik **APIs & Services** > **Library**
2. Search: `Google Drive API`
3. Klik **Google Drive API**
4. Klik **Enable**

#### 3.3 Create OAuth 2.0 Credentials

1. Klik **APIs & Services** > **Credentials**
2. Klik **Create Credentials** > **OAuth client ID**
3. Jika diminta, configure consent screen:
   - User Type: **External**
   - App name: `MLflow Wine Quality`
   - User support email: email Anda
   - Developer contact: email Anda
   - Save and continue
   - Scopes: skip (default)
   - Test users: tambah email Anda
   - Save and continue
4. Kembali ke Create OAuth client ID:
   - Application type: **Desktop app**
   - Name: `mlflow-desktop-client`
   - Create
5. Download JSON credentials
6. Simpan sebagai `client_secret.json`

#### 3.4 Generate Refresh Token

Buat script Python untuk generate token:

```python
# generate_token.py
from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)
    
    # Save credentials
    creds_data = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }
    
    print("="*50)
    print("Copy JSON berikut ke GitHub Secret:")
    print("="*50)
    print(json.dumps(creds_data, indent=2))
    print("="*50)

if __name__ == '__main__':
    main()
```

Run script:
```bash
pip install google-auth-oauthlib
python generate_token.py
```

Browser akan terbuka, login dengan akun Google Anda dan authorize.
Copy output JSON yang muncul di terminal.

#### 3.5 Dapatkan Folder ID

1. Buka [Google Drive](https://drive.google.com)
2. Buat folder baru: `MLflow-Wine-Quality-Artifacts`
3. Buka folder tersebut
4. Lihat URL di browser:
   ```
   https://drive.google.com/drive/folders/1ABCdefGHI123456789
   ```
   ID folder adalah: `1ABCdefGHI123456789`
5. Copy ID tersebut

### Step 4: Setup GitHub Secrets

1. Pergi ke repository GitHub Anda
2. Klik **Settings** > **Secrets and variables** > **Actions**
3. Klik **New repository secret**

#### Secret 1: DOCKERHUB_USERNAME
- Name: `DOCKERHUB_USERNAME`
- Secret: username Docker Hub Anda (misal: `devaniuser`)
- Klik **Add secret**

#### Secret 2: DOCKERHUB_TOKEN
- Name: `DOCKERHUB_TOKEN`
- Secret: token yang di-copy dari Docker Hub (Step 2.2)
- Klik **Add secret**

#### Secret 3: GOOGLE_DRIVE_CREDENTIALS
- Name: `GOOGLE_DRIVE_CREDENTIALS`
- Secret: JSON credentials dari Step 3.4
- Klik **Add secret**

#### Secret 4: GOOGLE_DRIVE_FOLDER_ID
- Name: `GOOGLE_DRIVE_FOLDER_ID`
- Secret: Folder ID dari Step 3.5 (misal: `1ABCdefGHI123456789`)
- Klik **Add secret**

### Step 5: Push Code ke GitHub

```bash
# Di folder Workflow-CI-Devani
git init
git add .
git commit -m "Initial commit: MLflow CI/CD Wine Quality with Advanced features"
git branch -M main
git remote add origin https://github.com/<USERNAME>/Workflow-CI-Devani.git
git push -u origin main
```

Replace `<USERNAME>` dengan username GitHub Anda.

### Step 6: Trigger Workflow

Workflow akan otomatis berjalan setelah push. Atau trigger manual:

1. Pergi ke tab **Actions** di repository
2. Klik workflow **MLflow Wine Quality Training CI/CD**
3. Klik **Run workflow** > **Run workflow**

### Step 7: Monitor Execution

1. Klik workflow run yang sedang berjalan
2. Amati setiap step:
   - ✅ Checkout repository
   - ✅ Set up Python
   - ✅ Install dependencies
   - ✅ Run mlflow project
   - ✅ Get latest run_id
   - ✅ Upload to Google Drive
   - ✅ Build Docker Model
   - ✅ Log in to Docker Hub
   - ✅ Tag Docker Image
   - ✅ Push Docker Image
   - ✅ Complete job

### Step 8: Verifikasi Hasil

#### Verifikasi Google Drive
1. Buka folder Google Drive yang dibuat
2. Pastikan ada folder `mlruns` dengan artifacts

#### Verifikasi Docker Hub
1. Login ke Docker Hub
2. Pergi ke Repositories
3. Cari repository: `<USERNAME>/wine-quality-model`
4. Verifikasi ada image dengan tag `latest`

#### Test Docker Image
```bash
# Pull image
docker pull <USERNAME>/wine-quality-model:latest

# Run container
docker run -p 5000:8080 <USERNAME>/wine-quality-model:latest

# Di terminal lain, test prediction
curl -X POST http://localhost:5000/invocations \
  -H 'Content-Type: application/json' \
  -d '{
    "dataframe_split": {
      "columns": [
        "fixed_acidity", "volatile_acidity", "citric_acid", 
        "residual_sugar", "chlorides", "free_sulfur_dioxide",
        "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"
      ],
      "data": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
    }
  }'
```

Expected output:
```json
{
  "predictions": [1]
}
```

---

## 🎉 Kriteria Terpenuhi

Jika semua step berhasil, Anda telah memenuhi:

- ✅ **Basic (2 pts)**: Folder MLProject + workflow CI yang melatih model
- ✅ **Skilled (3 pts)**: Basic + menyimpan artifacts ke Google Drive
- ✅ **Advance (4 pts)**: Skilled + Docker image ke Docker Hub dengan `mlflow models build-docker`

---

## 🐛 Troubleshooting

### Error: "Authentication failed" di Google Drive

**Solusi**:
1. Regenerate credentials dengan `generate_token.py`
2. Pastikan scope includes `drive.file`
3. Update GitHub Secret dengan credentials baru

### Error: "Docker build failed"

**Solusi**:
1. Pastikan model di-log dengan:
   ```python
   mlflow.sklearn.log_model(model, artifact_path="model")
   ```
2. Verifikasi run_id valid di step sebelumnya
3. Check log detail di GitHub Actions

### Error: "Permission denied" di Docker Hub

**Solusi**:
1. Verifikasi token masih valid
2. Regenerate token di Docker Hub
3. Update GitHub Secret `DOCKERHUB_TOKEN`

### Workflow tidak trigger otomatis

**Solusi**:
1. Pastikan file workflow ada di `.github/workflows/ci.yml`
2. Pastikan push ke branch `main` (bukan `master`)
3. Trigger manual via Actions tab

---

## 📚 Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [Google Drive API Python Quickstart](https://developers.google.com/drive/api/quickstart/python)

---

## ✅ Submission Checklist

Sebelum submit, pastikan:

- [ ] Repository GitHub public dan accessible
- [ ] README.md lengkap dengan dokumentasi
- [ ] Folder MLProject dengan file:
  - [ ] `MLProject` (tanpa ekstensi)
  - [ ] `conda.yaml`
  - [ ] `modelling.py`
  - [ ] `wine-quality-white_preprocessing.csv`
- [ ] File `.github/workflows/ci.yml`
- [ ] Workflow berhasil berjalan (hijau ✅)
- [ ] Artifacts tersimpan di Google Drive
- [ ] Docker image tersimpan di Docker Hub
- [ ] File `docker_hub_link.txt` atau tautan di README
- [ ] GitHub Secrets sudah di-setup
- [ ] Screenshots hasil workflow (opsional tapi recommended)

---

**Good luck with your submission! 🚀**
