import string
from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])

string_component=input('Enter a string component:')
search_component=input("Enter search component:")
search_list=[]
search_count=0

string_lenght=len(string_component)

if search_component in string_component:
    print(search_component,"  is listed in ", string_component)
    for i in string_component:
        if i==search_component:
            search_list.append(search_count)
        search_count=search_count+1
    print(search_component,' is appeared',len(search_list),'times in',string_component)
    print(search_component, " appreared in ",search_list ,"positions of",string_component )
else :
    print(search_component,"  is not listed in ", string_component)

printline()



# ########################################################################################
# ###################### d:/Goli/p_time/6.1_if_test.py ###################################
# Enter a string component:My Name is Narasimha Goli
# Enter search component:a
# a   is listed in  My Name is Narasimha Goli
# a  is appeared 4 times in My Name is Narasimha Goli
# a  appreared in  [4, 12, 14, 19] positions of My Name is Narasimha Goli
# ########################################################################################
# PS D:\Goli\p_time> 

# ########################################################################################
# ###################### d:/Goli/p_time/6.1_if_test.py ###################################
# Enter a string component:My Name is Narasimha Goli
# Enter search component:z
# z   is not listed in  My Name is Narasimha Goli
# ########################################################################################
# PS D:\Goli\p_time> 

