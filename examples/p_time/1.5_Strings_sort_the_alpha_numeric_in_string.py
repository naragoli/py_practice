from src.utils.clear import *


clear()
whoami(argv[0])

print('Enter a random string with alpha-numeric content:', end="")
main_string = input()

temp_alpha_string = ""
temp_numeric_string = ""
temp_special_string = ""
result_string = ""

for string_character in main_string:
    if string_character.isalpha():
        temp_alpha_string += string_character
    elif string_character.isnumeric():
        temp_numeric_string += string_character
    else:
        temp_special_string += string_character
else:
    result_string = temp_alpha_string + temp_numeric_string + temp_special_string
    print("Sorted String is :", result_string)



