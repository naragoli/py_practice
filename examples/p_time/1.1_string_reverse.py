from src.utils.clear import *


clear()
whoami(argv[0])

print('Enter a random string to reverse the content in string:')
Test_string = input()
count = len(Test_string)
print('Entered String is :', Test_string)
print('Reversed String is:', end='')
while Test_string:
    count -= 1
    print(Test_string[count], end='')
    if count == 0:
        break

#Method 2
print()
print('Reversed string in Method2 ')
print(Test_string[::-1])
