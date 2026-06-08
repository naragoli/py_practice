from src.utils.clear import *
clear()
printfilename(argv[0])
x=input('Enter a string:')
list1=[]
list2=[]
count=0
rcount=-1
print('Entered string is:',x,',and its lenght is:',len(x))

while count<len(x):
    list1.append(x[count])
    count+=1
print(list1)

while rcount>=-len(x):
    list2.append(x[rcount])
    rcount-=1
print(list2)


# ###################### d:/Goli/p_time/9.4_string_printing_with_list.py ###################################
# Enter a string:Narasimha Goli
# Entered string is: Narasimha Goli ,and its lenght is: 14
# ['N', 'a', 'r', 'a', 's', 'i', 'm', 'h', 'a', ' ', 'G', 'o', 'l', 'i']
# ['i', 'l', 'o', 'G', ' ', 'a', 'h', 'm', 'i', 's', 'a', 'r', 'a', 'N']
# PS D:\Goli\p_time> 
