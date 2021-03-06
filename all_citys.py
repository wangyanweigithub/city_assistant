# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import string
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from setting import Common
from PyQt5.QtCore import pyqtSignal
from area import Ui_Area
from tools import get_earas
from PyQt5.QtWidgets import QMessageBox


class MyLabel(QtWidgets.QLabel):
    city_clicked = pyqtSignal(str)

    def __init__(self, parent=None, main_window=None):
        super(MyLabel, self).__init__(parent)
        self.city_clicked.connect(main_window.choose_city)

    def mouseReleaseEvent(self, e):
        self.city_clicked.emit(self.text())




class CitysShow(object):

    def gen_citys(self, window):
        Form = window.Form
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(50, 131, 798, 800))
        # self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("QScrollArea{border:none;}")
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 800, 3500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.verticalScrollBar().setValue(500)


        group_box_high = 0
        num_per_line = 7
        for k, v in Common.citys.items():
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setStyleSheet("QGroupBox{border:none;}")
            groupBox.setGeometry(QtCore.QRect(50, group_box_high, 791, 320))
            groupBox.setObjectName("groupBox" + k)
            setattr(self, "groupBox" + k, groupBox)
            group_box_high += 160

            city_index = QtWidgets.QLabel(getattr(self, "groupBox" + k))
            city_index.setGeometry(QtCore.QRect(15, 30, 28, 31))
            city_index.setObjectName("cityIndex_" + k)
            city_index.setStyleSheet("QLabel{color:#e76464;}")
            city_index.setFont(QFont("Arial", 20, QFont.Normal))
            setattr(self, "cityIndex" + k, city_index)
            for num, name in enumerate(v):
                city_label = MyLabel(getattr(self, "groupBox" + k, None), window)
                city_label.setGeometry(
                    QtCore.QRect(70 + num % num_per_line * 100, 30 + num // num_per_line * 30, 200, 20))
                city_label.setObjectName(k + "_city_" + str(num))
                setattr(self, k + "_city_" + str(num), city_label)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        for k, v in Common.citys.items():
            city_index_label = getattr(self, "cityIndex" + k)
            city_index_label.setText(_translate("From", k))
            for num, name in enumerate(v):
                city_label = getattr(self, k + "_city_" + str(num))
                city_label.setText(_translate("From", name))


class Ui_AllCitys(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 800)
        # Form.setStyleSheet("")
        self.Form = Form
        self.title = QtWidgets.QFrame(Form)
        self.title.setGeometry(QtCore.QRect(0, 0, 871, 41))
        self.title.setStyleSheet("QFrame#title{ background-color:#e76464;}")
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.title)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_2 = QtWidgets.QLabel(self.title)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 51, 41))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_9 = QtWidgets.QLabel(self.title)
        self.label_9.setGeometry(QtCore.QRect(160, 0, 81, 41))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("QLabel{color:#ffffff;}")
        self.label_10 = QtWidgets.QLabel(self.title)
        self.label_10.setGeometry(QtCore.QRect(240, 0, 54, 41))
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_line = QtWidgets.QLabel(Form)
        self.label_line.setGeometry(QtCore.QRect(70, 100, 800, 12))
        self.label_line.setObjectName("label_line")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 121, 16))
        self.label_4.setObjectName("label_4")

        self.citys_show = CitysShow()
        self.citys_show.gen_citys(self)

        for i, letter in enumerate(string.ascii_uppercase):
            letter_label = QtWidgets.QLabel(Form)
            letter_label.setGeometry(QtCore.QRect(200 + i * 25, 110, 16, 16))
            letter_label.setObjectName("letter_"+letter)
            letter_label.setFont(QFont("Arial", 10, QFont.Normal))
            letter_label.setStyleSheet(" QLabel{border-radius:15px;background:gray;}")
            setattr(self, "letter_" + letter, letter_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " 楼盘助手1.0 |"))
        self.label_2.setText(_translate("Form", " 用户名："))
        self.label_9.setText(_translate("Form", "12345678910"))
        self.label_10.setText(_translate("Form", "切换用户"))
        self.label_3.setText(_translate("Form", "选择城市"))
        self.label_line.setText(_translate("Form", "-" * 130))
        self.label_4.setText(_translate("Form", "按拼音部首字母选择:"))
        for letter in string.ascii_uppercase:
            letter_label = getattr(self, 'letter_'+letter)
            letter_label.setText(_translate("From", letter))

        self.citys_show.retranslateUi(Form)

    def choose_city(self, city):
        if not get_earas(city):
            reply = QMessageBox.warning(self.Form,
                                        "warning", "暂时不支持这个城市", QMessageBox.Yes | QMessageBox.No)
        else:
            self.Form.close()
            area = QtWidgets.QDialog()
            area_ui = Ui_Area()
            area_ui.setupUi(area, city)
            area.exec()

