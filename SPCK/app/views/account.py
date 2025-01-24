from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class Account(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path  # Add root_ui_path attribute
        uic.loadUi(root_ui_path + "account.ui", self)  # Use root_ui_path to load the UI
        self.setWindowTitle("Account")
        self.B_SaveChange.mousePressEvent = self.saveChange

    def saveChange(self, event):
        # Assuming you have instances for `register`, `main`, and `savechange`, you should close them properly.
        # For example, the instances should be accessible here, either passed into the class or set earlier.
        
        # Check if other windows (main, register) are part of this class or global
        if hasattr(self, 'register'):
            self.register.close()  # Close the register window if it exists
        
        if hasattr(self, 'main'):
            self.main.close()  # Close the main window if it exists

        self.close()  # Close the current Account window
