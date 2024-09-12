# Binary file
import pickle
f=open('student.dat','ab')
name=input(" Enter name : ")
roll=input(" Enter Roll No. : ")
student={'name':name,'roll':roll}
pickle.dump(student,f)
f.close()
print(" Data transfer to the file ..")

