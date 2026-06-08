from reusable_functions.clear import *
clear()
printline()
printfilename(argv[0])
prime_list=[]
non_prime_list=[]
print('Working on printing the prime numbers between two numbers')
start_range,end_range=[int(x) for x in input('Enter start and end range of numbers in , separated :').split(',')]

for i in range(start_range,end_range+1):
        if i>1:
            for num1 in range(2,i):
                if(i%num1)==0:
                    non_prime_list.append(i)
                    break
            else:
                prime_list.append(i)
else:
    print("completed processing prime numbers between",start_range,'and',end_range)

print('Prime Numbers list:',prime_list )
print('Non Prime numbers list',non_prime_list)


# ########################################################################################
# ###################### d:/Goli/p_time/7.5_prime_between_range.py ###################################
# Working on printing the prime numbers between two numbers
# Enter two numbers separated by ,:0,100
# completed processing prime numbers between 0 and 100
# Prime Numbers list: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# Non Prime numbers list [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]
# PS D:\Goli\p_time> 