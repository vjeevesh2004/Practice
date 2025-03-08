''' convert the given uppercase to lowercase'''

def convert_upper_to_lower(s):
    new_str = ""
    # upper == 0, lower == 0
    for char in s:
        if char.isupper():
            new_str += char.lower()
        # elif char.islower():
          #   new_str += char.upper()
        else:
            new_str += str
    return new_str 

s = input("enter the number")

final_str = convert_upper_to_lower(s) 
# print(f"The final output of the string is {final_str}")
print("The final output is: ", final_str)