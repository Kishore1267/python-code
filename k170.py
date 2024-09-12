# Dictionary
d={}
r=int(input(" Enter range : "))
for i in range(r):
    roll=int(input(" Enter Roll Number : "))
    name=input(" Enter Name : ")
    age=int(input(" Enter Age : "))
    marks=int(input(" Enter Marks : "))
    d[roll]=name,age,marks
print(d)

# insert new elements
d[3]="matrix","33","60"
print(d)
# UPDATE new elements
d[3]="CCC","33","33"
print(d)
# Remove the elements
del d[11]
print(d)
