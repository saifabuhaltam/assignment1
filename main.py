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

def printList():
    list1 = [1,2,3,4,5,6]
    list2 = list1[0:1]

    result = 0
    i = 0

    while i < len(list1):
        temp = list2[0] * list1[0]
        result = result + temp
        i = i+1

    print(result)

printList()