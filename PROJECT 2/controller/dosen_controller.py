import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime
from view.dosen_view import DosenView
from model.user_model import UserModel
from model.absensi_model import AbsensiModel

class DosenController:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.user_model = UserModel()
        self.absensi_model = AbsensiModel()
        self._all_mahasiswa = []
        self.view = DosenView(root, self, user)
        self._load_mahasiswa_list()
        self._set_default_date()

    def _set_default_date(self):
        today = date.today().isoformat()
        self.view.entry_tanggal.delete(0, "end")
        self.view.entry_tanggal.insert(0, today)

    def _load_mahasiswa_list(self, filter_text=""):
        self.view.listbox.delete(0, "end")
        self._all_mahasiswa = self.user_model.get_all_mahasiswa()
        filtered = [m for m in self._all_mahasiswa
                    if filter_text.lower() in m["nama"].lower()
                    or filter_text.lower() in m["username"].lower()]

        for m in filtered:
            self.view.listbox.insert("end", f"{m['nama']} ({m['username']})")

    def filter_mahasiswa(self, event=None):
        text = self.view.entry_search.get()
        self._load_mahasiswa_list(text)

    def on_select_mahasiswa(self, event):
        selection = self.view.listbox.curselection()
        if not selection:
            return
        idx = selection[0]

        filter_text = self.view.entry_search.get()
        filtered = [m for m in self._all_mahasiswa
                    if filter_text.lower() in m["nama"].lower()
                    or filter_text.lower() in m["username"].lower()]

        if idx >= len(filtered):
            return
        m = filtered[idx]
        self.view.selected_id = m["id"]
        self.view.entry_username.delete(0, "end")
        self.view.entry_username.insert(0, m["username"])
        self.view.entry_nama.delete(0, "end")
        self.view.entry_nama.insert(0, m["nama"])
        self.view.entry_password.delete(0, "end")

    def add_mahasiswa(self):
        username, nama, password = self.view.get_form_mahasiswa()
        if not username or not nama or not password:
            self.view.show_toast("Semua field harus diisi", False)
            return
        if self.user_model.add_mahasiswa(username, password, nama):
            self.view.clear_form_mahasiswa()
            self._load_mahasiswa_list()
            self.view.show_toast("Mahasiswa berhasil ditambahkan")
        else:
            self.view.show_toast("Username sudah digunakan", False)

    def edit_mahasiswa(self):
        if self.view.selected_id is None:
            self.view.show_toast("Pilih mahasiswa terlebih dahulu", False)
            return
        username, nama, password = self.view.get_form_mahasiswa()
        if not username or not nama:
            self.view.show_toast("Username dan nama harus diisi", False)
            return
        if self.user_model.update_mahasiswa(self.view.selected_id, username, password, nama):
            self.view.clear_form_mahasiswa()
            self._load_mahasiswa_list()
            self.view.show_toast("Data mahasiswa berhasil diupdate")
        else:
            self.view.show_toast("Username sudah digunakan", False)

    def delete_mahasiswa(self):
        if self.view.selected_id is None:
            self.view.show_toast("Pilih mahasiswa terlebih dahulu", False)
            return
        if messagebox.askyesno("Konfirmasi", "Hapus mahasiswa ini?\nData absensi juga akan dihapus."):
            self.user_model.delete_mahasiswa(self.view.selected_id)
            self.view.clear_form_mahasiswa()
            self._load_mahasiswa_list()
            self.view.show_toast("Mahasiswa berhasil dihapus")

    def load_absensi(self):
        tanggal = self.view.get_tanggal()
        if not tanggal:
            self.view.show_toast("Masukkan tanggal", False)
            return

        self.view.clear_absensi_rows()

        jam_sekarang = datetime.now().strftime("%H:%M:%S")

        mahasiswa_list = self.user_model.get_all_mahasiswa()
        absensi_list = self.absensi_model.get_absensi_by_tanggal(tanggal)
        absensi_map = {a["user_id"]: a for a in absensi_list}

        for i, m in enumerate(mahasiswa_list, 1):
            a = absensi_map.get(m["id"])
            jam_masuk = a["jam_masuk"] if a and a["jam_masuk"] else jam_sekarang
            jam_pulang = a["jam_pulang"] if a and a["jam_pulang"] else ""
            status = a["status"] if a and a["status"] else ""
            self.view.add_absensi_row(i, m["id"], m["nama"],
                                      jam_masuk, jam_pulang, status)

    def submit_absensi(self):
        tanggal = self.view.get_tanggal()
        if not tanggal:
            self.view.show_toast("Masukkan tanggal", False)
            return

        from datetime import datetime
        jam_sekarang = datetime.now().strftime("%H:%M:%S")
        count = 0

        for user_id, widgets in self.view.absensi_widgets.items():
            jam_masuk = widgets["jam_masuk"].get()
            jam_pulang = widgets["jam_pulang"].get()
            status = widgets["status"].get()

            if not status:
                continue

            absensi_id = self.absensi_model.check_existing(user_id, tanggal)
            if absensi_id:
                self.absensi_model.update_absensi(
                    absensi_id, jam_masuk or jam_sekarang, jam_pulang, status, ""
                )
            else:
                self.absensi_model.add_absensi(
                    user_id, tanggal, jam_masuk or jam_sekarang, status
                )
            count += 1

        self.view.show_toast(f"Absensi berhasil disimpan ({count} mahasiswa)")
        self.load_absensi()

    def logout(self):
        self.view.destroy()
        from controller.login_controller import LoginController
        LoginController(self.root, self.user_model)
