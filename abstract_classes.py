
from abc import ABC, abstractmethod
import random


class AbstractEncounter(ABC):

    @classmethod
    def get_instances(cls):
        return cls.instances

    @abstractmethod
    def encounter(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass


class AbstractCreature(ABC):

    def __init__(self, creature_type, hp):
        self.creature_type = creature_type
        self.hp = hp
        self.weapons = []

    
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    


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
    def create_feature(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass


class AbstractAttackStrategy(ABC):

    pass