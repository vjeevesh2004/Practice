def remove_and_split(string, word):
    newStr  = string.replace(word, "")
    return newStr.strip()

this = "          harryry iso9ss      hueheu     "
n  = remove_and_split(this, "harryry")
print(n)
# print(this)