import sys
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, \
    QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as Canvas

from hebner_project1 import p1s1_hebner as controller
from hebner_project1 import model


def update_db():
    controller.update_all()
    print("UPDATED")


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.pie = None
        self.setWindowTitle('IMDB DATABASE')
        self.setGeometry(300, 100, 400, 300)
        self.data_window = None
        self.setup_window()
        self.show()

    def setup_window(self):
        exit_button = QPushButton("EXIT", self)
        exit_button.move(50, 200)
        exit_button.pressed.connect(QApplication.instance().quit)

        update_button = QPushButton("UPDATE DATABASE", self)
        update_button.move(50, 50)
        update_button.clicked.connect(update_db)

        data_button = QPushButton("TABLES", self)
        data_button.move(50, 100)
        data_button.clicked.connect(self.visualize)

        compare_button = QPushButton("PIES", self)
        compare_button.move(50, 150)
        compare_button.pressed.connect(self.open_pie)

        compare_button_label = QLabel('Click here to compare up/down movers\n'
                                      'from Popular Movies and Show', self)
        compare_button_label.move(25, 710)

    def visualize(self):
        self.data_window = DataSelectWindow()

    def open_pie(self):
        self.pie = PieGraphWindow()
        self.pie.show()


class DataSelectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)
        self.last_col = None
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
        exit_button.pressed.connect(self.close_it)

        info_label = QLabel('Click on any table entry to see\n'
                            'distribution of user ratings.', self)
        info_label.move(200, 525)

    def close_it(self):
        self.close()

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

        elif category == 'MOST POPULAR':
            if media_type == 'MOVIES':
                table_name = 'popular_movies'
                data = model.PopularMedia.get_all_ordered_by('imdb.sqlite', table_name, order_by, sort)
                self.creat_table_popular(data)
            else:
                table_name = 'popular_shows'
                data = model.PopularMedia.get_all_ordered_by('imdb.sqlite', table_name, order_by, sort)
                self.creat_table_popular(data)
        else:
            print("ERROR: wrong parameter")
            return "ERROR: wrong parameter"

    # imdb_id is hidden in last column of both tables
    def creat_table_popular(self, data):
        self.table.setHorizontalHeaderLabels("TITLE;YEAR;RANK;RANK +/-;RATING;RATING COUNT;imdb_id".split(";"))
        self.table.setRowCount(len(data))
        self.last_col = 6
        for i in range(len(data)):
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        # self.table.setColumnHidden(6, True)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def creat_table_top250(self, data):
        self.table.setHorizontalHeaderLabels("TITLE;YEAR;RANK;RATING;RATING COUNT;imdb_id".split(";"))
        self.table.setRowCount(len(data))
        self.last_col = 5
        for i in range(len(data)):
            for j in range(6):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        # self.table.setColumnHidden(5, True)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def cell_clicked(self, row, _):
        if self.last_col == 5:
            print(self.last_col)

            # self.rating_window = RatingWindow(self.table.item(row, 5).text(), self.table.item(row, 0).text())
            self.rating_window = GraphWindow(self.table.item(row, 5).text(), self.table.item(row, 0).text())
            self.rating_window.show()
        if self.last_col == 6:
            print(self.last_col)
            # self.rating_window = RatingWindow(self.table.item(row, 5).text(), self.table.item(row, 0).text())
            self.rating_window = GraphWindow(self.table.item(row, 6).text(), self.table.item(row, 0).text())
            self.rating_window.show()

        return self.table.item(row, 5).text()  # returns imdb_id of clicked cell


class UserReviewCanvas(Canvas):
    def __init__(self, parent, imdb_id, title):
        self.imdb_id = imdb_id
        self.title = title
        controller.load_user_ratings(self.imdb_id)
        user_ratings = model.UserRatings.get_by_id('imdb.sqlite', self.imdb_id)
        y_axis = [user_ratings['rating_1_votes'], user_ratings['rating_2_votes'],
                  user_ratings['rating_3_votes'], user_ratings['rating_4_votes'],
                  user_ratings['rating_5_votes'], user_ratings['rating_6_votes'],
                  user_ratings['rating_7_votes'], user_ratings['rating_8_votes'],
                  user_ratings['rating_9_votes'], user_ratings['rating_10_votes']]
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot()
        super().__init__(self.figure)
        self.setParent(parent)
        self.ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y_axis)
        self.ax.set_ylabel('Votes')
        self.ax.set_xlabel('# of stars given')
        self.ax.grid()


class GraphWindow(QWidget):
    def __init__(self, imdb_id, title):
        super().__init__()
        self.imdb_id = imdb_id
        self.title = title

        self.resize(800, 800)
        self.chart = UserReviewCanvas(self, self.imdb_id, self.title)


class PieGraph(Canvas):
    def __init__(self, parent):
        self.movie_data = []
        self.show_data = []
        self.movie_data.append(model.PopularMedia.count_movers_by_dir('imdb.sqlite', 'popular_movies', '+'))
        self.movie_data.append(model.PopularMedia.count_movers_by_dir('imdb.sqlite', 'popular_movies', '-'))
        self.show_data.append(model.PopularMedia.count_movers_by_dir('imdb.sqlite', 'popular_shows', '+'))
        self.show_data.append(model.PopularMedia.count_movers_by_dir('imdb.sqlite', 'popular_shows', '-'))
        self.labels = ['UP', 'DOWN']
        self.figure, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 10))
        super().__init__(self.figure)
        self.setParent(parent)
        self.ax1.pie(self.movie_data, labels=self.labels, autopct='%1.1f%%')
        self.ax1.axis('equal')
        self.ax1.set_title('Popular Movies')
        self.ax1.grid()
        self.ax2.pie(self.show_data, labels=self.labels, autopct='%1.1f%%')
        self.ax2.axis('equal')
        self.ax2.set_title('Popular Shows')
        self.ax2.grid()


class PieGraphWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 800)
        self.graph = PieGraph(self)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
