def string_reserve1(string_to_reverse1):
    string_len=len(string_to_reverse1)-1 # to start from last index value
    reversed_string=""
    while string_len >= 0:
        reversed_string+=string_to_reverse1[string_len]
        string_len-=1

    return reversed_string

def string_reserve2(string_to_reverse2):
    return string_to_reverse2[::-1]

def string_reserve3(string_to_reverse3):
    return "".join(reversed(string_to_reverse3))

def main():
    main_string=input('Enter a random string:')
    print()
    reserved_string1= string_reserve1(main_string)
    reserved_string2= string_reserve2(main_string)
    reserved_string3= string_reserve3(main_string)
    print('Reversed strings are:')
    print("{}\n{}\n{}".format(reserved_string1,reserved_string2,reserved_string3))


if __name__ == '__main__':
    main()

