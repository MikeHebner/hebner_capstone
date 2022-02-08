import unittest
import p1s1_hebner
import model


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
                             "/MV5BZWYxODViMGYtMGE2ZC00ZGQ3LThhMWUtYTVkNGE3OWU4NWRkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjYwNDA2MDE@._V1_UX128_CR0,3,128,176_AL_.jpg",
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
        self.assertTrue(len(check), 1)
