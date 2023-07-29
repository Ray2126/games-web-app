import pytest
from games.domainmodel.models import User, Game, Review, Genre

@pytest.fixture
def create_user():
  return User("testuser", "testpassword")

@pytest.fixture
def create_game():
  return Game(0, "Game A")

def test_valid_review_attributes(create_user, create_game):
  user = create_user
  game = create_game
  review = Review(user, game, 4, "Great game!")

  assert review.user == user
  assert review.game == game
  assert review.rating == 4
  assert review.comment == "Great game!"

def test_invalid_user_type():
  with pytest.raises(ValueError):
      game = Game(0, "Game A")
      Review("invalid_user", game, 4, "Great game!")

def test_invalid_game_type(create_user):
  user = create_user
  with pytest.raises(ValueError):
      Review(user, "invalid_game", 4, "Great game!")

def test_invalid_rating_out_of_range(create_user, create_game):
  user = create_user
  game = create_game
  with pytest.raises(ValueError):
      Review(user, game, 6, "Great game!")

def test_invalid_rating_type(create_user, create_game):
  user = create_user
  game = create_game
  with pytest.raises(ValueError):
      Review(user, game, "invalid_rating", "Great game!")

def test_invalid_comment_type(create_user, create_game):
  user = create_user
  game = create_game
  with pytest.raises(ValueError):
      Review(user, game, 4, 12345)

def test_comment_strip(create_user, create_game):
  user = create_user
  game = create_game
  review = Review(user, game, 4, "  Great game!  ")
  assert review.comment == "Great game!"

def test_set_comment(create_user, create_game):
  user = create_user
  game = create_game
  review = Review(user, game, 4, "Great game!")
  review.comment = "This is a new comment."
  assert review.comment == "This is a new comment."

def test_set_invalid_comment_type(create_user, create_game):
  user = create_user
  game = create_game
  review = Review(user, game, 4, "Great game!")
  with pytest.raises(ValueError):
      review.comment = 12345

def test_set_invalid_rating_out_of_range(create_user, create_game):
  user = create_user
  game = create_game
  review = Review(user, game, 4, "Great game!")
  with pytest.raises(ValueError):
      review.rating = 6

def test_set_invalid_rating_type(create_user, create_game):
  user = create_user
  game = create_game
  review = Review(user, game, 4, "Great game!")
  with pytest.raises(ValueError):
      review.rating = "invalid_rating"