import pytest
from games.domainmodel.models import Game, User, Review

@pytest.fixture
def create_user():
    # Fixture to create a User object for testing
    return User("testuser", "testpassword")

def test_valid_user_attributes(create_user):
    user = create_user
    assert user.username == "testuser"
    assert user.password == "testpassword"

def test_invalid_username():
    with pytest.raises(ValueError):
        User("", "testpassword")

def test_invalid_password_type():
    with pytest.raises(ValueError):
        User("testuser", 12345)

def test_password_length():
    with pytest.raises(ValueError):
        User("testuser", "pass")

def test_username_lowercase(create_user):
    user = create_user
    assert user.username == "testuser"
    assert user.username != "TestUser"

def test_add_favourite_game(create_user):
    user = create_user
    game = Game(0, "Game A")
    user.add_favourite_game(game)
    assert game in user.favourite_games

def test_remove_favourite_game(create_user):
    user = create_user
    game = Game(0, "Game A")
    user.add_favourite_game(game)
    user.remove_favourite_game(game)
    assert game not in user.favourite_games

def test_add_review(create_user):
    user = create_user
    game = Game(0, "Game A")
    review = Review(user, game, 4, "Great game!")
    user.add_review(review)
    assert review in user.reviews

def test_remove_review(create_user):
    user = create_user
    game = Game(0, "Game A")
    review = Review(user, game, 4, "Great game!")
    user.add_review(review)
    user.remove_review(review)
    assert review not in user.reviews

def test_add_invalid_game_as_favourite(create_user):
    user = create_user
    with pytest.raises(ValueError):
        user.add_favourite_game("Invalid Game")

def test_remove_invalid_game_as_favourite(create_user):
    user = create_user
    with pytest.raises(ValueError):
        user.remove_favourite_game("Invalid Game")