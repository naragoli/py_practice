row=int(input('Enter number of rows'))

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

print("* " *25)

square_size = int(input('Enter Square size:'))
for row in range(1,square_size+1):
    for column in range(1,square_size+1):
        print("*", end=" ")
    print()

rectangle_row=int(input('Enter rectangle row:'))
rectangle_column=int(input('Enter rectangle column:'))

for row in range(1,rectangle_row+1):
    for column in range(1,rectangle_column+1):
        print("*", end=" ")
    print()

print("* " *25)
# printing pyramid of *
# if pyramid size is 5


height = int(input("Enter the height of the pyramid: "))

# Outer loop for rows
for i in range(height):
    # Print leading spaces
    print(" " * (height - i - 1), end="")

    # Inner loop for asterisks
    for j in range(2 * i + 1):
        print("*", end="")

    # Move to the next line after each row
    print()
print("* " *25)
for i in range(1,height+1):
    print(" "*(height-i),end="")
    print("* "*i)

print("* " *25)