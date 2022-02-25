'''
21. Write a Python program to print alphabet pattern 'L'.
Expected Output:

*
*
*
*
*
*
*****
'''

i = 0

while i < 7:
    j = 0
    while j < 5:
        if ((i<6) and (j>0)):
            print(" ", end="")
        else:
            print("*", end="")
        j += 1
    print()
    i += 1
