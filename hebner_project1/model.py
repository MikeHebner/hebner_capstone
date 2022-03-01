import sqlite3
from typing import Tuple


def open_db(file_name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(file_name)
    cursor = db_connection.cursor()
    return db_connection, cursor


def run_sql_file(file_name, db_name):
    file = open(file_name, 'r')
    sql_file = file.read()
    file.close()
    conn, cursor = open_db(db_name)
    cmds = sql_file.split(';')
    for cmd in cmds:
        conn.execute(cmd)


class TopTv:

    def __init__(self, imdb_id, rank, title, full_title, year,
                 crew, imdb_rating, imdb_rating_count):
        self.imdb_id = imdb_id
        self.rank = rank
        self.title = title
        self.full_title = full_title
        self.year = year
        self.crew = crew
        self.imdb_rating = imdb_rating
        self.imdb_rating_count = imdb_rating_count

    def __str__(self):
        return "%s - %s (%s)" % (self.rank, self.title, self.year)

    @classmethod
    def add(cls, db_name, imdb_id, rank, title, full_title, year,
            crew, imdb_rating, imdb_rating_count):
        query = "INSERT INTO top_shows(imdb_id, rank,  title," \
                " full_title, year, crew, imdb_rating, imdb_rating_count)" \
                " VALUES (?,?,?,?,?,?,?,?)"
        conn, cursor = open_db(db_name)
        conn.execute(query, (imdb_id, rank, title, full_title, year,
                             crew, imdb_rating, imdb_rating_count))
        conn.commit()

    @classmethod
    def delete(cls, db_name, imdb_id):
        q = "SELECT COUNT(imdb_id) FROM top_shows WHERE imdb_id=(?)"
        conn, cursor = open_db(db_name)
        response = conn.execute(q, (imdb_id,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM top_shows WHERE imdb_id=(?)"
            conn.execute(q, (imdb_id,))

            conn.commit()
            return 1

    @classmethod
    def get(cls, db_name, imdb_id):
        q = "SELECT * FROM top_shows WHERE imdb_id=(?)"
        conn, cursor = open_db(db_name)
        response = conn.execute(q, (imdb_id,))
        return response.fetchall()

    @classmethod
    def get_all(cls, db_name):
        query = 'SELECT rank, title, year, imdb_rating, imdb_rating_count, imdb_id FROM top_shows'
        conn, cursor = open_db(db_name)
        response = conn.execute(query)
        return response.fetchall()


class TopMovie:

    def __init__(self, imdb_id, rank, title, full_title, year,
                 crew, imdb_rating, imdb_rating_count):
        self.imdb_id = imdb_id
        self.rank = rank
        self.title = title
        self.full_title = full_title
        self.year = year
        self.crew = crew
        self.imdb_rating = imdb_rating
        self.imdb_rating_count = imdb_rating_count

    def __str__(self):
        return "%s - %s (%s)" % (self.rank, self.title, self.year)

    @classmethod
    def add(cls, db_name, imdb_id, rank, title, full_title, year,
            crew, imdb_rating, imdb_rating_count):
        query = "INSERT INTO top_movies(imdb_id, rank,  title," \
                " full_title, year, crew, imdb_rating, imdb_rating_count)" \
                " VALUES (?,?,?,?,?,?,?,?)"
        conn, cursor = open_db(db_name)
        conn.execute(query, (imdb_id, rank, title, full_title, year,
                             crew, imdb_rating, imdb_rating_count))
        conn.commit()

    @classmethod
    def delete(cls, db_name, imdb_id):
        q = "SELECT COUNT(imdb_id) FROM top_movies WHERE imdb_id=(?)"
        conn, cursor = open_db(db_name)
        response = conn.execute(q, (imdb_id,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM top_movies WHERE imdb_id=(?)"
            conn.execute(q, (imdb_id,))

            conn.commit()
            return 1
        else:
            return 0

    @classmethod
    def get(cls, db_name, imdb_id):
        q = "SELECT * FROM top_movies WHERE imdb_id=(?)"
        conn, cursor = open_db(db_name)
        response = conn.execute(q, (imdb_id,))
        return response.fetchall()

    @classmethod
    def get_all(cls, db_name):
        query = 'SELECT rank, title, year, imdb_rating, imdb_rating_count, imdb_id FROM top_movies'
        conn, cursor = open_db(db_name)
        response = conn.execute(query)
        return response.fetchall()


class UserRatings:

    def __init__(self, imdb_id, total_rating, total_rating_votes, rating_10,
                 rating_10_votes, rating_9, rating_9_votes, rating_8,
                 rating_8_votes, rating_7, rating_7_votes, rating_6,
                 rating_6_votes, rating_5, rating_5_votes, rating_4,
                 rating_4_votes, rating_3, rating_3_votes, rating_2,
                 rating_2_votes, rating_1, rating_1_votes):
        self.imdb_id = imdb_id
        self.total_rating = total_rating
        self.total_rating_votes = total_rating_votes
        self.rating_10 = rating_10
        self.rating_10_votes = rating_10_votes
        self.rating_9 = rating_9
        self.rating_9_votes = rating_9_votes
        self.rating_8 = rating_8
        self.rating_8_votes = rating_8_votes
        self.rating_7 = rating_7
        self.rating_7_votes = rating_7_votes
        self.rating_6 = rating_6
        self.rating_6_votes = rating_6_votes
        self.rating_5 = rating_5
        self.rating_5_votes = rating_5_votes
        self.rating_4 = rating_4
        self.rating_4_votes = rating_4_votes
        self.rating_3 = rating_3
        self.rating_3_votes = rating_3_votes
        self.rating_2 = rating_2
        self.rating_2_votes = rating_2_votes
        self.rating_1 = rating_1
        self.rating_1_votes = rating_1_votes

    @classmethod
    def add(cls, db_name, imdb_id, table_name, total_rating, total_rating_votes,
            rating_10, rating_10_votes, rating_9, rating_9_votes,
            rating_8, rating_8_votes, rating_7, rating_7_votes,
            rating_6, rating_6_votes, rating_5, rating_5_votes,
            rating_4, rating_4_votes, rating_3, rating_3_votes,
            rating_2, rating_2_votes, rating_1,
            rating_1_votes):
        query = "INSERT INTO {}(imdb_id, total_rating," \
                " total_rating_votes, rating_10, rating_10_votes," \
                "rating_9, rating_9_votes,rating_8, rating_8_votes," \
                " rating_7, rating_7_votes, rating_6," \
                " rating_6_votes, rating_5, rating_5_votes,rating_4," \
                " rating_4_votes, rating_3, rating_3_votes," \
                " rating_2, rating_2_votes, rating_1,rating_1_votes)" \
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?," \
                "?,?,?,?,?)".format(table_name)
        conn, cursor = open_db(db_name)
        conn.execute(query,
                     (imdb_id, total_rating, total_rating_votes, rating_10,
                      rating_10_votes, rating_9, rating_9_votes,
                      rating_8, rating_8_votes, rating_7, rating_7_votes,
                      rating_6, rating_6_votes, rating_5,
                      rating_5_votes, rating_4, rating_4_votes, rating_3,
                      rating_3_votes, rating_2, rating_2_votes, rating_1,
                      rating_1_votes))
        conn.commit()

    @classmethod
    def delete(cls, db_name, table_name, imdb_id):
        q = "SELECT COUNT(imdb_id) FROM {} WHERE imdb_id=(?)".format(table_name)
        conn, cursor = open_db(db_name)
        response = conn.execute(q, (imdb_id,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM {} WHERE imdb_id=(?)".format(table_name)
            conn.execute(q, (imdb_id,))
            conn.commit()
            return 1
        else:
            return 0


# One class to cover  both TV shows and Movies
class PopularMedia:

    def __init__(self, imdb_id, rank, rank_up_down, title,
                 full_title, year, image, crew, imdb_rating, imdb_rating_count):
        self.imdb_id = imdb_id
        self.rank = rank
        self.rank_up_down = rank_up_down
        self.title = title
        self.full_title = full_title
        self.year = year
        self.image = image
        self.crew = crew
        self.imdb_rating = imdb_rating
        self.imdb_rating_count = imdb_rating_count

    @classmethod
    def add(cls, db_name, table_name, imdb_id, rank,
            rank_up_down, title, full_title, year, image, crew, imdb_rating,
            imdb_rating_count):
        query = 'INSERT INTO {}(imdb_id, rank, rank_up_down,' \
                ' title, full_title, year, image, crew,' \
                ' imdb_rating,imdb_rating_count)' \
                ' VALUES (?,?,?,?,?,?,?,?,?,?)'.format(table_name)
        conn, cursor = open_db(db_name)
        conn.execute(query,
                     (imdb_id, rank, rank_up_down, title, full_title,
                      year, image, crew, imdb_rating,
                      imdb_rating_count))
        conn.commit()

    # direction = '+' or '-'; + corresponds to positive change, - to negative change
    # amount = how many entries you want returned; 5 = 5 movies
    # Returns the movie(s) with the largest rank_up_down change
    @classmethod
    def get_big_mover(cls, db_name, table_name, direction, amount):
        if direction == "+":
            direction = ' rank_up_down DESC'
        else:
            direction = 'rank_up_down'
        query = 'SELECT * FROM {} ORDER BY {} LIMIT {}'.format(table_name, direction, amount)
        conn, cursor = open_db(db_name)
        response = conn.execute(query)
        return response.fetchall()

    @classmethod
    def add_big_movers(cls, db_name, table_name, imdb_id, rank, rank_up_down):
        query = 'INSERT INTO {}(imdb_id, rank, rank_up_down) VALUES (?,?,?)'.format(table_name)
        conn, cursor = open_db(db_name)
        conn.execute(query, (imdb_id, rank, rank_up_down))
        conn.commit()

    @classmethod
    def get_all_ordered_by(cls, db_name, table_name, order_by, sort):
        query = 'SELECT rank, rank_up_down, title, year, imdb_rating, imdb_rating_count, imdb_id FROM {} ORDER BY {} {}'.format(table_name, order_by, sort)
        print(query)
        conn, cursor = open_db(db_name)
        response = conn.execute(query)
        return response.fetchall()

