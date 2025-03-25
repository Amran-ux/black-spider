import os

# Color Codes for Better Visibility
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
MAGENTA = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
BOLD = '\033[1m'
NC = '\033[0m'  # No Color

# Banner with Beautiful Colors (BLACK-SPIDER)
def banner():
    os.system('clear')  # Clear the screen
    print(f"{CYAN}")
    print("██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗████████╗    " + f"{BOLD}{CYAN}██████╗ ██████╗ ██████╗ {NC}")
    print("██╔══██╗██║  ██║██╔══██╗██║   ██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗")
    print("██████╔╝███████║██║  ██║██║   ██║   ██║       ██████╔╝██████╔╝██████╔╝")
    print("██╔═══╝ ██╔══██║██║  ██║██║   ██║   ██║       ██╔═══╝ ██╔═══╝ ██╔═══╝ ")
    print("██║     ██║  ██║██████╔╝╚██████╔╝   ██║       ██║     ██║     ██║     ")
    print("╚═╝     ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝     ╚═╝     ")
    print(f"{BOLD}{CYAN}        BLACK-SPIDER - All-in-One Information Gathering Tool{NC}")
    print(f"{NC}")

# Main Menu with Colors
def menu():
    banner()
    print(f"{YELLOW}[+] {GREEN}Select an option from the menu below:{NC}")
    print(f"1. {BOLD}{CYAN}IP Info Gathering{NC}")
    print(f"2. {BOLD}{CYAN}Domain Info Gathering{NC}")
    print(f"3. {BOLD}{CYAN}DNS Lookup{NC}")
    print(f"4. {BOLD}{CYAN}Whois Lookup{NC}")
    print(f"5. {BOLD}{CYAN}Reverse IP Lookup{NC}")
    print(f"6. {BOLD}{CYAN}Geolocation Lookup{NC}")
    print(f"7. {BOLD}{CYAN}OS & Version Detection{NC}")
    print(f"8. {BOLD}{CYAN}Sitemap Generator{NC}")
    print(f"9. {BOLD}{CYAN}SSL Certificate Info{NC}")
    print(f"10. {BOLD}{CYAN}Subdomain Enumeration{NC}")
    print(f"11. {BOLD}{CYAN}Port Scanning{NC}")
    print(f"12. {BOLD}{CYAN}Vulnerability Scanner{NC}")
    print(f"13. {BOLD}{CYAN}Google Dorking{NC}")
    print(f"14. {BOLD}{CYAN}Web Archive Lookup{NC}")
    print(f"15. {BOLD}{CYAN}Email Address Finder{NC}")
    print(f"16. {BOLD}{CYAN}Social Media Profile Lookup{NC}")
    print(f"17. {BOLD}{CYAN}API Endpoint Finder{NC}")
    print(f"18. {BOLD}{CYAN}HTTP Headers Lookup{NC}")
    print(f"19. {BOLD}{CYAN}Email Spoofing Check{NC}")
    print(f"20. {BOLD}{CYAN}Subdomain Takeover Detection{NC}")
    print(f"21. {BOLD}{CYAN}Nmap Scan{NC}")
    print(f"22. {BOLD}{CYAN}Social Engineering Toolkit (SET) Integration{NC}")
    print(f"23. {BOLD}{RED}Exit{NC}")

    choice = input("Select an option (1-23): ")

    if choice == '1':
        print(f"{GREEN}Running IP Info Gathering...{NC}")
        # Run IP Info Gathering
    elif choice == '2':
        print(f"{GREEN}Running Domain Info Gathering...{NC}")
        # Run Domain Info Gathering
    elif choice == '3':
        print(f"{GREEN}Running DNS Lookup...{NC}")
        # Run DNS Lookup
    elif choice == '4':
        print(f"{GREEN}Running Whois Lookup...{NC}")
        # Run Whois Lookup
    elif choice == '5':
        print(f"{GREEN}Running Reverse IP Lookup...{NC}")
        # Run Reverse IP Lookup
    elif choice == '6':
        print(f"{GREEN}Running Geolocation Lookup...{NC}")
        # Run Geolocation Lookup
    elif choice == '7':
        print(f"{GREEN}Running OS & Version Detection...{NC}")
        # Run OS & Version Detection
    elif choice == '8':
        print(f"{GREEN}Running Sitemap Generator...{NC}")
        # Run Sitemap Generator
    elif choice == '9':
        print(f"{GREEN}Running SSL Certificate Info...{NC}")
        # Run SSL Certificate Info
    elif choice == '10':
        print(f"{GREEN}Running Subdomain Enumeration...{NC}")
        # Run Subdomain Enumeration
    elif choice == '11':
        print(f"{GREEN}Running Port Scanning...{NC}")
        # Run Port Scanning
    elif choice == '12':
        print(f"{GREEN}Running Vulnerability Scanner...{NC}")
        # Run Vulnerability Scanner
    elif choice == '13':
        print(f"{GREEN}Running Google Dorking...{NC}")
        # Run Google Dorking
    elif choice == '14':
        print(f"{GREEN}Running Web Archive Lookup...{NC}")
        # Run Web Archive Lookup
    elif choice == '15':
        print(f"{GREEN}Running Email Address Finder...{NC}")
        # Run Email Address Finder
    elif choice == '16':
        print(f"{GREEN}Running Social Media Profile Lookup...{NC}")
        # Run Social Media Profile Lookup
    elif choice == '17':
        print(f"{GREEN}Running API Endpoint Finder...{NC}")
        # Run API Endpoint Finder
    elif choice == '18':
        print(f"{GREEN}Running HTTP Headers Lookup...{NC}")
        # Run HTTP Headers Lookup
    elif choice == '19':
        print(f"{GREEN}Running Email Spoofing Check...{NC}")
        # Run Email Spoofing Check
    elif choice == '20':
        print(f"{GREEN}Running Subdomain Takeover Detection...{NC}")
        # Run Subdomain Takeover Detection
    elif choice == '21':
        print(f"{GREEN}Running Nmap Scan...{NC}")
        # Run Nmap Scan
    elif choice == '22':
        print(f"{GREEN}Running Social Engineering Toolkit (SET) Integration...{NC}")
        # Run SET Integration
    elif choice == '23':
        print(f"{RED}Exiting...{NC}")
        exit(0)
    else:
        print(f"{RED}Invalid choice. Try again.{NC}")

# Run the Menu in a Loop
while True:
    menu()