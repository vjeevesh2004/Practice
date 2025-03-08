# Create a function that counts the number of vowels in a string.

def count_vowel(str):
  vowels = "aeiouAEIOU"
  count = 0
  for char in str:
    if char in vowels:
      count += 1
  return count

str = "Hjio"
num_str = count_vowel(str)
print(num_str) 

