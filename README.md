# Workflow-CI: Wine Quality Model Training with MLflow

Repository ini merupakan implementasi **Kriteria 3** dari submission Machine Learning Terapan untuk mendemonstrasikan workflow CI/CD menggunakan MLflow Project dan GitHub Actions.

## 📋 Deskripsi

Project ini mengimplementasikan pipeline otomatis untuk:
- 🍷 Training model RandomForestClassifier untuk klasifikasi kualitas wine
- 📊 Tracking eksperimen dengan MLflow
- 🔄 CI/CD automation dengan GitHub Actions
- ☁️ Upload artifacts ke Google Drive
- 🐳 Docker Image deployment ke Docker Hub
- 💾 Reproducible training dengan MLflow Project

## 📁 Struktur Folder

```
Workflow-CI-Devani/
├── .github/
│   └── workflows/
│       └── ci.yml                                # GitHub Actions workflow
├── MLProject/
│   ├── modelling.py                             # Script training model
│   ├── conda.yaml                               # Dependency environment
│   ├── MLProject                                # MLflow Project config (tanpa ekstensi)
│   ├── wine-quality-white_preprocessing.csv     # Dataset preprocessing
│   ├── mlruns/                                  # MLflow tracking artifacts (auto-generated)
│   └── docker_hub_link.txt                      # Link Docker Hub image (auto-generated)
├── README.md
└── requirements.txt
```

## 🚀 Fitur Utama

### ✅ Level Advance (4 Points)

1. **MLflow Project Setup** ✅
   - Konfigurasi MLProject dengan parameterized entry points
   - Conda environment untuk reproducibility
   - Local tracking dengan MLflow

2. **GitHub Actions CI/CD** ✅
   - Trigger otomatis pada push ke branch `main`
   - Manual trigger dengan `workflow_dispatch`
   - Training model otomatis menggunakan Python script

3. **Artifact Management (Skilled)** ✅
   - Upload artifacts ke Google Drive
   - Persistent storage untuk semua hasil training
   - Tracking lengkap di MLflow

4. **Docker Deployment (Advance)** ✅
   - Build Docker image dengan `mlflow models build-docker`
   - Push ke Docker Hub otomatis
   - Versioning dengan latest tag
   - Model serving siap production

## 🛠️ Setup

### Prerequisites

- Python 3.9+
- MLflow 2.13.0+
- GitHub Repository
- Docker Hub Account
- Google Drive API Credentials

### Setup Local

```bash
# Clone repository
git clone https://github.com/<USERNAME>/Workflow-CI-Devani.git
cd Workflow-CI-Devani

# Install dependencies
pip install -r requirements.txt

# Run MLflow Project
cd MLProject
mlflow run . --env-manager=local

# View results
mlflow ui
```

### Setup GitHub Actions

#### 1. Buat GitHub Repository

Buat repository baru bernama `Workflow-CI-Devani` dengan visibilitas **Public**.

#### 2. Setup GitHub Secrets

Pergi ke `Settings > Secrets and variables > Actions` dan tambahkan secrets berikut:

##### Docker Hub Secrets:
- `DOCKERHUB_USERNAME`: Username Docker Hub Anda
- `DOCKERHUB_TOKEN`: Access token dari Docker Hub

##### Google Drive Secrets:
- `GOOGLE_DRIVE_CREDENTIALS`: Credentials JSON dari Google Cloud
- `GOOGLE_DRIVE_FOLDER_ID`: ID folder Google Drive tujuan

#### 3. Mendapatkan Docker Hub Token

