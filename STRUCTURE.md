# Struktur Repository - Workflow CI

## 📂 Tree Structure

```
Workflow-CI-Devani/
│
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 ci.yml                           ← GitHub Actions workflow (CRITICAL)
│
├── 📁 MLProject/                               ← MLflow Project folder (REQUIRED)
│   ├── 📄 MLProject                            ← MLflow config tanpa ekstensi (CRITICAL)
│   ├── 📄 conda.yaml                           ← Environment dependencies (REQUIRED)
│   ├── 📄 modelling.py                         ← Training script (REQUIRED)
│   ├── 📄 wine-quality-white_preprocessing.csv ← Dataset (REQUIRED)
│   └── 📄 docker_hub_link.txt                  ← Docker Hub info (GENERATED)
│
├── 📄 README.md                                ← Dokumentasi utama
├── 📄 SETUP_GUIDE.md                           ← Panduan setup step-by-step
├── 📄 SUBMISSION_CHECKLIST.md                  ← Checklist penilaian
├── 📄 STRUCTURE.md                             ← Dokumentasi ini
├── 📄 requirements.txt                         ← Python dependencies
├── 📄 .gitignore                               ← Git ignore rules
└── 📄 generate_token.py                        ← Script generate Google Drive token
```

---

## 🔍 Penjelasan File

### 🚨 CRITICAL FILES (Wajib Ada)

#### 1. `.github/workflows/ci.yml`
**Fungsi**: Workflow CI/CD untuk otomasi training dan deployment

**Isi Penting**:
- Trigger: `push` ke `main` atau `workflow_dispatch`
- Steps untuk training model
- Steps untuk upload ke Google Drive (Skilled)
- Steps untuk build & push Docker image (Advance)

**Contoh**:
```yaml
name: MLflow Wine Quality Training CI/CD
on:
  push:
    branches: [main]
  workflow_dispatch:
```

---

#### 2. `MLProject/MLProject` (tanpa ekstensi!)
**Fungsi**: Konfigurasi MLflow Project

**Format**:
```yaml
name: wine-quality-training
conda_env: conda.yaml
entry_points:
  main:
    parameters:
      data_path: {type: string, default: "wine-quality-white_preprocessing.csv"}
      n_estimators: {type: int, default: 100}
      random_state: {type: int, default: 42}
      test_size: {type: float, default: 0.2}
    command: "python modelling.py {data_path} {n_estimators} {random_state} {test_size}"
```

**⚠️ Penting**: File ini **TIDAK** ada ekstensi (.yaml, .yml, .txt)

---

#### 3. `MLProject/conda.yaml`
**Fungsi**: Definisi environment dependencies

**Isi**:
```yaml
name: mlflow-wine-quality-env
channels:
  - conda-forge
dependencies:
  - python=3.9
  - pip
  - pip:
    - mlflow==2.13.0
    - scikit-learn==1.5.1
    - pandas==2.2.3
    - numpy==2.0.0
```

---

#### 4. `MLProject/modelling.py`
**Fungsi**: Script untuk training model

**Requirements**:
- Accept command line arguments
- MLflow tracking
- **CRITICAL**: Explicit model logging dengan `mlflow.sklearn.log_model()`

**Contoh kode penting**:
```python
# CRITICAL untuk Docker build!
mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="model",
    registered_model_name="wine-quality-classifier"
)
```

---

#### 5. `MLProject/wine-quality-white_preprocessing.csv`
**Fungsi**: Dataset yang sudah di-preprocessing

**Format**:
- CSV dengan header
- Kolom target: `quality` (binary: 0 atau 1)
- Fitur: 11 kolom numerik

---

### 📚 DOCUMENTATION FILES

#### 6. `README.md`
**Fungsi**: Dokumentasi utama repository

**Isi**:
- Deskripsi project
- Struktur folder
- Cara setup
- Cara menggunakan
- Kriteria penilaian

---

#### 7. `SETUP_GUIDE.md`
**Fungsi**: Panduan step-by-step untuk setup

**Isi**:
- Setup GitHub repository
- Setup Docker Hub
- Setup Google Drive API
- Setup GitHub Secrets
- Push ke GitHub
- Verifikasi hasil

---

#### 8. `SUBMISSION_CHECKLIST.md`
**Fungsi**: Checklist untuk memastikan semua kriteria terpenuhi

**Isi**:
- Checklist struktur
- Checklist Basic (2 pts)
- Checklist Skilled (3 pts)
- Checklist Advance (4 pts)

