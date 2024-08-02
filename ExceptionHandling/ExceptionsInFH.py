#1.FileNotFound Exception

try:

    with open('index.html', 'r') as file:
    
        content = file.read()
    
        print(content)

except FileNotFoundError as e:

    print(f"Error: {e}")


#2.Permission Error

try:
    with open('SensitiveFile.txt', 'w') as file:
        file.write("Eswaran Arumugam Fullstack Developer @ Changepond Technologies Chennai")
except PermissionError as error:
    print(f"Error: {error}")

#3. IsADirectoryError

try:
    with open('/PYTHON', 'r') as file:
        content = file.read()
except IsADirectoryError as e:
    print(f"Error: {e}")


#4.IO Exception

try:
    with open('some_file.txt', 'r') as file:
        content = file.read()
except IOError as e:
    print(f"Error: {e}")














