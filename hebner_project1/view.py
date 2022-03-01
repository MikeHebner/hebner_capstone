import sys

import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, \
    QLabel
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
        self.data_window = DataSelectWindow()


class DataSelectWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.rating_window = None
        self.setWindowTitle('DATA SELECTION')
        self.setGeometry(300, 100, 1200, 800)
        self.setup_window()
        self.show()

    def setup_window(self):
        self.combo4 = QComboBox(self)
        self.combo3 = QComboBox(self)
        self.combo2 = QComboBox(self)
        self.combo1 = QComboBox(self)

        self.table = QTableWidget(self)
        self.table.move(200, 0)
        self.table.setMinimumSize(1000, 500)
        self.table.setColumnCount(6)
        self.table.cellClicked.connect(self.cell_clicked)

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
                data = model.TopMovie.get_all('imdb.sqlite')
                self.creat_table_top250(data)

            else:
                data = model.TopTv.get_all('imdb.sqlite')
                self.creat_table_top250(data)

        else:
            if media_type == 'MOVIES':
                table_name = 'popular_movies'
            else:
                table_name = 'popular_shows'
            data = model.PopularMedia.get_all_ordered_by('imdb.sqlite', table_name, order_by, sort)
            self.creat_table_popular(data)

    # imdb_id is hidden in last column of both tables
    def creat_table_popular(self, data):
        self.table.setHorizontalHeaderLabels("TITLE;YEAR;RANK;RANK +/-;RATING;RATING COUNT;imdb_id".split(";"))
        self.table.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        self.table.setColumnHidden(4, True)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def creat_table_top250(self, data):
        self.table.setHorizontalHeaderLabels("TITLE;YEAR;RANK;RATING;RATING COUNT;imdb_id".split(";"))
        self.table.setRowCount(len(data))

        for i in range(len(data)):
            for j in range(6):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        self.table.setColumnHidden(5, True)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def cell_clicked(self, row, _):
        self.rating_window = RatingWindow(self.table.item(row, 5).text(), self.table.item(row, 0).text())
        self.rating_window.show()
        return self.table.item(row, 5).text()  # returns imdb_id of clicked cell


class RatingWindow(QWidget):
    def __init__(self, imdb_id, title):
        super().__init__()
        self.graph = None
        self.imdb_id = imdb_id
        self.title = title
        self.plot = None
        self.setWindowTitle('USER RATING')
        self.setGeometry(300, 100, 800, 800)
        self.setup_window()

    def setup_window(self):
        controller.load_user_ratings(self.imdb_id)
        user_ratings = model.UserRatings.get_by_id('imdb.sqlite', self.imdb_id)
        y_axis = [user_ratings['rating_1_votes'], user_ratings['rating_2_votes'],
                  user_ratings['rating_3_votes'], user_ratings['rating_4_votes'],
                  user_ratings['rating_5_votes'], user_ratings['rating_6_votes'],
                  user_ratings['rating_7_votes'], user_ratings['rating_8_votes'],
                  user_ratings['rating_9_votes'], user_ratings['rating_10_votes']]

        title = "USER RATINGS FOR {}".format(self.title)
        print(title)
        self.plot = pg.plot(title=title)

        y = user_ratings['total_rating_votes']
        self.graph = pg.BarGraphItem(x=range(1, 11), height=y_axis, width=0.5)

        self.plot.addItem(self.graph)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
