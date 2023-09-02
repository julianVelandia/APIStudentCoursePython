from typing import List


class Classes:
    def __init__(self, class_id, title):
        self.class_id = class_id
        self.title = title

    def class_id(self):
        return self.class_id

    def title(self):
        return self.title


class Profile:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.classes = []

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_classes(self):
        return self.classes

    def set_classes_done(self, classes_done):
        self.classes = classes_done
