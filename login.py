# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QLineEdit
from remote_server import RemoteServer
from all_citys import Ui_AllCitys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(432, 200)
        Dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        self.Dialog = Dialog
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 40, 12))
        self.label.setObjectName("label")
        # self.label.setFont()
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 40, 12))
        self.label_2.setObjectName("label_2")
        self.acount_error_label = QLabel(Dialog)
        self.acount_error_label.setGeometry(QtCore.QRect(90, 88, 100, 20))
        self.acount_error_label.setObjectName("acount_error_label")
        self.acount_error_label.setStyleSheet("color:#e3bd96")
        self.acount_error_label.hide()
        self.password_error_label = QLabel(Dialog)
        self.password_error_label.setGeometry(QtCore.QRect(90, 130, 100, 20))
        self.password_error_label.setObjectName("password_error_label")
        self.password_error_label.setStyleSheet("color:#e3bd96")
        self.password_error_label.hide()
        self.account = QLineEdit(Dialog)
        self.account.setGeometry(QtCore.QRect(90, 60, 250, 20))
        self.account.setObjectName("account")
        self.password = QLineEdit(Dialog)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(90, 110, 250, 20))
        self.password.setObjectName("password")
        self.login_button = QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(180, 150, 81, 31))
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet("background-color: #e76464;color: #ffffff;");

        self.retranslateUi(Dialog)
        self.login_button.clicked.connect(self.login)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户登录"))
        self.label.setText(_translate("Dialog", "账户"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.acount_error_label.setText(_translate("Dialog", "*账户错误"))
        self.password_error_label.setText(_translate("Dialog", "*密码错误"))
        self.login_button.setText(_translate("Dialog", "登陆"))

    def login(self):
        account_input = self.account.text()
        passwd_input = self.password.text()
        # remote = RemoteServer("http://mcenterv2.thd99.com/V2/pythonApi/sign")
        # status, message = remote.login(account_input, passwd_input)
        if not True:
            print(message)
            self.acount_error_label.setText("* 账户错误")
            self.password_error_label.setText("* 密码错误")
            self.acount_error_label.setVisible(True)
            self.password_error_label.setVisible(True)
        else:
            self.Dialog.close()
            citys = QDialog()
            citys_ui = Ui_AllCitys()
            citys_ui.setupUi(citys)
            citys.exec()


