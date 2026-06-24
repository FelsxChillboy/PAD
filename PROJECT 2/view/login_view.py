import tkinter as tk

BG = "#F5F3F8"
WHITE = "#FFFFFF"
PRIMARY = "#553F83"
PRIMARY_DARK = "#432D6E"
PRIMARY_LIGHT = "#F0EBF8"
SECONDARY = "#111111"
MUTED = "#6B7280"
DANGER = "#DC2626"
SUCCESS = "#16A34A"
FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_SMALL = ("Segoe UI", 9)

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(root, bg=BG)
        self.frame.pack(fill="both", expand=True)

        self._build_toast()
        self._build_card()

    def _build_toast(self):
        self.toast_frame = tk.Frame(self.frame, bg=DANGER, height=0)
        self.toast_label = tk.Label(self.toast_frame, text="", font=FONT_BOLD,
                                    fg=WHITE, bg=DANGER, padx=20, pady=8)

    def show_toast(self, message, success=True):
        warna = SUCCESS if success else DANGER
        self.toast_frame.configure(bg=warna)
        self.toast_label.configure(text=message, bg=warna)
        self.toast_label.pack(fill="x")
        self.toast_frame.place(x=0, y=0, relwidth=1)
        self.root.after(3000, self._hide_toast)

    def _hide_toast(self):
        self.toast_frame.place_forget()

    def _build_card(self):
        self.card_frame = tk.Frame(self.frame, bg=WHITE, padx=45, pady=35,
                                   highlightbackground="#E5E7EB", highlightthickness=1)
        self.card_frame.place(relx=0.5, rely=0.45, anchor="center")

        self.logo_img = tk.PhotoImage(file="assets/logo.png")
        logo_canvas = tk.Canvas(self.card_frame, width=80, height=80,
                                bg=WHITE, highlightthickness=0)
        logo_canvas.pack(pady=0)
        logo_canvas.create_image(40, 40, image=self.logo_img)

        tk.Label(self.card_frame, text="Sistem Absensi", font=FONT_TITLE,
                 fg=PRIMARY, bg=WHITE).pack(pady=0)
        tk.Label(self.card_frame, text="Masuk ke akun Anda", font=FONT,
                 fg=MUTED, bg=WHITE).pack(pady=0)

        self._build_input("Username", self.controller.login)
        self.entry_username = self._last_entry
        self.entry_username.focus()

        self._build_input("Password")
        self.entry_password = self._last_entry
        self.entry_password.configure(show="*")
        self.entry_password.bind("<Return>", lambda e: self._on_login())

        self.btn_login = self._make_button(self.card_frame, "Login",
                                           PRIMARY, PRIMARY_DARK, self._on_login)
        self.btn_login.pack(fill="x", pady=8)

        self.label_error = tk.Label(self.card_frame, text="", font=FONT_SMALL,
                                    fg=DANGER, bg=WHITE)
        self.label_error.pack(pady=6)

    def _build_input(self, label_text, return_callback=None):
        tk.Label(self.card_frame, text=label_text, font=FONT_SMALL,
                 fg=MUTED, bg=WHITE, anchor="w").pack(fill="x", pady=0)
        entry = tk.Entry(self.card_frame, font=FONT, relief="solid",
                         bd=1, width=28, bg="#FAFAFA")
        entry.pack(fill="x", pady=0)
        self._bind_focus(entry)
        if return_callback:
            entry.bind("<Return>", lambda e: return_callback())
        self._last_entry = entry

    def _bind_focus(self, entry):
        entry.bind("<FocusIn>", lambda e: entry.configure(bg=WHITE, highlightbackground=PRIMARY, highlightthickness=2, highlightcolor=PRIMARY))
        entry.bind("<FocusOut>", lambda e: entry.configure(bg="#FAFAFA", highlightthickness=0))

    def _make_button(self, parent, text, bg, hover_bg, command):
        btn = tk.Button(parent, text=text, font=FONT_BOLD, bg=bg, fg=WHITE,
                        bd=0, padx=20, pady=9, cursor="hand2", command=command)
        btn.bind("<Enter>", lambda e: btn.configure(bg=hover_bg))
        btn.bind("<Leave>", lambda e: btn.configure(bg=bg))
        return btn

    def _on_login(self):
        self.btn_login.configure(text="Memproses...", state="disabled")
        self.root.update()
        self.controller.login()

    def enable_login(self):
        self.btn_login.configure(text="Login", state="normal")

    def show_error(self, msg):
        self.label_error.config(text=msg)
        self.enable_login()

    def clear_error(self):
        self.label_error.config(text="")

    def get_input(self):
        return self.entry_username.get(), self.entry_password.get()

    def destroy(self):
        self.frame.destroy()
