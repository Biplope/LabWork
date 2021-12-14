#Write a program to find the factorial of a number
a = int(input("Enter a number: ")) 
f = 1 
for i in range(1,a+1): 
	f = f * i 
print(f'The factorial of the number is {f}')