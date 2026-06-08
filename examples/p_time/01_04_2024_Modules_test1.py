import A14_03_2024_3_string_reverse
import A14_03_2024_3_string_reverse as m
from A14_03_2024_3_string_reverse import string_reserve1 as s1
from A14_03_2024_3_string_reverse import string_reserve2 as s2
from A14_03_2024_3_string_reverse import string_reserve3 as s3


def main():
    input_string=input('Enter a random string to reserve:')
    out_string1=A14_03_2024_3_string_reverse.string_reserve1(input_string)
    out_string2=A14_03_2024_3_string_reverse.string_reserve2(input_string)
    out_string3=A14_03_2024_3_string_reverse.string_reserve3(input_string)

    out_string4=s1(input_string)
    out_string5=s2(input_string)
    out_string6=s3(input_string)

    print('Input staring:',input_string,out_string1,out_string2,out_string3,out_string4,out_string5,out_string6,sep='\n')
    print(__name__)
    print(A14_03_2024_3_string_reverse.__file__)
    print(m.__file__)
    print(__file__)
    print(dir())
    print(dir(A14_03_2024_3_string_reverse))
    module_items=(dir(A14_03_2024_3_string_reverse))
    for item in module_items:
        print(m.item)

if __name__ == '__main__':
    main()