import sys, os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

from views.home import Home
from views.register import Register
from controllers.user_controller import UserController


class Login(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path
        uic.loadUi(root_ui_path + "Login.ui", self)
        self.setWindowTitle("Log In")
        self.B_Login.mousePressEvent = self.check_login
        self.B_Click.mousePressEvent = self.open_register
        # khai bao user controller
        self.userController = UserController()

    def check_login(self, event):
        username = self.B_Username.text()
        password = self.B_Password.text()

        if not (username and password):
            self.show_error("Vui lòng điền đầy đủ thông tin đăng nhập!")
            return
        else:
            # kiem tra tai khoan trong he thong
            # lay ra user co username giong
            currentUser = self.userController.search_by_username(username)
            if not currentUser:
                self.show_error("Tài khoản chưa tồn tại, vui lòng đăng ký!")
                return
            else:
                # dung username -> kiem tra mat khau
                # chi lay user dau tien trong danh sach loc duoc
                if currentUser["password"] == password:
                    # dang nhap thanh cong
                    # open main window
                    home = Home(self.root_ui_path, currentUser["email"])
                    home.show()
                    self.close()
                else:
                    # sai mat khau
                    self.show_error("Thông tin đăng nhập không chính xác!")
                    return

    def open_register(self, event):
        register = Register(self.root_ui_path)
        register.show()
        self.close()

    def show_error(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.addButton(QMessageBox.StandardButton.Ok)
        ok_button.setStyleSheet("background-color: #598896;")
        msg_box.exec()
