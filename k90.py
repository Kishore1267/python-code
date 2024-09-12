# count, vowels, consonents
str=str(input(" Enter string : "))
len=len(str)
b=0
v=0
no=0
up=0
lo=0
for i in range(len):
    if str[i]==' ':
        b=b+1
    elif str[i]=='a' or  str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
        v=v+1
    elif str[i]>='0' and str[i]<='9':
        no=no+1
    elif str[i]>='a' and str[i]<='z':
        lo=lo+1
    elif str[i]>='A' and str[i]<='Z':
        up=up+1
print(" String                            = ",str)
print(" Length                            = ",len)
print(" No.as char                        = ",(len-b))
print(" Blank                             = ",b)
print(" Consonents                        = ",len-(b+v+no))
print(" Numbers                           = ",no)
print(" Vowels                            = ",v)
print(" Upper char                        = ",up)
print(" Lower char                        = ",lo)
print(" Words                             = ",(b+1))

