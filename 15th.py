'''
15. Write a Python program to check the validity of password
input by users.
Validation :
● At least 1 letter between [a-z] and 1 letter between [A-Z].
● At least 1 number between [0-9].
● At least 1 character from [$#@].
● Minimum length 6 characters.
● Maximum length 16 characters.
'''

password = input("Enter the password : ")

i = 0
lenght = len(password)
validation = {"lower_alpha":False, "upper_alpha":False, "digit":False, "special":False}

while i<lenght:
    if lenght < 6 or lenght > 16:
        print("You need atleast minimum 6 and maximum 16 characters in password")
        break
    else:
        if password[i].isdigit():
            validation["digit"] = True
        elif password[i].islower():
            validation["lower_alpha"] = True
        elif password[i].isupper():
            validation["upper_alpha"] = True
        elif password[i] == "$" or password[i] == "#" or password[i] == "@":
            validation["special"] = True
        i += 1
        
if validation["digit"] == True and validation["lower_alpha"] == True and validation["upper_alpha"] == True and validation["special"] == True:
    print("Password is Strong!")
else:
    print("Password is Weak!\n\n)
    if validation["digit"] != True:
        print("You need atleast 1 digit in password!")
    if validation["lower_alpha"] != True:
        print("You need atleast 1 lowercase char in password!")
    if validation["upper_alpha"] != True:
        print("You need atleast 1 uppercase char in password!")
    if validation["special"] != True:
        print("You need atleast 1 special char in password!")
