from abstract_classes import AbstractEncounter, AbstractFeatureFactory
import random



class Apple(AbstractEncounter):

    def encounter(self, creature):
        
        added_lives = random.randint(3,15)
        creature.hp = creature.hp + added_lives
        print(f"Вы нашли яблочко с {added_lives} жизнями. Теперь у вас {creature.hp} жизней.")


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
            input_message = f"""Вы нашли новое оружее: {self.name} силой {self.power}.        
                1 - взять
                2 - пройти мимо \n
                """
            choice = input(input_message)
            if choice == "1":
                creature.add_feature(self)
                print(f"У вас новое оружее! {self.name} силой {self.power}.")
                break
            elif choice == "2":
                break                
            else:
                print("Выберете.")


class RandomFeatureFactory(AbstractFeatureFactory):

    def create_feature(self):
        
        choice = random.randint(0,4)
        
        if choice == 0:
            return Apple()
        
        power = random.randint(5,15)
        weapons = {1: "меч", 2: "лук", 3: "стрелы", 4: "книга заклинаний" }
        return Weapon(power=power, name=weapons[choice], code=choice)
        
        
