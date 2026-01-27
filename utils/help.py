from utils.colors import *

def help_tool():
    print(BOLD + CYAN + "\n[ Help & Usage Guide ]\n" + RESET)

    print(INFO, "How to use CyberKit:\n")

    print(WHITE +
          "1) Run the tool using Python 3\n"
          "2) Navigate using menu numbers\n"
          "3) Select the desired module\n"
          "4) Follow on-screen instructions\n"
          + RESET)

    print(BOLD + GREEN + "\nTips:\n" + RESET)
    print(OK, "Run the tool with sudo for network tools")
    print(OK, "Use strong passwords when testing")
    print(OK, "Read outputs carefully")

    print(BOLD + YELLOW + "\nImportant Notes:\n" + RESET)
    print(WARN, "Some tools require root privileges")
    print(WARN, "No data is stored or transmitted")
