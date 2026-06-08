#input : my name is narasimha goli
#output : vowels count : 8
#vowles : a e i o u

def main():
    vowels=['a','e','i','o','u']
    input_string=input('Enter a random string')
    split_string=input_string.split()
    found_vowels =[]
    for i in range(len(split_string)):
        for character in split_string[i]:
            if character in vowels:
                if character not in found_vowels:
                    found_vowels.append(character)
    print(found_vowels)
    print("{} {}".format('Vowels count in given input ',len(found_vowels)))

if __name__ =='__main__':
    main()