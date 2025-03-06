'''
Write a Python program to read
an entire text file.
'''

with open('this.txt','r') as f:
    text = f.read()
print(text)