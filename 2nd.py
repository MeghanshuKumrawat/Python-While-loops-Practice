'''
2. Write a Python program to convert temperatures to and from
celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius
and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''

temp = int(input('Enter temperature in celsius : '))
print("Fahrenheit -",(temp/5)*9+32)

temp = int(input('Enter temperature in fahrenheit : '))
print("Celsius -",(temp-32)*5/9)

