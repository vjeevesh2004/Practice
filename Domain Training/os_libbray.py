import os

print("Current working directory:", os.getcwd())
print("Files and directories:",os.listdir())

os.mkdir('test_dir')
print("Directory 'test dir' created.")
print("Directory 'test_dir' removed.")