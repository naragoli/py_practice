def nested_function():
    print('Working with nested_main function:')
    def nested_child():
        print('Working with child function')
    print('Printing local and global values:',locals(),globals(),sep='\n')
    nested_child()

def nested_function1():
    print('Working with nested_main function1:')
    def nested_child1():
        print('Working with child function1')
    print('Printing local and global values:',locals(),globals(),sep='\n')
    return nested_child1()


def main():
    print('Working with main function:')
    nested_function()
    try:
        nested_child()
    except Exception as e:
        print(e)
    print('*'*50)
    nested_return=nested_function1()
    nested_return
    



if __name__ == '__main__':
    main()

