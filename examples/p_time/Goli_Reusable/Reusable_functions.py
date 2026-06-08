from os import *
from sys import *


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def whoami(s):
    print('Current executing script name is :', s)


def word_count_in_string(s):
    temp_list = s.split()
    return len(temp_list)


def string_reverse(s):
    count = len(s)
    temp_list = []
    while True:
        count -= 1
        temp_list.append(s[count])
        if count == 0:
            break
    return''.join(temp_list)
