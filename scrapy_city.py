# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrapy_city.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from search_result import Ui_Result_Srcapy
from tools import get_pid_finish
from PyQt5.QtCore import QTimer
from tools import add_city_area_item

class Ui_Scrapy(object):
    def setupUi(self, Form, pid, city, area):
        Form.setObjectName("Form")
        Form.resize(652, 561)
        self.city = city
        self.area = area
        self.form = Form
        self.scrapy_pid = pid
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 761, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QFrame{ background-color:#e76464;}")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 5, 81, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 11, 54, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(185, 12, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(300, 15, 54, 12))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 70, 81, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 72, 81, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.add_city_area_item()
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 40, 761, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 160, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 160, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 160, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(170, 290, 300, 23))
        # self.progressBar.setProperty("value", 10)
        self.progressBar.setMaximum(0);
        self.progressBar.setMinimum(0);
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(210, 260, 141, 21))
        self.label_6.setObjectName("label_6")

        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.start()
        self.timer.timeout.connect(self.check_scrapy_finished)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "楼盘助手1.0 |"))
        self.label_2.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "12345678901"))
        self.label_4.setText(_translate("Form", "切换账户"))
        self.label_5.setText(_translate("Form", "---------" * 50))
        self.pushButton.setText(_translate("Form", "全部"))
        self.pushButton_2.setText(_translate("Form", "腾讯房产"))
        self.pushButton_3.setText(_translate("Form", "房天下"))
        self.pushButton_4.setText(_translate("Form", "透明房产"))
        self.label_6.setText(_translate("Form", "加载数据中"))

    def check_scrapy_finished(self):
        pid_finshed = get_pid_finish(self.scrapy_pid)
        if pid_finshed:
            self.scrapy_complete()

    def scrapy_complete(self):
        self.form.close()
        scrapy_result = QtWidgets.QDialog()
        scrapy_ui = Ui_Result_Srcapy()
        scrapy_ui.setupUi(scrapy_result, self.city, self.area_name)
        scrapy_result.exec()

    def add_city_area_item(self):
        area_name = add_city_area_item(self, self.city)
        self.area_name = area_name




