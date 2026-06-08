#input nested list possible 3 listed in single list
# 3x3 matrix should be printed

#[[10,20,30],[40,50,60],[70,80,90]]  # both are working.

def main():
    nested_list = eval(input('Enter a nested list:'))
    i = 0
    while i < len(nested_list):
        j = 0
        while j < len(nested_list[i]):
            print(nested_list[i][j], end=" ")
            j += 1
        print()  # Move this print statement to a new line
        i += 1  # Indent this line inside the outer while loop


'''def main():
    nested_list = eval(input('Enter a nested list:'))
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            print(nested_list[i][j],end=' ')
        print()
'''


if __name__ == '__main__':
    main()