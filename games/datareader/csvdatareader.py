import os
import csv
from games.domainmodel.models import Game, Publisher, Genre

class GameFileCSVReader:

    def __init__(self, filename):
        self.__filename = filename
        self.__dataset_of_games = []
        self.__dataset_of_publishers = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_games(self) -> list:
        return self.__dataset_of_games

    @property
    def dataset_of_publishers(self) -> set:
        return self.__dataset_of_publishers

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
      with open(self.__filename) as csv_file:
          csv_reader = csv.DictReader(csv_file, delimiter=',')
          for row in csv_reader:
              self.__dataset_of_games.append(Game(int(row["AppID"]), row["Name"]))
              self.__dataset_of_publishers.add(Publisher(row["Publishers"]))
              genre_names = row["Genres"].split(",")
              for genre_name in genre_names:
                  self.__dataset_of_genres.add(Genre(genre_name))