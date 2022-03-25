import copy
import random
import time
from typing import Optional

from coolman import Coolman
from human import Human

everyone_is_alive = True
POOL_VALUE: Optional[int] = 0  # пока только объявлена, но не инициализирована


human_player = Human(POOL_VALUE)
coolman_player = Coolman(POOL_VALUE)
gamer_list = [coolman_player, human_player]


def human_character_initialisation():
    global POOL_VALUE

    # создание данных человека
    human_player.dict_creation(input().split())

    print("There is your pool: ", human_player.human_pool_dict)
    print("There is colman: ", coolman_player.coolman_pool_dict)  # DELETE THAN ACTUALLY
    human_player.personal_heal = int(input("Enter your heal value: "))
    human_player.human_pool = POOL_VALUE
    print('pool =', human_player.human_pool)
    human_player.human_pool_dict[str(human_player.personal_heal)] -= 1
    human_player.DICT_ON_THIS_GAME = copy.deepcopy(human_player.human_pool_dict)  # THIS IS POINT OF COPY

    return 0


def coolman_character_initialisation():
    global POOL_VALUE

    # создание данных компьютера
    print(coolman_player.coolman_pool_dict)
    coolman_player.coolman_pool = POOL_VALUE
    coolman_player.coolman_pool_generation()
    print(coolman_player.coolman_pool_dict)
    coolman_player.heal_selection()

    return 0
# 3 1 0 0 0 0 0


def output_start_of_the_game():
    global POOL_VALUE

    print("B MO")

    POOL_VALUE = int(input("Enter the pool value : "))
    print('POOL_VALUE :', POOL_VALUE)

    print("You can enter any count of cubes, but its sum must be less then pool value.(4, 6, 8, 10, 12, 20, 100)")
    print("Example: 0 3 0 4 1 2 0 Means count 1d4 = 0 1d6 = 3 and etc. Sum of your pool = 288")
    print("Its OK if current Pool Value is 288 or less, else piss of")

    human_character_initialisation()
    coolman_character_initialisation()

    random.shuffle(gamer_list)


def reload_dict(work_dict: dict) -> dict:
    return dict(filter(lambda item: item[1] > 0, work_dict.items()))  # perfection


def intrigue_maker():

    print("ROLL.")
    time.sleep(1)
    print("ROLL..")
    time.sleep(1)
    print("ROLL...")
    time.sleep(1)

    return 0


def cubes_roll(attack_cube: int, block_cube: int) -> tuple:

    attack_value = random.randint(1, attack_cube)

    if block_cube != 0:
        block_value = random.randint(1, block_cube)
    else:
        block_value = block_cube

    if attack_value > block_value:
        return attack_value - block_value, attack_value, block_value

    else:
        return 0, attack_value, block_value


def output_battle_score() -> None:

    reload_dict(human_player.human_pool_dict)  # NOT SURE IN THE PLACE OF FUNC
    time.sleep(1)
    print('///')
    print('Your heal at this moment is :', human_player.personal_heal)
    print('Your available cubes now :', human_player.human_pool_dict)
    time.sleep(1)
    print('///')
    print('Your opponent heal at this moment is :', coolman_player.personal_heal)
    print('///')


def check_empty_dicts() -> int:

    if sum(list(human_player.human_pool_dict.values())) < 1 and sum(list(coolman_player.coolman_pool_dict.values())) < 1:
        print("BOTH PLAYERS POOL IS ENDED")
        return 1

    elif sum(list(human_player.human_pool_dict.values())) > 0 and sum(list(coolman_player.coolman_pool_dict.values())) < 1:
        print('COMPUTER POOL IS ENDED')

        return 2

    elif sum(list(human_player.human_pool_dict.values())) < 1 and sum(list(coolman_player.coolman_pool_dict.values())) > 0:
        print('HUMANS POOL IS ENDED')
        return 3

    else:
        return 0


def check_heal():
    global everyone_is_alive

    if coolman_player.personal_heal < 1 and human_player.personal_heal < 1:
        everyone_is_alive = False
    return everyone_is_alive


