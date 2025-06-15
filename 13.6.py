def display_prog():
    print("programming languages:")
    print("javascript")
    print("bio-python")
    print("sql")
    print("c")
    print("c++")
display_prog()
display_prog()
display_prog()

#new 
def display():
    return "hey..! i'm the zero arg function...!"
res=display()
print(res)
def namedfunction(name):
    return f"hey..! i'm the one arg function called by {name}"
res1=namedfunction("kavya")
print(res1)

#wap to check whether the user given integer is even or odd using functions
def even_odd(num):
    if (num%2==0):
        print(f"{num}is even")
    else:
        print(f"{num} is odd")
even_odd(1)
even_odd(10)
even_odd(11)
even_odd(25)
even_odd(0)

#to check whether the user given num is prime num or not using functions(using return)
def prime():
    return "given num is prime"
res=prime()
print(res)
def primenumber(num):
    return f"given num is prime {num}"
res1=primenumber(3)
print(res1)

#new
def prime(num):
    if (num%1==0)and(num%num==0):
        return print(f"{num}is prime")
    else:
        return print(f"{num} is not prime")
prime(2)
prime(3)
prime(4)
prime(5)
prime(8)

#wap to build the function which prints the multiplication table of n
# Function to print the multiplication table of a number
def print_table(n):
    print("Multiplication Table of", n)
    for i in range(1, 11):
        result = n * i
        print(n, "x", i, "=", result)
number = int(input("Enter a number to print its multiplication table: "))
print_table(number)

#new

    