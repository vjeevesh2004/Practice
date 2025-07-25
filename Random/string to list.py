sentence = input("Enter a sentence: ")

digits = sum(c.isdigit() for c in sentence)
uppercase = sum(c.isupper() for c in sentence)
lowercase = sum(c.islower() for c in sentence)

print(digits)
print(uppercase)
print(lowercase)