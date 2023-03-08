def gcd_calc(b, r):
    if r == 0:
        return b
    return gcd_calc(r, b % r)


def lcm_calc(a, b):
    return a * b // gcd_calc(a, b)


def calc(amount, digits):
    result = digits[0]
    for i in range(1, amount):
        result = lcm_calc(result, digits[i])
    return result


try:
    n = int(input().strip())
    if n <= 1:
        raise ValueError("The number of denominators must be greater than 1.")

    numbers = []
    for i in range(n):
        number = int(input().strip())
        if number <= 0:
            raise ValueError("The denominators must be positive integers.")
        numbers.append(number)

    print(calc(n, numbers))

except ValueError:
    print("Error")
