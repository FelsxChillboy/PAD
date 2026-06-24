import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "absensi.db")

def _connect():
    return sqlite3.connect(DB_PATH)

def init_database():
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            nama TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS absensi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            tanggal TEXT NOT NULL,
            jam_masuk TEXT,
            jam_pulang TEXT,
            status TEXT DEFAULT 'hadir',
            keterangan TEXT DEFAULT '',
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, tanggal)
        )
    """)
    conn.commit()
    conn.close()

def insert_default_data():
    conn = _connect()
    cur = conn.cursor()
    users = [
        ("dosen1", "123456", "dosen", "Dosen Satu"),
        ("mahasiswa1", "123456", "mahasiswa", "Mahasiswa Satu"),
        ("mahasiswa2", "123456", "mahasiswa", "Mahasiswa Dua"),
    ]
    for u in users:
        try:
            cur.execute("INSERT INTO users (username, password, role, nama) VALUES (?, ?, ?, ?)", u)
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()

# === USER QUERIES ===

def login(username, password):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "role": row[3], "nama": row[4]}
    return None

def get_all_mahasiswa():
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT id, username, nama FROM users WHERE role='mahasiswa' ORDER BY nama")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "username": r[1], "nama": r[2]} for r in rows]

def add_mahasiswa(username, password, nama):
    conn = _connect()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password, role, nama) VALUES (?, ?, 'mahasiswa', ?)",
                    (username, password, nama))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def update_mahasiswa(id, username, password, nama):
    conn = _connect()
    cur = conn.cursor()
    try:
        if password:
            cur.execute("UPDATE users SET username=?, password=?, nama=? WHERE id=?",
                        (username, password, nama, id))
        else:
            cur.execute("UPDATE users SET username=?, nama=? WHERE id=?", (username, nama, id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_mahasiswa(id):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM absensi WHERE user_id=?", (id,))
    cur.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

# === ABSENSI QUERIES ===

def get_all_absensi():
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.id, u.nama, a.tanggal, a.jam_masuk, a.jam_pulang, a.status, a.keterangan
        FROM absensi a JOIN users u ON a.user_id = u.id
        ORDER BY a.tanggal DESC, u.nama
    """)
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "nama": r[1], "tanggal": r[2], "jam_masuk": r[3],
             "jam_pulang": r[4], "status": r[5], "keterangan": r[6]} for r in rows]

def get_absensi_by_user(user_id):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, tanggal, jam_masuk, jam_pulang, status, keterangan
        FROM absensi WHERE user_id=? ORDER BY tanggal DESC
    """, (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "tanggal": r[1], "jam_masuk": r[2],
             "jam_pulang": r[3], "status": r[4], "keterangan": r[5]} for r in rows]

def get_absensi_by_tanggal(tanggal):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.id, u.nama, a.jam_masuk, a.jam_pulang, a.status, a.keterangan, a.user_id
        FROM absensi a JOIN users u ON a.user_id = u.id
        WHERE a.tanggal=? ORDER BY u.nama
    """, (tanggal,))
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "nama": r[1], "jam_masuk": r[2], "jam_pulang": r[3],
             "status": r[4], "keterangan": r[5], "user_id": r[6]} for r in rows]

def check_existing(user_id, tanggal):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM absensi WHERE user_id=? AND tanggal=?", (user_id, tanggal))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def add_absensi(user_id, tanggal, jam_masuk, status, keterangan=""):
    conn = _connect()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO absensi (user_id, tanggal, jam_masuk, status, keterangan)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, tanggal, jam_masuk, status, keterangan))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def update_absensi(id, jam_masuk, jam_pulang, status, keterangan):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE absensi SET jam_masuk=?, jam_pulang=?, status=?, keterangan=?
        WHERE id=?
    """, (jam_masuk, jam_pulang, status, keterangan, id))
    conn.commit()
    conn.close()

def get_rekap(user_id=None):
    conn = _connect()
    cur = conn.cursor()
    if user_id:
        cur.execute("""
            SELECT status, COUNT(*) FROM absensi
            WHERE user_id=? GROUP BY status
        """, (user_id,))
    else:
        cur.execute("SELECT status, COUNT(*) FROM absensi GROUP BY status")
    rows = cur.fetchall()
    conn.close()
    return {r[0]: r[1] for r in rows}
