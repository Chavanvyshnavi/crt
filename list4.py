#Write a python program to read the size of list as input from the userand take the list elements also as input from the userand find the 
#len of the listthe maximum element or th e number and similarly maximum , min, the summation of elements and print sorted list in ascending order
Size=int(input("Enter the Size of the list:"))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the Element at {i}index:"))
    Num.append(Temp)
print(f"Given List:{Num}")
print("maximum element:",max(Num))
print("minimum element:",min(Num))
print("summation element:",sum(Num))
print("sorted list:",sorted(Num))