#5 .question:Write a program to check if a string contains any special character


def has_special_characters(s):
    # special characters
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    # Check if string contains any special characters
    for char in s:
        if char in special_characters:
            return True
    
    return False


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    
    if has_special_characters(input_string):
        print("String contains special characters.")
    else:
        print("String does not contain any special characters.")
