file_path = "Hello!!.txt"

# Open the file and read the content
with open(file_path, 'r') as file:
        content = file.read()

# Reverse the content and separate each character with a comma
reversed_content = ','.join(content[::-1])

    # Write the modified content back to the file
with open(file_path, 'w') as file:
        file.write(reversed_content)

print("File content modified successfully.")