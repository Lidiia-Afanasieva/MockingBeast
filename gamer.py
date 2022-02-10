import random

class Gamer(object):

    cubes_value_list = [4, 6, 8, 10, 12, 20, 100]

    def reload_list(self, dick, current_pool):
        return [item for item in dick if item <= current_pool]


    def coolman_pool_generation(self, pool_value):
        coolman_pool_dict = {'4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '20': 0, '100': 0}
        coolman_pool_list = [4, 6, 8, 10, 12, 20, 100]

        while pool_value > 3:

            new_element = 0
            coolman_pool_list = self.reload_list(coolman_pool_list, pool_value)

            try:
                new_element = int(random.choice(coolman_pool_list))
            except IndexError:
                print("IndexError")

            pool_value -= new_element
            coolman_pool_dict[str(new_element)] += 1
            print(coolman_pool_list)

            # pool_value - int(coolman_pool.keys()
            # map(lambda coolman_pool_value(random.random(0, 6)) : )

        return coolman_pool_dict

    def __init__(self, personal_pool):
        print("!")
        pass



# / ||константа пула
# / создание двух и более тактик выбора кубов хила и оттуда стратегий
# / соединить пулы в ините и в методах
# / оборонительная комбинорованная и наступательная стратегии соответсяственно 10%>=  10%< =<30%  30%< ил от пула
# / добавить выбор наибольшего значения про двух последних элементов пула вовремя разбивки пула
# / лучше брать 1к100 в хил если есть

t = Gamer(500)
print(t.coolman_pool_generation(500))