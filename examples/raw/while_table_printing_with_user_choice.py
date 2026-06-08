print("Printing Tables in user choice with number of iterations")
table_variable=int(input("Enter which number table you want to print:"))
count_variable=1
table_end_variable=int(input("Enter the number of table iterations:"))

while count_variable <=table_end_variable:
    print(table_variable,"x",count_variable,"=",table_variable*count_variable)
    if count_variable == table_end_variable:
            print("Done with printing the",table_variable,"table","in",table_end_variable,"interations")
            break
    count_variable = count_variable + 123
    
