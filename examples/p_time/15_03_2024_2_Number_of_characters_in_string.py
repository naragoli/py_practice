#input AABBCCDDDDEE
#output  A2 B2 C2 D4 E2

def character_number(string_to_work):
    output ={}
    for temp in string_to_work:
        if temp not in output.keys():
            output[temp]=1
        else:
            output[temp]+=1
    return output

def main():
    input_string=input('Enter a random string with duplicate characters:')
    output_info=character_number(input_string)
    for k,v in output_info.items():
        print("{} character listed {} times".format(k,v))

if __name__ == '__main__':
    main()

