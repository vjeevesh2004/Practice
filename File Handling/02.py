'''
Write a Python program to read first n lines of a file.
'''

with open('file.txt') as file:
    content = ''.join(file.readlines()[:n])

print(content)