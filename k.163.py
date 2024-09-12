# Membership operator in python
#python program to illustrate
#same example withoutUsing 'in' operator
def overlapping(list_1,list2):
    c=0
    d=0
    for i in list_1:
        c+=1
        for i in list2:
            d+=1
            for i in range(0,c):
                for j in range(0,d):
                    if (list_1[i]==list2[j]):
                        return 1
                    else:
                        return 0
list_1=[1,2,3,4,5]
list2=[6,7,8,9]
if (overlapping(list_1,list2)):
    print("Overlapping")
else:
    print("Not overlapping")