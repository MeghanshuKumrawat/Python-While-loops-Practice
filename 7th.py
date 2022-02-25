'''
7. Write a Python program that prints each item and its
corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True,
'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
'''

datalist =  [1452, 11.23, 1+2j, True,'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
i = 0
while i < len(datalist):
    print(datalist[i],':', type(datalist[i]))
    i += 1
