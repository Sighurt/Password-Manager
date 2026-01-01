import json
import os

def option1Func():
    if os.path.exists("fil5.json"):
            print("You're out of Password-Slots! ")
    else:
        option1 = input("Input application name/adress: ")

        option1Two = input("Input password to application: ")

        option1Three = input("Input password again: ")

        if option1Two != option1Three:
            print("The passwords did not match!")
            option1Func()
        else:
            userData = {"Name": option1, "Password": option1Two}
            userData2 = {"Name": option1, "Password": option1Two}
            userData3 = {"Name": option1, "Password": option1Two}
            userData4 = {"Name": option1, "Password": option1Two}
            userData5 = {"Name": option1, "Password": option1Two}

            if not os.path.exists("fil.json"):
                print("The password has been added to the database! ")
                with open("fil.json", "w") as file:
                    json.dump(userData, file)
            elif not os.path.exists("fil2.json"): 
                print("The password has been added to the database! ")
                with open("fil2.json", "w") as file:
                    json.dump(userData2, file)
            elif not os.path.exists("fil3.json"):
                print("The password has been added to the database! ")
                with open("fil3.json", "w") as file:
                    json.dump(userData3, file)
            elif not os.path.exists("fil4.json"):
                print("The password has been added to the database! ")
                with open("fil4.json", "w") as file:
                    json.dump(userData4, file)
            elif not os.path.exists("fil5.json"):
                print("The password has been added to the database! ")
                with open("fil5.json", "w") as file:
                    json.dump(userData5, file)
            else:
                print("There are no more password slots! ")


if not os.path.exists("password.json"):
    setPassword = input("Set your password for the password manager: ")
    setPassword2 = input("Repeat the same password to set it: ")

    if setPassword == setPassword2:
        with open("password.json", "w") as file:
            json.dump(setPassword, file)

elif os.path.exists("password.json"):

    input1 = input("Input Password to get into application: ")

    with open("password.json", "r") as file:
        password = json.load(file)

        if password == input1:

            input2 = input("1 = Add Password, 2 = See Passwords. ")

            if input2 == "1":
                option1Func()

            elif input2 == "2":

                if os.path.exists("fil.json"):
                    with open("fil.json", "r") as file:
                        data = json.load(file)
                        print(data)
                if os.path.exists("fil2.json"):
                    with open("fil2.json", "r") as file:
                        data = json.load(file)
                        print(data)
                if os.path.exists("fil3.json"):
                    with open("fil3.json", "r") as file:
                        data = json.load(file)
                        print(data)
                if os.path.exists("fil4.json"):
                    with open("fil4.json", "r") as file:
                        data = json.load(file)
                        print(data)
                if os.path.exists("fil5.json"):
                    with open("fil5.json", "r") as file:
                        data = json.load(file)
                        print(data)
                elif not os.path.exists("fil.json") and not os.path.exists("fil2.json") and not os.path.exists("fil3.json") and not os.path.exists("fil4.json") and not os.oath.exists("fil5.json"):
                    reset = input("You don't have any passwords stored yet! Answer with a 1 if you want to store one. ")

                    if reset == "1":
                        option1Func()
 
        else:
            print("WRONG PASSWORD ")



    
        
