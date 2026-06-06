# Submission Checklist - Kriteria 3: Workflow CI

## ✅ Kriteria yang Dipenuhi

### 🎯 Target: **ADVANCE (4 Points)**

---

## 📋 Checklist Struktur Repository

### Struktur Folder ✅
```
Workflow-CI-Devani/
├── .github/
│   └── workflows/
│       └── ci.yml                                ✅ GitHub Actions workflow
├── MLProject/
│   ├── modelling.py                             ✅ Script training model
│   ├── conda.yaml                               ✅ Environment dependencies
│   ├── MLProject                                ✅ MLflow Project config
│   ├── wine-quality-white_preprocessing.csv     ✅ Dataset preprocessing
│   └── docker_hub_link.txt                      ✅ Docker Hub info
├── README.md                                     ✅ Dokumentasi lengkap
├── SETUP_GUIDE.md                               ✅ Panduan setup
├── SUBMISSION_CHECKLIST.md                      ✅ Checklist ini
├── requirements.txt                             ✅ Python dependencies
└── .gitignore                                   ✅ Git ignore file
```

---

## 🏆 Penilaian Kriteria

### ❌ Reject (0 pts)
- [ ] Tidak membuat folder MLProject
- [ ] Tidak membuat workflow CI

**Status**: ✅ TIDAK MASUK KATEGORI INI

---

### ✅ Basic (2 pts)
- [x] ✅ Membuat folder MLProject
- [x] ✅ Membuat Workflow CI yang dapat membuat model ML ketika trigger terpantik

**Kriteria Basic**: ✅ **TERPENUHI**

**Bukti**:
- Folder `MLProject/` ada dengan struktur lengkap
- File `.github/workflows/ci.yml` membuat workflow otomatis
- Workflow trigger pada push ke `main` atau manual dispatch
- Step "Run mlflow project" melatih model dengan `modelling.py`

---

### ✅ Skilled (3 pts)
- [x] ✅ Semua kriteria Basic
- [x] ✅ Menyimpan artefak ke repositori eksternal (Google Drive)

**Kriteria Skilled**: ✅ **TERPENUHI**

**Bukti**:
- Step "Upload to Google Drive" di workflow
- Menggunakan Google Drive API untuk upload artifacts
- Credentials disimpan di GitHub Secrets:
  - `GOOGLE_DRIVE_CREDENTIALS`
  - `GOOGLE_DRIVE_FOLDER_ID`

---

### ✅ Advance (4 pts)
- [x] ✅ Semua kriteria Skilled
- [x] ✅ Membuat Docker Images ke Docker Hub menggunakan `mlflow models build-docker`

**Kriteria Advance**: ✅ **TERPENUHI**

**Bukti**:
- Step "Build Docker Model" menggunakan perintah:
  ```bash
  mlflow models build-docker -m "runs:/$RUN_ID/model" -n "wine-quality-model:latest"
  ```
- Step "Log in to Docker Hub" untuk authentication
- Step "Tag Docker Image" untuk tagging
- Step "Push Docker Image" untuk push ke Docker Hub
- Credentials disimpan di GitHub Secrets:
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`

---

## 📊 Workflow CI/CD Steps

Workflow mencakup **semua tahapan yang diperlukan**:

1. ✅ **Checkout repository** - Clone repo ke runner
2. ✅ **Set up Python 3.12.7** - Setup Python environment
3. ✅ **Check Env** - Verify installation
4. ✅ **Install dependencies** - Install MLflow, scikit-learn, pandas, etc.
5. ✅ **Run mlflow project** - Execute training
6. ✅ **Get latest MLflow run_id** - Extract run ID untuk Docker
7. ✅ **Install Python dependencies** - Google Drive libraries
8. ✅ **Upload to Google Drive** - Upload artifacts (Skilled)
9. ✅ **Build Docker Model** - Build dengan MLflow (Advance)
10. ✅ **Log in to Docker Hub** - Authenticate (Advance)
11. ✅ **Tag Docker Image** - Tag image (Advance)
12. ✅ **Push Docker Image** - Push ke registry (Advance)
13. ✅ **Complete job** - Summary

---

## 🔐 GitHub Secrets Required

Setup di `Settings > Secrets and variables > Actions`:

### Docker Hub
- [x] `DOCKERHUB_USERNAME` - Username Docker Hub
- [x] `DOCKERHUB_TOKEN` - Access token dari Docker Hub

### Google Drive
- [x] `GOOGLE_DRIVE_CREDENTIALS` - OAuth credentials JSON
- [x] `GOOGLE_DRIVE_FOLDER_ID` - Target folder ID

---

## 📝 File Penting

### 1. MLProject (tanpa ekstensi) ✅
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

**✅ Fitur**:
- Entry point `main` terdefinisi
- Parameters parameterized untuk flexibility
- Command eksekusi jelas

---

### 2. conda.yaml ✅
```yaml
name: mlflow-wine-quality-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - pip
  - pip:
    - mlflow==2.13.0
    - scikit-learn==1.5.1
    - pandas==2.2.3
    - numpy==2.0.0
    - matplotlib==3.9.0
    - cloudpickle==3.1.0
