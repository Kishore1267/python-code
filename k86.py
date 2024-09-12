# Pyramid string 4
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
print(" Pyramid of = ",str)
for row in range(len):
    for sp in range(row+1):
        print("  ",sep='',end='')
    for col in range(len-row):
        print(str[col],end=' ')
    print()
