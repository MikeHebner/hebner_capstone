import unittest
import p1s1_hebner
import model


class Test250(unittest.TestCase):
    def test(self):
        self.assertTrue(p1s1_hebner.get_top_tv(), 250)


class TestTwo(unittest.TestCase):
    # Loads mock entry into test database
    # Queries the database for mock entry
    # If the length of the response is 1, the entry exists in the database.
    def test(self):
        test_show = {
            "items":
                {
                    "id": "tt5491994",
                    "rank": "42",
                    "title": "Bluey",
                    "fullTitle": "Bluey",
                    "year": "2022",
                    "image": "https://m.media-amazon.com/images/M"
                             "/MV5BZWYxODViMGYtMGE2ZC00ZGQ3LThhMW"
                             "UtYTVkNGE3OWU4NWRkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjY"
                             "wNDA2MDE@._V1_UX128_CR0,3,128,176_AL_.jpg",
                    "crew": "David Attenborough, Gordon Ramsey",
                    "imDb_rating": "10",
                    "imDb_rating_count": "690105"
                },
        }
        id = test_show['items']['id']
        rank = test_show['items']['rank']
        title = test_show['items']['title']
        full_title = test_show['items']['fullTitle']
        year = test_show['items']['year']
        crew = test_show['items']['crew']
        imdb_rating = test_show['items']['imDb_rating']
        imdb_rating_count = test_show['items']['imDb_rating_count']
        model.run_sql_file('hebner_project1/schema.sql', 'tester.sqlite')
        model.TopTv.add('tester.sqlite', id, rank, title, full_title, year, crew,
                        imdb_rating, imdb_rating_count)
        check = model.TopTv.get('tester.sqlite', id)
        try:
            self.assertTrue(len(check), 1)
        except AssertionError as msg:
            print(msg)


