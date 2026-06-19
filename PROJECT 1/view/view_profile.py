import tkinter as tk
from PIL import Image, ImageTk

# Constants for the theme
BG_COLOR = "#F0F2F5"
WHITE = "#FFFFFF"
PRIMARY_COLOR = "#1877F2"
FONT_NORMAL = ("Arial", 10)
FONT_BOLD = ("Arial", 10, "bold")
FONT_SMALL = ("Arial", 9)

class ProfileView:
    def __init__(self, root):
        self.root = root
        self.root.title("Thinkter - Profil Saya")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        main_frame = tk.Frame(root, bg=WHITE, padx=30, pady=25)
        main_frame.pack(padx=20, pady=20)

        self.label_foto = tk.Label(main_frame, bg=WHITE)
        self.label_foto.pack(pady=(0, 15))

        self.info_frame = tk.Frame(main_frame, bg=WHITE)
        self.info_frame.pack(fill="x")

    def display_foto(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.LANCZOS)
            self.foto = ImageTk.PhotoImage(img)
            self.label_foto.config(image=self.foto)
        except Exception:
            self.label_foto.config(text="[Foto tidak ditemukan]", font=FONT_SMALL, fg="#999")

    def display_info_data(self, data):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        for label, value in data:
            row = tk.Frame(self.info_frame, bg=WHITE)
            row.pack(fill="x", pady=3)

            tk.Label(row, text=label, font=FONT_BOLD,
                     bg=WHITE, fg=PRIMARY_COLOR, width=20, anchor="w").pack(side="left")
            tk.Label(row, text=value, font=FONT_NORMAL,
                     bg=WHITE, anchor="w").pack(side="left", fill="x", expand=True)

    def mainloop(self):
        self.root.mainloop()
