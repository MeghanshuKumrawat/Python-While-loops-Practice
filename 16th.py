'''
16. Write a Python program to find numbers between 100 and
400 (both included) where each digit of a number is an even
number. The numbers obtained should be printed in a
comma-separated sequence.
'''

i = 100

while i <= 400:
    temp = str(i)
    if all(int(j)/2==int(j)//2 for j in temp):
        print(i, end=",")
    i += 1
