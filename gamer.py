import random
import copy


class Gamer(object):
    cubes_value_list = [4, 6, 8, 10, 12, 20, 100]

    def reload_list(self, dick, current_pool):
        return [item for item in dick if item <= current_pool]

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
        self.current_attack = 0
        self.current_block = 0
        self.personal_heal = 0
        pass


# / ||константа пула
# / создание двух и более тактик выбора кубов хила и оттуда стратегий
# / соединить пулы в ините и в методах
# / оборонительная комбинорованная и наступательная стратегии соответсяственно 10%>=  10%< =<30%  30%< ил от пула
# / ||добавить выбор наибольшего значения про двух последних элементов пула вовремя разбивки пула
# / ||лучше брать 1к100 в хил если есть

# t = Gamer(500).
# print(t.coolman_pool_generation(60))
# print(t.heal_selection(t.coolman_pool_generation(60)))
