# write a python program for how to check if a given number is fibonacci
# Input the number to check
n=int(input("Enter a number: "))
# Initial two Fibonacci numbers
b=0
e=1
# Loop to generate Fibonacci numbers until we reach or exceed n
while b<n:
    # Update to the next Fibonacci numbers
    c=b+e
    b=e
    e=c

# Output the result
if b==n:
    print(n, "is a Fibonacci number.")
else:
    print(n, "is not a Fibonacci number.")

