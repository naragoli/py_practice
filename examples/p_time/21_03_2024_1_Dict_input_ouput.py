#input no of students with name,marks
#output display name and mark in dict

def dict_function(n):
    temp_count=1
    results={}
    while temp_count <= n:
        student=input('Enter the student name')
        marks=input('Enter the student marks')
        results[student]=marks
        temp_count+=1
    else:
        return results



def main():
    student_number=eval(input('Enter no of students'))
    student_marks=dict_function(student_number)
    print('student name','\t','student marks')
    for student in student_marks:
        print('\t',student,'\t','\t',student_marks[student])

if __name__ == '__main__':
    main()