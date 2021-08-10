import random
from abstract_classes import AbstractCreature, AbstractEncounter, AbstractCreatureFactory
from feature_models import FeatureFactory


class Monster(AbstractCreature, AbstractEncounter):

    def is_alive(self):
        if self.hp > 0:
            return True
        print("Монстр повержен!")
        return False

    def encounter(self, player):
        intro_text = f"""Ваш противник: {self.name} с числом жизней {self.hp}:
1 - драться
2 - бежать
"""
        while True:
            choice = input(intro_text)
            if choice == "1":
                break

            elif choice == "2":
                break
            else:
                print("Выберете.")


class MonsterFactory(AbstractCreatureFactory):

    def create_creature(self) -> Monster:
        creature_type = random.randint(1,3)
        feature_factory = FeatureFactory()
        features = {1: feature_factory.create_weapon(creature_type)}
            
        if creature_type == 2:
            features[3] = feature_factory.create_weapon(3)

        return Monster(creature_type=creature_type,
                       hp=random.randint(5,20),
                       features=features)