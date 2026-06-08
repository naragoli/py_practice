from sys import argv

print('Number of arguments passed to script are :', len(argv))
print('arguments list',argv)
print('argument list items')
for x in argv:
    print(x,sep='\n')


