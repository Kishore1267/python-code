# Binary file
import pickle
f=open('student.dat','rb')
data=pickle.load(f)
print(data)
f.close()
