# kantor.py

Automasi koneksi VPN, akses folder jaringan, dan buka web internal kantor secara otomatis di Windows.

## Fitur

- **Koneksi VPN Otomatis**: Menggunakan nama VPN dan kredensial dari environment variable.
- **Buka Folder Jaringan**: Otomatis membuka network share di File Explorer.
- **Buka Web Internal**: Otomatis membuka halaman web kantor di browser default.

## Cara Penggunaan

### 1. Siapkan Environment Variable
Sebelum menjalankan, set environment variable berikut di Windows:

```powershell
$env:VPN_USERNAME="username_anda"
$env:VPN_PASSWORD="password_anda"
```

### 2. Jalankan Skrip

```bash
python kantor.py
```

### 3. Build ke .exe (Opsional)

Skrip dapat dibundle menjadi executable Windows menggunakan PyInstaller. File hasil build ada di `dist/kantor.exe`.

Untuk build manual:

```bash
pyinstaller kantor.spec
```

## Konfigurasi

- Nama VPN, alamat folder jaringan, dan URL web dapat diubah di bagian bawah file `kantor.py`.

## Catatan

- Hanya berjalan di Windows.
- Pastikan VPN sudah dikonfigurasi di Windows dan dapat diakses dengan perintah `rasdial`.
- File `count.py` dan `countDate.py` tidak terkait langsung dengan skrip utama.

## Struktur Output

- `dist/kantor.exe` : File executable hasil build.
- `build/` : Artefak build PyInstaller (boleh diabaikan).

---

**Lisensi:** Bebas digunakan untuk keperluan internal kantor. 