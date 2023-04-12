import random

ANSWERS = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes — definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Yes',
           'Reply hazy, try again', ' Ask again later', 'Better not tell you now', 'Cannot predict now',
           'Concentrate and ask again', 'Don’t count on it', 'My reply is no',
           'My sources say no', 'Outlook not so good', 'Very doubtful']

def magic_ball():

    name = input("What's your name?\n")
    print(name + ', i am the Mystic 8 Ball, and i know answer for any question')


    while True:

        question = input('What is your question?\n')

        print('Hm... give me a second...')
        print(random.choice(ANSWERS))

        selection = input('Do you have any other questions? Write "yes" or "no"\n')

        if selection == 'no' or selection == 'n':
            print('Come back if you have more questions, ' + name)
            break

        else:
            continue
