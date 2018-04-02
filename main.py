import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from login import Ui_Dialog
from all_citys_a import Ui_AllCitys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()

    sys.exit(app.exec_())