---

### 🛠️ UTILITY FILES

#### 9. `requirements.txt`
**Fungsi**: Python dependencies untuk local development

**Isi**:
```
mlflow==2.13.0
scikit-learn==1.5.1
pandas==2.2.3
numpy==2.0.0
matplotlib==3.9.0
cloudpickle==3.1.0
docker<7.0.0
google-auth
google-auth-oauthlib
google-api-python-client
```

---

#### 10. `.gitignore`
**Fungsi**: Ignore files yang tidak perlu di-commit

**Isi penting**:
```
__pycache__/
mlruns/
mlartifacts/
credentials.json
*.key
.env
```

---

#### 11. `generate_token.py`
**Fungsi**: Script helper untuk generate Google Drive OAuth token

**Usage**:
```bash
pip install google-auth-oauthlib
python generate_token.py
```

---

### 🤖 GENERATED FILES (Auto-generated)

#### 12. `MLProject/docker_hub_link.txt`
**Fungsi**: Informasi Docker Hub image (di-generate oleh CI/CD)

**Isi**: URL Docker Hub, cara pull, cara run, dll.

---

## 🎯 Kriteria dan File Mapping

### Basic (2 pts)
```
✅ MLProject/
   ├── MLProject          ← MLflow config
   ├── conda.yaml         ← Dependencies
   ├── modelling.py       ← Training script
   └── dataset.csv        ← Data

✅ .github/workflows/ci.yml  ← Workflow CI
```

### Skilled (3 pts)
```
✅ Semua file Basic

✅ .github/workflows/ci.yml
   └── Step: Upload to Google Drive
```

### Advance (4 pts)
```
✅ Semua file Skilled

✅ .github/workflows/ci.yml
   ├── Step: Build Docker Model         ← mlflow models build-docker
   ├── Step: Log in to Docker Hub       ← docker login
   ├── Step: Tag Docker Image           ← docker tag
   └── Step: Push Docker Image          ← docker push
```

---

## 🔐 GitHub Secrets Required

Untuk menjalankan workflow, setup secrets:

### Docker Hub (Advance)
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

### Google Drive (Skilled)
- `GOOGLE_DRIVE_CREDENTIALS`
- `GOOGLE_DRIVE_FOLDER_ID`

---

## 📊 File Size Reference

| File | Size | Type |
|------|------|------|
| ci.yml | ~3-5 KB | YAML |
| MLProject | ~300 B | Text |
| conda.yaml | ~200 B | YAML |
| modelling.py | ~2-3 KB | Python |
| dataset.csv | ~200-500 KB | CSV |
| README.md | ~10-15 KB | Markdown |

---

## ✅ Pre-commit Checklist

Sebelum commit, pastikan:

- [ ] File `MLProject` **TIDAK** ada ekstensi
- [ ] File `conda.yaml` format valid
- [ ] File `modelling.py` ada `log_model()`
- [ ] Dataset CSV ada di `MLProject/`
- [ ] Workflow `ci.yml` lengkap dengan Docker steps
- [ ] README.md lengkap dan informatif
- [ ] `.gitignore` exclude credentials

---

## 🚫 Files to NEVER Commit

❌ **JANGAN COMMIT**:
- `client_secret.json` (Google OAuth)
- `google_drive_credentials.json` (Generated token)
- `credentials.json` (Any credentials)
- `.env` files
- `*.key` files
- Personal tokens

✅ **Gunakan**: GitHub Secrets untuk credentials!

---

## 📈 Workflow Execution Flow

```
Push to main
    ↓
GitHub Actions Triggered
    ↓
Setup Environment (Python 3.12.7)
    ↓
Install Dependencies (MLflow, scikit-learn, etc.)
    ↓
Run Training (modelling.py)
    ↓
Get Run ID
    ↓
Upload to Google Drive ← Skilled
    ↓
Build Docker Image ← Advance
    ↓
Login to Docker Hub ← Advance
    ↓
Tag Image ← Advance
    ↓
Push to Docker Hub ← Advance
    ↓
Complete ✅
```

---

## 🎉 Hasil Akhir

Setelah workflow selesai:

1. ✅ Model trained dan tracked di MLflow
2. ✅ Artifacts tersimpan di Google Drive
3. ✅ Docker image di Docker Hub: `<USERNAME>/wine-quality-model:latest`
4. ✅ Model dapat di-pull dan di-run untuk serving

---

**Repository ini siap untuk submission dengan kriteria Advance (4 points)!** 🚀
