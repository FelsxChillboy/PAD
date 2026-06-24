<div align="center">
  <br>
  <img src="assets/logo.png" alt="logo" width="96">
  <br><br>
  <h1>âŒ¨ Aplikasi Absensi</h1>
  <p>
    <code>Python 3.14</code>
    <code>Tkinter</code>
    <code>SQLite3</code>
    <code>MVC Pattern</code>
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
    <a href="#-fitur">Fitur</a> â€¢
    <a href="#-cara-menjalankan">Instalasi</a> â€¢
    <a href="#-akun-default">Akun</a> â€¢
    <a href="#-tampilan">Tampilan</a> â€¢
    <a href="#-struktur">Struktur</a>
  </p>
  <br>
</div>

---

<div align="center">
  <h3>ðŸ“Œ &nbsp; Ringkasan Proyek</h3>
  <p>
    Aplikasi desktop <strong>absensi mahasiswa</strong> berbasis <strong>Python Tkinter</strong>
    dan <strong>SQLite</strong> dengan arsitektur <strong>Model-View-Controller (MVC)</strong>.
    Dua role pengguna â€” Dosen dan Mahasiswa â€” dengan dashboard yang berbeda.
  </p>
  <p>
    <i>Zero external dependencies. 100% Python built-in.</i>
  </p>
</div>

---

## â—† Fitur

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>ðŸ” &nbsp; Autentikasi</h4>
      Login aman dengan username & password, routing otomatis sesuai role.
    </td>
    <td width="50%" valign="top">
      <h4>ðŸ‘¥ &nbsp; CRUD Mahasiswa</h4>
      Tambah, edit, dan hapus data mahasiswa dengan validasi input.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>ðŸ“‹ &nbsp; Absensi Harian</h4>
      Input kehadiran per tanggal: Hadir, Izin, Sakit, atau Alpha.
    </td>
    <td width="50%" valign="top">
      <h4>ðŸ“Š &nbsp; Rekap Otomatis</h4>
      Ringkasan jumlah Hadir, Izin, Sakit, Alpha per mahasiswa.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>ðŸ” &nbsp; Pencarian Real-Time</h4>
      Filter data mahasiswa langsung saat mengetik.
    </td>
    <td width="50%" valign="top">
      <h4>âš¡ &nbsp; Bulk Actions</h4>
      Isi cepat seluruh status (Semua Hadir / Izin / Alpha) satu klik.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>ðŸŽ¨ &nbsp; UI Modern</h4>
      Purple theme (#553F83), hover effects, sidebar navigasi, toast notification.
    </td>
    <td width="50%" valign="top">
      <h4>ðŸ“¦ &nbsp; Database Terpadu</h4>
      Satu file database.py menangani semua query â€” init, seed, CRUD, rekap.
    </td>
  </tr>
</table>

---

## â—† Cara Menjalankan

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

> ðŸ’¡ Pastikan Python 3 sudah terinstall. Cek dengan `python --version`.

### 4. Login

Gunakan akun default dari tabel di bawah.

### Troubleshooting

| Masalah | Solusi |
|---------|--------|
| `python` tidak dikenali | Coba `py main.py` atau `python3 main.py` |
| File tidak ditemukan | Pastikan sudah `cd "PROJECT 2"` |
| Database error | Hapus `database/absensi.db`, lalu jalankan ulang (terbuat otomatis) |

---

## â—† Akun Default

| Role | Username | Password |
|------|----------|----------|
| ðŸ‘¨â€ðŸ« **Dosen** | `dosen1` | `123456` |
| ðŸ‘¨â€ðŸŽ“ **Mahasiswa** | `mahasiswa1` | `123456` |
| ðŸ‘¨â€ðŸŽ“ **Mahasiswa** | `mahasiswa2` | `123456` |

---

## â—† Tampilan Aplikasi

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

## â—† Struktur Proyek

```
PROJECT 2/
â”‚
â”œâ”€â”€ main.py                       # Entry point (AbsensiApp class)
â”‚
â”œâ”€â”€ database/                     # Database layer
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ database.py               # init, seed, & semua query
â”‚   â””â”€â”€ absensi.db                # Database SQLite
â”‚
â”œâ”€â”€ views/                        # User interface layer
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ view_login.py             # Login dengan callback
â”‚   â”œâ”€â”€ view_dosen_dashboard.py   # Dashboard dosen + CRUD + absensi
â”‚   â””â”€â”€ view_mahasiswa_dashboard.py # Dashboard mahasiswa + rekap
â”‚
â””â”€â”€ assets/
    â””â”€â”€ logo.png                   # Logo aplikasi
```

---

## â—† Spesifikasi Teknis

| Komponen | Detail |
|----------|--------|
| **Bahasa** | Python 3.14 |
| **GUI Framework** | Tkinter (native library) |
| **Database** | SQLite3 (native library) |
| **Architecture** | Model-View-Controller (MVC) |
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

