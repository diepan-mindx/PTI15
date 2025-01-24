from datetime import datetime


class Note:

    def __init__(self, id, title, note, created_by, tag):
        self.__id = id
        self.__title = title
        self.__note = note
        self.__created_by = created_by 
        self.__created_at = (
            datetime.now()
        )  # Automatically set to the current date and time
        self.__tag = tag

    # Getter methods
    def get_title(self):
        return self.__title

    def get_note(self):
        return self.__note

    def get_created_by(self):
        return self.__created_by

    def get_created_at(self):
        return self.__created_at

    def get_tag(self):
        return self.__tag

    def get_id(self):
        return self.__id

    # Setter methods

    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_note(self, note):
        self.__note = note

    def set_created_by(self, created_by):
        self.__created_by = created_by

    def set_created_at(self, created_at):
        self.__created_at = created_at

    def set_tag(self, tag):
        self.__tag = tag

    def getDict(self):
        return {
            "id": self.get_id(),
            "title": self.get_title(),
            "note": self.get_note(),
            "created_by": self.get_created_by(),
            "created_at": self.get_created_at().isoformat(),  # Convert datetime to ISO format string
            "tag": self.get_tag(),
        }
