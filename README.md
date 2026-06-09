# Workflow-CI: Breast Cancer Model Training with MLflow

Repository ini merupakan implementasi **Kriteria 3** dari submission Membangun Sistem Machine Learning untuk mendemonstrasikan workflow CI/CD menggunakan MLflow Project dan GitHub Actions.

## 📋 Deskripsi

Project ini mengimplementasikan pipeline otomatis untuk:
- 🩺 Training model RandomForestClassifier untuk klasifikasi diagnosis breast cancer
- 📊 Tracking eksperimen dengan MLflow
- 🔄 CI/CD automation dengan GitHub Actions
- ☁️ Upload artifacts ke Google Drive
- 🐳 Docker Image deployment ke Docker Hub
- 💾 Reproducible training dengan MLflow Project

## 📁 Struktur Folder

```
Workflow-CI/
├── .github/
│   └── workflows/
│       └── ci.yml                                # GitHub Actions workflow
├── MLProject/
│   ├── modelling.py                             # Script training model
│   ├── conda.yaml                               # Dependency environment
│   ├── MLProject                                # MLflow Project config (tanpa ekstensi)
│   ├── breast-cancer_preprocessing.csv          # Dataset preprocessing
│   ├── mlruns/                                  # MLflow tracking artifacts (auto-generated)
│   └── docker_hub_link.txt                      # Link Docker Hub image
├── README.md
└── requirements.txt
```

## 🚀 Fitur Utama
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

- Python 3.12.7 (lokal opsional 3.9+; CI menggunakan 3.12.7)
- MLflow 2.19.0
- GitHub Repository
- Docker Hub Account
- Google Drive API Credentials

### Setup Local

```bash
# Clone repository
git clone https://github.com/devaanii/Workflow-CI.git
cd Workflow-CI

# Install dependencies
pip install -r requirements.txt

# Run MLflow Project
cd MLProject
mlflow run . --env-manager=local

# View results
mlflow ui
```

### Setup GitHub Actions

#### 1. Setup GitHub Secrets

Pergi ke `Settings > Secrets and variables > Actions` dan tambahkan secrets berikut:

##### Docker Hub Secrets:
- `DOCKERHUB_USERNAME`: Username Docker Hub Anda
- `DOCKERHUB_TOKEN`: Access token dari Docker Hub

##### Google Drive Secrets:
- `GOOGLE_DRIVE_CREDENTIALS`: Credentials JSON dari Google Cloud
- `GOOGLE_DRIVE_FOLDER_ID`: ID folder Google Drive tujuan

#### 2. Mendapatkan Docker Hub Token

1. Login ke [Docker Hub](https://hub.docker.com/)
2. Klik profile > Account Settings
3. Security > New Access Token
4. Beri nama token (misal: `github-actions`)
5. Copy token dan simpan sebagai GitHub Secret `DOCKERHUB_TOKEN`

#### 3. Push ke GitHub

```bash
git add .
git commit -m "MLflow CI/CD Breast Cancer"
git push origin main
```

## 📊 Parameter MLflow Project

File `MLProject` mendukung parameter berikut:

| Parameter      | Type  | Default                            | Deskripsi                    |
|----------------|-------|------------------------------------|------------------------------|
| `data_path`    | str   | `breast-cancer_preprocessing.csv`  | Path ke dataset              |
| `n_estimators` | int   | 100                                | Jumlah trees di Random Forest|
| `random_state` | int   | 42                                 | Seed untuk reproducibility   |
| `test_size`    | float | 0.2                                | Proporsi data test           |

### Contoh Custom Run

```bash
# Local run dengan parameter default
mlflow run . --env-manager=local

# Local run dengan custom parameters
mlflow run . --env-manager=local \
  -P n_estimators=200 \
  -P test_size=0.25
```

## 🐳 Docker Image

Docker image yang dihasilkan dapat diakses di Docker Hub: `devaanii/breast-cancer-model`.

### Menggunakan Docker Image

```bash
# Pull image dari Docker Hub
docker pull devaanii/breast-cancer-model:latest

# Run model server
docker run -p 5000:8080 devaanii/breast-cancer-model:latest

# Test prediction via API
curl -X POST http://localhost:5000/invocations \
  -H 'Content-Type: application/json' \
  -d '{
    "dataframe_split": {
      "columns": [
        "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
        "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension",
        "radius error", "texture error", "perimeter error", "area error", "smoothness error",
        "compactness error", "concavity error", "concave points error", "symmetry error", "fractal dimension error",
        "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness",
        "worst compactness", "worst concavity", "worst concave points", "worst symmetry", "worst fractal dimension"
      ],
      "data": [[17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.0787, 1.095, 0.9053, 8.589, 153.4, 0.0064, 0.049, 0.0537, 0.0159, 0.03, 0.0062, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]]
    }
  }'
```

Response example:
```json
{
  "predictions": [0]
}
```
- `0` = Malignant (ganas)
- `1` = Benign (jinak)

## 📈 Workflow CI/CD

### Trigger

Workflow akan berjalan otomatis ketika:
- Ada push ke branch `main`
- Manual trigger via GitHub Actions UI (`Actions` tab > `Run workflow`)

### Pipeline Steps

1. ✅ Set up job
2. ✅ Checkout repository
3. ✅ Set up Python 3.12.7
4. ✅ Check Env
5. ✅ Install dependencies (MLflow, scikit-learn, pandas, dll)
6. ✅ Run mlflow project (training dengan modelling.py)
7. ✅ Get latest MLflow run_id
8. ✅ Upload artifacts ke Google Drive
9. ✅ Build Docker image dengan `mlflow models build-docker`
10. ✅ Push Docker image ke Docker Hub
11. ✅ Complete job

## 🎯 Dataset & Model

### Dataset: Breast Cancer Wisconsin (Diagnostic)

- **Source**: UCI Machine Learning Repository (juga via scikit-learn)
- **Samples**: 569 baris
- **Features**: 30 fitur numerik (mean/standard error/worst dari radius, texture, perimeter, dll)
- **Target**: Binary classification
  - `0` = Malignant (ganas)
  - `1` = Benign (jinak)
- **Preprocessing**: Sudah dilakukan di tahap Kriteria 1

### Model Details

- **Algorithm**: Random Forest Classifier
- **Default Parameters**:
  - `n_estimators`: 100
  - `random_state`: 42
  - `test_size`: 0.2
- **Metrics**: Accuracy
- **Tracking**: MLflow dengan autolog

## 📚 Teknologi

- **MLflow 2.19.0**: Experiment tracking & model registry
- **Scikit-learn 1.5.1**: Machine learning library
- **Pandas 2.2.3**: Data manipulation
- **NumPy 1.26.4**: Numerical computing
- **GitHub Actions**: CI/CD automation
- **Docker**: Containerization
- **Docker Hub**: Image registry
- **Google Drive API**: Cloud storage

## 👨‍💻 Author

**Nama**: Devani  
**Program**: Dicoding x IBM - Membangun Sistem Machine Learning  
**Kriteria**: 3 - Membuat Workflow CI  
**Target**: Advance (4 points)  
**Dataset**: Breast Cancer Wisconsin (Diagnostic)

## 📌 Important Links

- **GitHub Repository**: `https://github.com/devaanii/Workflow-CI`
- **Docker Hub**: `https://hub.docker.com/r/devaanii/breast-cancer-model`
- **MLflow Docs**: https://mlflow.org/docs/latest/index.html
- **GitHub Actions Docs**: https://docs.github.com/en/actions