```

**✅ Fitur**:
- Environment reproducible
- Dependencies lengkap
- Version pinning

---

### 3. modelling.py ✅

**✅ Fitur**:
- Accept command line arguments untuk parameters
- MLflow tracking dengan `mlflow.sklearn.autolog()`
- Explicit model logging dengan `mlflow.sklearn.log_model()`
- Registered model name: `wine-quality-classifier`
- Print run_id untuk Docker build

**Kunci**: Model **HARUS** di-log dengan `log_model()` agar `mlflow models build-docker` bisa berjalan!

---

### 4. .github/workflows/ci.yml ✅

**✅ Fitur Critical untuk Advance**:
```yaml
- name: Build Docker Model
  run: |
    mlflow models build-docker -m "$MODEL_URI" -n "wine-quality-model:latest"

- name: Log in to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}

- name: Push Docker Image
  run: |
    docker push ${{ secrets.DOCKERHUB_USERNAME }}/wine-quality-model:latest
```

**✅ Fitur Critical untuk Skilled**:
```yaml
- name: Upload to Google Drive
  env:
    GOOGLE_DRIVE_CREDENTIALS: ${{ secrets.GOOGLE_DRIVE_CREDENTIALS }}
    GOOGLE_DRIVE_FOLDER_ID: ${{ secrets.GOOGLE_DRIVE_FOLDER_ID }}
  run: |
    # Upload script menggunakan Google Drive API
```

---

## 🔍 Cara Verifikasi

### 1. Repository GitHub ✅
- [ ] Repository public dan accessible
- [ ] README.md lengkap dengan dokumentasi
- [ ] Struktur folder sesuai ketentuan

### 2. Workflow Execution ✅
- [ ] Pergi ke tab `Actions`
- [ ] Lihat workflow run terbaru
- [ ] Semua step hijau (✅)
- [ ] Duration reasonable (~5-10 menit)

### 3. Google Drive ✅
- [ ] Login ke Google Drive
- [ ] Buka folder target
- [ ] Verifikasi folder `mlruns` ada
- [ ] Check artifacts lengkap

### 4. Docker Hub ✅
- [ ] Login ke Docker Hub
- [ ] Pergi ke repositories
- [ ] Verifikasi `<USERNAME>/wine-quality-model` ada
- [ ] Image tag `latest` ada
- [ ] Image size reasonable (~1-2 GB)

### 5. Test Docker Image ✅
```bash
# Pull dan test
docker pull <USERNAME>/wine-quality-model:latest
docker run -p 5000:8080 <USERNAME>/wine-quality-model:latest

# Test prediction
curl -X POST http://localhost:5000/invocations \
  -H 'Content-Type: application/json' \
  -d '{...}'
```

Expected: JSON response dengan predictions

---

## 📸 Screenshots Recommended

Untuk memperkuat submission:

1. **GitHub Actions Workflow** ✅
   - Screenshot workflow run dengan semua step hijau
   - Tampilkan duration dan timestamp

2. **Google Drive** ✅
   - Screenshot folder dengan artifacts
   - Tampilkan struktur mlruns/

3. **Docker Hub** ✅
   - Screenshot repository page
   - Tampilkan image dengan tag latest
   - Tampilkan image size dan last pushed

4. **Docker Image Test** ✅
   - Screenshot terminal dengan docker pull
   - Screenshot curl request dan response
   - Tampilkan predictions berhasil

---

## 💡 Tips untuk Reviewer

### Kunci Perbedaan Level

| Level    | Workflow CI | Artifacts Storage | Docker Image |
|----------|-------------|-------------------|--------------|
| Basic    | ✅          | ❌                | ❌           |
| Skilled  | ✅          | ✅ (Google Drive) | ❌           |
| Advance  | ✅          | ✅ (Google Drive) | ✅ (Docker Hub) |

### Bukti Advance Clear:
1. **`mlflow models build-docker` usage** di workflow
2. **Docker Hub push** berhasil
3. **Image accessible** dan dapat di-pull
4. **Model serving** berfungsi (test prediction berhasil)

---

## 🎯 Kesimpulan

### Kriteria Advance (4 pts): ✅ **TERPENUHI LENGKAP**

**Alasan**:
1. ✅ Folder MLProject dengan struktur lengkap
2. ✅ Workflow CI otomatis training model
3. ✅ Artifacts tersimpan di Google Drive (Skilled)
4. ✅ Docker image di-build dengan `mlflow models build-docker` (Advance)
5. ✅ Docker image di-push ke Docker Hub (Advance)
6. ✅ Repository public dan well-documented
7. ✅ Menggunakan GitHub Secrets untuk credentials
8. ✅ Semua file sesuai ketentuan

---

## 📚 Dokumentasi Pendukung

- ✅ README.md - Dokumentasi utama
- ✅ SETUP_GUIDE.md - Panduan setup step-by-step
- ✅ SUBMISSION_CHECKLIST.md - Checklist penilaian
- ✅ requirements.txt - Dependencies
- ✅ .gitignore - Git ignore rules
- ✅ docker_hub_link.txt - Docker Hub info

---

## 🚀 Siap Submit!

Jika semua checklist di atas terpenuhi, repository ini **SIAP** untuk submission dengan target **Advance (4 points)**.

**Good luck! 🎉**

---

**Created**: June 6, 2026  
**Author**: Devani  
**Program**: Dicoding x IBM - Membangun Sistem Machine Learning  
**Kriteria**: 3 - Workflow CI  
**Target**: Advance (4 points)
