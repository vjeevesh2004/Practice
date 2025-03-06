'''
Write a Python program to append text 
to a file and display the text.
'''

with open('file.txt','a+') as file:
         file.write("This")
         file.seek(0)

         content = file.read()
print(content)