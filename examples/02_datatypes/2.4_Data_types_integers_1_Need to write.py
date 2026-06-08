from reusable_functions.clear import *
clear() # clear the screen before executing the program.

print("################ working on integer base ################")
x=input("Enter a number of Decimal/Binary/Oct/Hexa type ")



# Defination :

# Decimal : 0-9 
# Binary : 0 & 1 
# Oct : 0-7 
# Hexa : 0 to 9 and a to f 






# Examples: 

# Input : str = "1010", base = 2
# Output : Yes

# Input : str = "1015", base = 2
# Output : No

# Input : str = "AF87", base = 16
# Output : Yes

# The idea is to one by one check if all digits are in the given base range. If yes, return true, else return false.