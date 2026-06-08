def dict_vowel_count(s):
    vowels=['a','e','i','o','u']
    results={}
    for char in s:
        if char in vowels:
            results[char]=results.get(char,0)+1
    else:
        return results


def main():
    input_string=input('Enter a random string with vowel presence:')
    vowel_results=dict_vowel_count(input_string)
    print('Input String is :',input_string)
    for char,count in vowel_results.items():
        print("{} vowel repeated {} time in inputs string".format(char,count))

if __name__ == '__main__':
    main()