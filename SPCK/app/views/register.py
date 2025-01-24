import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

from views.home import Home  # Import the Home class
from controllers.user_controller import UserController
from models.user import User


class Register(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path  # Add root_ui_path attribute
        uic.loadUi(
            root_ui_path + "register.ui", self
        )  # Load UI dynamically with root_ui_path
        self.setWindowTitle("Register")
        self.B_Continue.mousePressEvent = self.check_register
        self.B_Click1.mousePressEvent = self.open_login
        # khai bao user controller
        self.userController = UserController()

    def check_register(self, event):
        email = self.B_Email.text()
        username = self.B_Username.text()
        password = self.B_Password.text()

        # Validation for email, username, and password
        if not email:
            self.show_error("Vui lòng nhập email!")
            return
        if not username:
            self.show_error("Vui lòng nhập tên đăng nhập!")
            return
        if len(username) < 5:
            self.show_error("Tên đăng nhập phải có ít nhất 5 ký tự!")
            return
        if not username.isalnum():
            self.show_error(
                "Tên đăng nhập không được chứa ký tự đặc biệt hoặc khoảng trắng!"
            )
            return
        if not password:
            self.show_error("Vui lòng nhập mật khẩu!")
            return
        if len(password) < 6 or len(password) > 10:
            self.show_error("Mật khẩu phải có độ dài từ 6 đến 10 ký tự!")
            return
        # kiem tra username co bi trung khong ----
        if self.userController.search_by_username(username):
            self.show_error(
                "Username đã tồn tại, vui lòng nhập lại hoặc chuyển sang đăng nhập!"
            )
            return
        else:
            # tao moi user -> luu vao data json
            newUser = User(username=username, password=password, email=email, avatar="")
            self.userController.add_user(user=newUser)
            # Instantiate and show the Home window directly without storing it as an attribute
            home = Home(self.root_ui_path)
            home.show()
            self.close()

    def open_login(self, event):
        from views.login import Login

        # Instantiate and show the Login window directly without storing it as an attribute
        login_window = Login(self.root_ui_path)
        login_window.show()
        self.close()

    def show_error(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.addButton(QMessageBox.StandardButton.Ok)
        ok_button.setStyleSheet("background-color: #598896;")
        msg_box.exec()
