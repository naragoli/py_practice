from reusable_functions.clear import *
from os import *
clear()
printline()
x=input("Enter the string:")
print(f'Entered string is :{x}')

if x:
    if x.isupper():
        print(f'Entered string {x} is upper case string')
    else:
        if x.islower():
            print(f'Entered string {x} is Lower case string')
        else:
            print(f'Entered string {x} is mixed case string')

printline()

# ##########################################################
# Enter the string:My Name is Goli
# Entered string is :My Name is Goli
# Entered string My Name is Goli is mixed case string
# ##########################################################
# PS D:\Goli\p_time> 