from utils.colors import *

def about_tool():
    print(BOLD + CYAN + "\n[ About CyberKit ]\n" + RESET)

    print(INFO, "Project Name : CyberKit")
    print(INFO, "Type         : Linux Security Toolkit")
    print(INFO, "Purpose      : Educational & Academic")
    print(INFO, "Language     : Python 3\n")

    print(BOLD + GREEN + "Description:\n" + RESET)
    print(WHITE +
          "CyberKit is a modular Linux security toolkit designed\n"
          "to demonstrate basic system, network, and security\n"
          "concepts in a safe and educational environment.\n"
          + RESET)

    print(BOLD + PURPLE + "\nIncluded Modules:\n" + RESET)

    print(SEC, "Network Tools")
    print("  - MAC Address Changer")
    print("  - Ping Tool")

    print(SEC, "\nSystem Tools")
    print("  - OS & Kernel Info")
    print("  - CPU & RAM Info")
    print("  - Disk Usage")
    print("  - Logged-in Users")

    print(SEC, "\nSecurity Tools")
    print("  - Open Ports Checker")
    print("  - Running Services")
    print("  - Password Strength Checker")

    print(SEC, "\nUtilities")
    print("  - Random Password Generator")
    print("  - Hash Generator (MD5 / SHA256)")

    print(BOLD + YELLOW + "\nDisclaimer:\n" + RESET)
    print(WARN +
          "This tool is developed for educational purposes only.\n"
          "It does not perform any offensive or illegal actions.\n"
          "The authors are not responsible for misuse.\n"
          + RESET)
