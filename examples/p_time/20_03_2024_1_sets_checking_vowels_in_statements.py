# input : a random statement with multiple words
# output : what are the different vowel available in input


def set_function(s):
    vowels={'a','e','i','o','u'}
    s1=set(s)
    print("{}:{}\t {}:{}".format('s',type(s),'s1',type(s1)))
    results=s1.intersection(vowels)
    return results

def main():
    input_string=input('Enter a random string with multiple words:')
    output_chars= set_function(input_string)
    print("{} in {} are :{}".format('vowel characters',input_string,output_chars))



if __name__ == '__main__':
    main()