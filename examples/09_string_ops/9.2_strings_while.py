from src.utils.clear import *
clear()
printfilename(argv[0])

s=input('Enter a string:')
lenght=len(s)
forward_index_count=0
reverse_index_count=-1
print("Forward direction:")
while forward_index_count<lenght:
    print(s[forward_index_count],end=',')
    forward_index_count+=1
print()
print("Reverse direction:")
while reverse_index_count >= -lenght:
    print(s[reverse_index_count],end=',')
    reverse_index_count-=1