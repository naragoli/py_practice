def string_reserve(string_to_parse):
    temp_string =""
    string_length =len(string_to_parse)-1 # until last string index
    while string_length >= 0:
        temp_string+=string_to_parse[string_length]
        string_length-=1
    return temp_string

def content_manage(input_string):
    split_string=input_string.split()
    string_list_len=len(split_string)-1 # to count until end
    temp_list=[]
    temp_count=0
    while temp_count <= string_list_len:
        temp_list.append(string_reserve(split_string[temp_count]))
        temp_count+=1
    return " ".join(temp_list)

def content_reverse(input_string):
    split_string= input_string.split()
    string_list_len=len(split_string)-1 # for the index purpose
    temp_list=[]
    while string_list_len >=0:
        temp_list.append(string_reserve(split_string[string_list_len]))
        string_list_len-=1
    return " ".join(temp_list)


def main():
    random_string=input('Enter a random string with multiple words:')
    parsed_string=content_manage(random_string)
    reversed_content=content_reverse(random_string)
    print("{} {}\n {} {} \n {} {}".format('Actual string:',random_string,'Reversed string:',parsed_string,'content reverse',reversed_content))


if __name__=='__main__':
    main()