def print_calculation_of_human_attack() -> None:

    damage, attack_value, block_value = cubes_roll(human_player.current_attack, coolman_player.current_block)
    human_player.human_pool_dict[str(human_player.current_attack)] -= 1

    if damage > 0:
        coolman_player.personal_heal -= damage

        time.sleep(1)

        print('Human side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


# ADD CHECK OF EMPTY DICTS. OUTPUT THAT GAMER IS EMPTY// maybe as a check
def human_attack() -> None:

    time.sleep(1)
    human_player.current_attack = int(input("Your turn. Enter the attack cube value "))
    coolman_player.tactic_selection('block')
    print("You have been blocked with :", coolman_player.current_block)
    input("Roll cubes?")
    intrigue_maker()

    print_calculation_of_human_attack()


def print_calculation_of_coolman_attack() -> None:

    damage, attack_value, block_value = cubes_roll(coolman_player.current_attack, human_player.current_block)
    human_player.human_pool_dict[str(human_player.current_block)] -= 1

    if damage > 0:
        human_player.personal_heal -= damage
        time.sleep(1)
        print('Coolman side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        time.sleep(1)
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


# ADD CHECK OF EMPTY DICTS. OUTPUT THAT GAMER IS EMPTY// maybe as a check
def coolman_attack() -> None:
    time.sleep(1)

    human_player.current_block = int(input("Your turn. Enter the block cube value "))
    coolman_player.tactic_selection('attack')
    print("You have been attacked with :", coolman_player.current_attack)
    input("Roll cubes?")
    intrigue_maker()

    print_calculation_of_coolman_attack()


# ////////////////////////////////////////////////////////////
# START
# ////////////////////////////////////////////////////////////

output_start_of_the_game()

while everyone_is_alive:

    while check_empty_dicts() != 1 and everyone_is_alive:

        check_the_dicks = check_empty_dicts()

        # coolman empty
        if check_the_dicks == 2 and everyone_is_alive:

            time.sleep(1)

            print('Well, your opponent ended all his cubes, so now all your cubes will attack him.')
            print('Enjoy.')
            print('...')
            print('Your cubes now: ', human_player.human_pool_dict)
            intrigue_maker()
            start_heal = coolman_player.personal_heal

            for key, value in human_player.human_pool_dict.items():
                if value > 0:
                    for i in range(value):
                        damage, attack_value, block_value = cubes_roll(int(key), 0)
                        coolman_player.personal_heal -= damage
                        print('Your cube: {0}, its damage: {1}'.format(int(key), damage))

            print('Finally, damage is:', start_heal - coolman_player.personal_heal)

            if coolman_player.personal_heal < 1:
                print('COMPUTER HEAL IS ENDED')
                everyone_is_alive = False

        # human empty
        elif check_the_dicks == 3 and everyone_is_alive:

            time.sleep(1)

            print('Well, you ended all your cubes, so now your opponent will attack you with all his cubes.')
            print('Good luck.')
            intrigue_maker()
            start_heal = human_player.personal_heal

            for key, value in coolman_player.coolman_pool_dict.items():
                if value > 0:
                    for i in range(value):
                        damage, attack_value, block_value = cubes_roll(int(key), 0)
                        human_player.personal_heal -= damage
                        print('His cube: {0}, its damage: {1}'.format(int(key), damage))

            time.sleep(1)

            print('Finally, damage is:', start_heal - coolman_player.personal_heal)

            if human_player.personal_heal < 1:
                print("HA-HA\nHUMAN PLAYER HEAL IS ENDED")
                everyone_is_alive = False
            print(everyone_is_alive)

        else:

            if gamer_list[0] == human_player and check_empty_dicts() == 0:

                human_attack()
                output_battle_score()

                if check_heal() and check_empty_dicts() == 0:

                    coolman_attack()
                    output_battle_score()

            elif check_empty_dicts() == 0:

                coolman_attack()
                output_battle_score()

                if check_heal() and check_empty_dicts() == 0:

                    human_attack()
                    output_battle_score()

    print('\nNow you or your opponent are empty.\n')

    if everyone_is_alive:

        print('///')
        print('NEXT ROUND')
        print('///')
        coolman_player.coolman_pool_dict = coolman_player.DICT_ON_THIS_GAME
        human_player.human_pool_dict = human_player.DICT_ON_THIS_GAME
        output_battle_score()

if not everyone_is_alive:

    if coolman_player.personal_heal > human_player.personal_heal:
        print('SO YOU ARE DEAD NOW')

        time.sleep(1)

        print('YOU ARE FUCKIN PIECE OF SHIT')
        print('YOU LOOSE THIS GAME')
        print('STUPID COMPUTER WIN')

    elif coolman_player.personal_heal < human_player.personal_heal:

        print('Okay, you win')

        time.sleep(1)

        print('Im surprised. You make not only mistakes.')
        print('Like your parents, when they gave a life to you.')

    else:

        print('Well, I dont know whata happened')
        print('But anyway... You are an idiot')


# ещё там что-то доделать надо в coolman.py

# ВООБЩЕ КРАСИВО БЫЛО БЫ ПОТОМ НАПИСАТЬ БД ВОЗМОЖНЫХ ОТВЕТОВ КОМПА НА РАЗНЫЕ ПУНКТЫ, ЧТОБЫ НЕ ЗАМАЗОЛИЛО ГЛАЗА
# ВООБЩЕ ПОСВЕЖЕМУ НУЖНО ГЛЯНУТЬ НА АРХИТЕКТУРУ ИБО ОНА КОСТЫЛЬНАЯ
# ДА И КОД БОЛЕЕ... ПРОФИ СДЕЛАТЬ... БЫЛО БЫ КЛАССНО ДЕКОРАТОРЫ ТАМ ВПИХНУТЬ, АНОТАЦИИ
# TESTS

# 2 0 3 0 1 2 0

# try:
#     POOL_VALUE: Final = int(input())  # mypy
# except ValueError:
#     print("Pool value error.")


# пока хз думаю лучше засунуть в юнит тесты человеческого файла
# def check_cubes(gamer_cube_arr):
#     if sum(gamer_cube_arr) > POOL_VALUE:
#         return 0
#     else:
#         return 1


# print("before the fight while\nhuman_player.human_pool_dict :", human_player.human_pool_dict)
# print("coolman_player.coolman_pool_dict :", coolman_player.coolman_pool_dict)
