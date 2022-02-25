'''
3. Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses
wrong then the prompt appears again until the guess is
correct, on successful guess, user will get a "Well guessed!"
message, and the program will exit.
'''

num = 5
x = int(input('Guess the number : '))
while x != num:
    x = int(input('Again, Guess the number : '))
print('Well guessed!')
