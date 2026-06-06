# 📁 Google Drive API Setup - Step by Step

Panduan lengkap untuk setup Google Drive API dan mendapatkan credentials.

---

## 🎯 Tujuan

Mendapatkan 2 hal:
1. **GOOGLE_DRIVE_CREDENTIALS** - JSON credentials untuk authentication
2. **GOOGLE_DRIVE_FOLDER_ID** - ID folder tujuan upload

---

## 📋 Prerequisites

- [ ] Akun Google (Gmail)
- [ ] Browser (Chrome/Edge/Firefox)
- [ ] Python 3.9+ terinstall
- [ ] Library google-auth-oauthlib terinstall

---

## 🚀 Part 1: Setup Google Cloud Console

### Step 1: Buat Project

1. **Buka Google Cloud Console:**
   ```
   https://console.cloud.google.com/
   ```

2. **Login dengan akun Google Anda**

3. **Create New Project:**
   - Klik dropdown project di atas (sebelah logo Google Cloud)
   - Klik **"New Project"**
   - **Project name**: `mlflow-wine-quality`
   - **Location**: No organization (default)
   - Klik **"Create"**
   - Tunggu ~30 detik hingga project dibuat

4. **Pastikan project yang aktif adalah project baru:**
   - Klik dropdown project lagi
   - Pilih `mlflow-wine-quality`

---

### Step 2: Enable Google Drive API

1. **Buka API Library:**
   - Di menu kiri (☰), klik: **APIs & Services** > **Library**
   - Atau direct link: https://console.cloud.google.com/apis/library

2. **Search Google Drive API:**
   - Ketik di search box: `Google Drive API`
   - Klik hasil pertama: **Google Drive API** (by Google)

3. **Enable API:**
   - Klik tombol biru **"Enable"**
   - Tunggu ~10 detik
   - Anda akan diarahkan ke API Dashboard

---

### Step 3: Configure OAuth Consent Screen

⚠️ **IMPORTANT:** Tanpa ini, Anda tidak bisa buat credentials!

1. **Buka OAuth Consent Screen:**
   - Menu kiri: **APIs & Services** > **OAuth consent screen**
   - Atau direct link: https://console.cloud.google.com/apis/credentials/consent

2. **Select User Type:**
   - Pilih: **External** (untuk personal use)
   - Klik **"Create"**

3. **App Information:**
   - **App name**: `MLflow Wine Quality`
   - **User support email**: Pilih email Anda dari dropdown
   - **App logo**: Skip (optional)
   - **App domain**: Skip (optional)
   - **Authorized domains**: Skip
   - **Developer contact information**: Masukkan email Anda

4. **Klik "Save and Continue"**

5. **Scopes:**
   - Klik **"Save and Continue"** (skip, pakai default)

6. **Test Users:**
   - Klik **"Add Users"**
   - Masukkan email Google Anda
   - Klik **"Add"**
   - Klik **"Save and Continue"**

7. **Summary:**
   - Review informasi
   - Klik **"Back to Dashboard"**

✅ OAuth Consent Screen selesai!

---

### Step 4: Create OAuth Client ID

1. **Buka Credentials:**
   - Menu kiri: **APIs & Services** > **Credentials**
   - Atau direct link: https://console.cloud.google.com/apis/credentials

2. **Create Credentials:**
   - Klik tombol biru **"Create Credentials"** di atas
   - Pilih: **OAuth client ID**

3. **Application Type:**
   - **Application type**: Pilih **Desktop app** (PENTING!)
   - **Name**: `mlflow-desktop-client`
   - Klik **"Create"**

4. **Dialog "OAuth client created" muncul:**
   - Anda akan lihat **Client ID** dan **Client Secret**
   - Klik icon **"Download JSON"** (icon download di kanan bawah dialog)
   - File akan terdownload dengan nama panjang seperti:
     ```
     client_secret_1234567890-abc123xyz.apps.googleusercontent.com.json
     ```

5. **Rename File:**
   - Rename file yang di-download menjadi: **`client_secret.json`**
   - Pastikan ekstensi tetap `.json`

6. **Pindahkan File:**
   - Copy `client_secret.json` ke folder:
     ```
     Workflow-CI-Devani\
     ```
   - File harus di root folder project, sejajar dengan `generate_token.py`

✅ Client Secret selesai di-download!

---

## 🔑 Part 2: Generate Credentials

### Step 5: Run generate_token.py

1. **Buka Terminal/Command Prompt:**
   ```bash
   cd Workflow-CI-Devani
   ```

