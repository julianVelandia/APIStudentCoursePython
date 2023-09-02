class ProfileDTO:
    def __init__(self, email: str, name: str):
        self.email = email
        self.name = name

    def email(self):
        return self.email

    def name(self):
        return self.name
