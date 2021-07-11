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


def game():
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
        print('=============================\n')
        if monster_counter:
            print(f'{monster_counter} чудовище убито\n')

        act = random.randint(1, 3)
        choice = ""
        if act == 1:
            addedhp = random.randint(2, 6)
            hp += addedhp
            print(f'Вы съели яблочко с {addedhp} жизнями, теперь у вас {hp} жизней')

        elif act == 2:
            newattack = random.randint(4, 15)
            print(f'Вы нашли МЕЧ силой {newattack}, сила вашего меча: {attack}')

            while choice not in ['1', '2']:
                choice = input(f"1 - взять МЕЧ силой {newattack}, 2 - оставить МЕЧ силой {attack}: ")
            if choice == '1':
                attack = newattack
        else:
            monsterhp = random.randint(5, 19)
            monsterattack = random.randint(5, 18)
            print("БОЙ, вы встретили чудовище с количеством жизней {monsterhp} и силой: {monsterattack}")
            while choice not in ['1', '2']:
                choice = input("1 - драться (у вас {hp} жизней и меч силой {attack}), 2 - убежать: ")
            if choice == '1':
                if attack < monsterhp:
                    hp = 0
                monster_counter += 1
                hp -= monsterattack

        if hp <= 0:
            print("ПОРАЖЕНИЕ")
            break

        if monster_counter >= 10:
            print("ПОБЕДА!")
            break


game()
