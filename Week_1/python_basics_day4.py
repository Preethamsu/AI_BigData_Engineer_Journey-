#day4:program 1 sum of elements in the list
num=[10,20,30,40]
total=0
for i in num:
    total+=i
print("The total is:",total)

#day4:program 2 remove unique elements

nums=[1,1,1,2,2,3,3,4,4,5,6,7]
def remove_repeat(nums):
    seen=[]
    for num in nums:
        if num not in seen:
            seen.append(num)
    return seen
print(remove_repeat(nums))

age=int(input("enter the age"))
if(age>18):
    print("u can vote")
else:
    print("u cannot vote")

for i in range(1,50):
    if i%2==0:
        print(i)


nums = [5, 12, 3, 8, 21, 7, 15]
def sort(nums):
    greatest=[]
    for num in nums:
        if num>10:
            greatest.append(num)
    return greatest
print(sort(nums))

def count_vowels(sentence):
    count=0
    for char in sentence:
        if char in 'aeiou':
            count+=1
    return count
print(count_vowels("Preetham is an AI engineer"))           


countries=[{
    "country":"India",
    "capital":"Delhi"},
    {"country":"germany","capital":"berlin"}]
for country in countries:
    print(country)

nums = [1, 2, 3, 4, 2] 
for num in nums:
    if num==nums[::-1]:
        print(num)

def is_pallindrome(word):
    reversed_word=word[::-1]
    if word.lower()==reversed_word.lower():
        return True
    else:
        return False
print(is_pallindrome("Racecar"))
print(is_pallindrome("hello"))


nums=[1,2,3,1,4,5]
def has_repeat(nums):
    seen=[]
    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False
print(has_repeat(nums))


students = [
    {"name": "Preetham", "score": 92},
    {"name": "Rohit", "score": 85},
    {"name": "Shiva", "score": 70}
]
highestscore=students[0]

for student in students:
    if student["score"]>highestscore['score']:
        highestscore= student
print(highestscore['name'])


