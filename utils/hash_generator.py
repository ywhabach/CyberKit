import hashlib
from utils.colors import *

def hash_generator():
    print(BOLD + CYAN + "\n[ Hash Generator ]\n" + RESET)

    text = input("Enter text to hash >> ")

    if text.strip() == "":
        print(RED + "Input cannot be empty!" + RESET)
        return

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    print(GREEN + "\nGenerated Hashes:\n" + RESET)

    print(YELLOW + "MD5:" + RESET)
    print(md5_hash)

    print(YELLOW + "\nSHA256:" + RESET)
    print(sha256_hash)
