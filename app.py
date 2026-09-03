text = input("Enter a String: ")

for char in text:
    print("Character:", char)
    print("ASCII:", ord(char))
    print("Unicode:", "U+" + format(ord(char), "04X"))
    print()