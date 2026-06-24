<p align="center">
  <img src="assets/logo.png" alt="Logo" width="80" height="80">
</p>

<h1 align="center">Aplikasi Absensi</h1>
<p align="center">
  Tkinter MVC &bull; Python &bull; SQLite
</p>
<p align="center">
  <b>Ahmad Azarruddin</b> &mdash; 23260028
</p>

<br>

---

## Tentang

Aplikasi desktop absensi mahasiswa dengan GUI berbasis Python Tkinter dan SQLite, menggunakan arsitektur **MVC (Model-View-Controller)**. Mendukung dua role pengguna: **Dosen** dan **Mahasiswa**.

<br>

## Fitur

- **Autentikasi** &mdash; Login dengan username dan password
- **Role Dashboard** &mdash; Tampilan berbeda untuk Dosen dan Mahasiswa
- **CRUD Mahasiswa** &mdash; Tambah, edit, hapus data mahasiswa
- **Absensi Harian** &mdash; Input status Hadir / Izin / Sakit / Alpha
- **Rekap Otomatis** &mdash; Ringkasan absensi per mahasiswa
- **Pencarian** &mdash; Filter data real-time
- **Bulk Actions** &mdash; Isi cepat semua status sekaligus
- **Toast Notification** &mdash; Notifikasi modern tanpa messagebox

<br>

## Cara Menjalankan

```bash
cd "PROJECT 2"
python main.py
```

<br>

## Login Default

| Role | Username | Password |
|------|----------|----------|
| Dosen | `dosen1` | `123456` |
| Mahasiswa | `mahasiswa1` | `123456` |
| Mahasiswa | `mahasiswa2` | `123456` |

<br>

## Screenshot

| **Login** | **Dashboard Dosen** | **Dashboard Mahasiswa** |
|:---------:|:-------------------:|:-----------------------:|
| ![Login](image.png) | ![Dosen](image-1.png) | ![Mahasiswa](image-2.png) |

<br>

## Struktur Proyek

```
PROJECT 2/
├── main.py                 # Entry point
├── controller/             # Logic layer
│   ├── login_controller.py
│   ├── dosen_controller.py
│   └── mahasiswa_controller.py
├── model/                  # Data layer
│   ├── user_model.py
│   └── absensi_model.py
├── view/                   # UI layer
│   ├── login_view.py
│   ├── dosen_view.py
│   └── mahasiswa_view.py
└── assets/
    └── logo.png
```

<br>

## Teknologi

| | |
|---|---|
| **Bahasa** | Python 3.14 |
| **GUI** | Tkinter (standar library) |
| **Database** | SQLite3 (standar library) |
| **Arsitektur** | MVC Pattern |
| **Ketergantungan** | None (100% built-in) |
