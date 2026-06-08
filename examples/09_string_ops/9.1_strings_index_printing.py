from src.utils.clear import *
clear()
printfilename(argv[0])

print("Printing the random string\'s index based characters from front and back")
random_string=input('Enter a string:')
print('Entered string is:',random_string, 'And its lenght is :',len(random_string))

forward_count=0
reverse_count=1
for index_character in random_string:
    print('Character presented in [',forward_count,'] of forward position is:',index_character)
    print('Character presented in [-',reverse_count,'] of reserve position is:',random_string[-reverse_count])
    forward_count+=1
    reverse_count+=1

count=0
for i in random_string:
    print(" Character presented at positive index {} and negative index {} is {}".format(count,count-len(random_string),i))
    count+=1




# ###################### d:/Goli/p_time/9.1_strings_index_printing.py ###################################
# Printing the random string's index based characters from front and back
# Enter a string:Narasimha
# Entered string is: Narasimha And its lenght is : 9
# Character presented in [ 0 ] of forward position is: N
# Character presented in [- 1 ] of reserve position is: a
# Character presented in [ 1 ] of forward position is: a
# Character presented in [- 2 ] of reserve position is: h
# Character presented in [ 2 ] of forward position is: r
# Character presented in [- 3 ] of reserve position is: m
# Character presented in [ 3 ] of forward position is: a
# Character presented in [- 4 ] of reserve position is: i
# Character presented in [ 4 ] of forward position is: s
# Character presented in [- 5 ] of reserve position is: s
# Character presented in [ 5 ] of forward position is: i
# Character presented in [- 6 ] of reserve position is: a
# Character presented in [ 6 ] of forward position is: m
# Character presented in [- 7 ] of reserve position is: r
# Character presented in [ 7 ] of forward position is: h
# Character presented in [- 8 ] of reserve position is: a
# Character presented in [ 8 ] of forward position is: a
# Character presented in [- 9 ] of reserve position is: N
# PS D:\Goli\p_time> 

# Printing the random string's index based characters from front and back
# Enter a string:Narasimha
# Entered string is: Narasimha And its lenght is : 9
#  Character presented at positive index 0 and negative index -9 is N
#  Character presented at positive index 1 and negative index -8 is a
#  Character presented at positive index 2 and negative index -7 is r
#  Character presented at positive index 3 and negative index -6 is a
#  Character presented at positive index 4 and negative index -5 is s
#  Character presented at positive index 5 and negative index -4 is i
#  Character presented at positive index 6 and negative index -3 is m
#  Character presented at positive index 7 and negative index -2 is h
#  Character presented at positive index 8 and negative index -1 is a
# PS D:\Goli\p_time> 