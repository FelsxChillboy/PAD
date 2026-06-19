import os

class ProfileModel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._image_path = os.path.join(base_dir, "assets", "foto.png")
        self._data = [
            ("Nama", ": Ahmad Azaruddin"),
            ("Jenis Kelamin", ": Laki-laki"),
            ("Tempat, Tgl. Lahir", ": Lamongan, 28 September 2005"),
            ("Agama", ": Islam"),
            ("Alamat", ": Jl. Merpati Putih No. 187, Lamongan"),
            ("Email", ": felixmaou@gmail.com"),
            ("No. HP", ": +6281292675810"),
            ("Website", ": https://felsxchillboy.github.io/portofolio/"),
            ("Skills", ": Python, Tkinter, SQLite, Web Development"),
        ]

    def get_profile(self):
        return self._data

    def get_image_path(self):
        return self._image_path
