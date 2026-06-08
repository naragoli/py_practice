
print('Contine" ')
for i in range(10):
    if(i%2 == 0):
        continue
    print(i)

print("* " *25)


print('List with break')
list1=['goli','kiran','avadh','raaghavan','kittu']
for item in list1:
    if item == 'avadh':
        break
    print(item)


print("* " *25)
print('List with contine')
list2=['goli','kiran','avadh','raaghavan','kittu']

for item in list2:
    if item == 'avadh':
        continue
    print(item)

print("* " *25)
print('loops with else block')

list3= [10,20,30,40,50,60,200]
for item in list3:
    if item>100:
        print('item is out of range and doing break')
        break
    print(item)
else:
    print('Entire list is processed ')

print("* " *25)

list3.insert(3,110)
print(list3)
print("* " *25)
print('loops with else block')

#list3= [10,20,30,40,50,60]
for item in list3:
    if item>100:
        print('item is out of range and doing break')
        break
    print(item)
else:
    print('Entire list is processed ')

print("* " *25)