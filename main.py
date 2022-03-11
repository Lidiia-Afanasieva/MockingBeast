import random
import time
from typing import Optional

from human import Human
from coolman import Coolman

everyone_is_alive = True
POOL_VALUE: Optional[int]  # пока только объявлена, но не инициализирована


def human_character_initialisation():
    # создание данных человека
    human_player.dict_creation(input().split())
    print("There is your pool: ", human_player.human_pool_dict)
    human_player.personal_heal = int(input("Enter your heal value: "))
    human_player.human_pool_dict[str(human_player.personal_heal)] -= 1

    human_player.DICT_ON_THIS_GAME.deepcopy(human_player.human_pool_dict)  # THIS IS POINT OF COPY

    return 0


def coolman_character_initialisation():
    # создание данных компьютера
    coolman_player.coolman_pool_generation()
    coolman_player.heal_selection()

    return 0


def output_start_of_the_game():

    print("B MO")

    POOL_VALUE = int(input("Enter the pool value "))

    print("You can enter any count of cubes, but its sum must be less then pool value.(4, 6, 8, 10, 12, 20, 100)")
    print("Example: 0 3 0 4 1 2 0 Means count 1d4 = 0 1d6 = 3 and etc. Sum of your pool = 288")
    print("Its OK if current Pool Value is 288 or more, else piss of")

    human_character_initialisation()
    coolman_character_initialisation()

    random.shuffle(gamer_list)


def reload_list(work_list: list, pool_value_remainder: int) -> list:
    return [item for item in work_list if item <= pool_value_remainder]  # wtf its doing


def intrigue_maker():

    print("ROLL.")
    time.sleep(1)
    print("ROLL..")
    time.sleep(1)
    print("ROLL...")

    return 0


def cubes_roll(attack_cube: int, block_cube: int) -> tuple:

    attack_value = random.randint(1, attack_cube)
    block_value = random.randint(1, block_cube)

    if attack_value > block_value:
        return attack_value - block_value, attack_value, block_value

    else:
        return 0, attack_value, block_value


def output_battle_score() -> None:

    reload_list(human_player.human_pool_dict, 0)  # NOT SURE IN THE PLACE OF FUNC
    print('///')
    print('Your heal at this moment is :', human_player.personal_heal)
    print('Your available cubes now :', human_player.human_pool_dict)
    print('///')
    print('Your opponent heal at this moment is :', coolman_player.personal_heal)
    print('///')


def check_empty_dicts() -> int:

    if sum(human_player.human_pool_dict.items()) < 1 and sum(coolman_player.coolman_pool_dict.items()) < 1:
        return 1

    elif sum(human_player.human_pool_dict.items()) > 1 and sum(coolman_player.coolman_pool_dict.items()) < 1:
        return 2

    elif sum(human_player.human_pool_dict.items()) < 1 and sum(coolman_player.coolman_pool_dict.items()) > 1:
        return 3

    else:
        return 0


