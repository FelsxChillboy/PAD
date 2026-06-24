<div align="center">
  <br>
  <img src="assets/logo.png" alt="logo" width="96">
  <br><br>
  <h1>⌨ Aplikasi Absensi</h1>
  <p>
    <code>Python 3.14</code>
    <code>Tkinter</code>
    <code>SQLite3</code>
    <code>Callback Pattern</code>
  </p>
  <br>
  <table>
    <tr>
      <th align="center" colspan="2">Informasi Mahasiswa</th>
    </tr>
    <tr>
      <td align="right"><b>Nama</b></td>
      <td><code>Ahmad Azarruddin</code></td>
    </tr>
    <tr>
      <td align="right"><b>NIM</b></td>
      <td><code>23260028</code></td>
    </tr>
  </table>
  <br>
  <p>
    <a href="#-fitur">Fitur</a> •
    <a href="#-cara-menjalankan">Instalasi</a> •
    <a href="#-akun-default">Akun</a> •
    <a href="#-tampilan">Tampilan</a> •
    <a href="#-struktur">Struktur</a>
  </p>
  <br>
</div>

---

<div align="center">
  <h3>📌 &nbsp; Ringkasan Proyek</h3>
  <p>
    Aplikasi desktop <strong>absensi mahasiswa</strong> berbasis <strong>Python Tkinter</strong>
    dan <strong>SQLite</strong> dengan arsitektur <strong>callback-based</strong>.
    Dua role pengguna — Dosen dan Mahasiswa — dengan dashboard yang berbeda.
  </p>
  <p>
    <i>Zero external dependencies. 100% Python built-in.</i>
  </p>
</div>

---

## ◆ Fitur

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🔐 &nbsp; Autentikasi</h4>
      Login aman dengan username & password, routing otomatis sesuai role.
    </td>
    <td width="50%" valign="top">
      <h4>👥 &nbsp; CRUD Mahasiswa</h4>
      Tambah, edit, dan hapus data mahasiswa dengan validasi input.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>📋 &nbsp; Absensi Harian</h4>
      Input kehadiran per tanggal: Hadir, Izin, Sakit, atau Alpha.
    </td>
    <td width="50%" valign="top">
      <h4>📊 &nbsp; Rekap Otomatis</h4>
      Ringkasan jumlah Hadir, Izin, Sakit, Alpha per mahasiswa.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🔍 &nbsp; Pencarian Real-Time</h4>
      Filter data mahasiswa langsung saat mengetik.
    </td>
    <td width="50%" valign="top">
      <h4>⚡ &nbsp; Bulk Actions</h4>
      Isi cepat seluruh status (Semua Hadir / Izin / Alpha) satu klik.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🎨 &nbsp; UI Modern</h4>
      Purple theme (#553F83), hover effects, sidebar navigasi, toast notification.
    </td>
    <td width="50%" valign="top">
      <h4>📦 &nbsp; Database Terpadu</h4>
      Satu file database.py menangani semua query — init, seed, CRUD, rekap.
    </td>
  </tr>
</table>

---

## ◆ Cara Menjalankan

### 1. Clone Repository

Buka terminal/command prompt, lalu jalankan:

```bash
git clone https://github.com/FelsxChillboy/PAD.git
cd PAD
```

### 2. Masuk ke Folder Proyek

```bash
cd "PROJECT 2"
```

### 3. Jalankan Aplikasi

```bash
python main.py
```

> 💡 Pastikan Python 3 sudah terinstall. Cek dengan `python --version`.

### 4. Login

Gunakan akun default dari tabel di bawah.

### Troubleshooting

| Masalah | Solusi |
|---------|--------|
| `python` tidak dikenali | Coba `py main.py` atau `python3 main.py` |
| File tidak ditemukan | Pastikan sudah `cd "PROJECT 2"` |
| Database error | Hapus `database/absensi.db`, lalu jalankan ulang (terbuat otomatis) |

---

## ◆ Akun Default

| Role | Username | Password |
|------|----------|----------|
| 👨‍🏫 **Dosen** | `dosen1` | `123456` |
| 👨‍🎓 **Mahasiswa** | `mahasiswa1` | `123456` |
| 👨‍🎓 **Mahasiswa** | `mahasiswa2` | `123456` |

---

## ◆ Tampilan Aplikasi

<div align="center">
  <table>
    <tr>
      <th align="center">Login</th>
      <th align="center">Dashboard Dosen</th>
      <th align="center">Dashboard Mahasiswa</th>
    </tr>
    <tr>
      <td><img src="image.png" alt="Login"></td>
      <td><img src="image-1.png" alt="Dosen"></td>
      <td><img src="image-2.png" alt="Mahasiswa"></td>
    </tr>
  </table>
</div>

---

## ◆ Struktur Proyek

```
PROJECT 2/
│
├── main.py                       # Entry point (AbsensiApp class)
│
├── database/                     # Database layer
│   ├── __init__.py
│   ├── database.py               # init, seed, & semua query
│   └── absensi.db                # Database SQLite
│
├── views/                        # User interface layer
│   ├── __init__.py
│   ├── view_login.py             # Login dengan callback
│   ├── view_dosen_dashboard.py   # Dashboard dosen + CRUD + absensi
│   └── view_mahasiswa_dashboard.py # Dashboard mahasiswa + rekap
│
└── assets/
    └── logo.png                   # Logo aplikasi
```

---

## ◆ Spesifikasi Teknis

| Komponen | Detail |
|----------|--------|
| **Bahasa** | Python 3.14 |
| **GUI Framework** | Tkinter (native library) |
| **Database** | SQLite3 (native library) |
| **Architecture** | Callback-based (view langsung panggil database) |
| **External Dependencies** | None |
| **Total Files** | 7 file Python |
| **Database File** | `database/absensi.db` (auto-generated) |

---

<div align="center">
  <br>
  <sub>
    Tugas Pemrograman Aplikasi Desktop &bull; 2026
    <br>
    <code>Made with Python + Tkinter</code>
  </sub>
</div>
