from src.utils.clear import *
clear()
printfilename(argv[0])

print("Search operations in given string")
main_string=input('Enter a random string:')
sub_string=input('Enter a sub-string to search in main string:')
string_length=len(main_string)
sub_string_lenght=len(sub_string)
character_index=0
character_list=[]
if sub_string_lenght > 1:
    print("Entered search phrase",'\'',sub_string,'\'',"is a string not a characeter")
    if sub_string in main_string:
        print('\'',sub_string,'\'','Phrase is available in','\'',main_string,'\'')
        print('\'',sub_string,'\'','Phrase is located at',main_string.find(sub_string),"position of string",'\'',main_string,'\'')
    else:
        print('\'',sub_string,'\'','Phrase is not available in','\'',main_string,'\'')
else:
    print("Entered search phrase",'\'',sub_string,'\'',"is a character not a string")
    if sub_string in main_string:
        print('\'',sub_string,'\'','Character is available in String','\'',main_string,'\'')
        for temp in main_string:
            if temp==sub_string:
                character_list.append(character_index)
            character_index+=1
        print('\'',sub_string,'\'',"appeared",len(character_list),"times in string ",'\'',main_string,'\'')
        print('\'',sub_string,'\'',"appeared in",character_list,"positions of string",'\'',main_string,'\'')
    else:
        print('\'',sub_string,'\'','Character is not available in','\'',main_string,'\'')
    
# ###################### d:/Goli/p_time/9.5_string_search.py ###################################
# Search operations in given string
# Enter a random string:My Company Name is JP Morgan chase bank 
# Enter a sub-string to search in main string:z
# Entered search phrase ' z ' is a character not a string
# ' z ' Character is not available in ' My Company Name is JP Morgan chase bank  '
# PS D:\Goli\p_time> 
###################### d:/Goli/p_time/9.5_string_search.py ###################################
# Search operations in given string
# Enter a random string:My Name is Narasimha Goli
# Enter a sub-string to search in main string:a
# Entered search phrase ' a ' is a character not a string
# ' a ' Character is available in String ' My Name is Narasimha Goli '
# ' a ' appeared 4 times in string  ' My Name is Narasimha Goli '
# ' a ' appeared in [4, 12, 14, 19] positions of string  ' My Name is Narasimha Goli '
# PS D:\Goli\p_time> 

# ###################### d:/Goli/p_time/9.5_string_search.py ###################################
# Search operations in given string
# Enter a random string:i am working in JP Morgan Chase bank 
# Enter a sub-string to search in main string:bank
# Entered search phrase ' bank ' is a string not a characeter
# ' bank ' Phrase is available in ' i am working in JP Morgan Chase bank  '
# PS D:\Goli\p_time> 

# ###################### d:/Goli/p_time/9.5_string_search.py ###################################
# Search operations in given string
# Enter a random string:I am working for JP morgan chase bank 
# Enter a sub-string to search in main string:bunk
# Entered search phrase ' bunk ' is a string not a characeter
# ' bunk ' Phrase is not available in ' I am working for JP morgan chase bank  '
# PS D:\Goli\p_time> 