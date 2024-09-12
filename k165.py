# Binary file
import pickle
import os
f1=open('student.dat','rb')
f2=open('temp.dat','wb')
s=input(" Enter number to delete : ")
while True:
    try:
        data=pickle.load(f1)
        if s!=data['name']:
            pickle.dump(data,f2)
    except:
        break
f1.close()
f2.close()
#os.remove('student.dat')
#os.rename('temp.dat','student.dat')
print(" Recorded deleted ..")

