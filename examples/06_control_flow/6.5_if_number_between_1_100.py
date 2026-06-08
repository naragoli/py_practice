from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])

print("checking if the entered number is betweek 1 to 100")
n=int(input('Enter a number:'))

if n>=1 and n<=100:
    print('Entered number ',n,'is within 1-100 range')
else:
    print('Entered number ',n,'is not within 1-100 range')





# ########################################################################################
# ###################### d:/Goli/p_time/6.5_if_number_between_1_100.py ###################################
# checking if the entered number is betweek 1 to 100
# Enter a number:101
# Entered number  101 is not within 1-100 range
# PS D:\Goli\p_time> 

# ########################################################################################
# ###################### d:/Goli/p_time/6.5_if_number_between_1_100.py ###################################
# checking if the entered number is betweek 1 to 100
# Enter a number:-3
# Entered number  -3 is not within 1-100 range
# PS D:\Goli\p_time> 


# ########################################################################################
# ###################### d:/Goli/p_time/6.5_if_number_between_1_100.py ###################################
# checking if the entered number is betweek 1 to 100
# Enter a number:1.234
# Traceback (most recent call last):
#   File "d:\Goli\p_time\6.5_if_number_between_1_100.py", line 7, in <module>
#     n=int(input('Enter a number:'))
# ValueError: invalid literal for int() with base 10: '1.234'
# PS D:\Goli\p_time> 

# ########################################################################################
# ###################### d:/Goli/p_time/6.5_if_number_between_1_100.py ###################################
# checking if the entered number is betweek 1 to 100
# Enter a number:1
# Entered number  1 is not within 1-100 range
# PS D:\Goli\p_time> 