import os
import sys

# Add the project root (or a directory containing 'spck') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from models.user import User
from DAO import DAO


class UserController:
    def __init__(self):
        self.__user_list = []
        self.__generate_user_list()

    # private methods (only this class can use)
    def __generate_user_list(self):
        # get from data json
        self.__user_list = DAO.load_json_data("user")

    def __save_user_list(self):
        # save list for file data
        DAO.write_json_data(self.__user_list, "user")

    def get_user_list(self):
        return self.__user_list

    # read -------------------------
    def search_by_username(self, username):
        # tra ve 1 user co user tuong ung
        for user in self.__user_list:
            if user["username"] == username:
                return user
        print("Khong co user tuong ung")
        return None

    def search_by_email(self, email):
        # tra ve 1 user co email tuong ung
        for user in self.__user_list:
            if user["email"] == email:
                return user
        print("Khong co user tuong ung")
        return None

    # update ------------------------
    def add_user(self, user: User):
        # them user moi vao cuoi cung cua danh sach
        self.__user_list.append(user.getDict())
        # thay doi du lieu cho file json
        self.__save_user_list()

    def update_user(self, user: User):
        # chinh sua = username
        for i in range(len(self.__user_list)):
            if self.__user_list[i]["username"] == user.username:
                self.__user_list[i] = user  # cap nhat
                # thay doi du lieu cho file json
                self.__save_user_list()
                return

    # delete ----------------------------
    def delete_user_by_username(self, user):
        for i in range(len(self.__user_list)):
            if self.__user_list[i]["username"] == user.username:
                self.__user_list.remove(self.__user_list[i])  # xoa trong list
                # thay doi du lieu cho file json
                self.__save_user_list()
                return

    # sort -------------------------------------
    def sort_by_username(self):
        # function 1 dong -> lambda
        get_username = lambda user: user["username"]
        # key yeu cau truyen vao 1 ham tra ve username khi loc qua tung user
        return self.__user_list.sort(key=get_username)

    def sort_by_email(self):
        # sap xep theo thuoc tinh email (tu A -> Z), key la tieu chi de so sanh
        self.__user_list.sort(key=lambda user: user.email)
        
