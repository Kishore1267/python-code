# Write a python program palindrome for how many open brackets and closing brackets in place
str=input(" Enter the bracket string : ")
len=len(str)
left_brackets=0
right_brackets=0
is_palindrome=True
# Check if the string is a palindrome.
for i in range(len//2):
    if str[i]!=str[len-i-1]:
        is_palindrome=False
        break
# count the open and close brackets
for char in str:
    if char=='(':
        left_brackets=left_brackets+1
    elif char==')':
        right_brackets=right_brackets+1

if is_palindrome:
    print("The string",str, "is a palindrome.")
else:
    print("The string",str, "is not a palindrome.")
print("Number of left brackets:", left_brackets)
print("Number of right brackets:", right_brackets)