1. Login ke [Docker Hub](https://hub.docker.com/)
2. Klik profile > Account Settings
3. Security > New Access Token
4. Beri nama token (misal: `github-actions`)
5. Copy token dan simpan sebagai GitHub Secret `DOCKERHUB_TOKEN`

#### 4. Mendapatkan Google Drive Credentials

1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru atau pilih existing project
3. Enable Google Drive API
4. Buat OAuth 2.0 credentials
5. Download credentials JSON
6. Authorize aplikasi dan dapatkan refresh token
7. Format credentials sebagai JSON dan simpan ke `GOOGLE_DRIVE_CREDENTIALS`

Format credentials:
```json
{
  "token": "YOUR_ACCESS_TOKEN",
  "refresh_token": "YOUR_REFRESH_TOKEN",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "scopes": ["https://www.googleapis.com/auth/drive.file"]
}
```

#### 5. Push ke GitHub

```bash
git init
git add .
git commit -m "Initial commit - MLflow CI/CD Wine Quality"
git branch -M main
git remote add origin https://github.com/<USERNAME>/Workflow-CI-Devani.git
git push -u origin main
```

## 📊 Parameter MLflow Project

File `MLProject` mendukung parameter berikut:

| Parameter      | Type  | Default                              | Deskripsi                    |
|----------------|-------|--------------------------------------|------------------------------|
| `data_path`    | str   | `wine-quality-white_preprocessing.csv` | Path ke dataset            |
| `n_estimators` | int   | 100                                  | Jumlah trees di Random Forest|
| `random_state` | int   | 42                                   | Seed untuk reproducibility   |
| `test_size`    | float | 0.2                                  | Proporsi data test           |

### Contoh Custom Run

```bash
# Local run dengan parameter default
mlflow run . --env-manager=local

# Local run dengan custom parameters
mlflow run . --env-manager=local \
  -P n_estimators=200 \
  -P test_size=0.25

# Run dari GitHub
mlflow run https://github.com/<USERNAME>/Workflow-CI-Devani.git \
  -P n_estimators=150
```

## 🐳 Docker Image

Docker image yang dihasilkan dapat diakses di Docker Hub.

### Menggunakan Docker Image

```bash
# Pull image dari Docker Hub
docker pull <USERNAME>/wine-quality-model:latest

# Run model server
docker run -p 5000:8080 <USERNAME>/wine-quality-model:latest

# Test prediction via API
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

Response example:
```json
{
  "predictions": [1]
}
```
- `0` = Bad Wine (quality < 6)
- `1` = Good Wine (quality >= 6)

## 📈 Workflow CI/CD

### Trigger

Workflow akan berjalan otomatis ketika:
- Ada push ke branch `main`
- Manual trigger via GitHub Actions UI (`Actions` tab > `Run workflow`)

### Pipeline Steps

Workflow ini mengimplementasikan semua tahapan untuk kriteria **Advanced**:

1. ✅ **Set up job** - Initialize runner
2. ✅ **Run actions/checkout@v3** - Checkout repository
3. ✅ **Set up Python 3.12.7** - Setup Python environment
4. ✅ **Check Env** - Verify Python installation
5. ✅ **Install dependencies** - Install MLflow, scikit-learn, pandas, dll
6. ✅ **Run mlflow project** - Execute training dengan modelling.py
7. ✅ **Get latest MLflow run_id** - Extract run ID untuk Docker build
8. ✅ **Install Python dependencies** - Install Google Drive libraries
9. ✅ **Upload to Google Drive** - Upload artifacts ke cloud storage
10. ✅ **Build Docker Model** - Build image dengan `mlflow models build-docker`
11. ✅ **Log in to Docker Hub** - Authenticate ke Docker Hub
12. ✅ **Tag Docker Image** - Tag image dengan username/repo:latest
13. ✅ **Push Docker Image** - Push ke Docker Hub registry
14. ✅ **Post Log in to Docker Hub** - Confirmation log
15. ✅ **Post Set up Python 3.12.7** - Cleanup log
16. ✅ **Post Run actions/checkout@v3** - Cleanup log
17. ✅ **Complete job** - Final summary

### Monitoring Workflow

1. Pergi ke repository GitHub
2. Klik tab `Actions`
3. Pilih workflow run terbaru
4. Lihat logs untuk setiap step
5. Verifikasi artifacts di Google Drive dan Docker Hub

## 📝 Kriteria Penilaian

| Level      | Poin | Status | Deskripsi                                          |
|------------|------|--------|----------------------------------------------------|
| Reject     | 0    | ❌     | Tidak ada folder MLProject atau workflow CI        |
| Basic      | 2    | ✅     | MLProject + CI yang bisa melatih model             |
| Skilled    | 3    | ✅     | Basic + menyimpan artifacts ke Google Drive        |
| **Advance**| **4**| **✅** | **Skilled + Docker image ke Docker Hub**           |

### Checklist Kriteria Advance

- [x] Folder MLProject dengan struktur lengkap
- [x] File MLProject (tanpa ekstensi) dengan entry points
- [x] File conda.yaml dengan dependencies
- [x] File modelling.py yang dapat dijalankan
- [x] Dataset preprocessing (wine-quality-white_preprocessing.csv)
- [x] GitHub Actions workflow (.github/workflows/ci.yml)
- [x] Upload artifacts ke repository eksternal (Google Drive)
- [x] Build Docker image dengan `mlflow models build-docker`
- [x] Push Docker image ke Docker Hub
- [x] Repository GitHub dengan visibilitas Public
- [x] Menggunakan GitHub Secrets untuk credentials

## 🔍 Verifikasi

### Cek Training Results

Setelah workflow selesai:
```bash
# Clone repository
git clone https://github.com/<USERNAME>/Workflow-CI-Devani.git
cd Workflow-CI-Devani/MLProject

# View MLflow UI
mlflow ui
```

Buka browser: http://localhost:5000

### Cek Google Drive

1. Buka Google Drive
2. Pergi ke folder yang ditentukan di `GOOGLE_DRIVE_FOLDER_ID`
3. Lihat folder `mlruns` dengan semua artifacts

### Cek Docker Hub

1. Login ke [Docker Hub](https://hub.docker.com/)
2. Pergi ke repository `<USERNAME>/wine-quality-model`
3. Lihat image dengan tag `latest`
4. Verifikasi image size, build date, dan metadata

### Test Docker Image

```bash
# Pull dan run image
docker pull <USERNAME>/wine-quality-model:latest
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

## 🎯 Dataset & Model

### Dataset: Wine Quality (White Wine)

- **Source**: UCI Machine Learning Repository
- **Samples**: 4898 rows
- **Features**: 11 features (fixed acidity, volatile acidity, citric acid, dll)
- **Target**: Binary classification
  - `0` = Bad Wine (original quality < 6)
  - `1` = Good Wine (original quality >= 6)
- **Preprocessing**: Sudah dilakukan di tahap Kriteria 1

### Model Details

- **Algorithm**: Random Forest Classifier
- **Default Parameters**:
  - `n_estimators`: 100
  - `random_state`: 42
  - `test_size`: 0.2
- **Metrics**: Accuracy, Precision, Recall, F1-Score
- **Tracking**: MLflow dengan autolog

### Expected Performance

- **Accuracy**: ~75-80%
- **Training Time**: ~5-10 detik
- **Model Size**: ~5-10 MB

## 📚 Teknologi

- **MLflow 2.13.0**: Experiment tracking & model registry
- **Scikit-learn 1.5.1**: Machine learning library
- **Pandas 2.2.3**: Data manipulation
- **NumPy 2.0.0**: Numerical computing
- **GitHub Actions**: CI/CD automation
- **Docker**: Containerization
- **Docker Hub**: Image registry
- **Google Drive API**: Cloud storage

## 🔧 Troubleshooting

### Workflow Gagal di Step "Upload to Google Drive"

**Solusi**:
1. Pastikan `GOOGLE_DRIVE_CREDENTIALS` berisi credentials yang valid
2. Pastikan `GOOGLE_DRIVE_FOLDER_ID` adalah ID folder yang benar
3. Verifikasi folder memiliki permission untuk write

### Docker Build Gagal

**Solusi**:
1. Pastikan model berhasil di-log dengan `mlflow.sklearn.log_model()`
2. Verifikasi run_id valid dengan: `mlflow runs list --experiment-name wine-quality-basic`
3. Check Docker daemon status di GitHub Actions runner

### Model Prediction Error

**Solusi**:
1. Pastikan input features sesuai urutan dan jumlah (11 features)
2. Gunakan format JSON `dataframe_split` yang benar
3. Verifikasi semua fitur numerik, tidak ada missing values

## 👨‍💻 Author

**Nama**: Devani  
**Program**: Dicoding x IBM - Membangun Sistem Machine Learning  
**Kriteria**: 3 - Membuat Workflow CI  
**Target**: Advance (4 points)  
**Dataset**: Wine Quality (White Wine)

## 📄 License

Project ini dibuat untuk keperluan submission program Dicoding x IBM.

---

**Created**: June 6, 2026  
**Last Updated**: June 6, 2026

## 📌 Important Links

- **GitHub Repository**: `https://github.com/<USERNAME>/Workflow-CI-Devani`
- **Docker Hub**: `https://hub.docker.com/r/<USERNAME>/wine-quality-model`
- **MLflow Docs**: https://mlflow.org/docs/latest/index.html
- **GitHub Actions Docs**: https://docs.github.com/en/actions
