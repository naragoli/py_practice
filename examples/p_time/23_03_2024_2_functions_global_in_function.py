def fun_global_test():
    global a
    a=500
    b=600
    print('Printing a from fun_global_test function module: ',a)
    print('Local variable:',locals())
    print('Global variable:',globals())

def fun_Local_test1():

    try:
        a=700
        print('Printing a from  fun_Local_test1 module:',a)
        print('Printing global value of a from fun_global_test:',globals()['a'])
        print('Local variable:',locals())
        print('Global variable:',globals())
    except Exception as e:
        print(e)

def fun_using_global_test2():
    try:
        global a
        b=800
        a=a+1
        b=b+1
        print('Printing a value from fun_using_global_test2 module',a)
        print('Printing b value from fun_using_global_test2 module',b)
        print('Local variable:',locals())
        print('Global variable:',globals())
    except Exception as e:
        print(e)
def main():
    print('* '*25)
    fun_global_test()
    print('* '*25)
    fun_Local_test1()
    print('* '*25)
    fun_using_global_test2()
    print('* '*25)

if __name__ == '__main__':
    main()