#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
MyClass2 = __import__('8-my_class').MyClass2
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)


m = MyClass2("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
