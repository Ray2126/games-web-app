from games.domainmodel.Review import Review
from games.domainmodel.Game import Game

class User:
  def __init__(self, username, password):
    if not isinstance(username, str) or not username.strip():
        raise ValueError
    if not isinstance(password, str):
        raise ValueError
    if len(password) < 7:
        raise ValueError

    self._username = username.strip().lower()
    self._password = password
    self._favourite_games = []
    self._reviews = []

  def __repr__(self):
    return f"<User {self._username}>"

  def __eq__(self, other):
    if isinstance(other, User):
        return self._username == other._username
    return False

  def __lt__(self, other):
    if isinstance(other, User):
        return self._username < other._username
    return NotImplemented

  def __hash__(self):
    return hash(self._username)

  @property
  def username(self):
    return self._username

  @property
  def password(self):
    return self._password

  @property
  def favourite_games(self):
    return self._favourite_games

  @property
  def reviews(self):
    return self._reviews

  def add_favourite_game(self, game):
    if not isinstance(game, Game):
        raise ValueError
    if game not in self._favourite_games:
        self._favourite_games.append(game)

  def remove_favourite_game(self, game):
    if not isinstance(game, Game):
        raise ValueError
    self._favourite_games.remove(game)

  def add_review(self, review):
    if not isinstance(review, Review):
        raise ValueError
    if review not in self._reviews:
        self._reviews.append(review)

  def remove_review(self, review):
    if not isinstance(review, Review):
        raise ValueError
    self._reviews.remove(review)