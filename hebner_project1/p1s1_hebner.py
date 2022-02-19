# Michael Hebner
import json
import secrets
import requests

import model


# add comment to test workflow


# Gets the top 250 TV shows and saves the json response to the project directory
# I did this to cut down on the api request
def get_top_tv():
    url = 'https://imdb-api.com/en/API/Top250TVs/{}'.format(secrets.API_KEY, )
    response = requests.get(url)
    data = response.json()
    with open('topTv.json', 'w') as file:
        # Erase contents and dump updated list
        file.truncate(0)
        json.dump(data, file)
    # Only returns len(data) for test.py purposes
    return len(data)


# Gets the top 250 Movies and saves the json response to the project directory
# I did this to cut down on the api request
def get_top_movies():
    url = 'https://imdb-api.com/en/API/Top250Moviess/{}'.format(secrets.API_KEY, )
    response = requests.get(url)
    data = response.json()
    with open('topMovies.json', 'w') as file:
        # Erase contents and dump updated list
        file.truncate(0)
        json.dump(data, file)
    # Only returns len(data) for test.py purposes
    return len(data)


# opens the main text file and appends the list of top 250 shows to it
def put_top_tv():
    file = open("topTv.json")
    data = json.loads(file.read())
    file.close()
    file = open("dataMain.txt", "a")
    file.write("TOP 250 TV SHOWS:\n")
    for i in data['items']:
        rank = i['rank']
        title = i['title']
        year = i['year']
        line = rank + " -- " + title + " (" + year + ") ,\n"
        file.write(line)


# Function takes one id (IMDB id)
# Formats the returned rating into a readable format
# Appends it to the main text file
def get_user_rating_data(id):
    url = "https://imdb-api.com/en/API/UserRatings/{}/{}".format(secrets.API_KEY, id)
    response = requests.get(url)
    data = response.json()
    title = data['title']
    ratings = data['ratings']
    file = open("dataMain.txt", "a")
    file.write(title + "\n")
    for i in ratings:
        line = "RATING:{} PERCENT:{} VOTES:{}\n".format(i['rating'], i['percent'], i['votes'])
        file.write(line)
    file.write("\n")
    file.close()


# I will delete above function once grading for sprint 1 is complete.
# This function is doing the same, just for database instead of txt file.
def get_user_rating_data_v2(id):
    url = "https://imdb-api.com/en/API/UserRatings/{}/{}".format(secrets.API_KEY, id)
    response = requests.get(url)
    data = response.json()
    imdb_id = data['imDbId']
    total_rating = data['totalRating']
    total_rating_votes = data['totalRatingVotes']
    # Each is a row in rating_i
    rating_percents = []
    # Each is a row in rating_i_votes
    rating_votes = []
    ratings = data['ratings']
    # Ran into an issue of a top show having no ratings returned.
    # If this happens, dummy data is added to those rows.
    if len(ratings) == 0:
        for i in range(10):
            percent = 10 - i
            votes = 10 - i
            rating_percents.append(percent)
            rating_votes.append(votes)
    else:
        for i in ratings:
            percent = i['percent']
            percent = percent[:-1]
            votes = i['votes']
            rating_percents.append(percent)
            rating_votes.append(votes)
    return imdb_id, total_rating, total_rating_votes, rating_percents, rating_votes


# Returns imdb id from rank off of top 250 shows or by name
def get_id(not_id):
    # get id from ranking
    if type(not_id) is int:
        rank = not_id
        # index of each is its rank minus one.
        # 1 ranked is in 0th index
        index = rank - 1
        top_tv = open('topTv.json')
        top_tv = json.loads(top_tv.read())
        return top_tv['items'][index]['id']
    # get id from (str) name
    if type(not_id) is str:
        name = not_id
        url = "https://imdb-api.com/en/API/SearchSeries/{}/{}".format(secrets.API_KEY, name)
        response = requests.get(url)
        data = response.json()
        return data["results"][0]["id"]
    else:
        return "INVALID INPUT"


def load_top_tv():
    file = open("topTv.json")
    data = json.loads(file.read())
    file.close()
    for i in data['items']:
        imdb_id = i['id']
        rank = i['rank']
        title = i['title']
        full_title = i['fullTitle']
        year = i['year']
        crew = i['crew']
        imdb_rating = i['imDbRating']
        imdb_rating_count = i['imDbRatingCount']
        model.TopTv.add('imdb.sqlite', imdb_id, rank, title, full_title, year,
                        crew, imdb_rating, imdb_rating_count)


