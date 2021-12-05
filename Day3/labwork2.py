#WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 


a=int(input("Marks of Maths:"))
b=int(input("Marks of Science:"))
c=int(input("Marks of English:"))
d=int(input("Marks of Computer:"))
Total_marks=(a+b+c+d)/4

if Total_marks>100:
    print("Envalid")
    
elif Total_marks>=70:
    print("Distinction")

elif Total_marks>=60:
    print("First")

elif Total_marks>=40:
    print("Pass")

else:
    print("Fail")