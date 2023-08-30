class Class:
    def __init__(self, class_id, title, creation_date, content, read_time):
        self.class_id = class_id
        self.title = title
        self.creation_date = creation_date
        self.content = content
        self.read_time = read_time

    def class_id(self):
        return self.class_id

    def title(self):
        return self.title

    def creation_date(self):
        return self.creation_date

    def content(self):
        return self.content

    def read_time(self):
        return self.read_time

    @classmethod
    def new_class(cls, class_id, title, creation_date, content, read_time):
        return cls(class_id, title, creation_date, content, read_time)
