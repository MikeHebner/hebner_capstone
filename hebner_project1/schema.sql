DROP TABLE IF EXISTS TopShows;
CREATE TABLE TopShows
(
  imDb_ID INT NOT NULL,
  rank INT NOT NULL,
  title VARCHAR NOT NULL,
  full_title VARCHAR NOT NULL,
  year VARCHAR(4) NOT NULL,
  crew VARCHAR NOT NULL,
  imdb_rating VARCHAR NOT NULL,
  imdb_rating_count INT NOT NULL,
  PRIMARY KEY (imDb_ID)
);

DROP TABLE IF EXISTS User_Ratings;
CREATE TABLE User_Ratings
(
  imDb_ID VARCHAR NOT NULL,
  total_rating INT NOT NULL,
  total_rating_votes INT NOT NULL,
  rating_10 INT NOT NULL,
  rating_10_votes INT NOT NULL,
  rating_9 INT NOT NULL,
  rating_9_votes INT NOT NULL,
  rating_8 INT NOT NULL,
  rating_8_votes INT NOT NULL,
  rating_7 INT NOT NULL,
  rating_7_votes INT NOT NULL,
  rating_6 INT NOT NULL,
  rating_6_votes INT NOT NULL,
  rating_5 INT NOT NULL,
  rating_5_votes INT NOT NULL,
  rating_4 INT NOT NULL,
  rating_4_votes INT NOT NULL,
  rating_3 INT NOT NULL,
  rating_3_votes INT NOT NULL,
  rating_2 INT NOT NULL,
  rating_2_votes INT NOT NULL,
  rating_1 INT NOT NULL,
  rating_1_votes INT NOT NULL,
  FOREIGN KEY (imDb_ID) REFERENCES TopShows(imDb_ID)
);

DROP TABLE IF EXISTS popular_shows;
CREATE TABLE popular_shows
(
    imDb_ID VARCHAR NOT NULL,
    rank INT NOT NULL,
    rank_up_down INT NOT NULL,
    title INT NOT NULL,
    full_title INT NOT NULL,
    year INT NOT NULL,
    image VARCHAR NOT NULL,
    crew VARCHAR NOT NULL,
    imDb_rating VARCHAR NOT NULL,
    imDb_rating_count VARCHAR NOT NULL,
    PRIMARY KEY (imDb_ID)
);

DROP TABLE IF EXISTS popular_movies;
CREATE TABLE popular_movies
(
    imDb_ID VARCHAR NOT NULL,
    rank INT NOT NULL,
    rank_up_down INT NOT NULL,
    title VARCHAR NOT NULL,
    full_title VARCHAR NOT NULL,
    year INT NOT NULL,
    image VARCHAR NOT NULL,
    crew VARCHAR NOT NULL,
    imDb_rating VARCHAR NOT NULL,
    imDb_rating_count VARCHAR NOT NULL,
    PRIMARY KEY (imDb_ID)
);

DROP TABLE IF EXISTS big_movers_movies;
CREATE TABLE big_movers_movies
(
    imDb_ID VARCHAR NOT NULL,
    rank INT NOT NULL,
    rank_up_down INT NOT NULL,
    PRIMARY KEY (imDb_ID),
    FOREIGN KEY (imDb_ID) REFERENCES popular_movies(imDb_ID)
)
