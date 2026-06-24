import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import database.database as db

BG = "#F5F3F8"
WHITE = "#FFFFFF"
PRIMARY = "#553F83"
PRIMARY_DARK = "#432D6E"
PRIMARY_LIGHT = "#F0EBF8"
SECONDARY = "#111111"
MUTED = "#6B7280"
SUCCESS = "#16A34A"
WARNING = "#D97706"
DANGER = "#DC2626"
BORDER = "#E5E7EB"
FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_HEADER = ("Segoe UI", 16, "bold")
FONT_SMALL = ("Segoe UI", 9)
SIDEBAR_W = 180

class DosenDashboard:
    def __init__(self, root, user, on_logout):
        self.root = root
        self.user = user
        self.on_logout = on_logout
        self.root.title("Dashboard Dosen - Sistem Absensi")
        self.root.geometry("920x640")

        self.frame = tk.Frame(root, bg=BG)
        self.frame.pack(fill="both", expand=True)

        self._build_header()
        self._build_toast()
        self._build_body()

        self.selected_id = None
        self._load_mahasiswa_list()

    def _build_header(self):
        header = tk.Frame(self.frame, bg=PRIMARY, padx=20, pady=0, height=52)
        header.pack(fill="x")
        header.pack_propagate(False)

        inner = tk.Frame(header, bg=PRIMARY)
        inner.pack(fill="both", expand=True)

        tk.Label(inner, text="Sistem Absensi", font=("Segoe UI", 13, "bold"),
                 fg=WHITE, bg=PRIMARY).pack(side="left")

        avatar = tk.Canvas(inner, width=30, height=30, bg=PRIMARY, highlightthickness=0)
        avatar.pack(side="right", padx=(0, 8))
        avatar.create_oval(2, 2, 28, 28, fill=WHITE, outline="")
        inisial = self.user["nama"][0].upper()
        avatar.create_text(15, 15, text=inisial, fill=PRIMARY, font=("Segoe UI", 11, "bold"))

        tk.Label(inner, text=self.user["nama"], font=FONT_BOLD,
                 fg=WHITE, bg=PRIMARY).pack(side="right", padx=(0, 4))
        tk.Label(inner, text="(Dosen)", font=FONT_SMALL,
                 fg="#D4C5F0", bg=PRIMARY).pack(side="right", padx=(0, 10))

        self.btn_logout = tk.Button(inner, text="Logout", font=FONT_SMALL,
                                    bg=WHITE, fg=PRIMARY, bd=0, padx=10, pady=3,
                                    cursor="hand2", command=self._on_logout)
        self.btn_logout.pack(side="right", padx=(8, 0))

    def _on_logout(self):
        self.frame.destroy()
        self.on_logout()

    def _build_toast(self):
        self.toast_frame = tk.Frame(self.frame, bg=DANGER, height=0)

    def show_toast(self, message, success=True):
        warna = SUCCESS if success else DANGER
        self.toast_frame.configure(bg=warna)
        for w in self.toast_frame.winfo_children():
            w.destroy()
        lbl = tk.Label(self.toast_frame, text=message, font=FONT_BOLD,
                       fg=WHITE, bg=warna, padx=20, pady=8)
        lbl.pack(fill="x")
        self.toast_frame.place(x=0, y=0, relwidth=1)
        self.root.after(3000, self._hide_toast)

    def _hide_toast(self):
        self.toast_frame.place_forget()

    def _build_body(self):
        self.body_frame = tk.Frame(self.frame, bg=BG)
        self.body_frame.pack(fill="both", expand=True)

        sidebar = tk.Frame(self.body_frame, bg=WHITE, width=SIDEBAR_W,
                           highlightbackground=BORDER, highlightthickness=1)
        sidebar.pack(fill="y", side="left")
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="Menu", font=FONT_SMALL, fg=MUTED,
                 bg=WHITE, anchor="w", padx=16, pady=16).pack(fill="x")

        self.nav_btns = []
        for text, cmd in [("  Mahasiswa", self._show_mahasiswa), ("  Absensi", self._show_absensi)]:
            btn = self._make_nav_btn(sidebar, text, cmd)
            btn.pack(fill="x", padx=8, pady=2)
            self.nav_btns.append(btn)

        self.content_frame = tk.Frame(self.body_frame, bg=BG)
        self.content_frame.pack(fill="both", expand=True, padx=12, pady=12)

        self.page_mahasiswa = tk.Frame(self.content_frame, bg=BG)
        self.page_absensi = tk.Frame(self.content_frame, bg=BG)

        self._build_page_mahasiswa()
        self._build_page_absensi()

        self._show_mahasiswa()

    def _make_nav_btn(self, parent, text, command):
        btn = tk.Button(parent, text=text, font=FONT, anchor="w", padx=12, pady=7,
                        bd=0, cursor="hand2", bg=WHITE, fg=SECONDARY, command=command)
        btn.bind("<Enter>", lambda e: btn.configure(bg=PRIMARY_LIGHT) if btn != self._active_nav else None)
        btn.bind("<Leave>", lambda e: btn.configure(bg=WHITE) if btn != self._active_nav else None)
        return btn

    def _activate_nav(self, active_btn):
        for btn in self.nav_btns:
            btn.configure(bg=WHITE, fg=SECONDARY)
        active_btn.configure(bg=PRIMARY, fg=WHITE)
        self._active_nav = active_btn

    def _show_mahasiswa(self):
        self._activate_nav(self.nav_btns[0])
        self.page_absensi.pack_forget()
        self.page_mahasiswa.pack(fill="both", expand=True)

    def _show_absensi(self):
        self._activate_nav(self.nav_btns[1])
        self.page_mahasiswa.pack_forget()
        self.page_absensi.pack(fill="both", expand=True)

    def _build_page_mahasiswa(self):
        main = tk.Frame(self.page_mahasiswa, bg=WHITE, padx=20, pady=16,
                        highlightbackground=BORDER, highlightthickness=1)
        main.pack(fill="both", expand=True)

        tk.Label(main, text="Data Mahasiswa", font=FONT_HEADER,
                 fg=PRIMARY, bg=WHITE).pack(anchor="w", pady=0)
        tk.Label(main, text=f"Selamat datang, {self.user['nama']}",
                 font=FONT, fg=MUTED, bg=WHITE).pack(anchor="w", pady=0)

        search_frame = tk.Frame(main, bg=WHITE)
        search_frame.pack(fill="x", pady=0)

        tk.Label(search_frame, text="Cari:", font=FONT, fg=MUTED,
                 bg=WHITE).pack(side="left", padx=(0, 6))
        self.entry_search = tk.Entry(search_frame, font=FONT, relief="solid",
                                     bd=1, width=24, bg="#FAFAFA")
        self.entry_search.pack(side="left")
        self.entry_search.bind("<KeyRelease>", lambda e: self._load_mahasiswa_list())

        form_frame = tk.Frame(main, bg=WHITE)
        form_frame.pack(fill="x", pady=0)

        left = tk.Frame(form_frame, bg=WHITE)
        left.pack(side="left", fill="x", expand=True)
        right = tk.Frame(form_frame, bg=WHITE)
        right.pack(side="right", padx=(20, 0))

        self._label(left, "Username")
        self.entry_username = self._entry(left)
        self._label(left, "Nama")
        self.entry_nama = self._entry(left)
        self._label(left, "Password")
        self.entry_password = self._entry(left, show="*")

        btn_frame = tk.Frame(right, bg=WHITE)
        btn_frame.pack(fill="x")
        self.btn_add = self._btn(btn_frame, "Tambah", PRIMARY, PRIMARY_DARK, self._add_mahasiswa)
        self.btn_add.pack(side="left", padx=(0, 4), fill="x", expand=True)
        self.btn_edit = self._btn(btn_frame, "Edit", WARNING, "#B45309", self._edit_mahasiswa)
        self.btn_edit.pack(side="left", padx=4, fill="x", expand=True)
        self.btn_delete = self._btn(btn_frame, "Hapus", DANGER, "#B91C1C", self._delete_mahasiswa)
        self.btn_delete.pack(side="left", padx=(4, 0), fill="x", expand=True)

        list_frame = tk.Frame(main, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        list_frame.pack(fill="both", expand=True)

        cols = ("ID", "Username", "Nama")
        self.tree = ttk.Treeview(list_frame, columns=cols, show="headings", height=10, selectmode="browse")
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.column("Nama", width=250, anchor="w")
        self.tree.bind("<<TreeviewSelect>>", self._on_select)
        scroll = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def _label(self, parent, text):
        tk.Label(parent, text=text, font=FONT_SMALL, fg=MUTED, bg=WHITE,
                 anchor="w").pack(fill="x", pady=0)

    def _entry(self, parent, show=""):
        e = tk.Entry(parent, font=FONT, relief="solid", bd=1, width=22, bg="#FAFAFA", show=show)
        e.pack(fill="x", pady=0)
        return e

    def _btn(self, parent, text, bg, hover_bg, command):
        btn = tk.Button(parent, text=text, font=FONT_BOLD, bg=bg, fg=WHITE,
                        bd=0, padx=10, pady=6, cursor="hand2", command=command)
        btn.bind("<Enter>", lambda e: btn.configure(bg=hover_bg))
        btn.bind("<Leave>", lambda e: btn.configure(bg=bg))
        return btn

    def _load_mahasiswa_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        search = self.entry_search.get().lower()
        all_mhs = db.get_all_mahasiswa()
        filtered = [m for m in all_mhs if search in m["nama"].lower() or search in m["username"].lower()]

        for m in filtered:
            self.tree.insert("", "end", values=(m["id"], m["username"], m["nama"]))

    def _on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.selected_id = int(values[0])
        self.entry_username.delete(0, "end")
        self.entry_username.insert(0, values[1])
        self.entry_nama.delete(0, "end")
        self.entry_nama.insert(0, values[2])

    def _add_mahasiswa(self):
        username = self.entry_username.get()
        nama = self.entry_nama.get()
        password = self.entry_password.get()
        if not username or not nama or not password:
            self.show_toast("Semua field harus diisi", False)
            return
        if db.add_mahasiswa(username, password, nama):
            self.show_toast("Mahasiswa berhasil ditambahkan")
            self._load_mahasiswa_list()
            self.entry_username.delete(0, "end")
            self.entry_nama.delete(0, "end")
            self.entry_password.delete(0, "end")
        else:
            self.show_toast("Username sudah digunakan", False)

    def _edit_mahasiswa(self):
        if self.selected_id is None:
            self.show_toast("Pilih mahasiswa terlebih dahulu", False)
            return
        username = self.entry_username.get()
        nama = self.entry_nama.get()
        password = self.entry_password.get()
        if not username or not nama:
            self.show_toast("Username dan Nama harus diisi", False)
            return
        if db.update_mahasiswa(self.selected_id, username, password, nama):
            self.show_toast("Mahasiswa berhasil diupdate")
            self._load_mahasiswa_list()
        else:
            self.show_toast("Username sudah digunakan", False)

    def _delete_mahasiswa(self):
        if self.selected_id is None:
            self.show_toast("Pilih mahasiswa terlebih dahulu", False)
            return
        if messagebox.askyesno("Konfirmasi", "Hapus mahasiswa ini?\nData absensi juga akan dihapus."):
            db.delete_mahasiswa(self.selected_id)
            self._load_mahasiswa_list()
            self.show_toast("Mahasiswa berhasil dihapus")

    def clear_form_mahasiswa(self):
        self.entry_username.delete(0, "end")
        self.entry_nama.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.selected_id = None

    def _build_page_absensi(self):
        main = tk.Frame(self.page_absensi, bg=WHITE, padx=20, pady=16,
                        highlightbackground=BORDER, highlightthickness=1)
        main.pack(fill="both", expand=True)

        tk.Label(main, text="Input Absensi Harian", font=FONT_HEADER,
                 fg=PRIMARY, bg=WHITE).pack(anchor="w", pady=0)
        tk.Label(main, text=f"Selamat datang, {self.user['nama']}",
                 font=FONT, fg=MUTED, bg=WHITE).pack(anchor="w", pady=0)

        date_frame = tk.Frame(main, bg=WHITE)
        date_frame.pack(fill="x", pady=(0, 6))

        tk.Label(date_frame, text="Tanggal (YYYY-MM-DD):", font=FONT,
                 fg=SECONDARY, bg=WHITE).pack(side="left")
        self.entry_tanggal = tk.Entry(date_frame, font=FONT, relief="solid",
                                      bd=1, width=14, bg="#FAFAFA")
        self.entry_tanggal.pack(side="left", padx=(8, 10))

        self.btn_load = self._btn(date_frame, "Load", PRIMARY, PRIMARY_DARK, self._load_absensi)
        self.btn_load.pack(side="left")

        self.btn_submit = self._btn(date_frame, "Simpan Semua", SUCCESS, "#15803D", self._submit_absensi)
        self.btn_submit.pack(side="right")

        quick_frame = tk.Frame(main, bg=WHITE)
        quick_frame.pack(fill="x", pady=(0, 6))
        tk.Label(quick_frame, text="Isi Cepat:", font=FONT_SMALL, fg=MUTED,
                 bg=WHITE).pack(side="left", padx=(0, 4))
        self.btn_all_hadir = self._btn(quick_frame, "Semua Hadir", SUCCESS, "#15803D",
                                       lambda: self._set_all_status("hadir"))
        self.btn_all_hadir.pack(side="left", padx=2)
        self.btn_all_izin = self._btn(quick_frame, "Semua Izin", WARNING, "#B45309",
                                      lambda: self._set_all_status("izin"))
        self.btn_all_izin.pack(side="left", padx=2)
        self.btn_all_alpha = self._btn(quick_frame, "Semua Alpha", DANGER, "#B91C1C",
                                       lambda: self._set_all_status("alpha"))
        self.btn_all_alpha.pack(side="left", padx=2)

        header_row = tk.Frame(main, bg=PRIMARY_LIGHT, padx=8, pady=6)
        header_row.pack(fill="x")
        for txt, w in [("No", 40), ("Nama", 220), ("Jam Masuk", 110), ("Jam Pulang", 110), ("Status", 120)]:
            tk.Label(header_row, text=txt, font=FONT_BOLD, fg=PRIMARY,
                     bg=PRIMARY_LIGHT, width=w//7, anchor="w").pack(side="left")

        canvas = tk.Canvas(main, bg=WHITE, highlightthickness=0)
        scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)
        self.absensi_rows_frame = tk.Frame(canvas, bg=WHITE)
        self.absensi_rows_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.absensi_rows_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.absensi_widgets = {}

    def _set_all_status(self, status):
        for widgets in self.absensi_widgets.values():
            widgets["status"].set(status)

    def clear_absensi_rows(self):
        for w in self.absensi_rows_frame.winfo_children():
            w.destroy()
        self.absensi_widgets.clear()

    def add_absensi_row(self, no, user_id, nama, jam_masuk, jam_pulang, status):
        bg_baris = WHITE if no % 2 == 1 else "#FAF9FC"
        row = tk.Frame(self.absensi_rows_frame, bg=bg_baris, padx=8, pady=4)
        row.pack(fill="x")

        tk.Label(row, text=str(no), font=FONT, bg=bg_baris, fg=MUTED,
                 width=4, anchor="center").pack(side="left")
        tk.Label(row, text=nama, font=FONT, bg=bg_baris, fg=SECONDARY,
                 width=28, anchor="w").pack(side="left", padx=(5, 10))

        jam_masuk = jam_masuk if jam_masuk else ""
        jam_pulang = jam_pulang if jam_pulang else ""

        entry_masuk = tk.Entry(row, font=FONT, relief="solid", bd=1, width=10, bg="#FAFAFA")
        entry_masuk.insert(0, jam_masuk)
        entry_masuk.pack(side="left", padx=(0, 8))

        entry_pulang = tk.Entry(row, font=FONT, relief="solid", bd=1, width=10, bg="#FAFAFA")
        entry_pulang.insert(0, jam_pulang)
        entry_pulang.pack(side="left", padx=(0, 8))

        combo = ttk.Combobox(row, values=("hadir", "izin", "sakit", "alpha"),
                             font=FONT, state="readonly", width=10)
        combo.set(status if status else "hadir")
        combo.pack(side="left")

        self.absensi_widgets[user_id] = {
            "jam_masuk": entry_masuk,
            "jam_pulang": entry_pulang,
            "status": combo,
        }

    def get_tanggal(self):
        return self.entry_tanggal.get()

    def _load_absensi(self):
        tanggal = self.get_tanggal()
        if not tanggal:
            self.show_toast("Masukkan tanggal", False)
            return

        self.clear_absensi_rows()

        jam_sekarang = datetime.now().strftime("%H:%M:%S")
        mahasiswa_list = db.get_all_mahasiswa()
        absensi_list = db.get_absensi_by_tanggal(tanggal)
        absensi_map = {a["user_id"]: a for a in absensi_list}

        for i, m in enumerate(mahasiswa_list, 1):
            a = absensi_map.get(m["id"])
            jam_masuk = a["jam_masuk"] if a and a["jam_masuk"] else jam_sekarang
            jam_pulang = a["jam_pulang"] if a and a["jam_pulang"] else ""
            status = a["status"] if a and a["status"] else ""
            self.add_absensi_row(i, m["id"], m["nama"], jam_masuk, jam_pulang, status)

    def _submit_absensi(self):
        tanggal = self.get_tanggal()
        if not tanggal:
            self.show_toast("Masukkan tanggal", False)
            return

        jam_sekarang = datetime.now().strftime("%H:%M:%S")
        count = 0

        for user_id, widgets in self.absensi_widgets.items():
            jam_masuk = widgets["jam_masuk"].get()
            jam_pulang = widgets["jam_pulang"].get()
            status = widgets["status"].get()

            if not status:
                continue

            absensi_id = db.check_existing(user_id, tanggal)
            if absensi_id:
                db.update_absensi(absensi_id, jam_masuk or jam_sekarang, jam_pulang, status, "")
            else:
                db.add_absensi(user_id, tanggal, jam_masuk or jam_sekarang, status)
            count += 1

        self.show_toast(f"{count} data absensi berhasil disimpan")
        self._load_absensi()
