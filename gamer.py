class Gamer(object):

    cubes_value_list = [4, 6, 8, 10, 12, 20, 100]

    def __init__(self, pool_value):

        self.pool_value = pool_value
        self.DICT_ON_THIS_GAME = {}
        self.current_attack = 0
        self.current_block = 0
        self.personal_heal = 0

