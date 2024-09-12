# split first four char of the each word from input string
str=input(" Enter string : ")
str_list=[]
str_list=str.split(" ")
wc=len(str_list)
for i in range(wc):
    t=str_list[i] # store words in t
    if len(t)<4:
        print(i+1,".",t,".->is<4 char",sep='')
    else:
        print(i+1,".",t, ".->",end='',sep='')
        for j in range(4):
            print(t[j],end='',sep='')
        print()
