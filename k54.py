# palindrome
n=int(input(" Enter number : "))
n1=n
rev=0
while(n>0):
    mod=n%10
    rev=rev*10+mod
    n=n//10
if n1==rev:
    print(" Palindrome ")
else:
    print(" Not Palindrome ")
    