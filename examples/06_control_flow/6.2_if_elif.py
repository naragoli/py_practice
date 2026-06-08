from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])

x=int(input("Enter a number:"))

if x>1 and x<=10:
    print("Entered number ",x,"is between 0 and 10 ")
elif x>10 and x<=20:
    print("Entered number ",x,"is between 10 and 20 ")
elif x>20 and x<=30:
    print("Entered number ",x,"is between 20 and 30 ")
else:
    print('Entered number',x," is greater than 30")


# ########################################################################################
# ###################### d:/Goli/p_time/6.2_if_elif.py ###################################
# Enter a number:21
# Entered number  21 is between 20 and 30 
# PS D:\Goli\p_time> 

# ########################################################################################
# ###################### d:/Goli/p_time/6.2_if_elif.py ###################################
# Enter a number:100
# Entered number 100  is greater than 30
# PS D:\Goli\p_time> 
