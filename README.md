# Flet Project Setup Guide

## 📥 Clone Repository
```sh
git clone https://github.com/your-repo/flet-project.git
cd flet-project
```

## 🛠 Install Poetry
Jika belum menginstal Poetry, silakan install terlebih dahulu:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Tambahkan Poetry ke PATH:
```sh
export PATH="$HOME/.local/bin:$PATH"
```

## 🏗 Aktifkan Virtual Environment
```sh
poetry env use python3
poetry shell
```

## 📦 Install Dependencies
```sh
poetry install
```

## 🚀 Jalankan Aplikasi di Desktop (Port 8081)
```sh
poetry run flet run -d -r main.py --port 8081
```
Atau langsung dengan:
```sh
poetry run python main.py
```

## 📱 Jalankan di Flet App Android
1. **Unduh dan Instal** aplikasi Flet di Android melalui [Google Play Store](https://play.google.com/store/apps/details?id=app.flet)
2. **Jalankan Server Flet di Desktop**
   ```sh
   poetry run flet run -r main.py --port 8081
   ```
3. **Masukkan IP dan Port di Flet App Android**
   - Buka aplikasi Flet di Android
   - Masukkan `http://<IP-KOMPUTER>:8081` pada kolom URL
   - Tekan **Connect**

> 💡 **Catatan**: Pastikan perangkat Android dan komputer berada dalam satu jaringan Wi-Fi.

## 🛠 Troubleshooting
- Jika Poetry tidak dikenali sebagai command, coba restart terminal atau tambahkan ke PATH.
- Pastikan firewall tidak memblokir port 8081 saat mengakses dari Android.
- Cek alamat IP komputer dengan `ipconfig` (Windows) atau `ifconfig` (Mac/Linux).

---
✨ **Happy Coding with Flet!** ✨

