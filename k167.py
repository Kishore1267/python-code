# Binary file
import pickle
f=open('student.dat','rb')
while True:
    try:
        data=pickle.load(f)
        print(data)
    except:
        break
f.close()
