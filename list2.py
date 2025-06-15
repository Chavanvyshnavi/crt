#write a python program to read list elements as input from the user &diplay the list element using for loop
Size=int(input("Enter the size of List:"))
prog_lang=[]
#reading the list elements as input
for i in range(Size):
   Temp=input("Enter a programming lang:")
   prog_lang.append(Temp)
print("Elements of the List:")
print(prog_lang)