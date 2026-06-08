#input AABBAACCDD
#output ABCD

def string_duplicate_merger(s):
    result=''
    for i in s:
        if i not in result:
            result+=i
    else:
        return  result


def main():
    input_string=input('Enter a random character set with duplicate characters:')
    sorted_string=string_duplicate_merger(input_string)
    print("{} {}".format('Actual string',sorted_string))


if __name__ =='__main__':
    main()