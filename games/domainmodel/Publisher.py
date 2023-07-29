def sanitize_publisher_name(publisher_name):
    if(not isinstance(publisher_name, str) or publisher_name == ""):
      return None
    return publisher_name.strip()

class Publisher:
    def __init__(self, publisher_name: str):
        self.__publisher_name = sanitize_publisher_name(publisher_name)

    @property
    def publisher_name(self) -> str:
        return self.__publisher_name

    @publisher_name.setter
    def publisher_name(self, new_publisher_name: str):
        self.__publisher_name = sanitize_publisher_name(new_publisher_name)

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
