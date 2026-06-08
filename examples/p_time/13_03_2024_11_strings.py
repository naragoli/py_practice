s=input('Enter a random string:')

i=0
for x in s:
    print("character at positive index {} and Negative index {} is {}".format(i,i-len(s),x))
    i+=1

print("# "*30)
temp=0
for index,value in enumerate(s):
    print("character {} at index {} and negative index is {}".format(value,index,temp-len(s)))
    temp+=1

print("# "*30)

#printing forward and backward characers in programatic

print('Actual string is :',s)
string_len=len(s)
temp_count=0

print('forward direction')

while temp_count < string_len:
    print(s[temp_count],end=" ")
    temp_count+=1
print()
print('Backword printing')
temp_count=-1
while temp_count>=-string_len:
    print(s[(temp_count)],end=" ")
    temp_count-=1
print()
print("# "*30)
print()
print(s, 'printing in forward', s[::], end=" ")
print()
print(s, 'printing in backward', s[::-1],end=" ")
print()
print("# "*30)
print()
print('Substring check')
sub_string=input("Enter a substring to check in main string")
if sub_string in s:
    print("{} is part of {}".format(sub_string,s))
else:
    print("{} not part of {}".format(sub_string,s))