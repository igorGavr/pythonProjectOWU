from random import choice, randint


class Player():

    def __init__(self, name):
        self.name = name
        self.__health = 100
        # self.__armor = 100
        self.protection = False
        self._max_damage = 50
        self._min_damage = 10

    def attack(self, target):
        dodge_list = [True, True, True, True, False]
        if isinstance(target, Player):
            if target.protection:
                print('Удар по щиті')
            else:
                if choice(dodge_list):
                    current_damage = randint(self._min_damage, self._max_damage)