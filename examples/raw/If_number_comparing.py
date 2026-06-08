num1=int(input("Enter Num1 "))
num2=int(input("Enter num2 "))
num3=int(input("Enter num3 "))
print(f"Num1:{num1},Num2:{num2},Num3:{num3}",sep='\n')

if num1 < num2:
    temp=num1
    if temp<num3:
        print("num1 is small number",temp,)
else:
    if num2<num3:
        temp=num2
        print("num2 is small nuber",temp)
    else:
        print("Num3 is small number",num3)