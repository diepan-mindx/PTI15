import os
import sys

from models.note import Note  # Import your Note model here
from DAO import DAO  # Assuming DAO is used for data persistence


class NoteController:
    def __init__(self, email):
        self.currentUserEmail = email
        self.__note_list = []
        self.__generate_note_list()

    # private methods (only this class can use)
    def __generate_note_list(self):
        # Get from JSON or database
        all_notes = DAO.load_json_data("note")
        self.__note_list = [
            note for note in all_notes if note["created_by"] == self.currentUserEmail
        ]

    def __save_note_list(self):
        DAO.write_json_data(self.get_full_data(), "note")

    def get_note_list(self):
        return self.__note_list

    def get_full_data(self):
        # get old list
        old_list = DAO.load_json_data("note")
        # add + update data in list
        full_list = [
            note for note in old_list if note["created_by"] != self.currentUserEmail
        ]
        full_list += self.__note_list
        return full_list

    def get_tag_list(self):
        # chuyen sang set -> xoa tag trung lap
        return set([note["tag"] for note in self.__note_list])

    # ------------------ Search Methods ------------------ #
    def search_by_title(self, title):
        # Return notes with the matching title
        return [
            note for note in self.__note_list if title.lower() in note["title"].lower()
        ]

    def search_by_tag(self, tag):
        # Return notes that contain the tag
        return [note for note in self.__note_list if tag in note["tag"]]

    def search_by_date(self, date):
        # Return notes created on the given date (formatted in the same way as stored)
        return [note for note in self.__note_list if note["created_at"] == date]

    # ------------------ Update Methods ------------------ #
    def generate_note_id(self):
        return len(self.__note_list)

    def add_note(self, note):
        print(note)
        # Add new note to the end of the list
        note["id"] = self.generate_note_id()
        self.__note_list.append(note)
        print(self.__note_list)
        # Persist changes to data source
        self.__save_note_list()

    def update_note(self, note):
        for i in range(len(self.__note_list)):
            if self.__note_list[i]["id"] == note["id"]:
                self.__note_list[i] = note  # Update
                break
        # Persist changes to data source
        self.__save_note_list()

    # ------------------ Delete Methods ------------------ #
    def delete_note_by_id(self, id):
        # Remove note from list by id
        self.__note_list = [note for note in self.__note_list if note["id"] != id]
        # Persist changes to data source
        self.__save_note_list()

    # ------------------ Sort Methods ------------------ #
    def sort_by_tag(self):
        # Sort notes by tag
        return self.__note_list.sort(key=lambda note: note["tag"])

    def sort_by_created_at(self):
        # Sort notes by creation date
        return sorted(self.__note_list, key=lambda note: note["created_at"])
