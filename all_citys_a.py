# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_citys.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import string
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from setting import Common

class Ui_AllCitys(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 800)
        Form.setStyleSheet("QFrame#title{background:rgb(225, 78, 48);}")
        # Form.setWindowFlags(Qt.FramelessWindowHint)
        self.title = QtWidgets.QFrame(Form)
        self.title.setGeometry(QtCore.QRect(0, 0, 871, 41))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.title)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.title)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.title)
        self.label_9.setGeometry(QtCore.QRect(160, 10, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.title)
        self.label_10.setGeometry(QtCore.QRect(240, 10, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 121, 16))
        self.label_4.setObjectName("label_4")

        for i, letter in enumerate(string.ascii_uppercase):
            letter_label = QtWidgets.QLabel(Form)
            letter_label.setGeometry(QtCore.QRect(220 + i * 25, 110, 16, 16))
            letter_label.setObjectName("letter_"+letter)
            setattr(self, "letter_" + letter, letter_label)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 160, 16, 16))
        self.label_6.setObjectName("label_6")
        # for i in


        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 160, 431, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 561, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 150, 561, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "   楼盘助手1.0"))
        self.label_2.setText(_translate("Form", "用户名："))
        self.label_9.setText(_translate("Form", "12345678910"))
        self.label_10.setText(_translate("Form", "切换用户"))
        self.label_3.setText(_translate("Form", "选择城市"))
        self.label_4.setText(_translate("Form", "按拼音部首字母选择:"))
        for letter in string.ascii_uppercase:
            letter_label = getattr(self, 'letter_'+letter)
            letter_label.setText(_translate("From", letter))
        self.label_6.setText(_translate("Form", "A"))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.label_8.setText(_translate("Form", "TextLabel"))

