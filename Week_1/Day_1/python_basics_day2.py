#day 2 Program 1: Print numbers 1 to 10 using a loop
for num in range(2,11):
    print(num)
#or
i=1
while i<=10:
    print(i)
    i+=1

#day2 Program 2: Sum of first N numbers
n = int(input("Enter a number: "))
total = 0

for i in range(1, n+1):
    total += i

print("Sum of first", n, "numbers is:", total)

#day 2 program 3: check prime or not
num=int(input("enter the number:"))
if(num<=1):
    print("the number is not prime")
else:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print("the number is prime")
    else:
        print("number is not prime")

#day2 program 4:Reverse a string
string="preetham"
rev_str=""
for ch in string:
    rev_str=ch+rev_str
print(rev_str)

#day2 program 5:count vowels
text=input("enter the text")
vowels=["a","e","i","o","u"]
count=0
for ch in text:
    if ch.lower() in vowels:
        count+=1
print(count)


            


#---------end--------------Day2---------------