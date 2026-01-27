import os
import re

def ping_tool():
    target = input("Enter IP address or domain: ")

    # تحقق بسيط من الإدخال (IP أو domain)
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    domain_pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not re.match(ip_pattern, target) and not re.match(domain_pattern, target):
        print("Invalid IP or domain format")
        return

    count = input("Number of packets (default 4): ")
    if count.strip() == "":
        count = "4"

    print("\nPinging target...\n")
    os.system(f"ping -c {count} {target}")
