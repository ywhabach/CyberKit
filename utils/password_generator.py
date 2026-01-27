import random
import string
from utils.colors import *

def password_generator():
    print(BOLD + CYAN + "\n[ Random Password Generator ]\n" + RESET)

    try:
        length = int(input("Enter password length (default 12) >> "))
    except:
        length = 12

    if length < 6:
        print(RED + "Password length too short!" + RESET)
        return

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        "!@#$%^&*()_+-="
    )

    password = "".join(random.choice(characters) for _ in range(length))

    print(GREEN + "\nGenerated Password:\n" + RESET)
    print(BOLD + YELLOW + password + RESET)
