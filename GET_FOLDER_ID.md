# 📂 Cara Mendapatkan Google Drive Folder ID

## Quick Steps:

1. **Buka Google Drive:**
   - Pergi ke: https://drive.google.com

2. **Buat Folder Baru:**
   - Klik tombol **"New"** (biru, di kiri atas)
   - Pilih **"Folder"**
   - **Folder name**: `MLflow-Wine-Quality-Artifacts`
   - Klik **"Create"**

3. **Buka Folder:**
   - Double click folder yang baru dibuat

4. **Lihat URL di Address Bar:**
   ```
   https://drive.google.com/drive/folders/1ABC123def456GHI789jkl
   ```

5. **Copy Folder ID:**
   - ID folder adalah bagian setelah `/folders/`
   - Dari contoh di atas: `1ABC123def456GHI789jkl`
   - **COPY ID ini!**

---

## 📝 Contoh URL dan Folder ID:

| URL | Folder ID |
|-----|-----------|
| `https://drive.google.com/drive/folders/1AbC-DeFgHiJ` | `1AbC-DeFgHiJ` |
| `https://drive.google.com/drive/folders/1XyZ123abc789` | `1XyZ123abc789` |

---

## ✅ Setelah Dapat Folder ID:

Anda akan punya 2 values untuk GitHub Secrets:

1. **GOOGLE_DRIVE_CREDENTIALS** ← JSON yang panjang (sudah ada ✅)
2. **GOOGLE_DRIVE_FOLDER_ID** ← ID folder (contoh: `1ABC123def456GHI789jkl`)

---

## 🔐 Tambahkan ke GitHub Secrets:

1. Pergi ke: `https://github.com/<USERNAME>/Workflow-CI-Devani/settings/secrets/actions`

2. **Add Secret 1:**
   - Name: `GOOGLE_DRIVE_CREDENTIALS`
   - Secret: Paste JSON credentials
   - Add secret

3. **Add Secret 2:**
   - Name: `GOOGLE_DRIVE_FOLDER_ID`
   - Secret: Paste Folder ID
   - Add secret

Done! ✅
