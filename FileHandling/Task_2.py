import os

def delete_file(file_path):
    
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    else:
        print(f"File '{file_path}' does not exist.")

def main():
    file_path = input("Enter the File Path:")
    delete_file(file_path)

if __name__ == "__main__":
    main()
    