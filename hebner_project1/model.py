import sqlite3
import sqlite3 as sql
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


class TopTv:

    def __init__(self, id, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count):
        self.id = id
        self.rank = rank
        self.title = title
        self.full_title = full_title
        self.year = year
        self.crew = crew
        self.imdb_rating = imdb_rating
        self.imdb_rating_count = imdb_rating_count

    @classmethod
    def add(cls, id, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count):
        query = "INSERT INTO TopShows(id, rank,  title, full_title, year, crew, imdb_rating, imdb_rating_count)" \
                " VALUES (?,?,?,?,?,?,?,?)"
        conn, cursor = open_db('imdb.sqlite')
        conn.execute(query, (id, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count))
        conn.commit()


class UserRatings:

    def __init__(self, imdbID, total_rating, total_rating_votes, rating_10, rating_10_votes, rating_9, rating_9_votes,
                 rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, rating_5, rating_5_votes,
                 rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, rating_1,
                 rating_1_votes):
        self.imdbID = imdbID
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
    def __add__(self, imdbID, total_rating, total_rating_votes, rating_10, rating_10_votes, rating_9, rating_9_votes,
                 rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, rating_5, rating_5_votes,
                 rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, rating_1,
                 rating_1_votes):
        query = "INSERT INTO User_Ratings(imdbID, total_rating, total_rating_votes, rating_10, rating_10_votes, " \
                "rating_9, rating_9_votes,rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, "\
                "rating_5, rating_5_votes,rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, "\
                "rating_1,rating_1_votes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        conn, cursor = open_db('imdb.sqlite')
        conn.execute(query, (imdbID, total_rating, total_rating_votes, rating_10, rating_10_votes, rating_9, rating_9_votes,
                 rating_8, rating_8_votes, rating_7, rating_7_votes, rating_6, rating_6_votes, rating_5, rating_5_votes,
                 rating_4, rating_4_votes, rating_3, rating_3_votes, rating_2, rating_2_votes, rating_1,
                 rating_1_votes))
        conn.commit()
