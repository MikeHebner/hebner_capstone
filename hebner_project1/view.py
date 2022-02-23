import sys
from PyQt5.QtWidgets import QDialog, QApplication
from main_window import Ui_Form
from hebner_project1 import p1s1_hebner as controller


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.update_all)
        self.ui.pushButton.clicked.connect(self.close)
        self.show()

    def update_all(self):
        controller.update_all()
        print('Clicked')


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
