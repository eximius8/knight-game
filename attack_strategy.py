"""Стратегии аттак."""
from abstract_classes import AbstractAttackStrategy


class AttackStrategy(AbstractAttackStrategy):

    def __init__(self, fighter_type) -> None:
        self.fighter_type = fighter_type

    def get_available_weapons(self, player):

        available_tools = {}
        if 1 in player.features:
            available_tools[1] = "меч"
        if 2 in player.features and 4 in player.features:
            available_tools[2] = "лук со стрелами"
        if 3 in player.features:
            available_tools[3] = "книга заклинаний"
        return available_tools

    def choose_weapon(self, player):
        available_tools = self.get_available_weapons(player)
        if len(available_tools) == 1:
            weapon = next(iter(available_tools))
            print(f"Атака оружием {available_tools[weapon]}...")
            return weapon
        while True:
            print("Выберите доступное оружее:")
            for key, weapon in available_tools.items():
                print(f"{key} - {weapon}")
            choice = input("Ваш выбор: ")
            if int(choice) in available_tools.keys():
                return int(choice)

    def attack(self, player, other):
        weapon = self.choose_weapon(player)
