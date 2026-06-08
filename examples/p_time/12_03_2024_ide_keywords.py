import keyword

print('Printing possible keywords in python')
key_list = keyword.kwlist
print(key_list, end='\n')
#for key in key_list:
 #   print(key)
total_key_count = len(key_list)
print('Total keyword count is :',total_key_count)
#key_search = str(input('Enter a word to search its a python keyword'))

while True:
    key_search = str(input('Enter a word to search its a python keyword:'))
    if key_search in key_list:
        print('entered word is keyword')
        continue
    else:
        print('entered word is not a key word')
        key_search = ""




