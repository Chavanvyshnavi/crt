#write prog to remove the duplicate valye from thelist
original_list=[12,24,27,98,98,76,45,3,25,16]

# Remove duplicates using a set
unique_list = list(set(original_list))

# Optional: Sort the result if order matters
unique_list.sort()

# Print the result
print("Original List:", original_list)
print("List after removing duplicates:", unique_list)

#or
list=[12,12,27,98,98,76,45,3,25,16]
print("original list:")
print(list)
New_list=[]
for i in list:
    if i not in New_list:
        New_list.append(i)
print(New_list)

#to read the list elements as input from the user and print a new list of numbers which are multiples of 5 

list=[]
New_list=[]
len=int(input("enter the size of list:"))
for i in range(len):
    temp=int(input(f"enter the integer value at {i}index:"))
    list.append(temp)
print("given list:")
print(list)
for i in list:
    if i%5==0:
        New_list.append(i)

print(New_list)

#to read the list elements as input from the user and print a new list of numbers which are multiples of 5 and 3


