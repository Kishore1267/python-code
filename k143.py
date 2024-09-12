# first step to create file
f=open('matrix.txt','w')
f.write('MATRIX COMPUTERS \n')
f.write('C-81,SAMTA COLONY \n')
f.write('RAIPUR (C.G.)\n')
f.write('C,C++,JAVA,PYTHON')

# Second open the file to read
f=open('matrix.txt','r')
print(f.read())

# another file abc to write
f1=open('matrix.txt','w')
for i in f:
    f.write(i)
f2=open('matrix.txt','r')
for i in f:
    print(f2.read())
