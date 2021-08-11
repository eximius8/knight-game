"""Стратегии аттак."""
from abstract_classes import AbstractAttackStrategy
from constants import weapons

class AttackStrategy(AbstractAttackStrategy):

    def __init__(self, fighter_type) -> None:
        self.fighter_type = fighter_type

    def get_available_weapons(self, player):

        available_tools = {}
        if 1 in player.features:
            available_tools[1] = weapons[1]
        if 2 in player.features and 4 in player.features:
            available_tools[2] = weapons[2]
        if 3 in player.features:
            available_tools[3] = weapons[3]
        return available_tools

    def choose_weapon(self, player):
        available_tools = self.get_available_weapons(player)
        if len(available_tools) == 1:
            weapon = next(iter(available_tools))
            print(f"{player.player_name}-{player.name} атакует оружием {available_tools[int(weapon)]}...")
            return weapon
        while True:
            print("Выберите доступное оружее:")
            for key, weapon in available_tools.items():
                print(f"{key} - {weapon}")
            choice = input("Ваш выбор: ")
            if int(choice) in available_tools.keys():
                print(f"{player.player_name}-{player.name} атакует оружием {available_tools[int(choice)]}...")
                return int(choice)

    def attack(self, player, other):
        weapon_player = self.choose_weapon(player)
        attack_player = player.features[weapon_player].power
        attack_player
