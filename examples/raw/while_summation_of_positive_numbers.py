print("Forcing the user to enter the positive numbers for summation")
num1=int(input("Enter First positive number:"))
num2=int(input("Enter second positive number:"))
while num1 < 0 or num2 < 0:
    if num1 < 0:
        num1 = int(input("Enter a positive number for num1:"))
    if num2 < 0:
        num2 = int(input("Enter a positive number for num2:"))
num3=num1+num2
print(f"num1:{num1}  num2:{num2}")
print(f"num3={num1}+{num2}={num3}")