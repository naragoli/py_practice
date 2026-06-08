from ast import arg
from src.utils.clear import *
clear()
printfilename(argv[0])


rows=int(input('Number of rows:'))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# for i in range(1,rows+1):
#     print("*" *i,end="\n")


for row in range(1,rows+1):
    print(" " * (rows-row),end="")
    print("* " * row)

print()
for row in range(rows,0,-1):
    print(" " * (rows-row),end="")
    print("* " * row)

# ###################### d:/Goli/p_time/8.1_nested_loop.py ###################################
# Number of rows:5
# *
# **
# ***
# ****
# *****
# PS D:\Goli\p_time> 
# ###################### d:/Goli/p_time/8.1_nested_loop.py ###################################
# Number of rows:5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# PS D:\Goli\p_time> 