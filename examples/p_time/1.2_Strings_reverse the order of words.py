from src.utils.clear import *


def word_count_in_string(s):
    temp_list = s.split()
    return len(temp_list)


clear()
whoami(argv[0])

print('Enter a random line to print the words in reverse order:', end="")
main_string = input()
word_count = word_count_in_string(main_string)
print('Word count in given string is :', word_count)

temp_string_list = main_string.split()
temp_count = word_count
reversed_string_list = []

while True:
    temp_count -= 1
    reversed_string_list.append(temp_string_list[temp_count])
    if temp_count == 0:
        break

result = " ".join(reversed_string_list)
print("Actual string:", main_string)
print('Reversed string :', result)


