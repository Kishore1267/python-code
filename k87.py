# Search char
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
s=input(" Enter char to search : ")
po=0
for i in range(len):
    if s==str[i]:
        po=i+1
        break
if po==0:
    print(" char not found ")
else:
    print(" char found at ",po,'position')
