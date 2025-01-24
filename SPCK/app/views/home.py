from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

from views.setting import Setting  # Import the SettingsWindow class
from views.account import Account  # Import the account window class
from views.edit import Edit
from controllers.note_controller import NoteController
from components.note_item import NoteItem
from components.tag_item import TagItem
from models.user import User
from PyQt6.QtCore import Qt


class Home(QMainWindow):
    def __init__(self, root_ui_path, userEmail):
        super().__init__()
        self.noteController = NoteController(userEmail)
        self.root_ui_path = root_ui_path
        self.row_size = 2
        self.userEmail = userEmail
        self.ui = uic.loadUi(root_ui_path + "home.ui", self)
        self.setWindowTitle("Main Window")
        # add button
        self.add_btn.mousePressEvent = self.create_note
        # account button
        self.profile_btn.mousePressEvent = self.open_account
        # setting button
        self.setting_btn.mousePressEvent = self.open_settings
        # bat su kien nut all
        self.all_btn.clicked.connect(
            lambda: self.load_current_notes(self.getAllNotes())
        )
        # bat su kien cho button search
        self.search_btn.clicked.connect(self.search_notes)
        # load current notes
        self.load_current_notes(self.getAllNotes())
        self.load_tag_list()

    def getAllNotes(self):
        notes_by_currentUser = self.noteController.get_note_list()
        return [
            notes_by_currentUser[i : i + self.row_size]
            for i in range(0, len(notes_by_currentUser), self.row_size)
        ]

    def load_current_notes(self, noteList):
        # clear old data
        self.clear_layout(self.gridLayout)
        for row in range(len(noteList)):
            for col in range(len(noteList[row])):
                note = noteList[row][col]
                note_widget = NoteItem(self.root_ui_path, note, self.userEmail)
                self.gridLayout.addWidget(note_widget, row, col)
                #  Set alignment to top-left for the NoteItem widget
                self.gridLayout.setAlignment(
                    note_widget,
                    Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
                )

    def clear_layout(self, layout):
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            nested_layout = item.layout()
            if nested_layout is not None:
                self.clear_layout(nested_layout)

    def load_tag_list(self):
        for tag in self.noteController.get_tag_list():
            tag_item = TagItem(tag)
            # bat su kien cho tag
            tag_item.clicked.connect(
                lambda checked, t=tag: self.filter_by_tag_clicked(t)
            )
            self.tag_list.addWidget(tag_item)

    def filter_by_tag_clicked(self, tag):
        notes_by_tag = self.noteController.search_by_tag(tag)
        noteList = [
            notes_by_tag[i : i + self.row_size]
            for i in range(0, len(notes_by_tag), self.row_size)
        ]
        self.load_current_notes(noteList)

    def search_notes(self):
        # get search input data
        search_input = self.search_input.text()
        search_list = self.noteController.search_by_title(search_input)
        search_list = [
            search_list[i : i + self.row_size]
            for i in range(0, len(search_list), self.row_size)
        ]
        self.load_current_notes(search_list)

    def create_note(self, event):
        if not hasattr(self, "edit_window"):
            self.edit_window = Edit(
                self.root_ui_path, "Create note", currentEmail=self.userEmail
            )
        self.edit_window.show()
        self.load_current_notes(self.getAllNotes())
        self.load_tag_list()

    def open_settings(self, event):
        # han che mo nhieu cua so trong 1 app
        if not hasattr(self, "settings_window"):
            self.settings_window = Setting(self.root_ui_path)
        self.settings_window.show()

    def open_account(self, event):
        if not hasattr(self, "account_window"):
            self.account_window = Account(self.root_ui_path)
        self.account_window.show()
