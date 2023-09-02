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

    def set_classes_done(self, classes_done: List[Classes]):
        self.classes = classes_done
