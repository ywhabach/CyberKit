import os
from utils.colors import *

def disk_usage():
    print(BOLD + CYAN + "\n[ Disk Usage Information ]\n" + RESET)

    print(GREEN + "Filesystem usage:\n" + RESET)
    os.system("df -h")

    print(GREEN + "\nTop directories by size (Home):\n" + RESET)
    os.system("du -h ~ --max-depth=1 2>/dev/null | sort -hr | head -n 10")
