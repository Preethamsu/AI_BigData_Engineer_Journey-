

list1=[1,1,2,3,4,5,6]
print(list1.index(1))



countries=("India","Italy","Finland")
temp=list(countries)
temp.insert(1,"France")
countries=tuple(temp)
print(countries)

import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=time.strftime('%H')
print(hour)
minutes=time.strftime('%M')
print(minutes)
seconds=time.strftime('%S')
print(seconds)
if(hour<'12' and hour>'0'):
    print("good morning")
elif(hour>'12' and hour<'18'):
    print("good afternoon")
else:
    print("good evening")


print("Welcome to Koun Banega Crorepati")

initial = 100000
moneyforcorrectanswer = 10000

question = "Who is the best player in cricket?"
options = ["Kohli", "Patidar", "Dhoni", "Hardik"]

print(question)
print("A.", options[0])
print("B.", options[1])
print("C.", options[2])
print("D.", options[3])

correct_answer = "a"

user_answer = input("Enter your answer (A/B/C/D): ").lower()

if user_answer == correct_answer:
    print("Answer is correct! You won 10,000")
    print("Current amount:", initial + moneyforcorrectanswer)
else:
    print("Answer is wrong! You lost")
    print("Money remaining:", initial - moneyforcorrectanswer)

price=49.0098776897
txt=print(f"the amount is {price:.2f}")
print(f"{2*30.1234:.2f}")



def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
