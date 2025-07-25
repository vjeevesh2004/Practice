filename = "Hello!!.txt"

# Number of students
n = int(input("Enter the number of students: "))

# List to store student data
students = []

# Input student data
for i in range(1, n + 1):
    name = input(f"Enter name of student {i}: ")
    roll_no = input(f"Enter roll number of student {i}: ")
    students.append((name, roll_no))

with open(filename, 'w') as file:
        for name, roll_no in students:
            file.write(f"{name},{roll_no}\n")

with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
