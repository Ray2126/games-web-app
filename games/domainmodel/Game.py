from datetime import datetime
from games.domainmodel.Publisher import Publisher

def sanitize(title):
    strippedTitle = title.strip()
    if(not isinstance(title, str) or strippedTitle == ""):
      return None
    return strippedTitle

class Game:
  def __init__(self, game_id: int, title: str):
    if(not isinstance(game_id, int) or game_id < 0):
      raise ValueError
    self.__game_id = game_id
    self.__title = sanitize(title)
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
      self.__title = sanitize(new_title)
  
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
    self.__description = sanitize(new_description)
  
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
    self.__image_url = sanitize(new_image_url)
  
  @property
  def website_url(self) -> str:
      return self.__website_url

  @website_url.setter
  def website_url(self, new_website_url):
    self.__website_url = sanitize(new_website_url)

  def __repr__(self):
    return f"<Game {self.__game_id}, {self.__title}>"
  
  def add_genre(self, genre):
    self.__genres.append(genre)
  
  def remove_genre(self, genre):
    self.__genres.remove(genre)

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    return self.__game_id == other.game_id

  def __lt__(self, other):
    return self.__game_id < other.game_id

  def __hash__(self):
    return hash(self.__game_id)