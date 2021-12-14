#Write a Python program to count the number of even and odd numbers from a series of numbers.
l = [2,4,6,10, 21, 4, 45, 66, 93, 1,11,31] 
even, odd= 0, 0
for i in l: 
    if i % 2 == 0: 
        even += 1
    else: 
        odd+= 1          
print("Even : ", even) 
print("Odd : ", odd)