def dict_function_string(string_to_parse):
    result ={}
    for char in string_to_parse:
        result[char]=result.get(char,0)+1
    return result


def main():
    input_string = input("Enter a random string:")
    parsed_results=dict_function_string(input_string)
    for char,nums in parsed_results.items():
        print("{} character repeated {} time in input string".format(char,nums))


if __name__ =='__main__':
    main()



#input random string
#output  count of characters in string