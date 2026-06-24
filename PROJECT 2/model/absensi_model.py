import sqlite3
import os
from datetime import date

class AbsensiModel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(base_dir, "absensi.db")

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def get_all_absensi(self):
        conn = self._connect()
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

    def get_absensi_by_user(self, user_id):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, tanggal, jam_masuk, jam_pulang, status, keterangan
            FROM absensi WHERE user_id=? ORDER BY tanggal DESC
        """, (user_id,))
        rows = cur.fetchall()
        conn.close()
        return [{"id": r[0], "tanggal": r[1], "jam_masuk": r[2],
                 "jam_pulang": r[3], "status": r[4], "keterangan": r[5]} for r in rows]

    def get_absensi_by_tanggal(self, tanggal):
        conn = self._connect()
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

    def check_existing(self, user_id, tanggal):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id FROM absensi WHERE user_id=? AND tanggal=?", (user_id, tanggal))
        row = cur.fetchone()
        conn.close()
        return row[0] if row else None

    def add_absensi(self, user_id, tanggal, jam_masuk, status, keterangan=""):
        conn = self._connect()
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

    def update_absensi(self, id, jam_masuk, jam_pulang, status, keterangan):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE absensi SET jam_masuk=?, jam_pulang=?, status=?, keterangan=?
            WHERE id=?
        """, (jam_masuk, jam_pulang, status, keterangan, id))
        conn.commit()
        conn.close()

    def get_rekap(self, user_id=None):
        conn = self._connect()
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
