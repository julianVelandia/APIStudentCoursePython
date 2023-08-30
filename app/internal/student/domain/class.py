class Class:
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
