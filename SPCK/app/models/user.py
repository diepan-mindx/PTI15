class User:
    def __init__(self, username, password, email, avatar):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__avatar = avatar

    # Getter methods
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_avatar(self):
        return self.__avatar

    # Setter methods
    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def set_avatar(self, avatar):
        self.__avatar = avatar

    def getDict(self):
        return {
            "username": self.get_username(),
            "password": self.get_password(),
            "email": self.get_email(),
            "avatar": self.get_avatar(),
        }