2. **Pastikan client_secret.json ada:**
   ```bash
   # Windows
   dir client_secret.json
   
   # Harusnya muncul file client_secret.json
   ```

3. **Install dependency (jika belum):**
   ```bash
   pip install google-auth-oauthlib
   ```

4. **Run script:**
   ```bash
   python generate_token.py
   ```

5. **Output yang muncul:**
   ```
   ======================================================================
   Google Drive OAuth Credentials Generator
   ======================================================================

   ✅ client_secret.json ditemukan

   🌐 Browser akan terbuka untuk authorization...
      Silakan login dan authorize aplikasi
   ```

6. **Browser akan otomatis terbuka:**
   - Jika tidak terbuka otomatis, copy URL dari terminal dan paste di browser
   - **Login** dengan akun Google yang sama dengan yang Anda setup di test users
   
7. **Google akan menampilkan warning:**
   ```
   "Google hasn't verified this app"
   ```
   - Klik **"Advanced"** atau **"Lanjutan"**
   - Klik **"Go to MLflow Wine Quality (unsafe)"**
   - Ini aman karena ini aplikasi Anda sendiri

8. **Authorize permissions:**
   - Google akan tanya: "MLflow Wine Quality wants to access your Google Account"
   - Anda akan lihat permission: "See, edit, create, and delete only the specific Google Drive files you use with this app"
   - Klik **"Allow"**

9. **Success page:**
   - Browser akan menampilkan: "The authentication flow has completed."
   - Anda bisa close browser tab tersebut

10. **Kembali ke Terminal:**
    - Terminal akan menampilkan:
    ```
    ======================================================================
    ✅ Authorization berhasil!
    ======================================================================

    📄 Credentials disimpan di: google_drive_credentials.json

    ======================================================================
    📋 COPY JSON BERIKUT KE GITHUB SECRET:
       Secret Name: GOOGLE_DRIVE_CREDENTIALS
    ======================================================================

    {
      "token": "ya29.a0AfB_byD...",
      "refresh_token": "1//0gXYZ123...",
      "token_uri": "https://oauth2.googleapis.com/token",
      "client_id": "1234567890-abc123.apps.googleusercontent.com",
      "client_secret": "GOCSPX-...",
      "scopes": [
        "https://www.googleapis.com/auth/drive.file"
      ]
    }
    
    ======================================================================
    ```

11. **COPY JSON di atas:**
    - Select semua JSON dari `{` sampai `}`
    - Ctrl+C untuk copy
    - Simpan di notepad sementara

✅ Credentials JSON berhasil di-generate!

---

## 📂 Part 3: Get Folder ID

### Step 6: Create Google Drive Folder

1. **Buka Google Drive:**
   ```
   https://drive.google.com
   ```

2. **Create New Folder:**
   - Klik **"New"** (tombol biru di kiri atas)
   - Pilih **"Folder"**
   - **Folder name**: `MLflow-Wine-Quality-Artifacts`
   - Klik **"Create"**

3. **Buka folder yang baru dibuat:**
   - Double click folder `MLflow-Wine-Quality-Artifacts`

4. **Lihat URL di browser:**
   ```
   https://drive.google.com/drive/folders/1ABCdefGHI123456789XYZ
   ```

5. **Copy Folder ID:**
   - ID folder adalah bagian setelah `/folders/`
   - Contoh dari URL di atas: `1ABCdefGHI123456789XYZ`
   - Copy ID tersebut
   - Simpan di notepad sementara

✅ Folder ID berhasil didapat!

---

## 🔐 Part 4: Add to GitHub Secrets

### Step 7: Setup GitHub Secrets

1. **Buka repository GitHub Anda:**
   ```
   https://github.com/<YOUR_USERNAME>/Workflow-CI-Devani
   ```

2. **Pergi ke Settings:**
   - Klik tab **"Settings"** (di kanan atas)

3. **Buka Secrets:**
   - Menu kiri: **"Secrets and variables"** > **"Actions"**
   - Atau direct link: `https://github.com/<USERNAME>/Workflow-CI-Devani/settings/secrets/actions`

4. **Add Secret 1 - GOOGLE_DRIVE_CREDENTIALS:**
   - Klik tombol hijau **"New repository secret"**
   - **Name**: `GOOGLE_DRIVE_CREDENTIALS`
   - **Secret**: Paste JSON yang Anda copy dari Step 5.11
     ```json
     {
       "token": "ya29.a0AfB_byD...",
       "refresh_token": "1//0gXYZ123...",
       "token_uri": "https://oauth2.googleapis.com/token",
       "client_id": "1234567890-abc123.apps.googleusercontent.com",
       "client_secret": "GOCSPX-...",
       "scopes": ["https://www.googleapis.com/auth/drive.file"]
     }
     ```
   - Klik **"Add secret"**

