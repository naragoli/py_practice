from reusable_functions.clear import *
clear()
printfilename(argv[0])
from sys import argv
print('argv type :',type(argv))
print('Number of arguments in argv list',len(argv))
print('Content in argv list',argv)
print('Content in argv list in new line')
for x in argv: print(x)
printline()
