# ===== TEXT COLORS =====
RED     = "\033[91m"   # Errors
GREEN   = "\033[92m"   # Success
YELLOW  = "\033[93m"   # Warnings / Input
BLUE    = "\033[94m"   # Processing
PURPLE  = "\033[95m"   # Security
CYAN    = "\033[96m"   # Information
WHITE   = "\033[97m"   # Normal text

# ===== STYLES =====
BOLD    = "\033[1m"
RESET   = "\033[0m"

# ===== SYMBOLS =====
OK      = GREEN + "[✔]" + RESET
ERR     = RED   + "[✖]" + RESET
INFO    = CYAN  + "[i]" + RESET
WARN    = YELLOW+ "[!]" + RESET
SEC     = PURPLE+ "[🔒]" + RESET
PROC    = BLUE  + "[~]" + RESET
