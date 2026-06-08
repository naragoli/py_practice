'''def string_merge(s1,s2):   # functions are partial working.
    s1_len=len(s1)-1
    s2_len=len(s2)-1
    temp_count=0
    merged_string=""
    if s1_len > s2_len:
        while temp_count <= s1_len:
            merged_string+=s1[temp_count]+s2[temp_count]
            temp_count+=1
        return merged_string
    else:
        while temp_count <= s2_len:
            merged_string+=s2[temp_count]+s1[temp_count]
            temp_count+=1
        return merged_string

def string_merge(s1,s2):
    s1_len=len(s1)-1
    s2_len=len(s2)-1
    temp_count=0
    merged_string=""
    if s1_len == s2_len:
        while temp_count <= s1_len:
            merged_string+=s1[temp_count]+s2[temp_count]
            temp_count+=1
        return merged_string
    elif s1_len < s2_len:
        while temp_count <= s2_len:
            merged_string+=s2[temp_count]+s1[temp_count]
            temp_count+=1
        return merged_string
    elif s1_len > s2_len:
        while temp_count <= s1_len:
            merged_string+=s1[temp_count]+s2[temp_count]
            temp_count+=1
        return merged_string
'''

def string_merge(s1,s2):
    merged_string=""
    max_len=max(len(s1),len(s2))
    for i in range(max_len):
        if i< len(s1):
            merged_string+=s1[i]
        if i< len(s2):
            merged_string+=s2[i]
    return merged_string

def main():
    string1=input('Enter first string:')
    string2=input('Enter Second String:')
    merged_string=string_merge(string1,string2)
    print("{} {}".format('Merged string is:',merged_string))


if __name__=='__main__':
    main()