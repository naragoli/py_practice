#Input : first 100 numbers & sum of previous 2 numbers
#output : 0,1,1,2,3,5,8,13,21,...

def generator_fib(num1):
     x,y=0,1
     while x <=num1:
         print('Round:',x)
         yield x
         print('x value printed:',x)
         x,y=y,x+y
         print('x ,y values after:',x,y)

def generator_fib1(num1):
    x,y,z=0,1,2
    while x <=num1:
        print('Round:',x)
        yield x
        print('x value printed:',x)
        x,y,z=y,z,x+y+z
        print('x ,y,z values after:',x,y,z)

def main():
    output_list=[]
    output_list1=[]
    input_value=eval(input('Enter a random number'))
    output_list=list(generator_fib(input_value))
    for i in output_list:
        print(i,end='\t')
    output_list1=list(generator_fib1(input_value))
    for i in output_list1:
        print(i,end='\t')
if __name__ == '__main__':
    main()

'''
def generator_fib(num1):
    def inner_function():
        x,y=0,1
        while True:
            yield x
            x,y=y,x+y
    for n in inner_function():
        if n >num1:
            break
        print(n)
'''

