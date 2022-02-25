'''
5. Write a Python program that accepts a word from the user
and reverse it.
'''

word = input('Enter any word : ')

# solution 1
print(word[::-1])

# solution 2
temp = ''
i = 0
while i < len(word):
    temp = word[i] + temp
    i += 1
print(temp)

# solution 3
stack = []
temp = ''
i = 0
while i < len(word):
    stack.append(word[i])
    i += 1
i = 0
while i < len(word):
    temp += stack.pop()
    i += 1
    
print(temp)
