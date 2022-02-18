from gamer import Gamer
import random
import copy


class Coolman(Gamer):

    def __init__(self, pool_value):
        super().__init__(pool_value)
        self.coolman_pool_dict = {'4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '20': 0, '100': 0}
        self.coolman_pool_list = copy.deepcopy(self.cubes_value_list)
        self.coolman_pool = pool_value
        self.personal_heal = 0

    def coolman_pool_generation(self):
        pool_value_remainder = self.coolman_pool

        while pool_value_remainder > 3:

            new_element = 0
            self.coolman_pool_list = self.reload_list(self.coolman_pool_list, pool_value_remainder)

            if len(self.coolman_pool_list) == 2:
                new_element = max(self.coolman_pool_list)  # нет смысла брать меньшее,т.к цикл закончится
            else:
                try:
                    new_element = int(random.choice(self.coolman_pool_list))
                except IndexError:
                    print("IndexError")

            pool_value_remainder -= new_element
            self.coolman_pool_dict[str(new_element)] += 1

        # если новое значение пула меньше заданного, необходимо обновить его
        self.coolman_pool = sum([int(key) * value for key, value in self.coolman_pool_dict.items()])

        return self.coolman_pool_dict

    def heal_selection(self):
        if self.coolman_pool_dict.get("100") >= 1:
            self.personal_heal = 100 # лучше 100 быть хила не может, а тратить на атаку/защиту 1к100 жалко
        else:
            self.personal_heal = random.choice([int(item) for item in self.coolman_pool_dict.keys()
                                           if self.coolman_pool_dict.get(item) > 0])

        return self.personal_heal

    # выбор тактики боя в зависимости от значения хила
    def tactic_selection(self, ):

        if self.heal_selection <= 0.1 * self.personal_heal:
            return self.small_heal_tactics()

        elif 0.1 * self.personal_heal < self.heal_selection <= 0.2 * self.personal_heal:
            return self.balanced_heal_tactics()

        elif self.heal_selection > 0.2 * self.personal_heal:
            return self.high_heal_tactics()

    def small_heal_tactics(self):

        pass

    def high_heal_tactics(self):

        pass

    def balanced_heal_tactics(self):

        pass

    pass
