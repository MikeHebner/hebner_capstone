DROP TABLE IF EXISTS TopShows;
CREATE TABLE TopShows
(
  imDbId INT NOT NULL,
  rank INT NOT NULL,
  title VARCHAR NOT NULL,
  full_title VARCHAR NOT NULL,
  year VARCHAR(4) NOT NULL,
  crew VARCHAR NOT NULL,
  imdb_rating VARCHAR NOT NULL,
  imdb_rating_count INT NOT NULL,
  PRIMARY KEY (imDbId)
);

DROP TABLE IF EXISTS User_Ratings;
CREATE TABLE User_Ratings
(
  imDbId VARCHAR NOT NULL,
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
  FOREIGN KEY (imdbId) REFERENCES TopShows(imDbId)
);

DROP TABLE IF EXISTS popular_shows;
CREATE TABLE popular_shows
(
    imDbId VARCHAR NOT NULL,
    rank INT NOT NULL,
    rankUpDown INT NOT NULL,
    title INT NOT NULL,
    full_title INT NOT NULL,
    year INT NOT NULL,
    image VARCHAR NOT NULL,
    crew VARCHAR NOT NULL,
    imDbRating VARCHAR NOT NULL,
    imDbRatingCount VARCHAR NOT NULL,
    PRIMARY KEY (imDbId)
);

DROP TABLE IF EXISTS popular_movies;
CREATE TABLE popular_movies
(
    imDbId VARCHAR NOT NULL,
    rank INT NOT NULL,
    rankUpDown INT NOT NULL,
    title VARCHAR NOT NULL,
    full_title VARCHAR NOT NULL,
    year INT NOT NULL,
    image VARCHAR NOT NULL,
    crew VARCHAR NOT NULL,
    imDbRating VARCHAR NOT NULL,
    imDbRatingCount VARCHAR NOT NULL,
    PRIMARY KEY (imDbId)
);
