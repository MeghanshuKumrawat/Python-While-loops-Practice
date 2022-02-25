'''
13. Write a Python program which accepts a sequence of comma
separated 4 digit binary numbers as its input and print the
numbers that are divisible by 5 in a comma separated
sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
'''

data = '0100,0011,1010,1001,1100,1001'
data = data.split(',')
i = 0
while i < len(data):
    if int(data[i], 2)%5 == 0:
        print(data[i], end=',')
    i += 1
