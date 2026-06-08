def find_string_type(string_check):
       if string_check.isnumeric():
           return 'numeric'
       elif string_check.isalpha():
           if string_check.isupper():
               return 'upper alpha'
           else:
               return 'lower alpha'
       elif string_check.isalnum():
           return 'alpha numeric'
       elif string_check.isspace():
           return 'space'
       else:
           return 'special character'


def main():
    main_string=input('Enter a random string to find alphanum type:')
    string_type=find_string_type(main_string)
    print("{} is {} type".format(main_string,string_type))

if __name__=='__main__':
    main()
