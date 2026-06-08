def find_biggest_number(num1,num2,num3):
    print("Values received from main block are {} {} {}".format(num1,num2,num3))
    try:
        if num1>num2 and num1>num3:
            print("num1 {} is max number".format(num1))
        elif num2 > num3:
            print("num2 {} is max number".format(num2))
        else:
            print("num3 {} is max number".format(num3))
    except ValueError:
        print("Invalid Inputs formats")


def main():
    n1,n2,n3=[int(x) for x in input("Enter three numbers in comma separated:").split(',')]
    find_biggest_number(n1,n2,n3)
    print('main block execution completed')


if __name__ == '__main__':
    main()



