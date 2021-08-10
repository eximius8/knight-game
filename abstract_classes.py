"""Классы, от которых наследуются остальные классы игры."""
from abc import ABC, abstractmethod


class AbstractEncounter(ABC):
    """Встречаемый объект.
    Встречаемым бъектом может быть как монстр так и артефакт."""

    @abstractmethod
    def encounter(self):
        """Функция, с логикой встречи с игроком.
        Данная функция отвечает за выбор игроком дальнейших
        дейтсвий после встречи с объектом. После выбра функция
        запускает логику для дальнейшего развития событий.
        """
        pass


class AbstractCreature(ABC):

    def __init__(self, creature_type, hp, features):
        self.creature_type = creature_type
        names = {1: "воин", 2: "лучник", 3: "маг"}
        self.name = names[self.creature_type]
        self.hp = hp
        self.features = features

    def add_feature(self, feature):
        self.features[feature.code] = feature


class AbstractCreatureFactory(ABC):

    @abstractmethod
    def create_creature(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass


class AbstractFeatureFactory(ABC):

    @abstractmethod
    def create_random_feature(self):
        """
        Функция для создания случайного артефакта.
        """
        pass


class AbstractAttackStrategy(ABC):
    """Стратегия аттаки."""

    pass
