# Palindrome
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
for i in range(len):
    if str[i]!=str[len-(i+1)]:
        print(" Not palindrome ")
        exit(0) # close the program
print(" palindrome ")


