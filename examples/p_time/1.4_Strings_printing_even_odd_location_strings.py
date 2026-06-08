from src.utils.clear import *


clear()
whoami(argv[0])

print('Enter a random sting:', end="")
main_string = input()
print('Entered String:', main_string)
print("Entered string length:", len(main_string))
index_count = 0
even_string_list = []
odd_string_list = []

for temp_string in main_string:
    if index_count % 2 == 0:
        even_string_list.append(main_string[index_count])
        index_count += 1
    else:
        odd_string_list.append(main_string[index_count])
        index_count += 1
else:
    print('Characters in even index:', " ".join(even_string_list))
    print('Characters in odd index:', " ".join(odd_string_list))

