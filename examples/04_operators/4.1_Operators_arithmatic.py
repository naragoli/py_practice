from reusable_functions.clear import *
clear()
printline()

# a=int(input('Enter Num1:'))
# b=int(input('Enter Num2:'))

a=2+3j
b=2

print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b) # Floating point value 
print(a,"%",b,"=",a%b)  #Remainder
print(a,"//",b,"=",a//b) # Decimal Point value of division
print(a,"**",b,"=",a**b) # Power of 
printline()




# ##########################################################
# (2+3j) + 2 = (4+3j)
# (2+3j) - 2 = 3j
# (2+3j) * 2 = (4+6j)
# (2+3j) / 2 = (1+1.5j)
# Traceback (most recent call last):
#   File "d:\Goli\p_time\4.1_Operators_arithmatic.py", line 15, in <module>
#     print(a,"%",b,"=",a%b)  #Remainder
# TypeError: unsupported operand type(s) for %: 'complex' and 'int'
# PS D:\Goli\p_time> 