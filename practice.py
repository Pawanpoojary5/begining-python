# # # a=6
# # # b=7
# # # print(a*b)
# # # e=True or False
# # # print(e)

# # # a+=3
# # # print(a)
# # # a=3.00
# # # b=float(a)
# # # t=type(b)
# # a=int(input("Enter a number"))
# # b=int(input("enter a number"))
# # print(a+b)
# # print(a*b)
# # print(a-b)
# # print(a/b)
# # # print(a**b)
# # # print(a%b)
# # # print(a//b)
# # print("a is", a, "and b is", b)
# # # print("a is", a, "and b is", b, "and a+b is", a+b)
# # print(f"a is {a} and b is {b} and a+b is {a+b}")
# # # print(f"a is {a} and b is {b} and a*b is {
# from operator import countOf
# from sqlite3 import SQLITE_CONSTRAINT_TRIGGER


# # print(name[0:2])
# # print(name)
# # ch1=name[1]
# # print(ch1)
# # print(name[-4:-1])
# name="pawan"
# print(len(name))
# print(name.capitalize())
# print(name.endswith("g"))
# a='i am a good boy\n but not a bad\'boy\''
# print(a)
# input("Enter your name")
# print(f"good afternoon,{name}")#format print with name otherwise it print as it is
# letter=''' Dear Name,
# you are selected!
# Date'''
# print(letter.replace("Name","pawan").replace("Date","24 september 2005"))
name="pawan"
print(name.find("n"))

print(name.replace("a","x"))
fruits=["Apple","Mango","Grapes","Orange"]
fruits.append("cherry")
print(fruits)
fruits.sort()
fruits.reverse()
fruits.insert(3,4444)
print(fruits)
fruits.pop(3)
print(fruits)
