decimal = int(input("Enter a decimal number (0-300): "))

if 0 <= decimal <= 300:
    binary = format(decimal, "08b")
    octal = format(decimal, "o")
    hexadecimal = format(decimal, "X")

    print("\nConverted Number:")
    print("Binary:      ", binary)
    print("Octal:       ", octal)
    print("Hexadecimal: ", hexadecimal)
else:
    print("Error: Please enter a number between 0 and 300.")