5. **Add Secret 2 - GOOGLE_DRIVE_FOLDER_ID:**
   - Klik tombol hijau **"New repository secret"** lagi
   - **Name**: `GOOGLE_DRIVE_FOLDER_ID`
   - **Secret**: Paste Folder ID dari Step 6.5
     ```
     1ABCdefGHI123456789XYZ
     ```
   - Klik **"Add secret"**

6. **Verify Secrets:**
   - Anda sekarang harus lihat 2 secrets:
     - ✅ `GOOGLE_DRIVE_CREDENTIALS`
     - ✅ `GOOGLE_DRIVE_FOLDER_ID`

✅ GitHub Secrets berhasil di-setup!

---

## 🧹 Part 5: Cleanup (IMPORTANT!)

### Step 8: Hapus File Sensitif

⚠️ **JANGAN COMMIT FILE-FILE INI KE GITHUB!**

File-file berikut berisi credentials yang sensitif:

1. **Delete client_secret.json:**
   ```bash
   del client_secret.json
   ```

2. **Delete google_drive_credentials.json:**
   ```bash
   del google_drive_credentials.json
   ```

3. **Verify .gitignore includes them:**
   ```gitignore
   # File .gitignore sudah include:
   credentials.json
   client_secret.json
   google_drive_credentials.json
   token.pickle
   *.key
   ```

✅ Cleanup selesai!

---

## ✅ Verification Checklist

Sebelum lanjut, pastikan:

- [ ] Google Cloud project `mlflow-wine-quality` sudah dibuat
- [ ] Google Drive API sudah enabled
- [ ] OAuth consent screen sudah configured
- [ ] OAuth client ID sudah dibuat (Desktop app)
- [ ] File `client_secret.json` sudah di-download dan di-rename
- [ ] Script `generate_token.py` sudah dijalankan
- [ ] Browser authorization sudah selesai (Allow)
- [ ] JSON credentials sudah di-copy
- [ ] Google Drive folder sudah dibuat
- [ ] Folder ID sudah di-copy
- [ ] GitHub Secret `GOOGLE_DRIVE_CREDENTIALS` sudah di-add
- [ ] GitHub Secret `GOOGLE_DRIVE_FOLDER_ID` sudah di-add
- [ ] File `client_secret.json` dan `google_drive_credentials.json` sudah dihapus

---

## 🐛 Troubleshooting

### Error: "client_secret.json not found"
**Solusi:**
- Pastikan file `client_secret.json` ada di folder `Workflow-CI-Devani\`
- Pastikan nama file exact: `client_secret.json` (bukan `client_secret (1).json`)
- Check path: run `dir` di folder untuk verifikasi

### Error: "Google hasn't verified this app"
**Solusi:**
- Ini normal untuk app testing
- Klik "Advanced" > "Go to MLflow Wine Quality (unsafe)"
- Aman karena ini app Anda sendiri

### Error: "Access blocked: This app's request is invalid"
**Solusi:**
- Pastikan OAuth consent screen sudah configured
- Pastikan email Anda sudah ditambahkan sebagai test user
- Pastikan application type adalah **Desktop app** (bukan Web app)

### Browser tidak otomatis terbuka
**Solusi:**
- Copy URL yang muncul di terminal
- Paste di browser manually
- Complete authorization

### Token expired / invalid
**Solusi:**
- Run `python generate_token.py` lagi
- Re-authorize di browser
- Copy JSON baru ke GitHub Secret

---

## 📚 Resources

- [Google Cloud Console](https://console.cloud.google.com/)
- [Google Drive API Documentation](https://developers.google.com/drive/api/guides/about-sdk)
- [OAuth 2.0 for Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app)
- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

## 🎉 Done!

Jika semua step berhasil, Anda sudah punya:

✅ **GOOGLE_DRIVE_CREDENTIALS** di GitHub Secrets  
✅ **GOOGLE_DRIVE_FOLDER_ID** di GitHub Secrets

Sekarang workflow CI/CD Anda bisa upload artifacts ke Google Drive!

---

**Next Step:** Lanjut ke **Step 4** di SETUP_GUIDE.md (Setup Docker Hub Secrets)
