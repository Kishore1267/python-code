# Reverse as String
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
print(" Reverse as string = ",str,"=",end='')
for i in range(len-1,-1,-1):
    print(str[i],end='')
