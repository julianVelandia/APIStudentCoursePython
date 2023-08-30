class Profile:
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def email(self):
        return self.email

    def name(self):
        return self.name

    @classmethod
    def new_profile(cls, email, name):
        return cls(email, name)
