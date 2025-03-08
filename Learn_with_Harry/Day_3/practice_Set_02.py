letter = '''Dear <|Name|>
 You are selected!

 date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
