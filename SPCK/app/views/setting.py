from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys

# from views.register import Register  # Import the Register class
# from views.home import Home  # Import the Home class


class Setting(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        uic.loadUi(root_ui_path + "setting.ui", self)  # Load the UI file
        self.setWindowTitle("Settings")
        self.B_LogOut.mousePressEvent = self.log_out  # Connect logout button

    def log_out(self, event):
        from views.login import Login  # Import the Login class

        # Create and show the Login window directly
        login_window = Login()  # Instantiate Login
        login_window.show()
        self.close()  # Close the settings window
