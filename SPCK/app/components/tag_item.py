from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize


class TagItem(QPushButton):
    def __init__(self, text:str, color=""):
        super().__init__()

        # Set maximum size (100 width, maximum height)
        # self.setMaximumSize(QSize(16777215, 50))  # Width 100px, height maximum

        # Set the button text
        self.setText(text.upper())
