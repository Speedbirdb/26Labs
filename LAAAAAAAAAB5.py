import random
import string

dictionary = {}
letters = ["j","a","n","e","t"]
exceptional_chars = "!@#$%^&*()_+-=?"

for i in range(letters):
    chars = set()
    while len(chars) < 3:
        chars.add(random.choice(exceptional_chars))
    dictionary[i] = list(chars)
print(dictionary)

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    modified_password = ''
    for char in password:
        if char in dictionary:
            modified_password += random.choice(dictionary[char])
        else:
            modified_password += char
    passwords.append(modified_password)

categorized_passwords = {'strong': [], 'weak': []}
for password in passwords:
    replaced_count = sum(1 for char in password if char in exceptional_chars)
    if replaced_count > 4:
        categorized_passwords['strong'].append(password)
    else:
        categorized_passwords['weak'].append(password)

print("Generated Passwords:\n")
print("STRONG PASSWORDS:")
for password in categorized_passwords['strong']:
    print(password)
print("\nWEAK PASSWORDS:")
for password in categorized_passwords['weak']:
    print(password)

print("\nBonus - Categorized by special characters:")
categorized_passwords_bonus = {'strong': [], 'weak': []}
for password in passwords:
    special_count = sum(1 for char in password if char in exceptional_chars)
    if special_count > 4:
        categorized_passwords_bonus['strong'].append(password)
    else:
        categorized_passwords_bonus['weak'].append(password)

print("\nSTRONG PASSWORDS (Bonus):")
for password in categorized_passwords_bonus['strong']:
    print(password)
print("\nWEAK PASSWORDS (Bonus):")
for password in categorized_passwords_bonus['weak']:
    print(password)