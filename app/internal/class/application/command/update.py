class Update:
    def __init__(self, email, class_id, title):
        self.email = email
        self.class_id = class_id
        self.title = title

    def email(self):
        return self.email

    def class_id(self):
        return self.class_id

    def title(self):
        return self.title

    @classmethod
    def new_update(cls, email, class_id, title):
        return cls(email, class_id, title)