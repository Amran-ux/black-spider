import os

# Color Codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # No Color

# Banner
def banner():
    os.system('clear')
    print(f"{CYAN}")
    print("██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗████████╗    " + f"{CYAN}BLACK-SPIDER - Info Gathering Tool{NC}")
    print(f"{NC}")

# Functions for Different Options
def ip_info_gathering():
    print(f"{GREEN}Running IP Info Gathering...{NC}")
    os.system("curl ifconfig.me")

def domain_info_gathering():
    domain = input(f"{YELLOW}Enter Domain: {NC}")
    os.system(f"whois {domain}")

def dns_lookup():
    domain = input(f"{YELLOW}Enter Domain for DNS Lookup: {NC}")
    os.system(f"nslookup {domain}")

def exit_tool():
    print(f"{RED}Exiting...{NC}")
    exit()

# Menu Function
def menu():
    banner()
    print(f"{YELLOW}[+] {GREEN}Select an option from the menu below:{NC}")
    print(f"1. IP Info Gathering")
    print(f"2. Domain Info Gathering")
    print(f"3. DNS Lookup")
    print(f"23. Exit")

    choice = input("Select an option (1-23): ")

    if choice == '1':
        ip_info_gathering()
    elif choice == '2':
        domain_info_gathering()
    elif choice == '3':
        dns_lookup()
    elif choice == '23':
        exit_tool()
    else:
        print(f"{RED}Invalid choice! Please select again.{NC}")

# Run the Menu
while True:
    menu()