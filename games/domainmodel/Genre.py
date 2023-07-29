def sanitize_genre_name(genre_name):
    if(not isinstance(genre_name, str) or genre_name == ""):
      return None
    return genre_name.strip()

class Genre:
    def __init__(self, genre_name: str):
        self.__genre_name = sanitize_genre_name(genre_name)

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, new_genre_name: str):
        self.__genre_name = sanitize_genre_name(new_genre_name)

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
