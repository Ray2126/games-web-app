import pytest
from games.domainmodel.models import Genre

class TestGenre:

    def test_construction(self):
        genre = Genre("Action")
        assert str(genre) == "<Genre Action>"

    def test_name_getter(self):
        genre = Genre("Action")
        assert genre.genre_name == "Action"

    def test_name_setter(self):
        genre = Genre("Action")
        genre.genre_name = "Adventure"
        assert str(genre) == "<Genre Adventure>"
        genre.genre_name = 1234
        assert str(genre) == "<Genre None>"
    
    def test_name_trimmed(self):
        genre = Genre("        Action        ")
        assert genre.genre_name == "Action"
        genre.genre_name = "      Adventure      "
        assert str(genre) == "<Genre Adventure>"

    def test_name_invalid_type(self):
        genre = Genre("")
        assert genre.genre_name == None
        genre = Genre(1234)
        assert genre.genre_name == None

    def test_eq (self):
        genre1 = Genre("Action")
        genre2 = Genre("Action")
        assert genre1 == genre2
        genre1 = Genre("Action")
        genre2 = Genre("Adventure")
        assert genre1 != genre2
        genre = Genre("Action")
        assert genre != "Adventure"

    def test_sort (self):
        genre1 = Genre("Action")
        genre2 = Genre("Adventure")
        genre3 = Genre(None)
        assert genre1 < genre2
        assert genre2 > genre3
        assert genre1 > genre3

    def test_hash (self):
        genre1 = Genre("Action")
        genre2 = Genre("Action")
        my_set = set()
        my_set.add(genre1)
        my_set.add(genre2)
        assert len(my_set) == 1

