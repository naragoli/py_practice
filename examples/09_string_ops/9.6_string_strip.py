from src.utils.clear import *
clear()
printfilename(argv[0])

x=input("Enter a string with spaces to test the string-strip function:")
print('Entered text:',x)
print('Entered test lenght is :',len(x))
y=x.strip()
print('Strip Text is:',y)
print('strip test lenght is :',len(y))




# ###################### d:/Goli/p_time/9.6_string_strip.py ###################################
# Enter a string with spaces to test the string-strip function:    My Name is Narasimha Goli    
# Entered text:     My Name is Narasimha Goli    
# Entered test lenght is : 33
# Strip Text is: My Name is Narasimha Goli
# strip test lenght is : 25
# PS D:\Goli\p_time> 