from player_models import Player
from monster_models import MonsterFactory
import random

from custom_exceptions import GameWonException, GameLostException
from feature_models import FeatureFactory


player = Player()
feature_factory = FeatureFactory()
monster_factory = MonsterFactory()


while True:
    monster = monster_factory.create_creature()
    feature = feature_factory.create_random_feature()
    nex_step = random.choice([monster, feature])

    nex_step.encounter(player)

    try:
        player.check_status()
    except GameWonException:
        print("Ура, вы победили.")
        break
    except GameLostException:
        print("Вы проиграли.")
        break
