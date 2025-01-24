import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic
from views.login import Login

if __name__ == "__main__":
    root_ui_path = "MyTien/app/ui/"
    app = QApplication(sys.argv)
    login_window = Login(root_ui_path)
    login_window.show()
    sys.exit(app.exec())
