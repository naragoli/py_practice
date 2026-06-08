from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])

print('working on prime number identification')

num=int(input('Enter a number to check whether its prime:'))

if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("Entered number",num,'is not a prime')
            print(num,'is',i,'times of',num//i, )
            break
    else:
        print("Entered number",num,'is a prime')
else:
    print("Entered number",num,'is not a prime')
    



# ########################################################################################
# ###################### d:/Goli/p_time/7.4_prime_number_check.py ###################################
# working on prime number identification
# Enter a number to check whether its prime:407
# Entered number 407 is not a prime
# 407 is 11 times of 37
# PS D:\Goli\p_time> 

# ########################################################################################
# ###################### d:/Goli/p_time/7.4_prime_number_check.py ###################################
# working on prime number identification
# Enter a number to check whether its prime:9
# Entered number 9 is not a prime
# 9 is 3 times of 3
# PS D:\Goli\p_time> 