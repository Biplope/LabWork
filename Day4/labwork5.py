#A student will not be allowed to sit in exam if his/her attendence is less than 75%.Take following input from user number of classes held
#Number of classes attended.And printpercentage of class attended. Is student is allowed to sit in exam or not.



a=int(input("Total no. of class held:"))
b=int(input("No. of class attended:"))
percentage=b/a*100
if percentage<=75:
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")