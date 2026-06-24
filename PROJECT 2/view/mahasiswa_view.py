import tkinter as tk
from tkinter import ttk

BG = "#F5F3F8"
WHITE = "#FFFFFF"
PRIMARY = "#553F83"
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

STATUS_STYLE = {
    "hadir":  (SUCCESS, SUCCESS_LIGHT),
    "izin":   (WARNING, WARNING_LIGHT),
    "sakit":  (WARNING, WARNING_LIGHT),
    "alpha":  (DANGER, DANGER_LIGHT),
}

class MahasiswaView:
    def __init__(self, root, controller, user):
        self.root = root
        self.controller = controller
        self.user = user
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
        avatar.create_text(15, 15, text=inisial, fill=PRIMARY,
                          font=("Segoe UI", 11, "bold"))

        tk.Label(inner, text=self.user["nama"], font=FONT_BOLD,
                 fg=WHITE, bg=PRIMARY).pack(side="right", padx=(0, 4))
        tk.Label(inner, text="(Mahasiswa)", font=FONT_SMALL,
                 fg="#D4C5F0", bg=PRIMARY).pack(side="right", padx=(0, 10))

        self.btn_logout = tk.Button(inner, text="Logout", font=FONT_SMALL,
                                    bg=WHITE, fg=PRIMARY, bd=0, padx=10, pady=3,
                                    cursor="hand2", command=self.controller.logout)
        self.btn_logout.pack(side="right", padx=(8, 0))

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
        self.toast_frame.pack(fill="x", before=self.body_frame)
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

        tree_frame = tk.Frame(main, bg=WHITE, highlightbackground=BORDER,
                              highlightthickness=1)
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

    def update_rekap(self, rekap):
        for w in self.rekap_frame.winfo_children():
            w.destroy()

        items = [
            ("Hadir", rekap.get("hadir", 0), SUCCESS, SUCCESS_LIGHT),
            ("Izin", rekap.get("izin", 0), WARNING, WARNING_LIGHT),
            ("Sakit", rekap.get("sakit", 0), WARNING, WARNING_LIGHT),
            ("Alpha", rekap.get("alpha", 0), DANGER, DANGER_LIGHT),
        ]

        for label, count, warna, bg_warna in items:
            card = tk.Frame(self.rekap_frame, bg=WHITE, padx=14, pady=10,
                            highlightbackground=warna, highlightthickness=2)
            card.pack(side="left", padx=(0, 10))

            tk.Label(card, text=str(count), font=("Segoe UI", 22, "bold"),
                     fg=warna, bg=WHITE).pack()
            tk.Label(card, text=label, font=FONT_SMALL, fg=MUTED,
                     bg=WHITE).pack()

    def add_status_row(self, parent, status):
        warna, bg_warna = STATUS_STYLE.get(status, (MUTED, WHITE))
        lbl = tk.Label(parent, text=f"  {status.title()}  ", font=FONT_BOLD,
                       fg=warna, bg=bg_warna, padx=8, pady=2)
        lbl.pack(side="left")

    def destroy(self):
        self.frame.destroy()
