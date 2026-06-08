def decorator_function(func):
    def inner_function(n):
        if n %2 ==0:
            print(n,'Number is Even')
        else:
            print(n,'Number is odd')
    return inner_function

@decorator_function
def evennumber_print(number):
    print('Given number is Even:',number)

def main():
    input_num=eval(input('Enter a number to test its Even/odd:'))
    evennumber_print(input_num)
    print('* '*50)
    decorator_call = decorator_function2(evennumber_print2)
    decorator_call(input_num)


def decorator_function2(func):
    def inner_function2(n):
        if n %2 ==0:
            print(n,'Number is Even')
        else:
            print(n,'Number is odd')
    return inner_function2


def evennumber_print2(num1):
    print('Given number is Even:',num1)

if __name__=='__main__':
    main()