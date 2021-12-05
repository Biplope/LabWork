#Check whether the user input number is even or odd and display it to user. 

a=int(input("Enter the number"))
if(a%2)==0:
    print("{0} is a even number".format(a))
else:
    print("{0} is a odd number".format(a))