# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from ChatWindow import Ui_ChatWindow
import sqlite3
import hashlib
import time


class ChatUI(QMainWindow, Ui_ChatWindow):
    def __init__(self, parent=None):
        super(ChatUI, self).__init__(parent)
        self.setupUi(self)


class Ui_LoginWindow(object):

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(700, 457)
        LoginWindow.setFixedSize(700, 457)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        LoginWindow.setFont(font)
        self.OKButton = QtWidgets.QPushButton(LoginWindow)
        self.OKButton.setGeometry(QtCore.QRect(160, 390, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.OKButton.setFont(font)
        self.OKButton.setObjectName("OKButton")
        self.QuitButton = QtWidgets.QPushButton(LoginWindow)
        self.QuitButton.setGeometry(QtCore.QRect(400, 390, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QuitButton.setFont(font)
        self.QuitButton.setObjectName("QuitButton")
        self.Label1 = QtWidgets.QLabel(LoginWindow)
        self.Label1.setGeometry(QtCore.QRect(98, 30, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.Label1.setFont(font)
        self.Label1.setTextFormat(QtCore.Qt.AutoText)
        self.Label1.setAlignment(QtCore.Qt.AlignCenter)
        self.Label1.setObjectName("Label1")
        self.Label2 = QtWidgets.QLabel(LoginWindow)
        self.Label2.setGeometry(QtCore.QRect(160, 110, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Label2.setFont(font)
        self.Label2.setTextFormat(QtCore.Qt.AutoText)
        self.Label2.setAlignment(QtCore.Qt.AlignCenter)
        self.Label2.setObjectName("Label2")
        self.UserText = QtWidgets.QLineEdit(LoginWindow)
        self.UserText.setGeometry(QtCore.QRect(180, 180, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UserText.setFont(font)
        self.UserText.setObjectName("UserText")
        self.PasswordText = QtWidgets.QLineEdit(LoginWindow)
        self.PasswordText.setGeometry(QtCore.QRect(180, 260, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PasswordText.setFont(font)
        self.PasswordText.setObjectName("PasswordText")
        self.UserLabel = QtWidgets.QLabel(LoginWindow)
        self.UserLabel.setGeometry(QtCore.QRect(60, 186, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UserLabel.setFont(font)
        self.UserLabel.setObjectName("UserLabel")
        self.PasswordLabel = QtWidgets.QLabel(LoginWindow)
        self.PasswordLabel.setGeometry(QtCore.QRect(30, 264, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.RegisterButton = QtWidgets.QPushButton(LoginWindow)
        self.RegisterButton.setGeometry(QtCore.QRect(530, 200, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setObjectName("RegisterButton")
        self.AboutButton = QtWidgets.QPushButton(LoginWindow)
        self.AboutButton.setGeometry(QtCore.QRect(530, 250, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutButton.setFont(font)
        self.AboutButton.setObjectName("AboutButton")

        self.TargetButton = QtWidgets.QPushButton(LoginWindow)  # 隐藏按钮 用来触发
        self.TargetButton.hide()
        self.TargetButton.setObjectName("TargetButton")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        # 设置密码样式
        self.PasswordText.setEchoMode(QtWidgets.QLineEdit.Password)
        # 绑定事件
        self.OKButton.clicked.connect(self.Login)
        self.RegisterButton.clicked.connect(self.Register)
        self.AboutButton.clicked.connect(self.About)
        self.QuitButton.clicked.connect(self.close)
        # 初始化数据库
        self.InitSQLite()

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.OKButton.setText(_translate("LoginWindow", "OK"))
        self.QuitButton.setText(_translate("LoginWindow", "Quit"))
        self.Label1.setText(_translate("LoginWindow", "Computer Network"))
        self.Label2.setText(_translate("LoginWindow", "Lab 2 Socket Programming"))
        self.UserLabel.setText(_translate("LoginWindow", "User"))
        self.PasswordLabel.setText(_translate("LoginWindow", "Password"))
        self.RegisterButton.setText(_translate("LoginWindow", "Register"))
        self.AboutButton.setText(_translate("LoginWindow", "About"))

    # 绑定Button的四个函数login、register、about、quit(自带)

    def About(self):
        QtWidgets.QMessageBox.information(self, "About", "Author: Yan Xinyu Data: 2022-10-1")

    def InitSQLite(self):
        conn = sqlite3.connect("Data.db")  # 在此文件所在的文件夹打开或创建数据库文件
        c = conn.cursor()  # 设置游标
        # 创建表USER
        c.execute('''CREATE TABLE IF NOT EXISTS USER
               (NAME        TEXT    NOT NULL,
                PASSWORD    TEXT    NOT NULL);
               ''')
        conn.commit()
        conn.close()

    def Login(self):
        conn = sqlite3.connect("Data.db")  # 在此文件所在的文件夹打开或创建数据库文件
        cur = conn.cursor()
        UserName = self.UserText.text()
        UserPassword = self.PasswordText.text()
        if UserName == "" or UserPassword == "":
            QtWidgets.QMessageBox.warning(self, "Warning", "Please Enter Your Name and Password!")
        else:
            cur.execute("""SELECT PASSWORD FROM USER WHERE NAME = ?""", (UserName,))
            password = cur.fetchall()
            if not password:
                QtWidgets.QMessageBox.warning(self, "Warning", "This User Has Not Registered Yet!")
            else:
                if self.hash(UserPassword) == password[0][0]:
                    QtWidgets.QMessageBox.information(self, "Informing", "Login!")
                    time.sleep(0.5)  # 休眠，达到过渡效果
                    self.ChatWindow = ChatUI()
                    self.ChatWindow.show()
                    self.hide()
                else:
                    QtWidgets.QMessageBox.warning(self, "Warning", "Error, Please Check Your Password")

    def Register(self):
        conn = sqlite3.connect("Data.db")  # 在此文件所在的文件夹打开或创建数据库文件
        cur = conn.cursor()
        UserName = self.UserText.text()
        UserPassword = self.PasswordText.text()
        if UserName == "" or UserPassword == "":
            QtWidgets.QMessageBox.warning(self, "Warning", "Please Enter Your Name and Password!")
        else:
            UserPassword = self.hash(UserPassword)
            cur.execute("""SELECT PASSWORD FROM USER WHERE NAME = ?""", (UserName,))
            if not cur.fetchall():
                cur.execute("""INSERT INTO USER VALUES (?,?)""", (UserName, UserPassword))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Informing", "Registered!")
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "The User Has Already Existed!")

    @staticmethod
    def hash(src):
        src = (src + "1145141919810").encode("utf-8")  # 恶臭的Key
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()