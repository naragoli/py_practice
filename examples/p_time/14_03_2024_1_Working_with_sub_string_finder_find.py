def sub_string_finder(main_string,sub_string):
    sub_string_found = False  # starting as sub string not found, because of that string.find will return -1
    sub_string_position = -1
    sub_string_positions =[]
    sub_string_count=0
    main_string_length = len(main_string)
    while True:
        sub_string_position=main_string.find(sub_string,sub_string_position+1,main_string_length)
        if sub_string_position == -1:
            break
        sub_string_found=True
        sub_string_positions.append(sub_string_position)
        sub_string_count+=1
    if sub_string_found ==False:
        print('Sub string not found')
        return None
    return sub_string_positions,sub_string_count

def main():
    main_string=input('Enter a random main string:')
    sub_string=input('Enter sub string to search in main string to find the position:')
    sub_string_position,sub_string_counts= sub_string_finder(main_string,sub_string)
    if sub_string_position is not None:
        for position in sub_string_position:
            print("{} sub string found at {} position  in main string {}".format(sub_string,position,main_string))
    if sub_string_counts != 0:
        print("{} sub string is repeated {} time in {}".format(sub_string,sub_string_counts,main_string))

if __name__ == '__main__':
    main()