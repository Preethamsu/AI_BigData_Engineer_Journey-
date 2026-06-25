s1={1,2,4,6}
s2={2,7,8}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities={"Tokyo","Madrid","Chennai"}
cities2={"Tokyo","Madrid","Kolkata"}
print(cities.intersection(cities2))
cities3=cities.intersection_update(cities2)
print(cities)

print(cities.issubset(cities2))
info={"name":"Karan","age":18,"eligible":True}
print(info.items())
for key,value in info.items():
    print(f"The corresponding key {key} is {value}")



dict1={"name":"preetham","age":10,"marks":100}
dict1.update({"age":90})
del dict1["age"]
print(dict1)

for i in range(6):
    print(i)

else:
    print("sorry no i ")

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("sorry no i ")




