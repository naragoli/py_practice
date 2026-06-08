from reusable_functions.clear import *
clear()
printfilename(argv[0])

name=" "
while True:
    name=input("Enter the correct name:")
    if name=="Goli":
        print("Entered correct string, exiting the while loop")
        break


# while name!="Goli":
#     name=input("Enter the correct string")
# print("Entered the correct string and while loop stopped")