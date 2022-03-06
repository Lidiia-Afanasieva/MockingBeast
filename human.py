from gamer import Gamer
import random
import copy


# определить общие методы

class Human(Gamer):
    def __init__(self, pool_value):
        super().__init__(pool_value)
        self.human_pool_dict = {'4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '20': 0, '100': 0}
        self.human_pool_list = copy.deepcopy(self.cubes_value_list)
        self.human_pool = pool_value
        pass

    def dict_creation(self, human_list: list):
        self.human_pool_list = human_list
        self.human_pool_dict = dict(zip(self.human_pool_dict.keys(), human_list))
        return 0
