import random


def get_borders() -> tuple[str, str]:

    print('Input left border')
    left = input()

    print('Input right border')
    right = input()

    return left, right


def validate_borders(borders: tuple[str, str]) -> bool:

    if not borders[0].isdigit() or not borders[1].isdigit():
        return False

    elif int(borders[0]) >= int(borders[1]):
        return False

    else:
        left = int(borders[0])
        right = int(borders[1])
        return True


def get_random_number(borders: tuple[int, int]) -> int:

    return random.randint(borders[0], borders[1])


def restart_game() -> bool:

    print('Wanna play again?')
    answer = input()

    if answer.lower() == 'yes' or answer.lower() == 'y':
        return True

    else:
        return False


def randomizer() -> None:
    print('Hello! Welcome to the game "Randomizer"')

    while True:
        borders = get_borders()
        if not validate_borders(borders):
            print('Something went wrong... Try again')
            continue
        borders = tuple(map(int, borders))
        random_number = get_random_number(borders)
        while True:

            print('Try to answer my number')
            user_answer = input()

            if not user_answer.isdigit():
                print('Try again, this is not number...')
                continue

            elif int(user_answer) > random_number:
                print('Oops... Too much...')
                continue

            elif int(user_answer) < random_number:
                print('Oh... Too little...')
                continue

            else:
                print('Congratulations! You guessed my number.')

                if restart_game():
                    break

                else:
                    print('Thank you for playing. See you later!')
                    return
