import tkinter as tk
from model.profile_model import ProfileModel
from controller.profile_controller import ProfileController
from view.view_profile import ProfileView

def main():
    root = tk.Tk()
    model = ProfileModel()
    view = ProfileView(root)
    controller = ProfileController(model, view)
    controller.start_app()

if __name__ == "__main__":
    main()
