def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False
    return True


repeat = int(input('How many numbers do you want to check?\n'))
count = 0

for i in range(repeat):
    num = int(input('Enter a positive integer:\n'))
    if num < 0:
        print('PrimeFinder ignores negative numbers!')
        repeat += 1
    elif is_prime(num):
        print(num, 'is a prime number.')
        count += 1

print('Total prime numbers:', count)
