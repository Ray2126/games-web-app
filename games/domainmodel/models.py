from datetime import datetime

def sanitize_string(value):
    if(not isinstance(value, str) or value.strip() == ""):
      return None
    return value.strip()

class Game:
  def __init__(self, game_id: int, title: str):
    if(not isinstance(game_id, int) or game_id < 0):
      raise ValueError
    self.__game_id = game_id
    self.__title = sanitize_string(title)
    self.__genres = []
    self.__reviews = []
    self.__price = 0
    self.__release_date = None
    self.__description = None
    self.__publisher = None
    self.__image_url = None
    self.__website_url = None

  @property
  def title(self) -> str:
      return self.__title

  @title.setter
  def title(self, new_title):
      self.__title = sanitize_string(new_title)
  
  @property
  def game_id(self) -> str:
      return self.__game_id

  @property
  def reviews(self) -> []:
      return self.__reviews

  @property
  def genres(self) -> []:
      return self.__genres
  
  @property
  def price(self) -> str:
      return self.__price

  @price.setter
  def price(self, new_price):
    if(not isinstance(new_price, (int, float)) or new_price < 0):
      raise ValueError
    self.__price = new_price
  
  @property
  def release_date(self) -> str:
      return self.__release_date

  @release_date.setter
  def release_date(self, new_release_date):
    if not isinstance(new_release_date, str):
      raise ValueError
    datetime.strptime(new_release_date, "%b %d, %Y")
    self.__release_date = new_release_date
  
  @property
  def description(self) -> str:
      return self.__description

  @description.setter
  def description(self, new_description):
    self.__description = sanitize_string(new_description)
  
  @property
  def publisher(self) -> str:
      return self.__publisher

  @publisher.setter
  def publisher(self, new_publisher):
    if not isinstance(new_publisher, Publisher):
      self.__publisher = None
      return
    self.__publisher = new_publisher
  
  @property
  def image_url(self) -> str:
      return self.__image_url

  @image_url.setter
  def image_url(self, new_image_url):
    self.__image_url = sanitize_string(new_image_url)
  
  @property
  def website_url(self) -> str:
      return self.__website_url

  @website_url.setter
  def website_url(self, new_website_url):
    self.__website_url = sanitize_string(new_website_url)

  def __repr__(self):
    return f"<Game {self.__game_id}, {self.__title}>"
  
  def add_genre(self, genre):
    if not isinstance(genre, Genre):
      raise ValueError
    if genre not in self.__genres:
      self.__genres.append(genre)
  
  def remove_genre(self, genre):
    if not isinstance(genre, Genre):
      raise ValueError
    self.__genres.remove(genre)

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    return self.__game_id == other.game_id

  def __lt__(self, other):
    return self.__game_id < other.game_id

  def __hash__(self):
    return hash(self.__game_id)

class Genre:
  def __init__(self, genre_name: str):
    self.__genre_name = sanitize_string(genre_name)

  @property
  def genre_name(self) -> str:
    return self.__genre_name

  @genre_name.setter
  def genre_name(self, new_genre_name: str):
    self.__genre_name = sanitize_string(new_genre_name)

  def __repr__(self):
    return f"<Genre {self.__genre_name}>"

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    return self.__genre_name == other.genre_name

  def __lt__(self, other):
    if(self.genre_name is None):
      return True
    if(other.genre_name is None):
      return False
    return self.__genre_name < other.genre_name

  def __hash__(self):
    return hash(self.__genre_name)

class Publisher:
  def __init__(self, publisher_name: str):
    self.__publisher_name = sanitize_string(publisher_name)

  @property
  def publisher_name(self) -> str:
    return self.__publisher_name

  @publisher_name.setter
  def publisher_name(self, new_publisher_name: str):
    self.__publisher_name = sanitize_string(new_publisher_name)

  def __repr__(self):
    return f"<Publisher {self.__publisher_name}>"

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    return self.__publisher_name == other.publisher_name

  def __lt__(self, other):
    if(self.publisher_name is None):
      return True
    if(other.publisher_name is None):
      return False
    return self.__publisher_name < other.publisher_name

  def __hash__(self):
    return hash(self.__publisher_name)

class Review:
  def __init__(self, user, game, rating, comment):
    if not isinstance(user, User):
      raise ValueError
    if not isinstance(game, Game):
      raise ValueError
    if not isinstance(rating, int) or not (0 <= rating <= 5):
      raise ValueError
    if not isinstance(comment, str) or not comment.strip():
      raise ValueError

    self.__user = user
    self.__game = game
    self.__rating = rating
    self.__comment = comment.strip()

  def __repr__(self):
    return f"Review(User: {self.__user}, Game: {self.__game}, Rating: {self.__rating}, Comment: {self.__comment})"

  def __eq__(self, other):
    if isinstance(other, Review):
      return (
        self.__user == other.user and
        self.__game == other.game and
        self.__comment == other.comment
      )
    return False

  @property
  def user(self):
    return self.__user

  @property
  def game(self):
    return self.__game

  @property
  def comment(self):
    return self.__comment

  @comment.setter
  def comment(self, value):
    if not isinstance(value, str) or not value.strip():
      raise ValueError
    self.__comment = value.strip()

  @property
  def rating(self):
    return self.__rating

  @rating.setter
  def rating(self, value):
    if not isinstance(value, int) or not (0 <= value <= 5):
      raise ValueError
    self.__rating = value
  
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