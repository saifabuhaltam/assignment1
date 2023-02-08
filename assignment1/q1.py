def Pchatbot():
    cont = input('Hi, this is Pchatbot, can I talk to you?\n')

    if cont == 'Y' or cont == 'y':
        name = input('What is your name?\n')

        print("Nice to meet you, " + name + '.')

        wellness = input('How are you doing today?\n')

        if wellness == 'Good' or wellness == "I'm great" or wellness == "I'm good" or wellness == 'Fine':
            print("I'm glad you're feeling well, " + name + '.')
        elif wellness == 'Bad' or wellness == 'Not Okay' or wellness == "I'm not feeling good":
            print('Have some time to yourself to recharge!')
        else:
            print('I see!')

        age = input('How old are you?\n')

        if int(age) >= 18 and (wellness == 'Good' or wellness == "I'm great" or wellness == "I'm good" or wellness == 'Fine'):
            print('You are ready to drive.')
        else:
            print('Still taking the bus!')
    elif cont == 'N' or cont == 'n':
        print('Okay! Talk to you soon!')


Pchatbot()
