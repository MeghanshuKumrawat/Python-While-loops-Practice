'''
20. Write a Python program to print alphabet pattern 'G'.
Expected Output:

 ***
*   *
*
* ***
*   *
*   *
 ***
'''

i = 0

while i < 7:
    j = 0
    while j < 5:
        if ((i==0 or i==6) and (j==0 or j==4)) or ((i==1 or i==4 or i==5) and (j==1 or j==2 or j==3)) or ((i==2) and (j==1 or j==2 or j==3 or j==4)) or (i==3 and j==1):
            print(" ", end="")
        else:
            print("*", end="")
        j += 1
    print()
    i += 1
