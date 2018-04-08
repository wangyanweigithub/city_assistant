import os
import shutil
import psutil
from PyQt5.Qt import Qt
from PyQt5 import QtWidgets
from setting import PathHelp


class ScroLable(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(ScroLable, self).__init__(parent)
        self.setStyleSheet("QLabel{ background: #EEE8CD}")
        self.setAlignment(Qt.AlignCenter)

    def mouseReleaseEvent(self, QMouseEvent):
        if self.choosed:
            self.setStyleSheet("QLabel{background: #e76464;}")
        else:
            self.setStyleSheet("QLabel{ background: #EEE8CD}")


class ButtonLabel(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super(ButtonLabel, self).__init__(parent)
        self.choosed = False
        # self.setStyleSheet("QLabel{ border: 1px solid  #ff0000;background: gray}")
        self.setStyleSheet("QLabel{ background: #EEE8CD}")
        self.setAlignment(Qt.AlignCenter)

    def mouseReleaseEvent(self, QMouseEvent):
        self.choosed = not self.choosed
        if self.choosed:
            self.setStyleSheet("QLabel{background: #e76464;}")
        else:
            self.setStyleSheet("QLabel{ background: #EEE8CD}")

def get_pid_finish(pid):
    pids = list(map(lambda x:x.pid, psutil.process_iter()))
    if pid not in pids:
        return True
    return False

def get_all_community(city, area):
    path = os.path.join(PathHelp.tencent_result, city, area)
    return os.listdir(path)

def dele_files_from_scrapy_result(files, city, area, path=PathHelp.tencent_result):
    for file in files:
        file_path = os.path.join(path, city, area, file)
        if os.path.isdir:
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)