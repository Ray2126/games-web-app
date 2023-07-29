from games.domainmodel.Game import Game

class User:
  def __init__(self, username, password):
    if not isinstance(username, str) or not username.strip():
        raise ValueError
    if not isinstance(password, str):
        raise ValueError
    if len(password) < 7:
        raise ValueError

    self.__username = username.strip().lower()
    self.__password = password
    self.__favourite_games = []
    self.__reviews = []

  def __repr__(self):
    return f"<User {self.__username}>"

  def __eq__(self, other):
    if isinstance(other, User):
        return self.__username == other.__username
    return False

  def __lt__(self, other):
    if isinstance(other, User):
        return self.__username < other.__username
    return NotImplemented

  def __hash__(self):
    return hash(self.__username)

  @property
  def username(self):
    return self.__username

  @property
  def password(self):
    return self.__password

  @property
  def favourite_games(self):
    return self.__favourite_games

  @property
  def reviews(self):
    return self.__reviews

  def add_favourite_game(self, game):
    if not isinstance(game, Game):
        raise ValueError
    if game not in self.__favourite_games:
        self.__favourite_games.append(game)

  def remove_favourite_game(self, game):
    if not isinstance(game, Game):
        raise ValueError
    self.__favourite_games.remove(game)

  def add_review(self, review):
    self.__reviews.append(review)

  def remove_review(self, review):
    self.__reviews.remove(review)