# write a python program to read an integer value as input from the user and find number of digits present in that particular number

Num=int(input("Enter the value"))
DigitCount=0
while(Num!=0):
    Num=Num//10
    DigitCount+=1
print(f"{Num} has {DigitCount} digits")

n = int(input("Enter the value of n: "))
print(f"\nReversed Multiplication Table for {n}")
print("-" * 35)
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
    
# write a python program to read an integer value as input from the user and find number of digits present in that particular number

def count_digits(number):
    # Make the number positive if it's negative
    number = abs(number)
    
    # Special case: if the number is 0, it has 1 digit
    if number == 0:
        return 1

    count = 0
    while number > 0:
        number = number // 10  # Remove the last digit
        count += 1
    return count

# Read input from the user
num = int(input("Enter an integer: "))

# Get the number of digits
digit_count = count_digits(num)

# Print the result
print("Number of digits:", digit_count)

#to read the integer value as input from the user and find the submission of digits 
Num=int(input("Enter the integer value:"))
Temp=Num
DigitSum=0
Rem=0
while(Num!=0):
    Rem=Num%10
    DigitSum=DigitSum+Rem
    Num=Num//10
print(f"Summation is {DigitSum}")