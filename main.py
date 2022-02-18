# ПЕРВЫЙ ПУНКТ
# создание функции выбора пула и функции его проверки
# ||разбивка пула на кубы # можно рандомом вычислять какое значение куба выбрать и вычитать из пула
# ||пока ниодно не будет пропускаться
# ||вычисление хила (пусть пока по максимальному значению 3/4)
# определение первого хода рандомом
import random
from typing import Final

from human import Human
from coolman import Coolman
from cubes import Cubes

print("B MO")

print("Enter the pool value")

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

# создание данных человека
human_player = Human(POOL_VALUE)
human_player.dict_creation(input().split())

print("There is your pool: ", human_player.human_pool_dict)
print("Enter your heal value:")
human_player.personal_heal = int(input())

# создание данных компьютера
coolman_player = Coolman(POOL_VALUE)
coolman_player.coolman_pool_generation()
print('coolman_pool_dict :', coolman_player.coolman_pool_dict)
coolman_player.heal_selection()
print('personal_heal :', coolman_player.personal_heal)

gamer_list = [coolman_player, human_player]
random.shuffle(gamer_list)

while coolman_player.personal_heal > 0 and human_player.personal_heal > 0:

    if gamer_list[0] == human_player:
        print("Your turn. Enter the attack cube value")
        human_player.current_attack = int(input())
        coolman_player.tactic_selection(block)

    else:
        print("You are have been attacked. Enter your block cube value")
        human_player.current_block = int(input())
        coolman_player.tactic_selection(attack)


# сделано создание словаря у человека
# дальше оформлять мейн, и классы игроков по пути.
# рандомайзер

# !!! если значение пула будет 100 - 103 и как хил будет выбрана 100, то комп проиграет, надо исправить


# 2 0 3 0 1 2 0