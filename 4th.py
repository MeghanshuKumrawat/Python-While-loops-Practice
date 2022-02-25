'''
4. Write a Python program to construct the following pattern,
using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

i = 0
while i < 6:
    j = 0
    while j < (i+1):
        print('*', end='')
        j += 1
    print('')
    i += 1

i = 6
while i > 0:
    j = 0
    while j < i-1:
        print('*', end='')
        j += 1
    print('')
    i -= 1
