from view.login_view import LoginView
from view.dosen_view import DosenView
from view.mahasiswa_view import MahasiswaView
from controller.dosen_controller import DosenController
from controller.mahasiswa_controller import MahasiswaController

class LoginController:
    def __init__(self, root, user_model):
        self.root = root
        self.user_model = user_model
        self.view = LoginView(root, self)

    def login(self):
        self.view.clear_error()
        username, password = self.view.get_input()
        if not username or not password:
            self.view.show_error("Username dan password harus diisi")
            self.view.show_toast("Username dan password harus diisi", False)
            return

        user = self.user_model.login(username, password)
        if user is None:
            self.view.show_error("Username atau password salah")
            self.view.show_toast("Username atau password salah", False)
            return

        self.view.destroy()
        if user["role"] == "dosen":
            DosenController(self.root, user)
        else:
            MahasiswaController(self.root, user)
