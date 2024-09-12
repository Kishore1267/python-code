# Pyramid string
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
print(" Pyramid of = ",str)
for row in range(len):
    for col in range(row+1):
        print(str[col],end=' ')
    print()
    
