#Write a Python program to construct the following pattern, using a nested for loop.
for i in range(65,70):
    for j in range(65,i+1):
        print (chr(j),end="")
        print()