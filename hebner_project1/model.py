import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def runSQLfile(fileName, dbName):
    file = open(fileName, 'r')
    sqlFile = file.read()
    file.close()
    conn, cursor = open_db(dbName)
    cmds = sqlFile.split(';')
    for cmd in cmds:
        conn.execute(cmd)


class TopTv:

    def __init__(self, imDbId, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count):
        self.imDbId = imDbId
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
    def add(cls, dbName, imDbId, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count):
        query = "INSERT INTO TopShows(imDbId, rank,  title, full_title, year, crew, imdb_rating, imdb_rating_count)" \
                " VALUES (?,?,?,?,?,?,?,?)"
        conn, cursor = open_db(dbName)
        conn.execute(query, (imDbId, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count))
        conn.commit()

    @classmethod
    def delete(cls, dbName, imDbId):
        q = "SELECT COUNT(imDbId) FROM TopShows WHERE imDbId=(?)"
        conn, cursor = open_db(dbName)
        response = conn.execute(q, (imDbId,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM TopShows WHERE imDbId=(?)"
            conn.execute(q, (imDbId,))

            conn.commit()
            return 1
        else:
            return 0

    @classmethod
    def get(cls, dbName, imDbId):
        q = "SELECT * FROM TopShows WHERE imDbId=(?)"
        conn, cursor = open_db(dbName)
        response = conn.execute(q, (imDbId,))
        return response.fetchall()


class UserRatings:

    def __init__(self, imDbId, total_rating, total_rating_votes, rating_10, rating_10_votes, rating_9, rating_9_votes,
                 rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, rating_5, rating_5_votes,
                 rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, rating_1,
                 rating_1_votes):
        self.imDbId = imDbId
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
    def add(cls, dbName, imDbId, total_rating, total_rating_votes, rating_10, rating_10_votes, rating_9, rating_9_votes,
            rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, rating_5, rating_5_votes,
            rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, rating_1,
            rating_1_votes):
        query = "INSERT INTO User_Ratings(imDbId, total_rating, total_rating_votes, rating_10, rating_10_votes," \
                "rating_9, rating_9_votes,rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6," \
                " rating_6_votes, rating_5, rating_5_votes,rating_4, rating_4_votes, rating_3, rating_3_votes," \
                " rating_2, rating_2_votes, rating_1,rating_1_votes)" \
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        conn, cursor = open_db(dbName)
        conn.execute(query,
                     (imDbId, total_rating, total_rating_votes, rating_10, rating_10_votes, rating_9, rating_9_votes,
                      rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, rating_5,
                      rating_5_votes,
                      rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, rating_1,
                      rating_1_votes))
        conn.commit()

    @classmethod
    def delete(cls, dbName, imDbId):
        q = "SELECT COUNT(imDbId) FROM User_Ratings WHERE imDbId=(?)"
        conn, cursor = open_db(dbName)
        response = conn.execute(q, (imDbId,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM User_Ratings WHERE imDbId=(?)"
            conn.execute(q, (imDbId,))
            conn.commit()
            return 1
        else:
            return 0


# One class to cover  both TV shows and Movies
class PopularMedia:

    def __init__(self, imDbId, rank, rankUpDown, title, fullTitle, year, image, crew, imDbRating, imDbRatingCount):
        self.imDbId = imDbId
        self.rank = rank
        self.rankUpDown = rankUpDown
        self.title = title
        self.fullTitle = fullTitle
        self.year = year
        self.image = image
        self.crew = crew
        self.imDbRating = imDbRating
        self.imDbRatingCount = imDbRatingCount

    @classmethod
    def add(cls, dbName, tableName, imDbId, rank, rankUpDown, title, full_title, year, image, crew, imDbRating,
            imDbRatingCount):
        query = 'INSERT INTO {}(imDbId, rank, rankUpDown, title, full_title, year, image, crew,' \
                ' imDbRating,imDbRatingCount) VALUES (?,?,?,?,?,?,?,?,?,?)'.format(tableName)
        conn, cursor = open_db(dbName)
        conn.execute(query,
                     (imDbId, rank, rankUpDown, title, full_title, year, image, crew, imDbRating,
                      imDbRatingCount))
        conn.commit()

    # direction = '+' or '-'; + corresponds to positive change, - to negative change
    # amount = how many entries you want returned; 5 = 5 movies
    # Returns the movie(s) with the largest rankUpDown change
    @classmethod
    def getBigMover(cls, dbName, tableName, direction, amount):
        if direction == "+":
            direction = ' rankUpDown DESC'
        else:
            direction = 'rankUpDown'
        query = 'SELECT * FROM {} ORDER BY {} LIMIT {}'.format(tableName, direction, amount)
        conn, cursor = open_db(dbName)
        response = conn.execute(query)
        return response.fetchall()

    @classmethod
    def addBigMovers(cls, dbName, tableName, imDbId, rank, rankUpDown):
        query = 'INSERT INTO {}(imDbId, rank, rankUpDown) VALUES (?,?,?)'.format(tableName)
        conn, cursor = open_db(dbName)
        conn.execute(query, (imDbId, rank, rankUpDown))
        conn.commit()