def load_top_movie():
    file = open("topMovies.json")
    data = json.loads(file.read())
    file.close()
    for i in data['items']:
        imdb_id = i['id']
        rank = i['rank']
        title = i['title']
        full_title = i['fullTitle']
        year = i['year']
        crew = i['crew']
        imdb_rating = i['imDbRating']
        imdb_rating_count = i['imDbRatingCount']
        model.TopMovie.add('imdb.sqlite', imdb_id, rank, title, full_title, year,
                           crew, imdb_rating, imdb_rating_count)


# Takes the imdbID as input.
# Loads the User rating for given input into database.
# type = movie or tv
def load_user_ratings(id, type):
    imdb_id, total_rating, total_rating_votes, rating_percents, rating_votes \
        = get_user_rating_data_v2(id)
    if type == 'movie':
        model.UserRatings.add('imdb.sqlite', imdb_id, 'movie_user_ratings', total_rating,
                              total_rating_votes, rating_percents[0], rating_votes[0],
                              rating_percents[1], rating_votes[1], rating_percents[2],
                              rating_votes[2], rating_percents[3], rating_votes[3],
                              rating_percents[4], rating_votes[4], rating_percents[5],
                              rating_votes[5], rating_percents[6], rating_votes[6],
                              rating_percents[7], rating_votes[7], rating_percents[8],
                              rating_votes[8], rating_percents[9], rating_votes[9])

    elif type == 'tv':
        model.UserRatings.add('imdb.sqlite', imdb_id, 'tv_user_ratings', total_rating,
                              total_rating_votes, rating_percents[0], rating_votes[0],
                              rating_percents[1], rating_votes[1], rating_percents[2],
                              rating_votes[2], rating_percents[3], rating_votes[3],
                              rating_percents[4], rating_votes[4], rating_percents[5],
                              rating_votes[5], rating_percents[6], rating_votes[6],
                              rating_percents[7], rating_votes[7], rating_percents[8],
                              rating_votes[8], rating_percents[9], rating_votes[9])
    else:
        return "INVALID INPUT"


# input = tv or movie
def get_popular_media(media_type):
    if media_type == 'movie':
        query = 'https://imdb-api.com/en/API/MostPopularMovies/{}'.format(secrets.API_KEY)
        response = requests.get(query)
        return response.json()
    if media_type == 'tv':
        query = 'https://imdb-api.com/en/API/MostPopularTVs/{}'.format(secrets.API_KEY)
        response = requests.get(query)
        return response.json()
    else:
        return "ERROR: {} = INVALID INPUT--MUST BE 'tv' or 'movie".format(media_type)


def load_popular_media(db_name, table_name, data):
    for i in data['items']:
        imdb_id = i['id']
        rank = i['rank']
        rank_up_down = i['rankUpDown']
        title = i['title']
        full_title = i['fullTitle']
        year = i['year']
        image = i['image']
        crew = i['crew']
        imdb_rating = i['imDbRating']
        imdb_rating_count = i['imDbRatingCount']
        model.PopularMedia.add(db_name, table_name, imdb_id, rank, rank_up_down, title, full_title,
                               year, image, crew, imdb_rating, imdb_rating_count)


def main():
    # Drop and Create Tables
    model.run_sql_file('schema.sql', 'imdb.sqlite')
    # Raw input for userRatings
    raw_input = [1, 50, 100, 200, "Wheel of Time"]
    get_top_tv()
    load_top_tv()
    for i in raw_input:
        imdb_id = get_id(i)
        load_user_ratings(imdb_id, 'tv')
    movie_data = get_popular_media('movie')
    tv_data = get_popular_media('tv')
    load_popular_media('imdb.sqlite', 'popular_movies', movie_data)
    load_popular_media('imdb.sqlite', 'popular_shows', tv_data)
    up_movers = model.PopularMedia.get_big_mover('imdb.sqlite', 'popular_movies', '+', '3')
    down_movers = model.PopularMedia.get_big_mover('imdb.sqlite', 'popular_movies', '', '1')
    for i in up_movers:
        imdb_id = i[0]
        rank = i[1]
        rank_up_down = i[2]
        model.PopularMedia.add_big_movers('imdb.sqlite', 'big_movers_movies',
                                          imdb_id, rank, rank_up_down)
    for i in down_movers:
        imdb_id = i[0]
        rank = i[1]
        rank_up_down = i[2]
        model.PopularMedia.add_big_movers('imdb.sqlite', 'big_movers_movies',
                                          imdb_id, rank, rank_up_down)


if __name__ == "__main__":
    main()
