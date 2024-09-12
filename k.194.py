# write a python program for replace a char with given char
str=str(input(" Enter string : "))
len=len(str)
print(" String = ",str)
print(" Length = ",len)
s=input(" Enter char to search : ")
re=input(" Enter char to replace : ")
newstr=''
count=0
for i in str:
    if i==s:
        count=count+1
        newstr=newstr+re
    else:
        newstr=newstr+i
if count==0:
    print(" In",str,"char",s,"Not present")
else:
    print(" New String : ",newstr)

