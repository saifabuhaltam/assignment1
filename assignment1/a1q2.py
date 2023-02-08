k = int(input('Hi, how many operations do you want MagiCal to perform?\n'))


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


for i in range(k):

    sign = input(
        "Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n")

    try:
        sign = int(sign)
        if sign in [1, 2, 3, 4]:
            first = int(input('Enter the first number in the interval of [0,100]:\n'))

            second = int(input('Enter the second number in the interval of [0,100]:\n'))

            if 0 <= first <= 100 and 0 <= second <= 100:
                if sign == 1:
                    print(first, "+", second, "=", add(first, second))
                elif sign == 2:
                    print(first, "-", second, "=", subtract(first, second))
                elif sign == 3:
                    print(first, "*", second, "=", multiply(first, second))
                elif sign == 4:
                    if second != 0:
                        print(first, "/", second, "=", divide(first, second))
                    else:
                        print('The denominator cannot be 0.')
            else:
                print('Magic calculator can not perform your operation!')
        else:
            raise ValueError
    except ValueError:
        print('Invalid input!')
