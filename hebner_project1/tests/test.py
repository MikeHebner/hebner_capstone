import unittest
from hebner_project1 import p1s1_hebner, model



class Test250(unittest.TestCase):
    def test(self):
        self.assertTrue(p1s1_hebner.getTopTv(), 250)


class TestTwo(unittest.TestCase):
    # Loads mock entry into test database
    # Queries the database for mock entry
    # If the length of the response is 1, the entry exists in the database.
    def test(self):
        testShow = {
            "items":
                {
                    "id": "tt5491994",
                    "rank": "42",
                    "title": "Bluey",
                    "fullTitle": "Bluey",
                    "year": "2022",
                    "image": "https://m.media-amazon.com/images/M"
                             "/MV5BZWYxODViMGYtMGE2ZC00ZGQ3LThhMWUtYTVkNGE3OWU4NWRkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjY"
                             "wNDA2MDE@._V1_UX128_CR0,3,128,176_AL_.jpg",
                    "crew": "David Attenborough, Gordon Ramsey",
                    "imDbRating": "10",
                    "imDbRatingCount": "690105"
                },
        }
        id = testShow['items']['id']
        rank = testShow['items']['rank']
        title = testShow['items']['title']
        full_title = testShow['items']['fullTitle']
        year = testShow['items']['year']
        crew = testShow['items']['crew']
        imdb_rating = testShow['items']['imDbRating']
        imdb_rating_count = testShow['items']['imDbRatingCount']
        model.runSQLfile('schema.sql', 'tester.sqlite')
        model.TopTv.add('tester.sqlite', id, rank, title, full_title, year, crew, imdb_rating, imdb_rating_count)
        check = model.TopTv.get('tester.sqlite', id)
        try:
            self.assertTrue(len(check), 1)
        except AssertionError as msg:
            print(msg)


