# Calculate Percentage and grade
per=int(input(" Enter percentage : "))
if per<=40:
    grade='E'
elif per<=60:
    grade='D'
elif per<=70:
    grade='C'
elif per<=80:
    grade='B'
else:
    grade='A'
print(" Percentage = ",per)
print(" Grade = ",grade)
