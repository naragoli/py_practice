'''def string_words_in_reverse_order(string_to_parse):   ##### in return string concat is used - not working as expected
    split_string=string_to_parse.split()
    string_to_return_list=[]
    string_to_return=''
    split_string_list_length = len(split_string)-1 # to print from reserve

    while split_string_list_length >=0:
        string_to_return_list.append(split_string[split_string_list_length])
        split_string_list_length-=1
    for item in string_to_return_list:
        string_to_return+=item
    return string_to_return
'''
def string_words_in_reverse_order(string_to_parse):
    split_string = string_to_parse.split()
   # print('split string is : ',split_string)
    string_to_return_list=[]
    split_string_list_length = len(split_string)-1 # to print from reserve
    while split_string_list_length >=0:
       # print(split_string[split_string_list_length])
        string_to_return_list.append(split_string[split_string_list_length])
        split_string_list_length-=1
    return " ".join(string_to_return_list)

def main():
    temp_string=input('Enter a random string:')
    reversed_string=string_words_in_reverse_order(temp_string)
    print("{}\n{}".format(temp_string,reversed_string))

if __name__ =='__main__':
    main()