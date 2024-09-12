f=open('matrix.txt','w')
f.write('MATRIX COMPUTERS \n')
f.write('C-81,SAMTA COLONY \n')
f.write('RAIPUR (C.G.)\n')
f.write('C,C++,JAVA,PYTHON')

f=open('k142.py','r')
print(f.read())

f=open('matrix.txt','a')
f.write("\n------------------------------")
f=open('matrix.txt','r')
print(f.read())
'''
f=open('matrix.txt','r')
f.write("\n------------------------------")
f=open('matrix.txt','r')
print(f1.read())

f=open('matrix.txt','r')
print(f.read())# reads all file of data

for i in (f):
    print(i)# it will take line by line 
print(f.readline())# reads line by line 
print(f.readline())# reads next line 
print(f.readline(5))# print first chars if line 
print(f.readline(5))# print next chars if line
'''