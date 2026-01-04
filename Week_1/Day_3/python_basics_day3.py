#day 3: program 1 implementation of if-else using valid voter check
age=int(input("enter your age:"))
if age<18:
    print("you cant vote")
else:
    print("you can vote")


# day3:same program using fucntions 

def vote_check(oldness):
    if(oldness<18):
        print("not eligible to vote")
    else:
        print("eligible to vote")
ageinput=int(input("enter your age"))
vote_check(ageinput)

#day3: program 2 :Check Even or Odd

num=int(input("enter a number"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#day 3:program 3: largest of two numbers

num1=int(input("enter first number"))
num2=int(input("enter the second number"))
if(num1>num2):
    print("num1 is greater")
else:
    print("num2 is greater than num1")

#day 3:program 4:check number is positive negative or zero

number=int(input("enter the number"))
if(number>0):
    print("number is positive")
elif(number<0):
    print("the number is negative")
else:
    print("number is zero")

#day 3:program 5:add two numbers using python functions

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


#day3:program 6:check prime or not

def prime(value):
    if value <= 1:
        return False

    for i in range(2, value):
        if value % i == 0:
            return False

    return True


n = int(input("Enter the number: "))

if prime(n):
    print("The number is prime")
else:
    print("The number is not prime")




