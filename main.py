from games import magicball
from games import randomizer


print('Hello! Choose the game! I have randomizer or magicball')

while True:
    choose = input()

    if choose == 'randomizer':
        randomizer.randomizer()
        print('Wanna play more games?')
        answer = input()

        if answer == 'yes':
            print('Choose the game: randomizer, magicball')
            continue

        else:
            print('See you later!')
            break

    elif choose == 'magicball':
        magicball.magic_ball()
        print('Wanna play more games?')
        answer = input()

        if answer == 'yes':
            print('Choose the game: randomizer, magicball')
            continue

        else:
            print('See you later!')
            break

    elif choose == 'exit' or choose == 'close' or choose == 'no':
        print('See you later!')
        break

    else:
        print("Oops... I didn't have this game... Choose randomizer or magicball")
