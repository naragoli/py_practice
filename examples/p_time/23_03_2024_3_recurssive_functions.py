def fact_function(n):
    if n==0:
        return 1
    else:
        return n*fact_function(n-1)

def main():
    input_number=eval(input('Enter a number to find the factorial:'))
    fact_output= fact_function(input_number)
    print("{} factorial is {}".format(input_number,fact_output))


if __name__ == '__main__':
    main()