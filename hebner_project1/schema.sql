DROP TABLE IF EXISTS top_shows;
CREATE TABLE top_shows
(
  imdb_id INT NOT NULL,
  rank INT NOT NULL,
  title VARCHAR NOT NULL,
  full_title VARCHAR NOT NULL,
  year VARCHAR(4) NOT NULL,
  crew VARCHAR NOT NULL,
  imdb_rating VARCHAR NOT NULL,
  imdb_rating_count INT NOT NULL,
  PRIMARY KEY (imdb_id)
);

DROP TABLE IF EXISTS top_movies;
CREATE TABLE top_movies
(
  imdb_id INT NOT NULL,
  rank INT NOT NULL,
  title VARCHAR NOT NULL,
  full_title VARCHAR NOT NULL,
  year VARCHAR(4) NOT NULL,
  crew VARCHAR NOT NULL,
  imdb_rating VARCHAR NOT NULL,
  imdb_rating_count INT NOT NULL,
  PRIMARY KEY (imdb_id)
);

DROP TABLE IF EXISTS tv_user_ratings;
CREATE TABLE tv_user_ratings
(
  imdb_id VARCHAR NOT NULL,
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
  FOREIGN KEY (imdb_id) REFERENCES top_shows(imdb_id)
);

DROP TABLE IF EXISTS movie_user_ratings;
CREATE TABLE movie_user_ratings
(
  imdb_id VARCHAR NOT NULL,
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
  FOREIGN KEY (imdb_id) REFERENCES popular_movies(imdb_id)
);

DROP TABLE IF EXISTS popular_shows;
CREATE TABLE popular_shows
(
    imdb_id VARCHAR NOT NULL,
    rank INT NOT NULL,
    rank_up_down INT NOT NULL,
    title INT NOT NULL,
    full_title INT NOT NULL,
    year INT NOT NULL,
    image VARCHAR NOT NULL,
    crew VARCHAR NOT NULL,
    imdb_rating VARCHAR NOT NULL,
    imdb_rating_count VARCHAR NOT NULL,
    PRIMARY KEY (imdb_id)
);

DROP TABLE IF EXISTS popular_movies;
CREATE TABLE popular_movies
(
    imdb_id VARCHAR NOT NULL,
    rank INT NOT NULL,
    rank_up_down INT NOT NULL,
    title VARCHAR NOT NULL,
    full_title VARCHAR NOT NULL,
    year INT NOT NULL,
    image VARCHAR NOT NULL,
    crew VARCHAR NOT NULL,
    imdb_rating VARCHAR NOT NULL,
    imdb_rating_count VARCHAR NOT NULL,
    PRIMARY KEY (imdb_id)
);

DROP TABLE IF EXISTS big_movers_movies;
CREATE TABLE big_movers_movies
(
    imdb_id VARCHAR NOT NULL,
    rank INT NOT NULL,
    rank_up_down INT NOT NULL,
    PRIMARY KEY (imdb_id),
    FOREIGN KEY (imdb_id) REFERENCES popular_movies(imdb_id)
)