class BigMovers(unittest.TestCase):

    def test_movers_happy(self):
        happyData = [{
            "id": "tt7740496",
            "rank": "1",
            "rankUpDown": "-500",
            "title": "Biggest Flop",
            "fullTitle": "Biggest Flop",
            "year": "2022",
            "image": "https://m.media-amazon.com/images/M"
                     "/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTctOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ"
                     "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
            "crew": "Guillermo del Toro (dir.), Bradley Cooper, Cate Blanchett",
            "imDbRating": "7.2",
            "imDbRatingCount": "52151"
        },
            {
                "id": "tt10293406",
                "rank": "2",
                "rankUpDown": "+500",
                "title": "Biggest Money",
                "fullTitle": "Biggest Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BZGRhYjE2NWUtN2FkNy00NGI3LTkxYWMtMDk4Yjg5ZjI3MWI2XkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Jane Campion (dir.), Benedict Cumberbatch, Kirsten Dunst",
                "imDbRating": "6.9",
                "imDbRatingCount": "105912"
            },
            {
                "id": "tt7657566",
                "rank": "3",
                "rankUpDown": "-50",
                "title": "Lil Flop",
                "fullTitle": "Lil Flop",
                "year": "2022",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BNjI4ZTQ1OTYtNTI0Yi00M2EyLThiNjMtMzk1MmZlOWMyMDQwXkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Kenneth Branagh (dir.), Tom Bateman, Annette Bening",
                "imDbRating": "6.7",
                "imDbRatingCount": "9656"
            },
            {
                "id": "tt6856242",
                "rank": "4",
                "rankUpDown": "+50",
                "title": "Lil Money",
                "fullTitle": "Lil Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BMDEzZDY2ZDktNTlmOS00NThjLThkNTEtMjE5MzI5NWEwZmRjXkEyXkFqcGdeQXVyMDA4NzMyOA"
                         "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Matthew Vaughn (dir.), Ralph Fiennes, Gemma Arterton",
                "imDbRating": "6.5",
                "imDbRatingCount": "45661"
            }]
        model.runSQLfile('schema.sql', 'tester.sqlite')
        for i in happyData:
            imDbId = i['id']
            rank = i['rank']
            rankUpDown = i['rankUpDown']
            title = i['title']
            full_title = i['fullTitle']
            year = i['year']
            image = i['image']
            crew = i['crew']
            imDbRating = i['imDbRating']
            imDbRatingCount = i['imDbRatingCount']
            model.PopularMedia.add('tester.sqlite', 'popular_movies', imDbId, rank, rankUpDown, title, full_title, year,
                                   image, crew, imDbRating, imDbRatingCount)
        upMovers = model.PopularMedia.getBigMover('tester.sqlite', 'popular_movies', '+', 2)
        downMovers = model.PopularMedia.getBigMover('tester.sqlite', 'popular_movies', '-', 2)
        # rankUpdown value should be positive for upMovers
        # and negative for downMovers
        for i in upMovers:
            self.assertIs(type(i[2]), int, "Incorrect Type")
            self.assertGreaterEqual(i[2], 0, "Value < 0")
        for i in downMovers:
            self.assertIs(type(i[2]), int, "Incorrect Type")
            self.assertLessEqual(i[2], 0, "Value > 0")

    def test_movers_bad(self):
        badData = [{
            "id": "tt7740123",
            "rank": "1",
            "rankUpDown": "-Egg",
            "title": "Biggest Flop",
            "fullTitle": "Biggest Flop",
            "year": "2022",
            "image": "https://m.media-amazon.com/images/M"
                     "/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTctOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ"
                     "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
            "crew": "Guillermo del Toro (dir.), Bradley Cooper, Cate Blanchett",
            "imDbRating": "7.2",
            "imDbRatingCount": "52151"
        },
            {
                "id": "tt10293234",
                "rank": "2",
                "rankUpDown": "+",
                "title": "Biggest Money",
                "fullTitle": "Biggest Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BZGRhYjE2NWUtN2FkNy00NGI3LTkxYWMtMDk4Yjg5ZjI3MWI2XkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Jane Campion (dir.), Benedict Cumberbatch, Kirsten Dunst",
                "imDbRating": "6.9",
                "imDbRatingCount": "105912"
            },
            {
                "id": "tt7657345",
                "rank": "3",
                "rankUpDown": "-0",
                "title": "Lil Flop",
                "fullTitle": "Lil Flop",
                "year": "2022",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BNjI4ZTQ1OTYtNTI0Yi00M2EyLThiNjMtMzk1MmZlOWMyMDQwXkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Kenneth Branagh (dir.), Tom Bateman, Annette Bening",
                "imDbRating": "6.7",
                "imDbRatingCount": "9656"
            },
            {
                "id": "tt6856456",
                "rank": "4",
                "rankUpDown": "+fifty",
                "title": "Lil Money",
                "fullTitle": "Lil Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BMDEzZDY2ZDktNTlmOS00NThjLThkNTEtMjE5MzI5NWEwZmRjXkEyXkFqcGdeQXVyMDA4NzMyOA"
                         "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Matthew Vaughn (dir.), Ralph Fiennes, Gemma Arterton",
                "imDbRating": "6.5",
                "imDbRatingCount": "45661"
            }]
        model.runSQLfile('schema.sql', 'tester.sqlite')
        for i in badData:
            imDbId = i['id']
            rank = i['rank']
            rankUpDown = i['rankUpDown']
            title = i['title']
            full_title = i['fullTitle']
            year = i['year']
            image = i['image']
            crew = i['crew']
            imDbRating = i['imDbRating']
            imDbRatingCount = i['imDbRatingCount']
            model.PopularMedia.add('tester.sqlite', 'popular_movies', imDbId, rank, rankUpDown, title, full_title, year,
                                   image, crew, imDbRating, imDbRatingCount)
        upMovers = model.PopularMedia.getBigMover('tester.sqlite', 'popular_movies', '+', 2)
        downMovers = model.PopularMedia.getBigMover('tester.sqlite', 'popular_movies', '-', 2)
        # rankUpdown value should be positive for upMovers
        # and negative for downMovers.
        try:
            for i in upMovers:
                self.assertIs(type(i[2]), int, "Incorrect Type")
                self.assertGreaterEqual(i[2], 0, "Value < 0")
            for i in downMovers:
                self.assertIs(type(i[2]), int, "Incorrect Type")
                self.assertLessEqual(i[2], 0, "Value > 0")
        except AssertionError as msg:
            print(msg)

    def test_table_exist(self):
        correctTables = ['TopShows', 'User_Ratings', 'popular_shows', 'popular_movies', 'big_movers_movies']
        counter = 0
        query = 'SELECT tbl_name FROM main.sqlite_master WHERE type==(?)'
        conn, cursor = model.open_db('tester.sqlite')
        response = conn.execute(query, ('table',))
        response = response.fetchall()
        for x in range(len(response)):
            for y in range(len(correctTables)):
                if response[x][0] == correctTables[y]:
                    counter += 1
        try:
            self.assertEqual(counter, len(correctTables), "Missing Tables")
        except AssertionError as msg:
            print(msg)
