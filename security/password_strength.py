import re
from utils.colors import *

def password_strength():
    print(BOLD + CYAN + "\n[ Password Strength Checker ]\n" + RESET)

    password = input("Enter password to check >> ")

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1

    print("\nPassword Analysis:")

    if score <= 2:
        print(RED + "Weak Password ❌" + RESET)
    elif score == 3:
        print(YELLOW + "Medium Password ⚠️" + RESET)
    else:
        print(GREEN + "Strong Password ✔" + RESET)

    print("\nRecommendations:")
    if len(password) < 8:
        print("- Use at least 8 characters")
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters")
    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters")
    if not re.search(r"[0-9]", password):
        print("- Add numbers")
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        print("- Add special characters")
