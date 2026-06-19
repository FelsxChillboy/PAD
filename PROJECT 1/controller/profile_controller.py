class ProfileController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_app(self):
        data = self.model.get_profile()
        image_path = self.model.get_image_path()
        self.view.display_foto(image_path)
        self.view.display_info_data(data)
        self.view.mainloop()
