import platform
import os
from utils.colors import *

def cpu_ram_info():
    print(BOLD + CYAN + "\n[ CPU & RAM Information ]\n" + RESET)

    print(BOLD + GREEN + "CPU Information:\n" + RESET)
    print(f"{WHITE}Processor    : {platform.processor()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Total Cores  : {os.cpu_count()}")

    print(BOLD + GREEN + "\nRAM Information:\n" + RESET)
    os.system("free -h")

