from src.utils.clear import *

clear()
whoami(argv[0])

list1 = list2 = []

list1 = list(range(1, 10, 1))
list2 = list(range(11, 20, 1))

print('list1 type:', type(list1))
print('list2 type:', type(list2))

print(list1, list2, sep='\n')

list1.extend(list2)
print('list1 after extending with list2:', list1)
print('Enter a value from list1 to remove:', end='')
del_value = int(input())

if del_value in list1:
    list1.remove(del_value)
    print('list1 after deleting the [',del_value,']', list1)
else:
    print('[',del_value,']','not listed in list1',list1)
