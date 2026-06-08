mylist=["Hi","i","am","narasimha","goli","trying to ","learn","-1","True","0"]
print(mylist)
print(len(mylist))
mylist.append("i am from HYD")
print(mylist)
print(len(mylist))
print(mylist[1])

print(mylist[-1])
print(mylist[2:5])
print(mylist[3:])
print(mylist[:7])
print(mylist[-6:-2])
#mylist.insert(1:"Hyderabad")

if "narasimha" in mylist:
        print("string availabel in list")
count =0
for i in mylist:
        if i == "narasimha":
            print(f"String {i} is positioned at {count} index of list")
        count +=1
