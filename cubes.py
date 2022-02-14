class Cubes(object):

    def __init__(self, value, count, PERSONAL_POOL):
        self.PERSONAL_POOL = PERSONAL_POOL
        self.value = value
        self.count = count

        pass

    # def cubes_rate_definition(self, value, PERSONAL_POOL):

    #     self.PERSONAL_POOL = PERSONAL_POOL
    #     if self.PERSONAL_POOL <= 50:
    #         if value == 2: self.value = 2
    #         elif value == 4: self.value = 8
    #         elif value == 6: self.value = 8
    #         elif value == 8: self.value = 6
    #         elif value == 10: self.value = 5
    #         elif value == 12: self.value = 2
    #         elif value == 20: self.value = 10
    #         else: self.value = 2
    #         pass
    #
    #     elif 50 < self.PERSONAL_POOL < 70:
    #         pass
    #
    #     elif 70 <= self.PERSONAL_POOL < 85:
    #         pass
    #
    #     elif 85 <= self.PERSONAL_POOL < 100:
    #         pass
    #
    #     elif self.PERSONAL_POOL >= 100:
    #         pass
    #
    #     pass

# / нужно соединить мейн с классом через количество кубов
# / кубу нужно задать коэф при разном значении пула
# / функция подсчёта коэфициента после вычета и возращение
# /