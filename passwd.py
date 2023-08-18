def transform_password(existing_password):
    transformation_dict = {
        'a': '4',
        'A': '4',
        'e': '3',
        'E': '3',
        'i': '1',
        'I': '1',
        'o': '0',
        'O': '0',
        's': '$',
        'S': '$',
        't': '7',
        'T': '7',
        'b': '8',
        'B': '8',
        'g': '9',
        'G': '9',
        'z': '2',
        'Z': '2',
        'l': '|',
        'L': '|',
        'h': '#',
        'H': '#',
        'x': '*',
        'X': '*',
        'c': '[',
        'C': '[',
        'd': '}',
        'D': '}',
        'Q': '6',
        'q': '6',
    }

    transformed_password = ''
    for char in existing_password:
        transformed_password += transformation_dict.get(char, char)

    return transformed_password

# Get existing password from user
existing_password = input("Enter your existing password: ")

# Transform and print the strong password
strong_password = transform_password(existing_password)
print("Your strong password is:", strong_password)
