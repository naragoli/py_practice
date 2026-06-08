from sys import argv

sum=0

args=argv[1:]

for item in args:
    x=int(item)
    sum+=x
print('sum of arguments is :',sum)
