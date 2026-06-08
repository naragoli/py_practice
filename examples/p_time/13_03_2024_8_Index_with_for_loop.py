input_string = input('Enter a random string')
print("Entered string is :{}".format(input_string))

for index,value in enumerate(input_string):
    print("{} content is located at {} index".format(value,index))
