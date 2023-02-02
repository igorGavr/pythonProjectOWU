from random import choice, randint


class Player():

    def __init__(self, name):
        self.name = name
        self.__health = 100
        # self.__armor = 100
        self.protection = False
        self._max_damage = 50
        self._min_damage = 10
        self.protection_count = 3

    def attack(self, target):
        dodge_list = [True, True, True, True, False]
        if isinstance(target, Player):
            if target.protection:
                print('Удар по щиті')
                self.protection_count -= 1
                target.protection = False
            else:
                if choice(dodge_list):
                    current_damage = randint(self._min_damage, self._max_damage)
                    target.health_minus(current_damage)
                    print(f'{target.name} отримав {current_damage} урону')
                    target.get_player_info()
                    target.check_health_status()
                else:
                    print(f'{self.name} промахнувся!')
        else:
            print('Ви не можете атакувати цю ціль')

    def health_minus(self, damage_amount):
        self.__health -= damage_amount

    def check_health_status(self):
        if self.__health <= 0:
            print(f'{self.name} програв гру')
            exit(1)

    def get_player_info(self):
        print(f'Стан життя {self.name} - {self.__health} HP')

    def active_protection(self):
        if self.protection_count > 0:
            self.protection = True
            print('Щит активований')
        else:
            print('У вас не залишилося захисту')

    def off_protection(self):
        self.protection = False

print('Start game')
name1 = 'Jimi'
name2 = 'Ivan'
