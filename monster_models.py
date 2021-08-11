"""Для классов монстров."""
import random
from abstract_classes import AbstractCreature, AbstractEncounter, AbstractCreatureFactory
from feature_models import FeatureFactory
from attack_strategy import AttackStrategy


class Monster(AbstractCreature, AbstractEncounter):
    """Класс монстр.
    Наследуется от абстрактного героя и объекта, с которым можно встретится."""

    def is_alive(self):
        if self.hp > 0:
            return True
        print("Монстр повержен!")
        return False

    def encounter(self, player):
        while True:
            print(f"Ваш противник: {self.name} с числом жизней {self.hp}:")
            print("1 - драться\n2 - бежать")
            choice = input("Ваш выбор: ")
            if choice == "1":
                player.fight(self)
                self.fight(player)
                break
            elif choice == "2":
                break


class MonsterFactory(AbstractCreatureFactory):

    def create_creature(self) -> Monster:
        creature_type = random.randint(1,3)
        feature_factory = FeatureFactory()
        features = {creature_type: feature_factory.create_weapon(creature_type)}

        if creature_type == 2:
            features[4] = feature_factory.create_weapon(4)

        return Monster(player_name="монстр",
                       creature_type=creature_type,
                       hp=random.randint(5,20),
                       features=features,
                       attack_strategy=AttackStrategy(fighter_type=int(creature_type)))
