# Occurance
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
s=input(" Enter char to search : ")
count=0
for i in range(len):
    if s==str[i]:
        count=count+1
if count==0:
    print(" char not found ")
else:
    print(" char found at ",count,'Times')
