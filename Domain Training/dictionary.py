employees = {
    "name": "Johan",
    "age": 25,
    "salary": 40000}
print(employees)

for key in employees:
    print(employees[key])

print(employees.get('name'))
print(len(employees))

employees["location"] = "chennai"

del employees['location']

employees.popitem()
employees.clear()

#shallow copy - changes reflect in orginial and copy both 

#deep copy - changes done in copied won't be affected in orginal one


