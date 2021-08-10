"""Модели для инвентаря (артефактов)."""
from abstract_classes import AbstractEncounter, AbstractFeatureFactory
import random


class Apple(AbstractEncounter):
    """Артефакт яблочко - при поедании число жизней возрастает."""

    def encounter(self, creature):
        """Встреча игрока с яблочком.

            creature - модель игрока.
            По итогу встречи число жизней увеличивается."""
        added_lives = random.randint(3,15)
        creature.hp = creature.hp + added_lives
        print(f"Вы нашли яблочко с {added_lives} жизнями. Теперь у вас {creature.hp} жизней.")


class Totem(AbstractEncounter):

    def __init__(self) -> None:
        self.code = 5

    def __str__(self) -> str:
        return "тотем"

    def save_game(self, player):
        self.player = player.deepcopy()

    def encounter(self, creature):
        while True:
            print("Вы нашли тотем")
            print("\n1 - взять тотем \n2 - пройти мимо\n")
            choice = input("Ваш выбор: ")
            if choice == "1":
                # self.save_game(creature)
                creature.add_feature(self)
                print("Вы взяли тотем!")
                break
            elif choice == "2":
                break


class Weapon(AbstractEncounter):

    def __init__(self, power, name, code) -> None:
        self.power = power
        self.name = name
        self.code = code
        super().__init__()

    def __str__(self):
        return f"{self.name} силой {self.power}"

    def encounter(self, creature):

        while True:
            print(f"Вы нашли новое оружее: {self.name} силой {self.power}.")
            print("1 - взять\n2 - пройти мимо\n")
            choice = input("Ваш выбор: ")
            if choice == "1":
                creature.add_feature(self)
                print(f"У вас новое оружее! {self.name} силой {self.power}.")
                break
            elif choice == "2":
                break


class FeatureFactory(AbstractFeatureFactory):

    def create_random_feature(self):

        choice = random.randint(0,5)

        if choice == 0:
            return Apple()
        elif choice == 5:
            return Totem()
        power = random.randint(5,15)
        weapons = {1: "меч", 2: "лук", 3: "книга заклинаний", 4: "стрелы"}
        return Weapon(power=power, name=weapons[choice], code=choice)

    def create_weapon(self, weapon_code):
        weapons = {1: "меч", 2: "лук", 3: "книга заклинаний", 4: "стрелы"}
        return Weapon(power=random.randint(5,15),
                      name=weapons[weapon_code],
                      code=weapon_code)
