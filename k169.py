# Binary file
import pickle
f=open('student.dat','wb')
name=input(" Enter name : ")
roll=int(input(" Enter Roll No : "))
student={'name':name,'roll':roll}
pickle.dump(student,f)
f.close()
print(" Data transfer to the file..")
