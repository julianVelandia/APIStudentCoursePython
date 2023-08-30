class View:
    def __init__(self, email, class_id, title):
        self.email = email
        self.class_id = class_id
        self.title = title

    def title(self):
        return self.title

    def email(self):
        return self.email

    def class_id(self):
        return self.class_id

    @classmethod
    def new_view(cls, email, class_id, title):
        return cls(email, class_id, title)
