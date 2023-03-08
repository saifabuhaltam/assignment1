n = int(input(""))

numbers = []
for i in range(n):
    number = int(input(""))
    numbers.append(number)

max_sum = 0
for i in range(n):
    current_sum = numbers[i]
    for j in range(i+1, n):
        current_sum += numbers[j]
        if max_sum == 0 or current_sum > max_sum:
            max_sum = current_sum

print(max_sum)
