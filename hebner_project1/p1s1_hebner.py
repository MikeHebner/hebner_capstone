# Michael Hebner
import json
import requests
import secrets
import model


# Gets the top 250 TV shows and saves the json response to the project directory
# I did this to cut down on the api request
def getTopTv():
    url = "https://imdb-api.com/en/API/Top250TVs/{}".format(secrets.IMDB_KEY)
    response = requests.get(url)
    data = response.json()
    with open('topTv.json', 'w') as file:
        json.dump(data, file)
    # Only returns len(data) for test.py purposes
    return len(data)


# opens the main text file and appends the list of top 250 shows to it
def putTopTv():
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
def getUserRatingData(id):
    url = "https://imdb-api.com/en/API/UserRatings/{}/{}".format(secrets.IMDB_KEY, id)
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
def getUserRatingDataV2(id):
    url = "https://imdb-api.com/en/API/UserRatings/{}/{}".format(secrets.IMDB_KEY, id)
    response = requests.get(url)
    data = response.json()
    imdbID = data['imDbId']
    total_rating = data['totalRating']
    total_rating_votes = data['totalRatingVotes']
    # Each is a row in rating_i
    ratingPercents = []
    # Each is a row in rating_i_votes
    ratingVotes = []
    ratings = data['ratings']
    # Ran into an issue of a top show having no ratings returned.
    # If this happens, dummy data is added to those rows.
    if len(ratings) == 0:
        for i in range(10):
            percent = 10 - i
            votes = 10 - i
            ratingPercents.append(percent)
            ratingVotes.append(votes)
    else:
        for i in ratings:
            percent = i['percent']
            percent = percent[:-1]
            votes = i['votes']
            ratingPercents.append(percent)
            ratingVotes.append(votes)
    return imdbID, total_rating, total_rating_votes, ratingPercents, ratingVotes


# Returns imdb id from rank off of top 250 shows or by name
def getID(notID):
    # get id from ranking
    if type(notID) is int:
        rank = notID
        # index of each is its rank minus one.
        # 1 ranked is in 0th index
        index = rank - 1
        topTv = open('topTv.json')
        topTv = json.loads(topTv.read())
        return topTv['items'][index]['id']
    # get id from (str) name
    if type(notID) is str:
        name = notID
        url = "https://imdb-api.com/en/API/SearchSeries/{}/{}".format(secrets.IMDB_KEY, name)
        response = requests.get(url)
        data = response.json()
        return data["results"][0]["id"]
    else:
        return "INVALID INPUT"


def loadTopTv():
    file = open("topTv.json")
    data = json.loads(file.read())
    file.close()
    for i in data['items']:
        id = i['id']
        rank = i['rank']
        title = i['title']
        full_title = i['fullTitle']
        year = i['year']
        crew = i['crew']
        imdb_rating = i['imDbRating']
        imdb_rating_count = i['imDbRatingCount']
        model.TopTv.add('imdb.sqlite', id, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count)


# Takes the imdbID as input.
# Loads the User rating for given input into database.
def loadUserRatings(id):
    imdbID, total_rating, total_rating_votes, rating_percents, rating_votes = getUserRatingDataV2(id)
    model.UserRatings.add('imdb.sqlite', imdbID, total_rating, total_rating_votes, rating_percents[0], rating_votes[0],
                          rating_percents[1],
                          rating_votes[1], rating_percents[2], rating_votes[2], rating_percents[3], rating_votes[3],
                          rating_percents[4], rating_votes[4], rating_percents[5], rating_votes[5], rating_percents[6],
                          rating_votes[6], rating_percents[7], rating_votes[7], rating_percents[8], rating_votes[8],
                          rating_percents[9], rating_votes[9])


# Loads schema into database.
model.runSQLfile('schema.sql', 'imdb.sqlite')
# Required user ratings to get stored in array
rawInput = [1, 50, 100, 200, "Wheel of Time"]
# loads top 250 shows into db table.
loadTopTv()
# Gets IMDB id for each input, then queries user ratings with the returned input.
for i in rawInput:
    IMDBid = getID(i)
    print(IMDBid)
    loadUserRatings(IMDBid)
