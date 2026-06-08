from sys import argv
sum = 0
args = argv[1:]

print("Arguments:", args)
print(type(args))

for item in args:
    print("Processing argument:", item)
    try:
        arg_list_numbers = [int(x) for x in item.split(',')]
        for arg_number in arg_list_numbers:
            sum += arg_number
        print("Sum of list items in :",item, 'is', sum)
        sum=0
    except ValueError:
        print('List conversion issue for:', item)



