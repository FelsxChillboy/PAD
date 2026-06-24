import sqlite3
import os

class UserModel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(base_dir, "absensi.db")

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def login(self, username, password):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        row = cur.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "username": row[1], "role": row[3], "nama": row[4]}
        return None

    def get_all_mahasiswa(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, username, nama FROM users WHERE role='mahasiswa' ORDER BY nama")
        rows = cur.fetchall()
        conn.close()
        return [{"id": r[0], "username": r[1], "nama": r[2]} for r in rows]

    def add_mahasiswa(self, username, password, nama):
        conn = self._connect()
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

    def update_mahasiswa(self, id, username, password, nama):
        conn = self._connect()
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

    def delete_mahasiswa(self, id):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM absensi WHERE user_id=?", (id,))
        cur.execute("DELETE FROM users WHERE id=?", (id,))
        conn.commit()
        conn.close()