class BigMovers(unittest.TestCase):

    def test_movers_happy(self):
        happy_data = [{
            "id": "tt7740496",
            "rank": "1",
            "rankUpDown": "-500",
            "title": "Biggest Flop",
            "fullTitle": "Biggest Flop",
            "year": "2022",
            "image": "https://m.media-amazon.com/images/M"
                     "/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTc"
                     "tOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ"
                     "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
            "crew": "Guillermo del Toro (dir.), Bradley Cooper, Cate Blanchett",
            "imDb_rating": "7.2",
            "imDb_rating_count": "52151"
        },
            {
                "id": "tt10293406",
                "rank": "2",
                "rankUpDown": "+500",
                "title": "Biggest Money",
                "fullTitle": "Biggest Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BZGRhYjE2NWUtN2FkNy00NGI3LTkxYWM"
                         "tMDk4Yjg5ZjI3MWI2XkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Jane Campion (dir.), Benedict Cumberbatch, Kirsten Dunst",
                "imDb_rating": "6.9",
                "imDb_rating_count": "105912"
            },
            {
                "id": "tt7657566",
                "rank": "3",
                "rankUpDown": "-50",
                "title": "Lil Flop",
                "fullTitle": "Lil Flop",
                "year": "2022",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BNjI4ZTQ1OTYtNTI0Yi00M2EyLThiNj"
                         "MtMzk1MmZlOWMyMDQwXkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Kenneth Branagh (dir.), Tom Bateman, Annette Bening",
                "imDb_rating": "6.7",
                "imDb_rating_count": "9656"
            },
            {
                "id": "tt6856242",
                "rank": "4",
                "rankUpDown": "+50",
                "title": "Lil Money",
                "fullTitle": "Lil Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BMDEzZDY2ZDktNTlmOS00NThjLThkNTE"
                         "tMjE5MzI5NWEwZmRjXkEyXkFqcGdeQXVyMDA4NzMyOA"
                         "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Matthew Vaughn (dir.), Ralph Fiennes, Gemma Arterton",
                "imDb_rating": "6.5",
                "imDb_rating_count": "45661"
            }]
        model.run_sql_file('hebner_project1/schema.sql', 'tester.sqlite')
        for i in happy_data:
            imdb_id = i['id']
            rank = i['rank']
            rank_up_down = i['rankUpDown']
            title = i['title']
            full_title = i['fullTitle']
            year = i['year']
            image = i['image']
            crew = i['crew']
            imdb_rating = i['imDb_rating']
            imdb_rating_count = i['imDb_rating_count']
            model.PopularMedia.add('tester.sqlite', 'popular_movies', imdb_id, rank,
                                   rank_up_down, title, full_title, year,
                                   image, crew, imdb_rating, imdb_rating_count)
        up_movers = model.PopularMedia.get_big_mover('tester.sqlite', 'popular_movies', '+', 2)
        down_movers = model.PopularMedia.get_big_mover('tester.sqlite', 'popular_movies', '-', 2)
        # rankUpdown value should be positive for upMovers
        # and negative for downMovers
        for i in up_movers:
            self.assertIs(type(i[2]), int, "Incorrect Type")
            self.assertGreaterEqual(i[2], 0, "Value < 0")
        for i in down_movers:
            self.assertIs(type(i[2]), int, "Incorrect Type")
            self.assertLessEqual(i[2], 0, "Value > 0")

    def test_movers_bad(self):
        bad_data = [{
            "id": "tt7740123",
            "rank": "1",
            "rankUpDown": "-Egg",
            "title": "Biggest Flop",
            "fullTitle": "Biggest Flop",
            "year": "2022",
            "image": "https://m.media-amazon.com/images/M"
                     "/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTc"
                     "tOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ"
                     "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
            "crew": "Guillermo del Toro (dir.), Bradley Cooper, Cate Blanchett",
            "imDb_rating": "7.2",
            "imDb_rating_count": "52151"
        },
            {
                "id": "tt10293234",
                "rank": "2",
                "rankUpDown": "+",
                "title": "Biggest Money",
                "fullTitle": "Biggest Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BZGRhYjE2NWUtN2FkNy00NGI3LTkxYW"
                         "MtMDk4Yjg5ZjI3MWI2XkEyXkFqcGdeQXVyMT"
                         "EyMjM2NDc2._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Jane Campion (dir.), Benedict Cumberbatch, Kirsten Dunst",
                "imDb_rating": "6.9",
                "imDb_rating_count": "105912"
            },
            {
                "id": "tt7657345",
                "rank": "3",
                "rankUpDown": "-0",
                "title": "Lil Flop",
                "fullTitle": "Lil Flop",
                "year": "2022",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BNjI4ZTQ1OTYtNTI0Yi00M2EyLThiNjMtM"
                         "zk1MmZlOWMyMDQwXkEyXkFqcGdeQXVyMTEyMjM2NDc2"
                         "._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Kenneth Branagh (dir.), Tom Bateman, Annette Bening",
                "imDb_rating": "6.7",
                "imDb_rating_count": "9656"
            },
            {
                "id": "tt6856456",
                "rank": "4",
                "rankUpDown": "+fifty",
                "title": "Lil Money",
                "fullTitle": "Lil Money",
                "year": "2021",
                "image": "https://m.media-amazon.com/images/M"
                         "/MV5BMDEzZDY2ZDktNTlmOS00NThjLThkNTEtMjE"
                         "5MzI5NWEwZmRjXkEyXkFqcGdeQXVyMDA4NzMyOA"
                         "@@._V1_UX128_CR0,3,128,176_AL_.jpg",
                "crew": "Matthew Vaughn (dir.), Ralph Fiennes, Gemma Arterton",
                "imDb_rating": "6.5",
                "imDb_rating_count": "45661"
            }]
        model.run_sql_file('hebner_project1/schema.sql', 'tester.sqlite')
        for i in bad_data:
            imdb_id = i['id']
            rank = i['rank']
            rank_up_down = i['rankUpDown']
            title = i['title']
            full_title = i['fullTitle']
            year = i['year']
            image = i['image']
            crew = i['crew']
            imdb_rating = i['imDb_rating']
            imdb_rating_count = i['imDb_rating_count']
            model.PopularMedia.add('tester.sqlite', 'popular_movies', imdb_id, rank,
                                   rank_up_down, title, full_title, year,
                                   image, crew, imdb_rating, imdb_rating_count)
        up_movers = model.PopularMedia.get_big_mover('tester.sqlite', 'popular_movies', '+', 2)
        down_movers = model.PopularMedia.get_big_mover('tester.sqlite', 'popular_movies', '-', 2)
        # rankUpdown value should be positive for upMovers
        # and negative for downMovers.
        try:
            for i in up_movers:
                self.assertIs(type(i[2]), int, "Incorrect Type")
                self.assertGreaterEqual(i[2], 0, "Value < 0")
            for i in down_movers:
                self.assertIs(type(i[2]), int, "Incorrect Type")
                self.assertLessEqual(i[2], 0, "Value > 0")
        except AssertionError as msg:
            print(msg)

    # Matches the returned tables to correctTables[]
    # After iterating through, int counter should equal the len(correctTables[])
    def test_table_exist(self):
        correct_tables = ['top_shows', 'top_movies', 'tv_user_ratings',
                          'movie_user_ratings', 'popular_shows', 'popular_movies',
                          'big_movers_movies']
        counter = 0
        query = 'SELECT tbl_name FROM main.sqlite_master WHERE type==(?)'
        conn, cursor = model.open_db('tester.sqlite')
        response = conn.execute(query, ('table',))
        response = response.fetchall()
        for x in range(len(response)):
            for y in range(len(correct_tables)):
                if response[x][0] == correct_tables[y]:
                    counter += 1
        try:
            self.assertEqual(counter, len(correct_tables), "Missing Tables")
        except AssertionError as msg:
            print(msg)

    # Adds a test entry into the (empty) table and checks if it's there.
    # If it is, it clears the table.
    def test_write_table(self):
        model.PopularMedia.add_big_movers('tester.sqlite', 'big_movers_movies', 'testID', 1, +1)
        query = "SELECT * FROM main.big_movers_movies"
        conn, cursor = model.open_db('tester.sqlite')
        response = conn.execute(query)
        response = response.fetchall()
        try:
            self.assertIs(len(response), 1, "Table not added")
            query = "DELETE FROM main.big_movers_movies"
            conn.execute(query)
            conn.commit()
        except AssertionError as msg:
            print(msg)

    def test_foreign_key(self):
        model.run_sql_file('hebner_project1/schema.sql', 'tester.sqlite')
        movie_data = p1s1_hebner.get_popular_media('movie')
        tv_data = p1s1_hebner.get_popular_media('tv')
        p1s1_hebner.load_popular_media('tester.sqlite', 'popular_movies', movie_data)
        p1s1_hebner.load_popular_media('tester.sqlite', 'popular_shows', tv_data)
        up_movers = model.PopularMedia.get_big_mover('tester.sqlite', 'popular_movies', '+', '3')
        down_movers = model.PopularMedia.get_big_mover('tester.sqlite', 'popular_movies', '', '1')
        for i in up_movers:
            imdb_id = i[0]
            rank = i[1]
            rank_up_down = i[2]
            model.PopularMedia.add_big_movers('tester.sqlite', 'big_movers_movies',
                                              imdb_id, rank, rank_up_down)
        for i in down_movers:
            imdb_id = i[0]
            rank = i[1]
            rank_up_down = i[2]
            model.PopularMedia.add_big_movers('tester.sqlite', 'big_movers_movies',
                                              imdb_id, rank, rank_up_down)
        # If the foreign key works, query should return the 4 entries that are added above.
        # The title is included as an additional check
        # because it only exists in popular_movies table.
        query = 'SELECT imdb_id, title FROM popular_movies' \
                ' JOIN big_movers_movies USING(imdb_id)'
        conn, cursor = model.open_db('tester.sqlite')
        response = conn.execute(query)
        response = response.fetchall()
        try:
            self.assertTrue(len(response) == 4, "Foreign Key Error")
        except AssertionError as msg:
            print(msg)
