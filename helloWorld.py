from os import listdir


user_name = input("Enter your name: ")
project_name = input("Enter your project name: ")
folder_path = input("Enter the path to get files: ")
file_names = listdir(folder_path)

print(f"Hello {user_name}")
print(f"Your project name is: {project_name}")
print("Git is awsome!")
print(f"files in folder: {folder_path}:")
for file_name in file_names:
    print(file_name)