def print_calculation_of_human_attack() -> None:

    damage, attack_value, block_value = cubes_roll(human_player.current_attack, coolman_player.current_block)
    human_player.human_pool_dict[str(human_player.current_attack)] -= 1

    if damage > 0:
        coolman_player.personal_heal -= damage
        print('Human side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


# ADD CHECK OF EMPTY DICTS. OUTPUT THAT GAMER IS EMPTY// maybe as a check
def human_attack() -> None:

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
        print('Human side is won this time. '
              'Score is {0} : {1}. Damage is : {2}'.format(attack_value, block_value, damage))

    else:
        print('Coolman side was full blocked. Score is {0} : {1}'.format(attack_value, block_value))


# ADD CHECK OF EMPTY DICTS. OUTPUT THAT GAMER IS EMPTY// maybe as a check
def coolman_attack() -> None:

    human_player.current_block = int(input("Your turn. Enter the block cube value "))
    coolman_player.tactic_selection('attack')
    print("You have been attacked with :", coolman_player.current_attack)
    input("Roll cubes?")
    intrigue_maker()

    print_calculation_of_coolman_attack()


# ////////////////////////////////////////////////////////////
# START


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


output_start_of_the_game()

human_player = Human(POOL_VALUE)
coolman_player = Coolman(POOL_VALUE)
gamer_list = [coolman_player, human_player]


while everyone_is_alive:

    while check_empty_dicts() != 1:

        check_the_dicks = check_empty_dicts()

        # coolman empty
        if check_the_dicks == 2:

            print('Well, your opponent ended all his cubes, so now all your cubes will attack him.')
            print('Enjoy.')
            print('...')
            print('Your cubes now: ', human_player.human_pool_dict)
            intrigue_maker()
            start_heal = coolman_player.personal_heal

            for cube_value in human_player.human_pool_dict.keys():

                for cube_count in human_player.human_pool_dict.values():

                    damage, attack_value, block_value = cubes_roll(int(cube_value), 0)
                    coolman_player.personal_heal -= damage
                    print('Your cube: {0}, its damage: {1}'.format(cube_value, damage))

            print('Finally, damage is:', start_heal - coolman_player.personal_heal)

            if coolman_player.personal_heal == 0:
                everyone_is_alive = False

        # human empty
        elif check_the_dicks == 3:

            print('Well, you ended all your cubes, so now your opponent will attack you with all his cubes.')
            print('Good luck.')
            intrigue_maker()
            start_heal = human_player.personal_heal

            for cube_value in coolman_player.coolman_pool_dict.keys():

                for cube_count in coolman_player.coolman_pool_dict.values():

                    damage, attack_value, block_value = cubes_roll(int(cube_value), 0)
                    human_player.personal_heal -= damage
                    print('His cube: {0}, its damage: {1}'.format(cube_value, damage))

            print('Finally, damage is:', start_heal - human_player.personal_heal)

            if human_player.personal_heal == 0:
                everyone_is_alive = False

        else:

            if gamer_list[0] == human_player:

                human_attack()
                output_battle_score()

                if coolman_player.personal_heal > 0 and human_player.personal_heal > 0:

                    coolman_attack()
                    output_battle_score()

                else:

                    everyone_is_alive = False

            else:
                coolman_attack()
                output_battle_score()

                if coolman_player.personal_heal > 0 and human_player.personal_heal > 0:

                    human_attack()
                    output_battle_score()

                else:

                    everyone_is_alive = False

    print('Now you and your opponent are empty.')

    if everyone_is_alive:

        print('///')
        print('NEXT ROUND')
        print('///')
        coolman_player.coolman_pool_dict = coolman_player.DICT_ON_THIS_GAME
        human_player.human_pool_dict = human_player.DICT_ON_THIS_GAME
        output_battle_score()

if not everyone_is_alive:

    if coolman_player.personal_heal > human_player.personal_heal:

        print('YOU ARE FUCKIN PIECE OF SHIT')
        print('YOU LOOSE THIS GAME')
        print('STUPID COMPUTER WIN')

    elif coolman_player.personal_heal < human_player.personal_heal:

        print('Okey, you win')
        print('Im surprised. You make not only mistakes.')
        print('Like your parents, when they gave a life to you.')

    else:

        print('Well, I dont know whata happened')
        print('But anyway... You are an idiot')


# если значение пула будет 100 - 103 и как хил будет выбрана 100, то комп проиграет, надо исправить (regeneration)
# ещё там что-то доделать надо в coolman.py

# ВООБЩЕ КРАСИВО БЫЛО БЫ ПОТОМ НАПИСАТЬ БД ВОЗМОЖНЫХ ОТВЕТОВ КОМПА НА РАЗНЫЕ ПУНКТЫ, ЧТОБЫ НЕ ЗАМАЗОЛИЛО ГЛАЗА
# ВООБЩЕ ПОСВЕЖЕМУ НУЖНО ГЛЯНУТЬ НА АРХИТЕКТУРУ ИБО ОНА КОСТЫЛЬНАЯ
# ДА И КОД БОЛЕЕ... ПРОФИ СДЕЛАТЬ... БЫЛО БЫ КЛАССНО ДЕКОРАТОРЫ ТАМ ВПИХНУТЬ, АНОТАЦИИ
# TESTS

# IM NOT SURE DICTS HAVE RESET, WHEN COUNT OF VALUE = 0!!!!!!!!!!!!!!!!!!


# 2 0 3 0 1 2 0
