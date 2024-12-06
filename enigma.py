import random
from datetime import date

# Make a random 5-digit number, always include leading zeros
def generate_random_key():
    return f"{random.randint(0, 99999):05}"

# Split the random key into 4 parts: A, B, C, and D
def extract_keys(key):
    return {
        "A": int(key[0:2]),  # First two digits
        "B": int(key[1:3]),  # Second and third digits
        "C": int(key[2:4]),  # Third and fourth digits
        "D": int(key[3:5]),  # Fourth and fifth digits
    }

# Use today's date to find offsets
def calculate_offsets(today):
    formatted_date = today.strftime("%d%m%y")  # Change the date to DDMMYY format
    squared_date = int(formatted_date) ** 2  # Square the number
    last_four = str(squared_date)[-4:]  # Take the last four digits
    return {
        "A": int(last_four[0]),  # First of the last four digits
        "B": int(last_four[1]),  # Second digit
        "C": int(last_four[2]),  # Third digit
        "D": int(last_four[3]),  # Fourth digit
    }

# Encrypt the message by shifting the letters
def encrypt_message(message, shifts, charset):
    encrypted_message = []
    for i, char in enumerate(message.lower()):  # Loop through each letter
        if char in charset:  # If the character is in the charset
            shift = shifts[i % 4]  # Use A, B, C, D shifts in order
            new_index = (charset.index(char) + shift) % len(charset)  # Find new position
            encrypted_message.append(charset[new_index])  # Add the new character
        else:
            encrypted_message.append(char)  # Leave non-alphabet characters as they are
    return "".join(encrypted_message)  # Combine everything into a single string

# Decrypt the message by reversing the shifts
def decrypt_message(message, shifts, charset):
    decrypted_message = []
    for i, char in enumerate(message.lower()):  # Loop through each letter
        if char in charset:  # If the character is in the charset
            shift = shifts[i % 4]  # Use A, B, C, D shifts in order
            new_index = (charset.index(char) - shift) % len(charset)  # Reverse the shift
            decrypted_message.append(charset[new_index])  # Add the original character
        else:
            decrypted_message.append(char)  # Leave non-alphabet characters as they are
    return "".join(decrypted_message)  # Combine everything into a single string

# Main part of the program
if __name__ == "__main__":
    charset = list("abcdefghijklmnopqrstuvwxyz ")  # Alphabet and space

    # Make a random key and calculate the shifts
    key = generate_random_key()  # Random 5-digit key
    keys = extract_keys(key)  # Break key into A, B, C, D
    today = date.today()  # Get today's date
    offsets = calculate_offsets(today)  # Find offsets from the date

    # Add the keys and offsets together for the final shifts
    shifts = [
        keys["A"] + offsets["A"],
        keys["B"] + offsets["B"],
        keys["C"] + offsets["C"],
        keys["D"] + offsets["D"],
    ]

    # Example: Encrypt and decrypt a message
    original_message = "hello world"
    encrypted = encrypt_message(original_message, shifts, charset)
    decrypted = decrypt_message(encrypted, shifts, charset)

    # Print the results
    print(f"Original Message: {original_message}")
    print(f"Encrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")
    print(f"Key: {key}, Shifts: {shifts}, Date: {today.strftime('%d%m%y')}")
