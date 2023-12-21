"""
Write a python code to print the count of valid strings 
and invalid strings from a given list of strings

A string is considered as valid if it contains combinations
of alphabetes (in upper case or lower case) with/without 
spaces.

Define a function to check if a given string is valid or not
i.e if it contains combination of alphabetes.

This function will take string as input and return True 
if the string is valid, otherwise will return False.

Example:

Input:
4
HelloGood Morning
abcd123Fghy
India
Progoto.c

Output:
Count Of Valid String = 2
Count of Invalid String = 2
"""
def isValidString(strList):
    countValidString = 0
    countInvalidString = 0
    for str in strList:
        temp = ""
        for word in str.split():
            temp = temp + word.strip()
        if temp.isalpha():
            countValidString = countValidString + 1
        else:
            countInvalidString = countInvalidString + 1
    return [countValidString, countInvalidString]

strList = []
for i in range(int(input())):
    strList.append(input())

valid,Invalid = isValidString(strList)
print("count of valid string = ", valid)
print("count of invalid string = " ,Invalid)
