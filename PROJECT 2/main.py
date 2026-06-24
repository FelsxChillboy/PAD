import tkinter as tk
from model.user_model import UserModel
from controller.login_controller import LoginController

def main():
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
