class Classes:
    def __init__(self, class_id, title, creation_date, content, read_time):
        self.class_id = class_id
        self.title = title
        self.creation_date = creation_date
        self.content = content
        self.read_time = read_time

    def get_class_id(self):
        return self.class_id

    def get_title(self):
        return self.title

    def get_creation_date(self):
        return self.creation_date

    def get_content(self):
        return self.content

    def get_read_time(self):
        return self.read_time

