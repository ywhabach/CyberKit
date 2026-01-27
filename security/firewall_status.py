import os
from utils.colors import *

def firewall_status():
    print(BOLD + CYAN + "\n[ Firewall Status Checker ]\n" + RESET)

    print(GREEN + "Checking UFW Firewall status:\n" + RESET)
    os.system("ufw status 2>/dev/null")

    print(GREEN + "\nChecking iptables rules:\n" + RESET)
    os.system("iptables -L -n 2>/dev/null")
