def is_prime(number):
    if number <= 1:
        return False
    for a in range(2, int(number ** 0.5) + 1):
        if number % a == 0:
            return False
    return True


def prime_divisors(digit):
    divisors = []
    for b in range(2, digit + 1):
        if digit % b == 0 and is_prime(b):
            divisors.append(b)
    return len(divisors)


def product_price(item_weight):
    if is_prime(item_weight):
        primes = [x for x in range(2, item_weight) if is_prime(x)]
        return len(primes)
    else:
        return prime_divisors(item_weight)


def total_discount(total):
    if is_prime(total):
        primes = [x for x in range(2, total) if is_prime(x)]
        return len(primes)
    else:
        return prime_divisors(total)


n = int(input())
total_price = 0
for i in range(n):
    weight = int(input())
    total_price += product_price(weight)

discount = total_discount(total_price)
print(total_price - discount)
