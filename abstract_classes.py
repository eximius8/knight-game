"""Классы, от которых наследуются остальные классы игры."""
from abc import ABC, abstractmethod
from typing import Any
from constants import global_names


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

    def __init__(self, player_name: str, creature_type: int,
                 hp: int, features: dict, attack_strategy):
        # игрок или монстр
        self.player_name = player_name
        # тип игрока
        self.creature_type = creature_type
        # название игрока
        self.name = global_names[self.creature_type]
        # жизни игрока
        self.hp = hp
        # артефакты игрока (например оружее, тотем и т.п.)
        self.features = features
        # стратегия аттаки
        self.attack_strategy = attack_strategy

    def add_feature(self, feature: Any):
        """Добавить артефакт к объекту."""
        self.features[feature.code] = feature

    def fight(self, other: Any):
        """Бой соперников."""
        self.attack_strategy.attack(self, other)


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
