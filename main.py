# ПЕРВЫЙ ПУНКТ
# создание функции выбора пула и функции его проверки
# ||разбивка пула на кубы # можно рандомом вычислять какое значение куба выбрать и вычитать из пула
# ||пока ниодно не будет пропускаться
# ||вычисление хила (пусть пока по максимальному значению 3/4)
# определение первого хода рандомом

from typing import Final

from human import Human
from coolman import Coolman
from cubes import Cubes

print("B MO")

try:
    POOL_VALUE: Final = int(input())  # mypy
except ValueError:
    print("Pool value error.")

print("You can enter any count of cubes, but its sum must be less then pool value.(4, 6, 8, 10, 12, 20, 100)")
print("Example: 0 3 0 4 1 2 0 Means count 1d4 = 0 1d6 = 3 and etc. Sum of your pool = 288")
print("Its OK if current Pool Value is 288 or more, else piss of")

# пока хз думаю лучше засунуть в юнит тесты человеческого файла
# def check_cubes(gamer_cube_arr):
#     if sum(gamer_cube_arr) > POOL_VALUE:
#         return 0
#     else:
#         return 1

# ||создать константу для значения пула игрока
# ||возможно создание класса игрока с пропиской этой константы и дальнейших функций

new_player = Human(POOL_VALUE)
print(input().split())
new_player.dict_creation(input().split())

print("There is your pool: ", new_player.human_pool_dict)
# сделано создание словаря у человека
# дальше оформлять мейн, и классы игроков по пути
# рандомайзер


