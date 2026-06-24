import tkinter as tk
import sqlite3
import os
from model.user_model import UserModel
from controller.login_controller import LoginController

def init_database():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "absensi.db")
    conn = sqlite3.connect(db_path)
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
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        for u in [("dosen1", "123456", "dosen", "Dosen Satu"),
                  ("mahasiswa1", "123456", "mahasiswa", "Mahasiswa Satu"),
                  ("mahasiswa2", "123456", "mahasiswa", "Mahasiswa Dua")]:
            try:
                cur.execute("INSERT INTO users (username, password, role, nama) VALUES (?, ?, ?, ?)", u)
            except sqlite3.IntegrityError:
                pass
    conn.commit()
    conn.close()

def main():
    init_database()

    root = tk.Tk()
    root.title("Sistem Absensi")
    root.geometry("920x640")
    root.configure(bg="#F5F3F8")
    root.resizable(False, False)
    root.eval("tk::PlaceWindow . center")

    user_model = UserModel()
    LoginController(root, user_model)

    root.mainloop()

if __name__ == "__main__":
    main()
