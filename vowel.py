def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([c for c in s if c not in vowels])


def add_string(s):
    length = len(s)

    if length > 4:
        if s[-3:] == 'xyz':
            s += 'uv'
        else:
            s += 'xyz'

    return s


def count_char(text):
    counter = 0
    for character in text:
        if character == 'ch':
            counter = counter + 1
    return counter


def numbers():
    print("Do you want to enter a number to add to a set of numbers:\n")
    cont = input()

    while cont in ['y', 'Y']:
        print("Enter a number: ")
        number = int(input())

        print(number)


def main():
    print("Enter a string to remove vowels from: \n")
    s = input()

    print(remove_vowels(s))
    print(add_string('rte'))
    print(add_string('dsa43'))
    print(add_string('12xyz'))

    print(count_char("ch"))

    numbers()

main()
