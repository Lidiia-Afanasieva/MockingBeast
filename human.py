import copy

from gamer import Gamer


class Human(Gamer):

    def __init__(self, pool_value: int):

        super().__init__(pool_value)
        self.human_pool_dict = {'4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '20': 0, '100': 0}
        self.human_pool_list = copy.deepcopy(self.cubes_value_list)
        self.human_pool = pool_value

    def dict_creation(self, human_list: list) -> None:

        self.human_pool_list = list(map(lambda item: int(item), human_list))
        self.human_pool_dict = dict(zip(self.human_pool_dict.keys(), self.human_pool_list))
