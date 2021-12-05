#Given three integers, print the smallest one. (Three integers should be user input) 

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a<=b and a<=c:
    print("First number is the smallest")
elif b<=a and b<=c:
    print("Second number is the smallest")
elif c<=a and c<=a:
    print("Third number is the smallest")
