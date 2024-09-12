# input
name=str(input(" Enter name : "))
age=int(input(" Enter age : "))
roll=int(input(" Enter roll : "))
m1=int(input(" Enter marks 1 : "))
m2=int(input(" Enter marks 2 : "))
m3=int(input(" Enter marks 3 : "))
m4=int(input(" Enter marks 4 : "))
# process
tot=m1+m2+m3+m4
per=(tot*100)/400
if per<=60:
    grade='D'
elif per<=70:
    grade='C'
elif per<=80:
    grade='B'
else:
    grade='A'
# display
print("-----------------------------------------------------")
print("                 Subject marks                       ")
print("-----------------------------------------------------")
print("  Mathematics                                   = ",m1)
print("  Chemistry                                     = ",m2)
print("  Physics                                       = ",m3)
print("  Computer                                      = ",m4)
print("-----------------------------------------------------")
print("   Total                                       = ",tot)
print("   Percentage                                  = ",per)
print("   Grade                                       = ",grade)

