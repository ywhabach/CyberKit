import platform
import os

def os_kernel_info():
    print("\n--- Operating System & Kernel Information ---\n")

    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    architecture = platform.machine()
    kernel = platform.uname().release

    print(f"OS Name        : {os_name}")
    print(f"OS Release     : {os_release}")
    print(f"OS Version     : {os_version}")
    print(f"Architecture   : {architecture}")
    print(f"Kernel Version : {kernel}")

    print("\nAdditional Info:\n")
    os.system("lsb_release -a 2>/dev/null")
