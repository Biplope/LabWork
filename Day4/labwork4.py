#Write a program to print absolute vlaue of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1

number=int(input("Number:"))
if number<0:
    print(number*-1)
else:
    print(number)