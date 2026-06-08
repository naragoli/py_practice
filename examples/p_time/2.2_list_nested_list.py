from src.utils.clear import *

clear()
whoami(argv[0])

list1 = list(range(10, 13, 1))
list2 = list(range(20, 23, 1))
list3 = list(range(30, 33, 1))
nested_list =[list1, list2, list3]

print('Nested list is :', nested_list)

print('Printing nested list in row')
for r in nested_list:
    print(r)

for row in range(len(nested_list)):
    for column in range(len(nested_list[row])):
        print(nested_list[row][column], end=" ")
    else:
        print()
else:
    print("Nested list printed in Matrix format")