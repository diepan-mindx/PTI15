from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from models.note import Note
from controllers.note_controller import NoteController


class Edit(QMainWindow):
    def __init__(self, root_ui_path, window_title, currentEmail, note=None):
        super().__init__()
        uic.loadUi(root_ui_path + "edit.ui", self)
        self.setWindowTitle(window_title)
        # kiem tra neu la man create => true, man hinh edit => false
        self.isCreateScreen = True if "Create" in window_title else False
        # dien du lieu vao truong-----
        if not note:
            # khong co du lieu dau vao => tao moi
            self.edit_title.setText(window_title)
        else:
            # da co du lieu dau vao =>
            self.title.setText(note["title"])
            self.tag.setText(note["tag"])
            self.note.setText(note["note"])
        # bat su kien cho nut save
        self.save_btn.mousePressEvent = self.save_data
        # bat su kien cho nut close
        self.B_Close.mousePressEvent = self.close_event
        self.currentEmail = currentEmail
        self.noteController = NoteController(currentEmail)

    def save_data(self, event):
        try:
            # get data from line edits
            tag = self.tag.text()
            title = self.title.text()
            note = self.note.text()
            note_object = {
                "id": 0,
                "title": title,
                "note": note,
                "created_by": self.currentEmail,
                "tag": tag,
            }

            # add note
            if self.isCreateScreen:
                self.noteController.add_note(note_object)
            else:
                # update note
                self.noteController.update_note(note_object)
            self.close()
        except Exception as e:
            print(e)

    def close_event(self):
        self.close()
