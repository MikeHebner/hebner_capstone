# Michael Hebner
import json
import requests
import secrets


def getTopTv():
    url = "https://imdb-api.com/en/API/Top250TVs/{}".format(secrets.IMDB_KEY)
    response = requests.get(url)
    data = response.json()
    with open('topTv.json', 'w') as file:
        json.dump(data, file)


def getUserRatingData(rank):
    IMDBid = getID(rank)
    url = "https://imdb-api.com/en/API/UserRatings/{}/{}".format(secrets.IMDB_KEY, IMDBid)
    response = requests.get(url)
    data = response.json()
    print(data)


# Returns imdb id from rank off of top 250 shows
def getID(rank):
    # index of each is its rank minus one.
    # 1 ranked is in 0th index
    index = rank - 1
    topTv = open('topTv.json')
    topTv = json.loads(topTv.read())
    return topTv['items'][index]['id']


getUserRatingData(1)
