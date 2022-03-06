import random
import time
from typing import Final

from human import Human
from coolman import Coolman
from cubes import Cubes


def intrigue_maker():
    print("ROLL.")
    time.sleep(1)
    print("ROLL..")
    time.sleep(1)
    print("ROLL...")
    return 0


def cubes_roll(attack_cube, block_cube):
    attack_value = random.randint(1, attack_cube)
    block_value = random.randint(1, block_cube)

    if attack_value > block_value:
        return attack_value - block_value, attack_value, block_value

    else:
        return 0, attack_value, block_value

# НУЖНО ТАКУЮЮ ДЛЯ КУЛМАНА
# ПОДУМАТЬ ЕЩЁ РАЗ ПРО ОКОНЧАНИЯ КУБОВ, НО НЕ ОКОНЧАНИЕ ХИЛА ,,, ВПИСАННЫЙ ЦИКЛ??
# ВООБЩЕ КРАСИВО БЫЛО БЫ ПОТОМ НАПИСАТЬ БД ВОЗМОЖНЫХ ОТВЕТОВ КОМПА НА РАЗНЫЕ ПУНКТЫ, ЧТОБЫ НЕ ЗАМАЗОЛИЛО ГЛАЗА
# ВООБЩЕ ПОСВЕЖЕМУ НУЖНО ГЛЯНУТЬ НА АРХИТЕКТУРУ ИБО ОНА КОСТЫЛЬНАЯ
# ДА И КОД БОЛЕЕ... ПРОФИ СДЕЛАТЬ... БЫЛО БЫ КЛАССНО ДЕКОРАТОРЫ ТАМ ВПИХНУТЬ, АНОТАЦИИ

def human_attack():
    # print("Your turn. Enter the attack cube value")
    human_player.current_attack = int(input("Your turn. Enter the attack cube value "))
    coolman_player.tactic_selection('block')
    print("You have been blocked with :", coolman_player.current_block)
    input("Roll cubes?")
    intrigue_maker()
    damage, attack_value, block_value = cubes_roll(human_player.current_attack, coolman_player.current_block)
    if damage > 0:
        coolman_player.personal_heal -= damage
        print('Human side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


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


# создание данных человека
human_player = Human(POOL_VALUE)
human_player.dict_creation(input().split())

print("There is your pool: ", human_player.human_pool_dict)
print("Enter your heal value:")
human_player.personal_heal = int(input())

# создание данных компьютера
coolman_player = Coolman(POOL_VALUE)
coolman_player.coolman_pool_generation()
print('coolman_pool_dict :', coolman_player.coolman_pool_dict)  # delete after
coolman_player.heal_selection()
print('personal_heal :', coolman_player.personal_heal)  # delete after

gamer_list = [coolman_player, human_player]
random.shuffle(gamer_list)  # надо будет вывести отдельно in func чтобы менять очерёдность после опкончания кубов?

while coolman_player.personal_heal > 0 and human_player.personal_heal > 0:
    # продумать окончание кубов, но не окончание хила

    if gamer_list[0] == human_player:
        human_attack()

        # нужно придумать как поочерёдно передавать ход

    else:
        # print("You are have been attacked. Enter your block cube value")
        human_player.current_block = int(input("You are have been attacked. Enter your block cube value "))
        coolman_player.tactic_selection('attack')

# output of current value of hill and pool_dict

# !!! если значение пула будет 100 - 103 и как хил будет выбрана 100, то комп проиграет, надо исправить (regeneration)


# 2 0 3 0 1 2 0
