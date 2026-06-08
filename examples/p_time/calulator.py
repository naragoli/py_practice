from src.utils.clear import *
clear()


print('###################Mathematical Calculator###################')
print('Enter Num1:', end="")
num1 = int(input())
print('Enter Num2:', end="")
num2 = int(input())

flag = True

def addition(a, b):
    return a+b

def subs(a, b): 
    return a-b

def mul(a,b):
    return a*b

def dev(a,b):
    try:
        c=a/b
        return  c
    except Exception as e:
        print(e)


def remainder(a,b):
    return a%b


while flag:
    print('Menu:')
    print("1:addition", "2:Substation", "3:Devision", "4:Remainder","5:Quit", sep='\n')
    print('Enter the choice:', end="")
    choice = int(input())
    if choice == 1:
        print("Addition of both the numbers :", addition(num1, num2))
    elif choice == 2:
        print("Subtraction of both the numbers:", subs(num1, num2))
    elif choice == 3:
        print("Devision of both the numbers :", dev(num1, num2))
    elif choice == 4:
        print("Remainder of both the numbers:",remainder(num1, num2))
    elif choice == 5:
        flag = False
    else:
        print('Exiting the prompt')

