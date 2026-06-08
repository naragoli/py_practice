from reusable_functions.clear import *
clear()
printline()

a=input('Enter number1:')
b=input('Enter number2:')
c=input('Enter number3:')

min=int()

min=a if a<b and a<c else b if b<c else c
max=a if a>b and a>c else b if b>c else c

print('Small number is:',min)
print('Big number is:',max)


# ##########################################################
# Enter number1:100
# Enter number2:99
# Enter number3:98
# Small number is: 100
# Big number is: 99
# PS D:\Goli\p_time> 
