import tkinter as tk
from tkinter import ttk
from view.mahasiswa_view import MahasiswaView
from model.user_model import UserModel
from model.absensi_model import AbsensiModel

class MahasiswaController:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.user_model = UserModel()
        self.absensi_model = AbsensiModel()
        self.view = MahasiswaView(root, self, user)
        self._load_absensi()

    def _load_absensi(self):
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)

        records = self.absensi_model.get_absensi_by_user(self.user["id"])
        for r in records:
            values = (r["tanggal"], r["jam_masuk"], r["jam_pulang"],
                      r["status"].title(), r["keterangan"])
            self.view.tree.insert("", "end", values=values)

        rekap = self.absensi_model.get_rekap(self.user["id"])
        self.view.update_rekap(rekap)

    def logout(self):
        self.view.destroy()
        from controller.login_controller import LoginController
        LoginController(self.root, self.user_model)
