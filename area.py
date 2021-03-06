# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'area.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from subprocess import Popen
from PyQt5 import QtCore, QtWidgets
from setting import Common, PathHelp
from scrapy_city import Ui_Scrapy
from tools import add_city_area_item


class Ui_Area(object):
    def setupUi(self, Form, city):
        Form.setObjectName("Form")
        Form.resize(796, 563)
        self.city = city
        self.form = Form
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QFrame#frame{ background-color:#e76464;}")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 15, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(164, 15, 81, 10))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(280, 14, 54, 12))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 69, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 60, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 83, 781, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 150, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 150, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 150, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_5 = QtWidgets.QPushButton(Form)
        # self.pushButton_5.setGeometry(QtCore.QRect(60, 250, 131, 41))
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{ background-color:#e76464; color:#ffffff}")

        self.pushButton_2.clicked.connect(lambda: self.choose_source(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.choose_source(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.choose_source(self.pushButton_4.text()))

        self.add_city_area_item()
        self.comboBox_2.activated['QString'].connect(self.on_activated)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add_city_area_item(self):
        area_name = add_city_area_item(self, self.city)
        self.area_name = area_name

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " 楼盘助手1.0 |"))
        self.label_2.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "12345678910"))
        self.label_4.setText(_translate("Form", "切换用户"))

        self.label_5.setText(_translate("Form", "---------------------------------------------------------------------------------------------------------------------------------"))
        self.pushButton_2.setText(_translate("Form", "腾讯房产"))
        self.pushButton_3.setText(_translate("Form", "房天下"))
        self.pushButton_4.setText(_translate("Form", "透明售房"))
        # self.pushButton_5.setText(_translate("Form", "确定"))

    def choose_source(self, source):
        print(source)
        if source in Common.data_source:
            self.start_scrapy(source)

    def start_scrapy(self, source):
        command = "python start.py %s %s" % (self.city, self.area_name)
        # command = "python a.py %s %s" % (self.city, self.area_name)
        print(command)
        code = Popen(command, cwd=PathHelp.tencent_path)
        if code.returncode:
            raise("Scrapy Wrong")
        print("pid is ", code.pid)

        try:
            self.form.close()
            self.wati_scrapy = QtWidgets.QDialog()
            scrapy_ui = Ui_Scrapy()
            scrapy_ui.setupUi(self.wati_scrapy, code.pid, self.city, self.area_name)
            self.wati_scrapy.exec()
        except Exception as e:
            print(e)

    def on_activated(self, area_name):
        self.area_name = area_name



