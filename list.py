Num_list=[10,20,30,40]
print(Num_list)
print("Accessing the list elements using for lopp without index")
for i in Num_list:
    print(i)
print("Accessing the list elements using for lopp with index")
#range(start,stop,stepsize),range(start,stop),range(start)
for i in range(len(Num_list)):
    print(Num_list[i])
print("Accessing the list elements using while loop")
i=0
while(i<len(Num_list)):
    print(Num_list[i])
    i+=1