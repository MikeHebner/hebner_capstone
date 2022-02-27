import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QPushButton
from hebner_project1 import p1s1_hebner as controller
from hebner_project1 import model


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IMDB DATABASE')
        self.setGeometry(300, 100, 400, 300)
        self.data_window = None
        self.setup_window()
        self.show()

    def setup_window(self):
        exit_button = QPushButton("EXIT", self)
        exit_button.move(50, 150)
        exit_button.pressed.connect(QApplication.instance().quit)

        update_button = QPushButton("UPDATE DATABASE", self)
        update_button.move(50, 50)
        update_button.clicked.connect(self.update_db)

        data_button = QPushButton("VISUALIZE", self)
        data_button.move(50, 100)
        data_button.clicked.connect(self.visualize)

    def update_db(self):
        controller.update_all()
        print("UPDATED")

    def visualize(self):
        self.data_window = DataWindow()


class DataWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DATA SELECTION')
        self.setGeometry(300, 100, 400, 300)
        self.setup_window()
        self.show()

    def setup_window(self):
        self.combo4 = QComboBox(self)
        self.combo3 = QComboBox(self)
        self.combo2 = QComboBox(self)
        self.combo1 = QComboBox(self)

        self.combo1.addItem("MOVIES")
        self.combo1.addItem("TV")
        self.combo1.move(50, 40)

        self.combo2.addItem("TOP 250")
        self.combo2.addItem("MOST POPULAR")
        self.combo2.move(50, 65)

        self.combo3.addItem("RANK_UP_DOWN")
        self.combo3.addItem("RANK")
        self.combo3.move(50, 90)


        self.combo4.addItem("ASC")
        self.combo4.addItem("DESC")
        self.combo4.move(50, 115)

        submit_button = QPushButton("SUBMIT", self)
        submit_button.move(100, 140)
        submit_button.clicked.connect(self.get_params)

        exit_button = QPushButton("EXIT", self)
        exit_button.move(25, 140)
        exit_button.pressed.connect(QApplication.instance().quit)

    def get_params(self):
        media_type = self.combo1.currentText()
        category = self.combo2.currentText()
        order_by = self.combo3.currentText()
        order_by = order_by.lower()
        sort = self.combo4.currentText()
        if category == 'TOP 250':
            if media_type == 'MOVIES':
                model.TopMovie.get_all('imdb.sqlite')
            else:
                model.TopTv.get_all('imdb.sqlite')
        else:
            if media_type == 'MOVIES':
                table_name = 'popular_movies'
            else:
                table_name = 'popular_shows'
            model.PopularMedia.get_all_ordered_by('imdb.sqlite', table_name, order_by, sort)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
