from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])

n1,n2,n3=[int(x) for x in input("Enter three numbers:").split(",")]
print('Entered numbers are :',n1,n2,n3,sep='\n')

if n1>n2 and n1>n3:
    print('Big number is :',n1)
elif n2>n3:
    print('Big number is:',n2)
else:
    print('Big number is:',n3)

if n1<n2 and n1<n3:
    print("Small number is :",n1)
elif n1<n3:
    print("Small number is :",n1)
else:
    print("Small number is :",n3)












# ########################################################################################
# ###################### d:/Goli/p_time/6.3_if_elif_bignumber.py ###################################
# Enter three numbers:12:13:14
# Traceback (most recent call last):
#   File "d:\Goli\p_time\6.3_if_elif_bignumber.py", line 6, in <module>
#     n1,n2,n3=[int(x) for x in input("Enter three numbers:").split(",")]
#   File "d:\Goli\p_time\6.3_if_elif_bignumber.py", line 6, in <listcomp>
#     n1,n2,n3=[int(x) for x in input("Enter three numbers:").split(",")]
# ValueError: invalid literal for int() with base 10: '12:13:14'
# PS D:\Goli\p_time> 


# ########################################################################################
# ###################### d:/Goli/p_time/6.3_if_elif_bignumber.py ###################################
# Enter three numbers:10,11,12
# Entered numbers are :
# 10
# 11
# 12
# Big number is: 12
# PS D:\Goli\p_time> 