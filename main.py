"""
Программа, реализующая игру про рыцаря и монстров.

Глобальные переменные:
    int monster_counter - число убитых монстров
    int hp - число жизней рыцаря
    int attack - сила атаки рыцаря
"""

import random

monster_counter = 0
hp = 10
attack = 10


def game() -> None:
    """Функция начинающая игру.

    внутренние переменные:
    int act - принимает любое значение из списка [1,2,3]. Определяет что встречается рыцарю:
            1 - яблочко
            2 - меч
            3 - чудовище
    str choice - варианты дейтсвий вводимые с клавиатуры пользователем
    int addedhp - количество добавленных жизней от яблочка
    int newattack - сила удара найденого меча
    int monsterhp - число жизней чудовища
    int monsterattack - сила удара чудовища.
    """
    global monster_counter
    global hp
    global attack

    while True:
       
        act = random.randint(1, 3)
        choice = ""
        if act == 1:
            addedhp = random.randint(1, 2)
            hp += addedhp
            print(f"Вы съели яблочко с {addedhp} жизнями, теперь у вас {hp} жизней")

        elif act == 2:
            newattack = random.randint(4, 15)
            print(f"Вы нашли МЕЧ силой {newattack}, сила вашего меча: {attack}")

            while True:
                choice = input(f"1 - взять МЕЧ силой {newattack}, 2 - оставить МЕЧ силой {attack}: ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("Введите 1 или 2.")
            if choice == "1":
                attack = newattack
        else:
            monsterhp = random.randint(5, 19)
            monsterattack = random.randint(5, 18)
            print(f"БОЙ, вы встретили чудовище с количеством жизней {monsterhp} и силой: {monsterattack}")
            while True:
                choice = input(f"1 - драться (у вас {hp} жизней и меч силой {attack}), 2 - убежать: ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("Введите 1 или 2.")
            if choice == "1":
                if attack < monsterhp:
                    print('ПОРАЖЕНИЕ! игра окончена')
                    break
                monster_counter += 1
                hp -= monsterattack

        if hp <= 0:
            print("ПОРАЖЕНИЕ! игра окончена")
            break

        if monster_counter >= 10:
            print("ПОБЕДА")
            break

#game()