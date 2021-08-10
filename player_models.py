"""Для классов игроков, монстров и инвентаря."""
from feature_models import Weapon

from custom_exceptions import GameLostException, GameWonException
from abstract_classes import AbstractCreature
from attack_strategy import AttackStrategy


class Player(AbstractCreature):

    def __init__(self):
        intro_text = "1 - войном\n2 - лучником\n3 - магом\nВаш выбор: "
        self.monsters_killed = 0
        while True:
            print("Кем хотите играть:")
            choice = input(intro_text)
            if choice in ["1", "2", "3"]:
                self.attack_strategy = AttackStrategy(fighter_type=int(choice))
                super().__init__(creature_type=int(choice),
                                 hp=10,
                                 features={1: Weapon(power=10, name='меч', code=1)})
                break

    def has_totem(self):
        return 5 in self.features

    def check_status(self):
        if self.hp < 1 and self.has_totem():
            self.hp = self.features[5].player.hp
            self.monsters_killed = self.features[5].player.monsters_killed
            self.features = self.features[5].player.features
        elif self.hp < 1:
            raise GameLostException
        if self.monsters_killed > 9:
            raise GameWonException
        print("====================================")
        print("====================================")
        print("====================================")
        print(f"У вас {self.hp} жизней")
        print("У вас есть следующие артефакты: " + ", ".join(
            [str(feature) for feature in self.features.values()]))
        print()

