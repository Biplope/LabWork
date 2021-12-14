#Write a Python program to guess a number between 1 to 9.
a= int(input("Enter a guess"))
while (a>9) or (a<1) :
   a=int(input("Enter a guess"))

else:
   print("Well guessed")