'''def string_odd_even(string_to_parse):   # both the functions are working.
    temp_count=0
    string_len=len(string_to_parse)-1 # to manage the index in loop
    odd_string =[]
    even_string = []
    while string_len >=0:
        if string_len %2 ==0:
            even_string.append(string_to_parse[string_len])
        else:
            odd_string.append(string_to_parse[string_len])
        string_len-=1
    return even_string,odd_string
'''
def string_odd_even(string_to_parse):
    temp_count=0
    string_len=len(string_to_parse)-1 # to manage the index in loop
    odd_string =[]
    even_string = []
    while temp_count <= string_len:
        if temp_count %2 ==0:
            even_string.append(string_to_parse[temp_count])
        else:
            odd_string.append(string_to_parse[temp_count])
        temp_count+=1
    return even_string,odd_string

def main():
    input_string=input('Enter a random string:')
    even_character,odd_character=string_odd_even(input_string)
    print("{} {}\n {} {}".format('even characters',even_character,'odd characters',odd_character))

if __name__ == '__main__':
    main()