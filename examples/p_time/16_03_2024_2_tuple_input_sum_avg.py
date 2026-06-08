#input (1,2,3,4,5)
#output sum 15  avg =7.5

def tuple_function(t):
    sum=0
    index_count=len(t)
    for i in t:
        sum+=i
    else:
        return sum,sum/index_count



def main():
    tuple_input=eval(input('Enter a tuple with numbers:'))
    output=tuple_function(tuple_input)
    print(type(output))
    print(output)


if __name__ == '__main__':
    main()


