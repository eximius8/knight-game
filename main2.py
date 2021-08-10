from player_models import Player, MonsterFactory
import random

from custom_exceptions import GameWonException, GameLostException
from feature_models import RandomFeatureFactory


player = Player()
random_feature_factory = RandomFeatureFactory()
monster_factory = MonsterFactory()


while True:
    monster = monster_factory.create_creature()
    feature = random_feature_factory.create_feature()
    encounter = random.choice([monster, feature])

    encounter.encounter(player)

    try:
        player.check_status()
    except GameWonException:
        print("Ура, вы победили.")
        break
    except GameLostException:
        print("Вы проиграли.")
        break