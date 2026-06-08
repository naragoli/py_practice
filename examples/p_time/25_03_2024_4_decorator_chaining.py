def Decorator_1(func):
    print('Working form Decorator1')
    def inner(x):
        print('working from Decorator1_inner')
        x=x+10
        print('Value in Decorator1_inner is :',x)
        return func(x)
    return inner

def Decorator_2(func):
    print('Working from Decorator2')
    def inner(y):
        print('Working from Decorator2_inner')
        y=y+12
        print('Value in Decorator2_inner is :',y)
        return func(y)
    return inner

@Decorator_2
@Decorator_1
def num_handle(z):
    print('Processed value after Decoration is :',z)
    return z


def main():
    input_num=eval(input('Enter a number:'))
    output_num=num_handle(input_num)
    print("Entered number is {} and Processed number is {}".format(input_num,output_num))


if __name__ == '__main__':
    main()