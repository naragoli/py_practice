# Positional
# Keyword
# default
# variable length

def fun_keyword(name,marks):
    print("{} person got {} marks".format(name,marks))

def fun_default(name,marks='100'):
    print("{} person got {} marks".format(name,marks))

def fun_variable_lengh(*n):
    sum=0
    result=""
    for i in n:
        sum+=i
    else:
        print("sum of aurguments is :",sum)



def main():
    print('Keyword arguments')
    try:
        fun_keyword(name='Goli',marks='45')
        fun_keyword(name='narasimha',marks='55')
        fun_keyword(marks='45',name='Kiran')
        fun_keyword()
        fun_keyword(name='avadh')
        fun_keyword(marks='90')
    except Exception as e:
        print(e)
    print('default arguments')
    try:
        fun_default(name='Goli',marks='45')
        fun_default(name='narasimha')
        fun_default(name='kiran',marks='90')
        fun_default(marks='45')
    except Exception as e:
        print(e)
    print('variable length arguments')
    try:
        fun_variable_lengh(1,2,3,4,5,6,7,8,9,10)
       ##fun_variable_lengh('goli','narasimha','kiran')
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()



