def fun_test():
    print('Printing variable a from function :',a)
    b=a+1
    print('Printing variable b after using a:',b)

def fun_test1():
    a=12
    print('Printing variable a from function1 :',a)


def main():
    global a
    a = 10
    print('Print variable a from main function A:',a)
    fun_test()
    fun_test1()
if __name__== '__main__':
    main()

