from reusable_functions.clear import *
clear()
printfilename(argv[0])

print('Summation of first N numebers, where N is user input')
num=int(input('Enter the value of N:'))
count=1
sum=0

while count<=num:
    sum=sum+count
    count=count+1

print('Summation of fist',num,'Number is',sum)



# ###################### d:/Goli/p_time/7.6_while.py ###################################
# Summation of first N numebers, where N is user input
# Enter the value of N:50
# Summation of fist 50 Number is 1275
# PS D:\Goli\p_time> 
