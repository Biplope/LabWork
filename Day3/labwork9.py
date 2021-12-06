username=input("Username")
password=input("Password")

for i in range(0,3):
    username1=input("Enter username")
    password1=input("Ener  password")
    if username ==username1 and password ==password1:
        print("You are logged successfully")
        print("You are logged in successfully")
        break
    #else:
        print("Invalid credentials")
    elif i<3:
        if username != username1 and password != password1 and i<3:
            print("Invalid Credentails. Please donot breach")
else:
    print("Attempt finished")
