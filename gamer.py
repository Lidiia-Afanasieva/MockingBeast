import random
import copy
import time


class Gamer(object):
    cubes_value_list = [4, 6, 8, 10, 12, 20, 100]

    def reload_list(self, dick, pool_value_remainder):
        return [item for item in dick if item <= pool_value_remainder]  # wtf its doing

    # @staticmethod
    # def heal_selection(self, coolman_pool_dict):
    #     if coolman_pool_dict.get("100") >= 1:
    #         personal_heal = 100
    #     else:
    #         personal_heal = random.choice([int(item) for item in coolman_pool_dict.keys()
    #                                        if coolman_pool_dict.get(item) > 0])
    #
    #     return personal_heal

    def __init__(self, pool_value):
        # self.coolman_pool_dict = coolm
        self.dict_on_this_game_const = {}
        self.current_attack = 0
        self.current_block = 0
        self.personal_heal = 0
        pass
