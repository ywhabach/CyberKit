import os
from utils.colors import *

def open_ports():
    print(BOLD + CYAN + "\n[ Open Ports Checker ]\n" + RESET)

    print(GREEN + "Listening ports on this system:\n" + RESET)

    # ss is modern replacement for netstat
    os.system("ss -tuln")
