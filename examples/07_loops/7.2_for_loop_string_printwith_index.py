from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])

print('Printing the characters of a string in index wise')

s1=input('Enter a random text:')
count=0

for c in s1:
    print('Character presented at [',count,'] index is ',c)
    count+=1


# ########################################################################################
# ###################### d:/Goli/p_time/7.2_for_loop_string_printwith_index.py ###################################
# Printing the characters of a string in index wise
# Enter a random text:Narasimha
# Character presented at [ 0 ] index is  N
# Character presented at [ 1 ] index is  a
# Character presented at [ 2 ] index is  r
# Character presented at [ 3 ] index is  a
# Character presented at [ 4 ] index is  s
# Character presented at [ 5 ] index is  i
# Character presented at [ 6 ] index is  m
# Character presented at [ 7 ] index is  h
# Character presented at [ 8 ] index is  a
# PS D:\Goli\p_time> 