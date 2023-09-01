class Classes:
    def __init__(self, class_id, title):
        self.class_id = class_id
        self.title = title

    def class_id(self):
        return self.class_id

    def title(self):
        return self.title

    @classmethod
    def new_class(cls, class_id, title):
        return cls(class_id, title)


class Profile:
    def __init__(self, email, name, classes):
        self.email = email
        self.name = name
        self.classes = classes

    def email(self):
        return self.email

    def name(self):
        return self.name

    def classes(self):
        return self.classes()

    @classmethod
    def new_profile(cls, email, name, classes):
        return cls(email, name, classes)
