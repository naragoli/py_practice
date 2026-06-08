# Challenge 1.1: Square numbers
# Create a list of squares for numbers 1 to 10
# Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#challenge_1_1 = 

numbers = list(range(1, 11))
print(type(numbers))
print(numbers)
sq_numbers= [x**2 for x in numbers]
print(sq_numbers)

x='#'
print(x*50)

words = ['apple', 'banana', 'cherry', 'date']
upper_case_words=[x.upper() for x in words]
print(words)
print(upper_case_words)

print(x*50)

words = ['python', 'java', 'c', 'javascript']
lengths_strings =[len(word) for word in words]
print(lengths_strings)

print(x*50)

multiple_of_5= [x*5 for x in range(1,11)]
print(multiple_of_5)

print(x*50)

numbers_1_20 =list(range(1,21))
even_number=[x for x in numbers_1_20 if x%2 ==0]
odd_number=[x for x in numbers_1_20 if x%2 !=0]

print("Even numbers:", even_number)
print("Odd numbers:", odd_number)
print(x*50)

words_1 = ['cat', 'dog', 'elephant', 'ant', 'butterfly', 'bat']

words_with_len=[x for x in words_1 if len(x)>3]

print("Words with more than 3 letters:", words_with_len)
print(x*50)

nums_1_20 = list(range(1,21))
SQ_Odd_numbers=[x**2 for x in nums_1_20 if x %2 !=0]
SQ_even_numbers=[x**2 for x in nums_1_20 if x%2==0]
print("Square of odd numbers from 1 to 20:", SQ_Odd_numbers)
print("Square of even numbers from 1 to 20:", SQ_even_numbers)
print(x*50)

random_words = ['apple', 'banana', 'apricot', 'cherry', 'avocado', 'date']
words_with_a = [x for x in random_words if x.startswith('a')]
print("Words that start with 'a':", words_with_a)
print(x*50)

random_numbers=list(range(1,20))
even_odd_list=['even' if x%2==0 else 'odd' for x in random_numbers]
print("Even or Odd list:", even_odd_list)
print(x*50)