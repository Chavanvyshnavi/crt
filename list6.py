prog_lang=['c','c++','java','python','go-lang']
print(prog_lang)
Front_End=['html','css','javascript','react','js']
print(Front_End)
prog_lang.extend(Front_End)
print(prog_lang)
print(prog_lang.count('html'))

#write a program to:
#add confirmed guests to a list
#remove a guests to a list
#check if a friend is on the list
#sort snd print the final guest list

Guest_list=[]
while(True):
    print("**********Menu**********")
    print("1.Add the Guest")
    print("2.Remove the Guest eho can cancels")
    print("3.check if a Guest is attending the party or not")
    print("4.view the final Guest list")
    print("5.exit")
    print("---------------------------------------")

    Choice=int(input("Enter your choice:"))
if(Choice>=1 and Choice<=5):
    if(Choice==1):
        GuestName=input("Enter the Guest name:")
        Guest_list.append(GuestName)
        print(f"{GuestName}is added to Guest list...!")
    elif(Choice==2):
        cancelledGuest=input("enter the cancelled Guest name:")
        if cancelledGuest in Guest_list:
            Guest_list.remove(cancelledGuest)
            print(f"{cancelledGuest}is removed from Guest...!")
        else:
            print(f"{cancelledGuest}is not in Guest list...!")
    elif(Choice==3):
        checkGuest=input("enter the guest name to check:")
        if checkGuest in Guest_list:
            print(f"{checkGuest}is attending the party...!")
        else:
            print(f"{checkGuest}is not attending the party...!")
    elif(Choice==4):
        if(len(Guest_list)==0):
            print("Guest list is empty...!")
        else:
            Guest_list.sort()
            print("hurray heres your final Guest list")
            print(Guest_list)
    else:
        print("enjoy your party.....!")
else:
    print("in-valid input")

                  