str=input("Enter the bracket string: ")
len=len(str)
left_brackets = 0
right_brackets = 0
# Check if the string is a palindrome and count the brackets
for i in range(len//2):
    if str[i]!=str[len-i-1]:
        print("The string",str,"is not a palindrome.")
        break
else:
    print("The string",str, "is a palindrome.")

# Count the open and close brackets
for char in str:
    if char == '(':
        left_brackets = left_brackets+1
    elif char == ')':
        right_brackets = right_brackets+1

print("Number of left brackets:", left_brackets)
print("Number of right brackets:", right_brackets)
