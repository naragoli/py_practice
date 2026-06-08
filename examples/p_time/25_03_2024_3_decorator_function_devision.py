def smart_division(func):
    def inner(x,y):
        print("Doing the devision of {} {}".format(x,y))
        if y==0:
            print('Devision by 0 is not possible')
            return
        else:
            return func(x,y)
    return inner
@smart_division
def division_num(a,b):
    return a/b

def main():
    num1,num2=[int(x) for x in input('Enter two number').split(',')]
    division_output=division_num(num1,num2)
    print("Divison of {} {} is {}".format(num1,num2,division_output))

if __name__=='__main__':
    main()