<div align="center">
  <br>
  <img src="assets/logo.png" alt="logo" width="96">
  <br><br>
  <h1>⌨ Aplikasi Absensi</h1>
  <p>
    <code>Python 3.14</code>
    <code>Tkinter</code>
    <code>SQLite3</code>
    <code>MVC Architecture</code>
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
    dan <strong>SQLite</strong> dengan arsitektur <strong>Model-View-Controller (MVC)</strong>.
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
      <h4>🏛 &nbsp; MVC Architecture</h4>
      Model terpisah dari View dan Controller — kode bersih dan terstruktur.
    </td>
  </tr>
</table>

---

## ◆ Cara Menjalankan

```bash
# 1. Buka terminal dan masuk ke direktori proyek
cd "PROJECT 2"

# 2. Jalankan aplikasi (tanpa installasi paket tambahan)
python main.py
```

> 💡 Pastikan Python 3 sudah terinstall di sistem Anda. Cek dengan `python --version`.

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
├── main.py                       # Entry point aplikasi
│
├── controller/                   # Business logic layer
│   ├── __init__.py
│   ├── login_controller.py       # Validasi login & routing
│   ├── dosen_controller.py       # CRUD mahasiswa & absensi
│   └── mahasiswa_controller.py   # Lihat absensi & rekap
│
├── model/                        # Database layer
│   ├── __init__.py
│   ├── user_model.py             # Query user & mahasiswa
│   └── absensi_model.py          # Query absensi
│
├── view/                         # User interface layer
│   ├── __init__.py
│   ├── login_view.py             # Form login
│   ├── dosen_view.py             # Dashboard dosen
│   └── mahasiswa_view.py         # Dashboard mahasiswa
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
| **Design Pattern** | Model-View-Controller (MVC) |
| **External Dependencies** | None |
| **Total Files** | 14 file Python |
| **Database File** | `absensi.db` (auto-generated) |

---

<div align="center">
  <br>
  <sub>
    Tugas Pemrograman Desktop &bull; 2026
    <br>
    <code>Made with Python + Tkinter</code>
  </sub>
</div>
