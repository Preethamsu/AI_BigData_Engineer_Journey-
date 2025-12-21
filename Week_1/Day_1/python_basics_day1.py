# Day 1: Python Basics
# Author: Preetham Siddapura Umesh
# Topics: Variables, Input/Output, Operators, Conditions

#Day 1 Program 1 Printing name age and field 
name="Preetham Siddapura Umesh"
age=22
field="Computer Science And Engineering"
print("Name:"+name)
print("Age:",age)
print("Field:"+field)

#Day 1 Program 2 Sum Difference Product Division

a=int(input("Enter first number:"))
b=int(input("Enter a second number:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter your choice"))
match choice:
    case 1:
        print("sum=",(a+b))
    case 2:
        print("difference",(a-b))
    case 3:
        print("product:",(a*b))
    case 4:
        res=a/b
        if(b==0):
            print("dividison not possible")
        else:
            print("division possible ")
        print("quotient",(res))
    case _:
        print("invalid choice")



#Day1 Program 3 check whether number is odd or even

a=int(input("enter a number to check whether number is odd or even"))
if(a%2==0):
    print("number is even")
else:
    print("number is odd")




#day 1 program 4 celsius to Fahrenheit

temperature=int(input("enter the temperature in celsius"))
F = (temperature *(9/5)) + 32
print("The celsius to fahrenheit is :",F)

#day1 program 5 Take a string input and print its length
message="Hello I am Preetham"
print("The length of String is :",len(message))

#day 1 program 6 Swap two numbers without using a third variable
num1=int(input("enter first number "))
num2=int(input("enter second number"))
num1,num2=num2,num1
print("num1:",num2)
print("num2:",num1)

#day1 program 6  to check whether a number is positive, negative, or zero
num=int(input("enter a number"))
if(num==0):
    print("number is zero")
elif(num>0):
    print("number is positive")
else:
    print("number is negative")


#---------end--------------Day1---------------