# Michael Hebner
import json
import requests
import secrets


# Gets the top 250 TV shows and saves the json response to the project directory
# I did this to cut down on the api request
def getTopTv():
    url = "https://imdb-api.com/en/API/Top250TVs/{}".format(secrets.IMDB_KEY)
    response = requests.get(url)
    data = response.json()
    with open('topTv.json', 'w') as file:
        json.dump(data, file)


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


# Below is where all the work was done.
# I saved the ranks to get as an array so I could loop the ideas through faster
ranksToGet = [1, 50, 100, 200]
# I've commented this out b/c it has done its job.
# for i in ranksToGet:
#     IMDBid = getID(i)
#     getUserRatingData(IMDBid)
#
# wot = "Wheel of Time"
# wotID = getID(wot)
# getUserRatingData(wotID)


# This function writes the top 250 shows to the text file.
# putTopTv()
