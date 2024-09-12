# char
r = int(input(" Enter range : "))
ch='A'
for row in range(1,r+1):
    for col in range(1,row+1):
        print(ch,end=' ')
        ch=chr(ord(ch)+1)
    ch='A'
    print()
# ch = ch+1 : you can take increment in char
# fun ord: it is used to convert char to ASCII value
# fun char: it is used to convert ASCII value to char