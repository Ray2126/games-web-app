import pytest
from games.domainmodel.Game import Game
from games.domainmodel.Genre import Genre
from games.domainmodel.Publisher import Publisher

@pytest.fixture
def game():
    return Game(0, "Valorant")

def test_construction(game):
  assert str(game) == "<Game 0, Valorant>"
  with pytest.raises(ValueError):
    game = Game(-1, "Valorant")
  with pytest.raises(ValueError):
    game = Game(None, "Valorant")
  with pytest.raises(ValueError):
    game = Game("1", "Valorant")
  game = Game(0, "        Valorant        ")
  assert game.title == "Valorant"
  game = Game(0, "")
  assert game.title == None
  game = Game(0, True)
  assert game.title == None
  
def test_game_id(game):
  assert game.game_id == 0

def test_reviews(game):
  assert game.reviews == []

def test_title(game):
  assert game.title == "Valorant"
  game.title = "   Overwatch   "
  assert game.title == "Overwatch"
  game.title = 1234
  assert game.title == None
  game.title = ""
  assert game.title == None

def test_price(game):
  assert game.price == 0
  game.price = 3.14
  assert game.price == 3.14
  with pytest.raises(ValueError):
    game.price = "$12"
  with pytest.raises(ValueError):
    game.price = -1

def test_release_date(game):
  assert game.release_date == None
  game.release_date = "Oct 21, 2008"
  assert game.release_date == "Oct 21, 2008"
  with pytest.raises(ValueError):
    game.release_date = "October 21st 2008"
  with pytest.raises(ValueError):
    game.release_date = 211008
  with pytest.raises(ValueError):
    game.release_date = True

def test_description(game):
  #TODO validate default value?
  game.description = "Boring game"
  assert game.description == "Boring game"
  game.description = 1234
  assert game.description == None
  game.description = ""
  assert game.description == None

def test_publisher(game):
  assert game.publisher == None
  publisher = Publisher("Riot Games")
  game.publisher = publisher
  assert game.publisher == publisher
  game.publisher = "Ubisoft"
  assert game.publisher == None

def test_image_url(game):
  game.image_url = "valorant.png"
  assert game.image_url == "valorant.png"
  game.image_url = 1234
  assert game.image_url == None
  game.image_url = ""
  assert game.image_url == None

def test_website_url(game):
  game.website_url = "google.com/valorant"
  assert game.website_url == "google.com/valorant"
  game.website_url = 1234
  assert game.website_url == None
  game.website_url = ""
  assert game.website_url == None

def test_add_remove_genres(game):
  genre1 = Genre("Action")
  genre2 = Genre("Adventure")
  game.add_genre(genre1)
  assert game.genres == [ genre1 ]
  game.add_genre(genre2)
  assert game.genres == [ genre1, genre2 ]
  game.remove_genre(genre1)
  assert game.genres == [ genre2 ]

def test_eq(game):
  game2 = Game(1, "Overwatch")
  assert game != game2
  game3 = Game(0, "Not Valorant")
  assert game == game3

def test_lt(game):
  game2 = Game(1, "Overwatch")
  assert game < game2

def test_hash(game):
  game2 = Game(0, "Overwatch")
  my_set = set()
  my_set.add(game)
  my_set.add(game2)
  assert len(my_set) == 1