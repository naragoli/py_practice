from src.utils.clear import *


clear()
whoami(argv[0])

print("Enter a random string with alpha-numeric content:", end="")
main_string = input()
output_sting = ""
previous_character = ""


for temp_character in main_string:
    if temp_character.isalpha():
        output_sting += temp_character
        previous_character = temp_character
    elif temp_character.isnumeric():
        output_sting = output_sting + previous_character * (int(temp_character)-1)
    else:
        print(end="")

else:
    print('Output string : ', output_sting)


