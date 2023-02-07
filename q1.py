print('Hi, this is Pchatbot, can I talk to you?\n')
cont = input()


if cont in ['Y', 'y']:
    print('What is your name?\n')
    name = input()

    print('Nice to meet you, ', name, '.')

    print('How are you doing today?\n')
    wellness = input().lower().strip()

    if wellness in ['good', "i'm great", "i'm good", 'fine']:
        print("I'm glad you’re feeling well, ", name, '.')
    elif wellness in ['bad', 'not okay', "i'm not feeling good"]:
        print('Have some time to yourself to recharge!')
    else:
        print('I see!')

    print('How old are you?\n')
    age = input()

    if int(age) > 18:
        print('You are ready to drive.')
    else:
        print('Still taking the bus!')
else:
    print('Okay! Talk to you soon!')
