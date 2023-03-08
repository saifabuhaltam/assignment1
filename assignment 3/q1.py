def anagrams_solver(word):
    word = word.lower().replace(' ', '').replace(',', '')
    return ''.join(sorted(word))


n = int(input(""))
words = [input("") for i in range(n)]


anagram_dict = {}
for word in words:
    key = anagrams_solver(word)
    if key in anagram_dict:
        anagram_dict[key].append(word)
    else:
        anagram_dict[key] = [word]

max_size = max(len(anagram_dict[key]) for key in anagram_dict)
print(max_size)
