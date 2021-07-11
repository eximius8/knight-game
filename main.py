import random


monster_counter = 0
hp = 10
attack = 10


def game():
    global monster_counter
    global hp
    global attack
   
    while True:
        act = random.randint(1,3)
        if act == 1:
            print('Вы съели яблочко!')
            hp += random.randint(2,6)
        elif act == 2:
            newattack = random.randint(4,10)
            print(f'Вы нашли МЕЧ силой {newattack}, сила вашего меча: {attack}')
            choice = ""
            if choice not in ['1','2']:
                choice = input(f"1 - взять МЕЧ силой {newattack}, 2 - оставить МЕЧ силой {attack}")
            if choice == '1':
                attack = newattack

        
        if hp <= 0:
            print("ПОРАЖЕНИЕ")
            break 


        if monster_counter >= 10:
            print("ПОБЕДА")
            break
            
