import random
import copy

from gamer import Gamer


def reload_list(work_list: list, pool_value_remainder: int) -> list:
    return [item for item in work_list if item <= pool_value_remainder]  # wtf its doing


class Coolman(Gamer):

    def __init__(self, pool_value: int):
        super().__init__(pool_value)
        self.coolman_pool_dict = {'4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '20': 0, '100': 0}
        self.coolman_pool_list = copy.deepcopy(self.cubes_value_list)
        self.coolman_pool = pool_value

    def coolman_pool_generation(self) -> dict:

        pool_value_remainder: int = self.coolman_pool

        while pool_value_remainder > 3:

            new_element = 0
            self.coolman_pool_list = reload_list(self.coolman_pool_list, pool_value_remainder)
            # print("reloded")

            if len(self.coolman_pool_list) == 2:
                new_element = max(self.coolman_pool_list)  # нет смысла брать меньшее,т.к цикл закончится

            else:

                try:
                    new_element = int(random.choice(self.coolman_pool_list))
                    # print("new_element add")

                except IndexError:
                    print("________IndexError________")

            pool_value_remainder -= new_element
            self.coolman_pool_dict[str(new_element)] += 1

        # если новое значение пула меньше заданного, необходимо обновить его
        self.coolman_pool = sum([int(key) * value for key, value in self.coolman_pool_dict.items()])

        return self.coolman_pool_dict

    def heal_selection(self) -> int:

        if self.coolman_pool_dict.get("100") >= 1 and self.coolman_pool > 103:

            self.personal_heal = 100  # лучше 100 быть хила не может, а тратить на атаку/защиту 1к100 жалко

        else:

            self.personal_heal = random.choice([int(item) for item in self.coolman_pool_dict.keys()
                                                if self.coolman_pool_dict.get(item) > 0])

        self.coolman_pool_dict[str(self.personal_heal)] -= 1

        self.DICT_ON_THIS_GAME = copy.deepcopy(self.coolman_pool_dict)  # THIS IS POINT OF COPY

        return self.personal_heal

    # выбор тактики боя в зависимости от значения хила
    def tactic_selection(self, action: str) -> int:

        if self.personal_heal <= 0.1 * self.coolman_pool:
            return self.small_heal_tactics(action)

        elif 0.1 * self.coolman_pool < self.personal_heal <= 0.2 * self.coolman_pool:
            return self.balanced_heal_tactics(action)

        elif self.personal_heal > 0.2 * self.coolman_pool:
            return self.high_heal_tactics(action)

    # занулить переменную атаки и блока!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def small_heal_tactics(self, action: str) -> int or str:

        self.current_attack = 0
        self.current_block = 0

        if action == 'block':
            self.current_block = max([int(item) for item in self.coolman_pool_dict.keys()
                                      if self.coolman_pool_dict.get(item) > 0])
            self.coolman_pool_dict[str(self.current_block)] -= 1
            return self.current_block

        elif action == 'attack':  # не ебу зачем тут баг стооит, но пусть будет
            self.current_attack = min([int(item) for item in self.coolman_pool_dict.keys()
                                       if self.coolman_pool_dict.get(item) > 0])
            self.coolman_pool_dict[str(self.current_attack)] -= 1
            return self.current_attack

        else:
            return "Error in tactics"

    def high_heal_tactics(self, action: str) -> int or str:

        self.current_attack = 0
        self.current_block = 0

        if action == 'block':
            self.current_block = min([int(item) for item in self.coolman_pool_dict.keys()
                                      if self.coolman_pool_dict.get(item) > 0])
            self.coolman_pool_dict[str(self.current_block)] -= 1
            return self.current_block

        elif action == 'attack':
            self.current_attack = max([int(item) for item in self.coolman_pool_dict.keys()
                                       if self.coolman_pool_dict.get(item) > 0])
            self.coolman_pool_dict[str(self.current_attack)] -= 1
            return self.current_attack

        else:
            return "Error in tactics"

    def balanced_heal_tactics(self, action: str) -> int or str:

        self.current_attack = 0
        self.current_block = 0

        if action == 'block':
            self.current_block = random.choice([int(item) for item in self.coolman_pool_dict.keys()
                                                if self.coolman_pool_dict.get(item) > 0])
            self.coolman_pool_dict[str(self.current_block)] -= 1
            return self.current_block

        elif action == 'attack':
            self.current_attack = random.choice([int(item) for item in self.coolman_pool_dict.keys()
                                                 if self.coolman_pool_dict.get(item) > 0])
            self.coolman_pool_dict[str(self.current_attack)] -= 1
            return self.current_attack

        else:
            return "Error in tactics"
