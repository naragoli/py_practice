print("Printing Tables")
table_variable=int(input("Enter which number table you want to print:"))
count_variable=1
table_end_variable=int(input("Enter the number of table iterations:"))

if count_variable <=table_end_variable:
    print(table_variable,"x",count_variable,"=",table_end_variable*count_variable)
    count_variable = count_variable + 1
    repeat
else:
    print("Done with printing the",table_end_variable,"table")


#break not working in if block 