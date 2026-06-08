#input a4b3c2
#output aaaabbbcc

def string_manipulator(s):
    output=""
    previous_string=""
    special_string =""
    for i in range(len(s)):
        if s[i].isalpha():
            output+=s[i]
            previous_string=s[i]
        elif s[i].isnumeric():
            output+=previous_string*(int(s[i])-1)
        else:
            special_string+=s[i]
    return output+special_string


def main():
    input_string=input('Enter a random alnumeric string: ')
    out_string=string_manipulator(input_string)
    print("{} {} \n {} {}".format('Input:',input_string,'Output:',out_string))

if __name__ == '__main__':
    main()