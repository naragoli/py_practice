#input : AABBCDDDEEFFCCDDHHII
#output : ABCDEFCDHI
def duplicate_finder(s):
    output=""
    for i in s:
        if i not in output:
            output+=i
    return output


def duplicate_finder1(s1):
    output=[]
    for temp in s1:
        if temp not in output:
            output.append(temp)
    else:
        return "".join(output)



def main():
    input_string=input('Entre a random string with duplicate characters:')
    result_string=duplicate_finder1(input_string)
    print("{}:{} \n {}:{}".format('Input',input_string,'Output',result_string))

if __name__ == '__main__':
    main()