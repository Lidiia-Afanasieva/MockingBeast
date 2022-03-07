import random
import time
from typing import Final

from human import Human
from coolman import Coolman
from cubes import Cubes

everyone_is_alive = True


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


def look_at_battle_score():

    human_player.reload_list()
    print('///')
    print('Your heal at this moment is :', human_player.personal_heal)
    print('Your available cubes now :', human_player.human_pool_dict)
    print('///')
    print('Your opponent heal at this moment is :', coolman_player.personal_heal)
    print('///')

    return 0


# ПОДУМАТЬ ЕЩЁ РАЗ ПРО ОКОНЧАНИЯ КУБОВ, НО НЕ ОКОНЧАНИЕ ХИЛА ,,, ВПИСАННЫЙ ЦИКЛ??
# ВООБЩЕ КРАСИВО БЫЛО БЫ ПОТОМ НАПИСАТЬ БД ВОЗМОЖНЫХ ОТВЕТОВ КОМПА НА РАЗНЫЕ ПУНКТЫ, ЧТОБЫ НЕ ЗАМАЗОЛИЛО ГЛАЗА
# ВООБЩЕ ПОСВЕЖЕМУ НУЖНО ГЛЯНУТЬ НА АРХИТЕКТУРУ ИБО ОНА КОСТЫЛЬНАЯ
# ДА И КОД БОЛЕЕ... ПРОФИ СДЕЛАТЬ... БЫЛО БЫ КЛАССНО ДЕКОРАТОРЫ ТАМ ВПИХНУТЬ, АНОТАЦИИ
# TESTS
# DELETE CUBES FILE

# ADD CHECK OF EMPTY DICTS. OUTPUT THAT GAMER IS EMPTY
def human_attack():
    human_player.current_attack = int(input("Your turn. Enter the attack cube value "))
    coolman_player.tactic_selection('block')
    print("You have been blocked with :", coolman_player.current_block)
    input("Roll cubes?")
    intrigue_maker()
    damage, attack_value, block_value = cubes_roll(human_player.current_attack, coolman_player.current_block)
    human_player.human_pool_dict[str(human_player.current_attack)] -= 1

    if damage > 0:
        coolman_player.personal_heal -= damage
        print('Human side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


# ADD CHECK OF EMPTY DICTS. OUTPUT THAT GAMER IS EMPTY
def coolman_attack():
    human_player.current_block = int(input("Your turn. Enter the block cube value "))
    coolman_player.tactic_selection('attack')
    print("You have been attacked with :", coolman_player.current_attack)
    input("Roll cubes?")
    intrigue_maker()
    damage, attack_value, block_value = cubes_roll(coolman_player.current_attack, human_player.current_block)
    human_player.human_pool_dict[str(human_player.current_block)] -= 1

    if damage > 0:
        human_player.personal_heal -= damage
        print('Human side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


# ////////////////////////////////////////////////////////////
# START
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

human_player.dict_on_this_game_const.deepcopy(human_player.human_pool_dict)

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


# END THIIIIIIIIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_the_dicks():

    if sum(human_player.human_pool_dict.items()) > 0 and sum(coolman_player.coolman_pool_dict.items()) > 0:
        pass

while everyone_is_alive:
    # продумать окончание кубов, но не окончание хила

    check_the_dicks()

    if gamer_list[0] == human_player:

        human_attack()
        look_at_battle_score()

        if coolman_player.personal_heal > 0 and human_player.personal_heal > 0:

            coolman_attack()
            look_at_battle_score()

        # MAKE THE WINNER FUNCTION
        # MAKE CHEKKING END OF CUBES FUNCTION

        else:

            everyone_is_alive = False
            # нужно придумать как поочерёдно передавать ход

    else:
        coolman_attack()
        look_at_battle_score()

        if coolman_player.personal_heal > 0 and human_player.personal_heal > 0:

            human_attack()
            look_at_battle_score()

        else:

            everyone_is_alive = False

# !!! если значение пула будет 100 - 103 и как хил будет выбрана 100, то комп проиграет, надо исправить (regeneration)


# 2 0 3 0 1 2 0
