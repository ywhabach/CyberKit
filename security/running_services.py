import os
from utils.colors import *

def running_services():
    print(BOLD + CYAN + "\n[ Running Services Checker ]\n" + RESET)

    print(GREEN + "Active running services:\n" + RESET)

    # systemctl is standard on modern Linux systems
    os.system("systemctl list-units --type=service --state=running")
