print(bool(10))
print(True+True)
print(True+False)
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(""))
print(bool(range(0)))
print(bool(set()))

#program
#single quotes
str1='good morning'
print(str1)
print(type(str1))
#doble quotes
str2="we are learning python "
print(str2)
print(type(str2))
#triple quotes
str3='''good afternoon'''
print(str3)
print(type(str3))
str4="i'm vyshu "
print(str4)
print(type(str4))

#new program
a=10
b='10'
print(a is b)

#new program
print("welcome",end='\n')
print("welcome",end='')
print("students")
print("to",)


#new 
str="python"
print(f"length of{str} is {len(str)}")
for i in str:
    print(i,end=" ")
print()
for i in range(len(str)):
    print(str[i],end=" ")



#new
str="python program"
print(str[1:6])
print(str[0:1])
print(str[7:11])
print(str[10:])
print(str[7:10])
print(str[2:6])
print(str[::-1])
print(str[-9::-1])
print(str[-1:8:-1])
print(str[-4:8:-1])

#new 
a="hello"
b="world"
c=a+" "+b
print(c)
#new
list=['h','e','l','l','o']
print(list)
#new
input=input("enter the string:")
print(f"user entered string:{input}")
str_list=input.split()
str="".join(str_list)
print(f"string without spaces:{str}")

