# Aplikasi Absensi - Tkinter MVC

**Nama:** Ahmad Azarruddin  
**NIM:** 23260028  

Aplikasi desktop absensi mahasiswa berbasis Python Tkinter dan SQLite dengan arsitektur MVC (Model-View-Controller). Mendukung dua role pengguna: Dosen dan Mahasiswa.

---

## Fitur

- Login dengan autentikasi username dan password
- Role-based dashboard (Dosen & Mahasiswa)
- CRUD data mahasiswa
- Input absensi harian (Hadir / Izin / Sakit / Alpha)
- Rekap absensi per mahasiswa
- Pencarian data real-time
- Notifikasi toast modern
- Sidebar navigasi

---

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstall
2. Buka terminal/command prompt
3. Masuk ke folder PROJECT 2:
   ```
   cd "PROJECT 2"
   ```
4. Jalankan aplikasi:
   ```
   python main.py
   ```

---

## Login Default

| Role      | Username     | Password |
|-----------|--------------|----------|
| Dosen     | dosen1       | 123456   |
| Mahasiswa | mahasiswa1   | 123456   |
| Mahasiswa | mahasiswa2   | 123456   |

---

## Screenshot

| Login | Dashboard Dosen | Dashboard Mahasiswa |
|-------|-----------------|---------------------|
| ![Login](image.png) | ![Dosen](image-1.png) | ![Mahasiswa](image-2.png) |

---

## Teknologi

- Python 3.14
- Tkinter (GUI)
- SQLite3 (Database)
- MVC Architecture Pattern
