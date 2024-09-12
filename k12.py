# Amount tax and Net value
amt=int(input(" Enter amount : "))
if amt<=1000:
    tax=0
elif amt<=2000:
    tax=(amt*10)/100
else:
    tax=(amt*20)/200
net=amt+tax
print(" Net value = ",net)
print(" Amount = ",amt)
print(" Tax = ",tax)


