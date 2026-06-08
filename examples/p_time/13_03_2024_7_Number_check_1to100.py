def num_finder(num1):
    print('num_finder function block starting')
    print('num1 {} received from the main block'.format(num1))
    #logic is : need to find the give number is between 1 to 100
    if num1>=1 and num1<=100:
        print("num1 {} is between 1 to 100".format(num1))
    else:
        print("num1 {} not in range".format(num1))

def main():
    print('Main block started')
    number_check = int(input('Enter a number to check :'))
    num_finder(number_check)

if __name__ == '__main__':
    main()

