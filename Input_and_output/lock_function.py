def lock_function():
    password = input("Set a new password: ")
    count = 0
    word = ""
    while word != password:
        word = input("Enter your password: ")
        if word==password:
            print("Password is correct!")
            break
        else:
            count=count+1
            if count==3:
                print("You have no attempts!")
                break
            else:
                print("You entered wrong password! {} attempts left".format(3-count))

lock_function()