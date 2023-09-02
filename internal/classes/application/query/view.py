class View:
    def __init__(self, email, class_id, title):
        self.email = email
        self.class_id = class_id
        self.title = title

    def get_title(self):
        return self.title

    def get_email(self):
        return self.email

    def get_class_id(self):
        return self.class_id
