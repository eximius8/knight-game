"""Для классов игроков, монстров и инвентаря."""
from abc import ABC, abstractmethod
import random
from custom_exceptions import GameLostException, GameWonException
from abstract_classes import AbstractCreature, AbstractEncounter,  AbstractCreatureFactory

    
class Monster(AbstractCreature, AbstractEncounter):

    def encounter(self, player):
        intro_text = f"""Вы встретили монстра с числом жизней {self.hp}:
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


        

class Player(AbstractCreature):        

    def __init__(self):       
        intro_text = """Кем хотите играть:
            1 - войном
            2 - лучником
            3 - магом
            """
        self.monsters_killed = 0
        self.features = {1: "Меч"}
        while True:
            choice = input(intro_text)
            if choice in {"1": "Воин", "2": "Лучник", "3": "Маг"}.keys():
                super().__init__(creature_type=int(choice), hp=10)
                break
            else:
                print("Выберете.")
    
    def add_feature(self, choice, human_readable):
        self.features[choice] = human_readable

    
    def check_status(self):
        if self.hp < 1:
            raise GameLostException
        if self.monsters_killed > 9:
            raise GameWonException




class MonsterFactory(AbstractCreatureFactory):

    def create_creature(self) -> Monster:

        return Monster(creature_type=random.randint(1,3), hp=random.randint(5,20))



