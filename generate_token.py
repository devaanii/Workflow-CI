"""
Script untuk generate Google Drive OAuth credentials
Jalankan script ini untuk mendapatkan credentials yang akan disimpan di GitHub Secrets

Prerequisites:
1. Download client_secret.json dari Google Cloud Console
2. Install dependencies: pip install google-auth-oauthlib

Usage:
    python generate_token.py

Output akan berupa JSON yang harus di-copy ke GitHub Secret: GOOGLE_DRIVE_CREDENTIALS
"""

from google_auth_oauthlib.flow import InstalledAppFlow
import json
import os

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    print("="*70)
    print("Google Drive OAuth Credentials Generator")
    print("="*70)
    print()
    
    # Check if client_secret.json exists
    if not os.path.exists('client_secret.json'):
        print("❌ ERROR: client_secret.json tidak ditemukan!")
        print()
        print("Cara mendapatkan client_secret.json:")
        print("1. Pergi ke https://console.cloud.google.com/")
        print("2. Pilih atau buat project")
        print("3. Enable Google Drive API")
        print("4. Buat OAuth 2.0 credentials (Desktop app)")
        print("5. Download JSON dan simpan sebagai client_secret.json")
        print()
        return
    
    print("✅ client_secret.json ditemukan")
    print()
    print("🌐 Browser akan terbuka untuk authorization...")
    print("   Silakan login dan authorize aplikasi")
    print()
    
    try:
        # Run OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
        
        print()
        print("="*70)
        print("✅ Authorization berhasil!")
        print("="*70)
        print()
        
        # Prepare credentials data
        creds_data = {
            'token': creds.token,
            'refresh_token': creds.refresh_token,
            'token_uri': creds.token_uri,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret,
            'scopes': creds.scopes
        }
        
        # Save to file
        with open('google_drive_credentials.json', 'w') as f:
            json.dump(creds_data, f, indent=2)
        
        print("📄 Credentials disimpan di: google_drive_credentials.json")
        print()
        print("="*70)
        print("📋 COPY JSON BERIKUT KE GITHUB SECRET:")
        print("   Secret Name: GOOGLE_DRIVE_CREDENTIALS")
        print("="*70)
        print()
        print(json.dumps(creds_data, indent=2))
        print()
        print("="*70)
        print()
        print("📌 Next Steps:")
        print("1. Copy JSON di atas")
        print("2. Pergi ke GitHub repository > Settings > Secrets")
        print("3. Klik 'New repository secret'")
        print("4. Name: GOOGLE_DRIVE_CREDENTIALS")
        print("5. Secret: Paste JSON yang di-copy")
        print("6. Klik 'Add secret'")
        print()
        print("⚠️  JANGAN COMMIT FILE INI KE GITHUB!")
        print("   File ini berisi credentials yang sensitif")
        print()
        
    except Exception as e:
        print()
        print("="*70)
        print("❌ ERROR:")
        print("="*70)
        print(str(e))
        print()

if __name__ == '__main__':
    main()
