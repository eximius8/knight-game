"""Классы, от которых наследуются остальные классы игры."""
from abc import ABC, abstractmethod
from typing import Any


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
    """Класс для героев игры (игроков и монстров)."""

    def __init__(self, creature_type: int, hp: int, features: dict):
        # тип игрока
        self.creature_type = creature_type
        names = {1: "воин", 2: "лучник", 3: "маг"}
        self.name = names[self.creature_type]
        # жизни игрока
        self.hp = hp
        # артефакты игрока (например оружее, тотем и т.п.)
        self.features = features

    def add_feature(self, feature: Any):
        """Добавить артефакт к объекту."""
        self.features[feature.code] = feature

    def fight(self, other, attack_strategy):
        """Бой соперников."""
        attack_strategy.attack(self, other)


class AbstractCreatureFactory(ABC):
    """Фабрика производства героев."""

    @abstractmethod
    def create_creature(self):
        """Метод для создания героев."""
        pass


class AbstractFeatureFactory(ABC):
    """Фабрика производства артефактов."""

    @abstractmethod
    def create_random_feature(self):
        """
        Функция для создания случайного артефакта.
        """
        pass


class AbstractAttackStrategy(ABC):
    """Стратегия аттаки.
    Данная программа использует Стратегию
    в качестве паттерна проектирования для поведения игрока или монстра."""

    @abstractmethod
    def get_available_weapons(self):
        """Получение доступного оружия игрока (монстра).
        возвращается список из доступных артефактов"""
        pass

    @abstractmethod
    def choose_weapon(self):
        """Выбор оружия для применения игроком.
        Если оружие только одно, оно выбирается автоматически."""
        pass

    @abstractmethod
    def attack(self):
        """Атака игрока (монстра) на соперника."""
        pass
