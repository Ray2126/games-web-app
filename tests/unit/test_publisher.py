import pytest
from games.domainmodel.Publisher import Publisher

class TestPublisher:

    def test_construction(self):
        publisher = Publisher("Ubisoft")
        assert str(publisher) == "<Publisher Ubisoft>"

    def test_name_getter(self):
        publisher = Publisher("Ubisoft")
        assert publisher.publisher_name == "Ubisoft"

    def test_name_setter(self):
        publisher = Publisher("Ubisoft")
        publisher.publisher_name = "EA"
        assert str(publisher) == "<Publisher EA>"
        publisher.publisher_name = 1234
        assert str(publisher) == "<Publisher None>"
    
    def test_name_trimmed(self):
        publisher = Publisher("        Ubisoft        ")
        assert publisher.publisher_name == "Ubisoft"
        publisher.publisher_name = "      EA      "
        assert str(publisher) == "<Publisher EA>"

    def test_name_invalid_type(self):
        publisher = Publisher("")
        assert publisher.publisher_name == None
        publisher = Publisher(1234)
        assert publisher.publisher_name == None

    def test_eq (self):
        publisher1 = Publisher("Ubisoft")
        publisher2 = Publisher("Ubisoft")
        assert publisher1 == publisher2
        publisher1 = Publisher("Ubisoft")
        publisher2 = Publisher("EA")
        assert publisher1 != publisher2
        publisher = Publisher("Ubisoft")
        assert publisher != "EA"

    def test_sort (self):
        publisher1 = Publisher("Ubisoft")
        publisher2 = Publisher("EA")
        publisher3 = Publisher(None)
        assert publisher1 > publisher2
        assert not publisher2 > publisher1
        assert publisher2 > publisher3
        assert publisher1 > publisher3

    def test_hash (self):
        publisher1 = Publisher("Ubisoft")
        publisher2 = Publisher("Ubisoft")
        my_set = set()
        my_set.add(publisher1)
        my_set.add(publisher2)
        assert len(my_set) == 1

