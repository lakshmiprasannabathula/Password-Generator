import random
import string

print("========== PASSWORD GENERATOR ==========")

length = int(input("Enter Password Length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:", password)