from src.utils.clear import *

clear()
whoami(argv[0])

print('Enter a string wit duplicate values to generate a dict to count the duplicate:', end='')
main_string = input()
dedup_dict = {}

for temp_character in main_string:
    if temp_character in dedup_dict.keys():
        dedup_dict[temp_character] += 1
    else:
        dedup_dict[temp_character] = 1
else:
    for k,v in dedup_dict.items():
        print('{} = {} Times'.format(k, v))