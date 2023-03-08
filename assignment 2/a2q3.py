text = input()

text = text.lower().replace(" ", "").replace(",", "")

if text == text[::-1]:
    print("Yes")
else:
    print("No")
