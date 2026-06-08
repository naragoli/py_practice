from src.utils.clear import *

clear()
whoami(argv[0])

print("Enter a string with duplicate values to de-dup it :", end="")
main_string = input()
temp_string_list = []

for temp_character in main_string:
    if temp_character not in temp_string_list:
        temp_string_list.append(temp_character)
else:
    out_string = "".join(temp_string_list)
    print("De-duped string is : ", out_string)
