#tuple packing
Tuple=10,20,30,40,50,60,70,80,90,100
print(Tuple)
print(type(Tuple))
#Tuple unpacking
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=Tuple
print(n1,type(n1))
print(n2,type(n2))

#repeating
b=[1,2,3]
result=b*3
print(result)
#concatenation
a=(10,20,30)
b=(1,2,3)
result=a+b
print(result)
#repeatation of tuple
b=(1,2,3)
result=b*3
print(tuple)
#nested tuple
Tuple=('a','b','c'),('A','B','C'),(1,2,3),(-1,-2,-3)
print(Tuple)
for i in Tuple:
    print(i,type(Tuple))

Tuple=(10,25,5,15,17,30,35)
print(Tuple)
print("Maximum number:",max(Tuple))
print("Minimum number:",min(Tuple))
print("summation:",sum(Tuple))
print("sorted Tuple:",sorted(Tuple))
print()
#to create tuple of prog languages being length as 15 and find the maximum element ,min element and print sorted tuple and reverse tuple
#to create a tuple of names and print the original tuple and print the names which has length of 5 from  the tuple

Tuple=('python','java','oracle','c','c++','html','dsa','c#','swift','sql','R','ruby','perl','typescript','kotlin')
print(Tuple)
print(len(Tuple))
print("Maximum element:",max(Tuple))
print("Minimum element:",min(Tuple))
print("Sorted Tuple:",sorted(Tuple))


#to display a menu of food items(list)
#create a Tuple of prices with respect to food items list 
#read the input from the user for ordering the food including quantity
#if it exists in the menu ..confirm order
#if not print a message 
#while billing , read phone no..,feeedback,read tip amount 
#add 18%gst to the bill &print the bill if bill>0














#to declare a list of words and declare a tuple of words and map it to print the a combined words
n=int(input("enter the word:"))
list=['marker','water','wrist','bread','class','home','black','crack']
tuple=('pen','bottle ','watch','jam','room','theatre','jam','coffee','jack')
i=1
while(i<=n):
    word=input("Enter the word:")
    index=list.index(word)
    print(f"{word}-{tuple[index]}")
    i+=1

#write a python prog to declare a list of grocery items and read the input from the user from 1 to 5 
#to display the list of grocery items in a sorted way
#to take the input from the user and add items to the cart
#to give the cart items 
#to update the quantity or the item present in the cart 
#generate a bill including item names , item quantity , price and if final bill amount is greater than 1000 the user will get 10%discount 
#if the user purchases anty item more than 10 kgs reduce the amount of 1 kg from that particular item price
#if the user prchases any particular item add buy 1 get 1 offer , add 25%gst to the over all bill and print bill 

grocery_items = ['oil','rice','dal','wheat']
print("Available Grocery Items (sorted):")
for item in sorted(grocery_items):
    print(f"{item} - ₹{grocery_items[item]} per kg")

# Take user input to add items to the cart
cart = {}
print("\nEnter items to add to your cart (max 5 items):")
for i in range(5):
    item = input(f"Enter item {i+1}: ").lower()
    if item in grocery_items:
        qty = float(input(f"Enter quantity of {item} in kg: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
    else:
        print("Item not available in grocery list.")





























































































































































































