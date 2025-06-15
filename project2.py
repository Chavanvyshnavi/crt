#take a list of toy names (somerepeated).
#remove duplicates
#sort and display the final toy list to pack
list=['teddy','softtoys','teddy','ball','doll','doll']
print("original :")
print(list)
New_list=[]




#to read marks of 5 students for 3 subjects each and print the amrks list for individual student along with the class where 
#if student are marks are more than 90% then first class , second class- more than 75%,thirdclass- more than 50% and fail less than 50%



#add 10 songs to a playlist
#show the playlist in normal and reverse order
list=['vachinde','chilakaa','undioporadhey','kannulabashalu','anthaistam','vaalukanula','oosupodhu','jarajara','manohara','ippatikiinka']
print(list)
list.reverse()
print(list)
#input a list of numbers
#create two new lists:one for even numbers , one for odd numbers
#display both lists
num=int(input("enter the number:"))
n=[2,3,4,5,56,23,68,90,80,7]
if (n%2==0):
    evennumbers=append.
    print("even")
elif (n%2!=0):
    print("odd")


#store 10 student names
#swap the positions of any two students
#print the new seating arrangement
students=str(input("enter the names:"))
print(students)
for i in range(10):
    students[i] = input(f"Enter name for seat {i+1}: ")

# Display current seating
print("\nCurrent Seating Arrangement:")
for i in range(10):
    print(f"Seat {i+1}: {students[i]}")

# Get positions to swap
print("\nEnter two seat numbers to swap (1-10):")
seat1 = int(input("First seat number: ")) - 1
seat2 = int(input("Second seat number: ")) - 1

# Validate and swap
if 0 <= seat1 < 10 and 0 <= seat2 < 10:
    temp = students[seat1]
    students[seat1] = students[seat2]
    students[seat2] = temp

    # Display new arrangement
    print("\nNew Seating Arrangement:")
    for i in range(10):
        print(f"Seat {i+1}: {students[i]}")
else:
    print("Invalid seat numbers! Please enter numbers between 1 and 10.")

#to read 2 integer values as input from the user and swap the numbers
num1=int(input("enter the value1:"))
num2=int(input("enter the value2:"))
print("num1",num1)
print("num2",num2)
print("after swapping:")
num1,num2==num2,num1
print("num1",num1)
print("num2",num2)