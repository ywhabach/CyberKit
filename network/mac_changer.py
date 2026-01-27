import subprocess
import re
from utils.colors import *

def get_interfaces():
    output = subprocess.check_output(["ip", "link"]).decode()
    return re.findall(r"\d+: ([^:]+):", output)

def get_current_mac(interface):
    output = subprocess.check_output(["ip", "link", "show", interface]).decode()
    mac = re.search(r"link/ether ([\w:]+)", output)
    return mac.group(1) if mac else None

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ip", "link", "set", interface, "down"])
    subprocess.call(["sudo", "ip", "link", "set", interface, "address", new_mac])
    subprocess.call(["sudo", "ip", "link", "set", interface, "up"])

def mac_changer_menu():
    print(BOLD + CYAN + "\n[ MAC Address Changer ]\n" + RESET)

    interfaces = get_interfaces()
    for i, iface in enumerate(interfaces):
        print(f"{GREEN}[{i}] {iface}{RESET}")

    try:
        choice = int(input("\nSelect interface >> "))
        interface = interfaces[choice]
    except:
        print(RED + "Invalid selection" + RESET)
        return

    current_mac = get_current_mac(interface)
    print(YELLOW + f"\nCurrent MAC: {current_mac}" + RESET)

    new_mac = input("Enter new MAC >> ")

    if not re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", new_mac):
        print(RED + "Invalid MAC format" + RESET)
        return

    print(BLUE + "\nChanging MAC address...\n" + RESET)
    change_mac(interface, new_mac)

    if get_current_mac(interface) == new_mac:
        print(GREEN + "MAC address changed successfully ✔" + RESET)
    else:
        print(RED + "MAC address change failed ✖" + RESET)
