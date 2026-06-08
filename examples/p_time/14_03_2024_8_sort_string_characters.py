#input b4c2aaa2
#output should bcaaa422

def character_sort(input_string):
    string_len=len(input_string)-1
    alpha_string=''
    num_string=''
    special_string =''
    for i in range(string_len):
        if input_string[i].isalpha():
            alpha_string+=input_string[i]
        elif input_string[i].isnumeric():
            num_string+=input_string[i]
        else:
            special_string+=input_string[i]

    return alpha_string+num_string+special_string

def main():
    random_string=input('Enter a random string:')
    sorted_character = character_sort(random_string)
    print("{} {}\n {} {}".format('Given string:',random_string,'sorted:',sorted_character))

if __name__ == '__main__':
    main()
