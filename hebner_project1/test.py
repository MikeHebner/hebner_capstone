import unittest
import p1s1_hebner


class Test250(unittest.TestCase):
    def test(self):
        self.assertTrue(p1s1_hebner.getTopTv(), 250)


class TestTwo(unittest.TestCase):
    testShow = {
        "items": [
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
        ]
    }
