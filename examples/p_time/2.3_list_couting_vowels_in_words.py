from src.utils.clear import *

clear()
whoami(argv[0])

vowels = ['a', 'e', 'i', 'o', 'u']
random_word = input("Enter a random word to count the vowels:")
found =[]

for each_character in random_word:
    if each_character in vowels:
        if each_character not in found:
            found.append(each_character)
        else:
            print(end="")
    else:
        print(end="")
else:
    print("vowel characters in given random word:", found)
    print('Number of different vowels present in', random_word, 'is :', len(found))
