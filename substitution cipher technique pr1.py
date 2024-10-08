def encrypt(text, shift):
    result = ""

    for char in text:
        # Check if the character is uppercase
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is lowercase
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetical characters are not changed

    return result

# Input from the user
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text
cipher = encrypt(text, shift)

# Output the result
print("Text: " + text)
print("Cipher: " + cipher)
