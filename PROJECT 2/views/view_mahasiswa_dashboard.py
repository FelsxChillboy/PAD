import tkinter as tk
from tkinter import ttk
import database.database as db

BG = "#F5F3F8"
WHITE = "#FFFFFF"
PRIMARY = "#553F83"
PRIMARY_DARK = "#432D6E"
PRIMARY_LIGHT = "#F0EBF8"
SECONDARY = "#111111"
MUTED = "#6B7280"
SUCCESS = "#16A34A"
SUCCESS_LIGHT = "#DCFCE7"
WARNING = "#D97706"
WARNING_LIGHT = "#FEF3C7"
DANGER = "#DC2626"
DANGER_LIGHT = "#FEE2E2"
BORDER = "#E5E7EB"
FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_HEADER = ("Segoe UI", 16, "bold")
FONT_SMALL = ("Segoe UI", 9)

STATUS_COLORS = {
    "hadir": ("Hadir", SUCCESS, SUCCESS_LIGHT),
    "izin": ("Izin", WARNING, WARNING_LIGHT),
    "sakit": ("Sakit", DANGER, DANGER_LIGHT),
    "alpha": ("Alpha", "#6B7280", "#F3F4F6"),
}

class MahasiswaDashboard:
    def __init__(self, root, user, on_logout):
        self.root = root
        self.user = user
        self.on_logout = on_logout
        self.root.title("Dashboard Mahasiswa - Sistem Absensi")
        self.root.geometry("920x640")

        self.frame = tk.Frame(root, bg=BG)
        self.frame.pack(fill="both", expand=True)

        self._build_header()
        self._build_toast()
        self._build_body()

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
        tk.Label(inner, text="(Mahasiswa)", font=FONT_SMALL,
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
        self.toast_frame.pack(fill="x", before=getattr(self, 'body_frame', None))
        self.root.after(3000, self._hide_toast)

    def _hide_toast(self):
        self.toast_frame.pack_forget()

    def _build_body(self):
        self.body_frame = tk.Frame(self.frame, bg=BG)
        self.body_frame.pack(fill="both", expand=True)

        main = tk.Frame(self.body_frame, bg=WHITE, padx=24, pady=20,
                        highlightbackground=BORDER, highlightthickness=1)
        main.pack(fill="both", expand=True, padx=12, pady=12)

        tk.Label(main, text="Riwayat Absensi", font=FONT_HEADER,
                 fg=PRIMARY, bg=WHITE).pack(anchor="w", pady=0)
        tk.Label(main, text=f"Selamat datang, {self.user['nama']}",
                 font=FONT, fg=MUTED, bg=WHITE).pack(anchor="w", pady=0)

        self.rekap_frame = tk.Frame(main, bg=WHITE)
        self.rekap_frame.pack(fill="x", pady=0)

        tree_frame = tk.Frame(main, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        tree_frame.pack(fill="both", expand=True)

        cols = ("Tanggal", "Jam Masuk", "Jam Pulang", "Status", "Keterangan")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings",
                                 height=14, selectmode="none")
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        self.tree.column("Keterangan", width=200, anchor="w")
        self.tree.column("Tanggal", width=110)

        scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=FONT, rowheight=28, borderwidth=0)
        style.configure("Treeview.Heading", font=FONT_BOLD, padding=(0, 4))

        self._load_absensi()

    def _load_absensi(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        records = db.get_absensi_by_user(self.user["id"])
        for r in records:
            status_info = STATUS_COLORS.get(r["status"], ("", MUTED, WHITE))
            tag = r["status"] if r["status"] in STATUS_COLORS else ""
            self.tree.insert("", "end", values=(
                r["tanggal"], r["jam_masuk"] or "-", r["jam_pulang"] or "-",
                status_info[0], r["keterangan"]
            ), tags=(tag,))
            self.tree.tag_configure(tag, foreground=status_info[1], background=status_info[2])

        self._load_rekap()

    def _load_rekap(self):
        for w in self.rekap_frame.winfo_children():
            w.destroy()

        rekap = db.get_rekap(self.user["id"])
        labels = [
            ("Hadir", rekap.get("hadir", 0), SUCCESS, "#166534"),
            ("Izin", rekap.get("izin", 0), WARNING, "#92400E"),
            ("Sakit", rekap.get("sakit", 0), DANGER, "#991B1B"),
            ("Alpha", rekap.get("alpha", 0), MUTED, "#4B5563"),
        ]

        total = sum(v for v in rekap.values()) if rekap else 0
        for text, count, color, text_color in labels:
            card = tk.Frame(self.rekap_frame, bg=WHITE, highlightbackground=color,
                            highlightthickness=2, padx=8, pady=6)
            card.pack(side="left", padx=(0, 10), pady=0)

            tk.Label(card, text=str(count), font=("Segoe UI", 22, "bold"),
                     fg=color, bg=WHITE).pack()
            tk.Label(card, text=text, font=FONT_SMALL, fg=MUTED, bg=WHITE).pack()
