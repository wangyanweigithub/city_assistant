# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_result.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from tools import get_all_community, ButtonLabel, dele_files_from_scrapy_result, add_city_area_item


class Ui_Result_Srcapy(object):
    def setupUi(self, Form, city, area):
        Form.setObjectName("Form")
        Form.resize(1100, 900)
        self.form = Form
        self.city = city
        self.area = area
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1100, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QFrame{ background-color:#e76464;}")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 21))
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 14, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(181, 13, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(274, 13, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 82, 773, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(45, 50, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(185, 50, 91, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.add_city_area_item()
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(214, 110, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(394, 110, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(304, 110, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(484, 110, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(53, 177, 81, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(123, 177, 351, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(487, 177, 40, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(529, 177, 31, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(551, 177, 40, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(603, 177, 40, 21))
        self.label_10.setObjectName("label_10")

        commus = self.get_communitys()
        num_per_line = 4
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 210, 1000, 600))
        self.scrollArea.setStyleSheet("QScrollArea{border:none;}")
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 970, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        for num, name in enumerate(commus):
            commu_label = ButtonLabel(self.scrollAreaWidgetContents)
            commu_label.setGeometry(
                QtCore.QRect(40 + num % num_per_line * 210, 10 + num // num_per_line * 60, 200, 50))
            commu_label.setObjectName("commu" + str(num))
            setattr(self, "commu" + str(num), commu_label)
        self.label_8.setText(str(len(commus)))
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 830, 120, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.if_dele_files)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "楼盘助手1.0 |"))
        self.label_2.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "12345678900"))
        self.label_4.setText(_translate("Form", "切换用户"))
        self.label_5.setText(_translate("Form", "--" * 100))
        self.pushButton.setText(_translate("Form", "全部"))
        self.pushButton_2.setText(_translate("Form", "房天下"))
        self.pushButton_3.setText(_translate("Form", "腾讯房产"))
        self.pushButton_5.setText(_translate("Form", "透明房产"))
        self.label_6.setText(_translate("Form", "搜索结果"))
        self.label_7.setText(_translate("Form", "搜索到"))
        # self.label_8.setText(_translate("Form", "15"))
        self.label_9.setText(_translate("Form", "条信息"))
        self.label_10.setText(_translate("Form", "重置"))
        for num, name in enumerate(self.get_communitys()):
            getattr(self, "commu" + str(num)).setText(_translate("Form", name))
        self.pushButton_4.setText(_translate("Form", "确认"))

    def get_communitys(self):
        return get_all_community(self.city, self.area)

    def if_dele_files(self):
        reply = QtWidgets.QMessageBox.question(self.form, "提示", "是否删除多余数据?",
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            print("delete")
            self.form.close()
            self.dele_files()
            new_window = QtWidgets.QDialog()
            self.setupUi(new_window, self.city, self.area)
            new_window.exec()
        else:
            print("Not dele file")

    def dele_files(self):
        dele_files = []
        for num, name in enumerate(self.get_communitys()):
            if not getattr(self, "commu" + str(num)).choosed:
                dele_files.append(getattr(self, "commu" + str(num)).text())

        print(dele_files)
        dele_files_from_scrapy_result(dele_files, self.city, self.area)

    def add_city_area_item(self):
        add_city_area_item(self, self.city)
        self.comboBox_2.setCurrentText(self.area)

