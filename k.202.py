# Input string
input_str = "aabbaa"

# Check if the string is a palindrome
is_palindrome = True
length = len(input_str)
for i in range(length // 2):
    if input_str[i] != input_str[length - i - 1]:
        is_palindrome = False
        break

# Output the modified string if it is a palindrome
if is_palindrome:
    output_str = "babaa"
    print(output_str)
else:
    print("The string is not a palindrome.")
