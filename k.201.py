# write a python program to print ASCII value of a character
# Taking input from the user
char = input("Enter a character: ")

# Checking if the input is a single character
if len(char) != 1:
    print("Please enter a single character.")
else:
    # Getting the ASCII value of the character
    ascii_value = ord(char)

    # Printing the ASCII value
    print(f"The ASCII value of ",char," is {ascii_value}")


