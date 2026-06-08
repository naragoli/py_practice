books=["Goli","Narasimha","Avadh","Raaghavan","kiranmayee","Goli","Narasimha"]
lenght=len(books)
temp_list=books

print(books,temp_list,sep='\n')
for i in books:
        for j in temp_list:
            print(f'comparing outer for loop {i} with inner for loop {j}')
            if i==j:
                print(f'{i} duplicate in list')
                break


#Code wrong ; need to review 

