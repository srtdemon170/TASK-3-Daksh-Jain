# ------------------------------------------
# Project 3: Random Password Generator
# Author: Daksh Jain
# ------------------------------------------

import random
import string

print("=" * 45)
print("       RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password must be at least 4 characters long.\n")
            continue
        break

    except ValueError:
        print("Please enter a valid number.\n")

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}?"

# Ensure at least one character from each category
password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(digits),
    random.choice(symbols)
]

# Remaining characters
all_characters = uppercase + lowercase + digits + symbols

for _ in range(length - 4):
    password.append(random.choice(all_characters))

# Shuffle password
random.shuffle(password)

# Convert list to string
final_password = "".join(password)

print("\n" + "=" * 45)
print("Generated Password")
print("-" * 45)
print(final_password)
print("=" * 45)

print("\nPassword Generated Successfully!")