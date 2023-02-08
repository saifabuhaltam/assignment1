def find_substring(s, t):
    n = len(s)
    max_substring = ""
    max_unique = 0

    for i in range(n - t + 1):
        substr = s[i:i + t]
        unique = len(set(substr))
        if unique > max_unique:
            max_unique = unique
            max_substring = substr
    return max_substring


while True:
    source = input()
    if source != "quit":
        k = int(input())
        result = find_substring(source, k)
        print(result)
    else:
        break
