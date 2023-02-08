def finder(s, t):
    n = len(s)
    m = len(t)
    for i in range(n - m + 1):
        if source[i:i + m] == target:
            return i
    return -1


source = input()
target = input()

result = finder(source, target)
print(result)
