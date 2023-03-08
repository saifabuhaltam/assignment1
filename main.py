# def getName() -> str:
#     name = input("Enter your name: ")
#     return name
#
#
# def getAge() -> float:
#     number = float(input("Enter your age: "))
#     return number
#
#
# def main():
#     print("Nice to meet you,", getName())
#     print(getAge(), "years young.")
#
#
# main()

# def somefunction():
#     for i in range(7):
#         print('@' * (7-i), end='')
#         for j in range(1, i + 2):
#             print(j, end='')
#         print()
#
# # somefunction()
#
# def another():
#     for i in range(8):
#         print(' ', '@ ' * i, end='')
#         print("\n")
#
# another()
#
# def solution():
#     for i in range(7):
#         print ('' * (7-i), end='')
#         for j in range(0, i+1):
#             print('@ ', end='')
#         print()
#
# solution()

# def printList():
#     list1 = [1, 2, 3, 4, 5, 6]
#     list2 = list1[0:1]
#
#     result = 0
#     i = 0
#
#     while i < len(list1):
#         temp = list2[0] * list1[0]
#         result = result + temp
#         i = i + 1
#
#     print(result)
#
#
# def unique(list):
#     other_list = []
#
#     for i in list:
#         if i not in other_list:
#             other_list.append(i)
#     return other_list
#
#
# def flat_list(list):
#     other_list = []
#
#     for items in list:
#         for i in items:
#             other_list.append(i)
#     return other_list
#
#
# def vowel_names(count):
#     name_list = []
#
#     for i in range(count):
#         name = input()
#         name_list.append(name)
#
#     vowels = [item for item in name_list if item[0] in "aeiouAEIOU"]
#     return len(vowels)
#
#
# def main():
#     name_number = int(input())
#     result = vowel_names(name_number)
#     print(result)
#
#
# main()
# print(unique([1, 1, 1, 2, 3, 4]))
# print(flat_list([[1], [1, 1, 2, 3]]))
#
# printList()

lst = [4, 5, 10]
print([x * 1 for x in lst if x > 5])