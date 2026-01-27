import os
from network.mac_changer import mac_changer_menu
from network.ping_tool import ping_tool
from system.os_kernel_info import os_kernel_info
from system.cpu_ram_info import cpu_ram_info
from utils.banner import show_banner
from utils.colors import *
from system.disk_usage import disk_usage
from security.open_ports import open_ports
from security.running_services import running_services
from security.firewall_status import firewall_status
from utils.password_generator import password_generator
from security.password_strength import password_strength
from utils.hash_generator import hash_generator
from utils.about import about_tool
from utils.help import help_tool



def clear():
    os.system("clear")

def pause():
    input("\nPress Enter to continue...")

# ================= MAIN MENU =================

def main_menu():
    while True:
        os.system("clear")
        show_banner()

        print(BOLD + CYAN + "Main Menu\n" + RESET)
        print(GREEN  + "[1] Network Tools"   + RESET)
        print(CYAN   + "[2] System Info"     + RESET)
        print(PURPLE + "[3] Security Tools"  + RESET)
        print(YELLOW + "[4] Utilities"       + RESET)
        print(BLUE   + "[5] About" + RESET)
        print(BLUE   + "[6] Help"  + RESET)
        print(RED    + "[0] Exit\n"           + RESET)

           
        choice =  input(YELLOW + "Select option >> " + RESET)

        if choice == "1":
            network_menu()
        elif choice == "2":
            system_menu()
        elif choice == "3":
            security_menu()
        elif choice == "4":
            utils_menu()
        elif choice == "5":
            about_tool()
            pause()
        elif choice == "6":
            help_tool()
            pause()
        elif choice == "0":
            print(INFO, "Exiting tool...")
            break
        else:
            print("Invalid option")
            pause()

# ================= NETWORK MENU =================
def network_menu():
    while True:
        clear()
        print(BOLD+CYAN+"""
--- Network Tools ---"""+RESET+GREEN+"""
[1] MAC Address Changer
[2] Ping Tool
[0] Back
"""+RESET)
        choice = input(">> ")

        if choice == "1":
            mac_changer_menu()
            pause()
        elif choice == "2":
            ping_tool()
            pause()
        elif choice == "0":
            break
        else:
            print("Invalid option")
            pause()

# ================= SYSTEM MENU =================
def system_menu():
    while True:
        clear()
        print(BOLD+CYAN+"""
--- System Information ---"""+RESET+GREEN+"""
[1] OS & Kernel Info
[2] CPU & RAM Info
[3] Disk Usage
[0] Back
"""+RESET)
        choice = input(">> ")

        if choice == "1":
            os_kernel_info()
            pause()
        elif choice == "2":
            cpu_ram_info()
            pause()
        elif choice == "3":
            disk_usage()
            pause()

       
        elif choice == "0":
            break
        else:
            print("Invalid option")
            pause()

# ================= SECURITY MENU =================
def security_menu():
    while True:
        clear()
        print(BOLD+CYAN+"""
--- Security Checks ---"""+RESET+GREEN+"""
[1] Check Open Ports
[2] Running Services
[3] Password Strength Check
[0] Back
"""+RESET)
        choice = input(">> ")

        if choice == "1":
             open_ports()
             pause()
        elif choice == "2":
            running_services()
            pause()

        elif choice == "3":
           password_strength()
           pause()
        elif choice == "0":
            break
        else:
            print("Invalid option")
            pause()

# ================= UTILITIES MENU =================
def utils_menu():
    while True:
        clear()
        print(BOLD+CYAN+"""
--- Utilities ---"""+RESET+GREEN+"""
[1] Random Password Generator
[2] Hash Generator (MD5 / SHA256)
[0] Back
"""+RESET)
        choice = input(">> ")

        if choice == "1":
             password_generator()
             pause()
        elif choice == "2":
             hash_generator()
             pause()
        elif choice == "0":
            break
        else:
            print("Invalid option")
            pause()
