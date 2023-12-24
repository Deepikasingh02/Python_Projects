"""
Write a python code to print the position or the index of the give String
(taken as an input from the user) from a given list of the string.

The code will take an input from the user in the form of a string
and will pass the dtring as argument to s function. The function will
take the strings as argument and return Position(or index) of the
list .
if string is present return"Postion of the string is: " , else return
"String not found"
"""

def isPresent(list,str):
    for i in range(len(list)):
        if list[i] == str:
            return i
    

list = []
for i in range(int(input())):
    list.append(input())

str = input()

a = isPresent(list,str)

if a == None :
    print("String not found")
else:
    print("Position of the string is :", a)
