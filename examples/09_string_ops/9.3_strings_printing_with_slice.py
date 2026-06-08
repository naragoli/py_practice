from src.utils.clear import *
clear()
printfilename(argv[0])

x=input("Enter a string:")
print("Printing in forward direction")
print('Method1:')
for i in x:
    print(i,end=',')
print()
print('Method2:')
for i in x[::]:
    print(i,end=',')
print()
print('Method2:')
for i in x[::1]:
    print(i,end=',')
print()
print("Printing in reverse direction")
for i in x[::-1]:
    print(i,end=',')