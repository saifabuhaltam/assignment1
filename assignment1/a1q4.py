def PyNum():
    h = int(input('What is the height of the pyramid?\n'))

    if 1 < h < 10:
        for i in range(h):
            print('  ' * (h - (i + 1)), end='')

            for j in range(1, i + 2):
                print(j, '', end='')
            for k in range(i, 0, -1):
                print(k, '', end='')
            print()
    else:
        print('PyNum cannot help you!')


PyNum()
