from player_models import *
from custom_exceptions import GameWonException, GameLostException


player = Player()


while True:
    try:
        player.check_status()
    except GameWonException:
        print("Ура, вы победили.")
        break
    except GameLostException:
        print("Вы проиграли.")
        break