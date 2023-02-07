h = int(input('What is the height of the pyramid?\n'))

if h < 2 or h > 9:
    print('PyNum cannot help you!')
else:
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        for k in range(i - 1, 0, -1):
            print(k, end=' ')
        print()
