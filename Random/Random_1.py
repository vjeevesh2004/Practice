''' You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
 For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately 
'''
def solve(s):
    words = s.split(' ')
    capitalized_words = []
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(words)
    return ' '.join(capitalized_words)

s = input("Enter the desired string: ")
print(solve(s)) 