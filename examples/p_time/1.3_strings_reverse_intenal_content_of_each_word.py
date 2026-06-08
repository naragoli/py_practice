from src.utils.clear import *


def string_reverse(s):
    count = len(s)
    temp_list = []
    while True:
        count -= 1
        temp_list.append(s[count])
        if count == 0:
            break
    return''.join(temp_list)


clear()
whoami(argv[0])


print("Enter a random string phrase: ", end='')
main_string = input()
word_count = word_count_in_string(main_string)
print('Actual given string :', main_string)
print('Word count in given string:', word_count)
temp_string_list1 = main_string.split()
temp_string_list2 = []

for temp_string in temp_string_list1:
    temp_string_list2.append(string_reverse(temp_string))
else:
    result = ' '.join(temp_string_list2)

print('Reversed strings in individual word:',result)




