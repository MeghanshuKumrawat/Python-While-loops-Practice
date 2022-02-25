'''
14. Write a Python program that accepts a string and
calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
    Letters 6
    Digits 2
'''

string = input("Enter any string : ")
letters = 0
digits = 0
i = 0
while i<len(string):
    if string[i].isalpha():
        letters += 1
    elif string[i].isdigit():
        digits += 1
    i += 1
    
print("Letters :",letters)
print("Digits :", digits)

