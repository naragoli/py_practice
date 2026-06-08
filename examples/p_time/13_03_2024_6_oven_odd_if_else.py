def even_odd_finder(num):
    try:
        print('num:{} receieved from main block for the execution'.format(num))
        if(num%2 == 0 ):
            return 'even'
        else:
            return 'odd'
    except TypeError:
        print('Input type casting error')

def main():
    print('Program to find over/odd from a user defined number:')
    n=int(input('Enter a random number:'))

    try:
        result= even_odd_finder(n)
        print("Entered number {} is {}".format(n,result))
    except Exception as e :
        print("Entered number {} is not validated ".format(n))


if __name__ == '__main__':
    main()
