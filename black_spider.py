import os
import subprocess

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

def banner():
    print(f"{CYAN}███████╗ ██████╗ ██╗  ██╗████████╗    {BOLD}{CYAN}██████╗ ██████╗ ██████╗ {NC}")
    print(f"██╔════╝██╔═══██╗██║ ██╔╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗")
    print(f"███████╗██║   ██║█████╔╝    ██║       ██████╔╝██████╔╝██████╔╝")
    print(f"╚════██║██║   ██║██╔═██╗    ██║       ██╔═══╝ ██╔═══╝ ██╔═══╝ ")
    print(f"███████║╚██████╔╝██║  ██╗   ██║       ██║     ██║     ██║     ")
    print(f"╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝     ╚═╝     ")
    print(f"{BOLD}{CYAN}        GHOST-BYTE-BD - All-in-One Information Gathering Tool{NC}")
    print(f"{NC}")

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

    choice = input(f"{YELLOW}[+] {GREEN}Select an option (1-23): {NC}")

    if choice == "1":
        print(f"{GREEN}Running IP Info Gathering...{NC}")
        # Call your function here
    elif choice == "2":
        print(f"{GREEN}Running Domain Info Gathering...{NC}")
        # Call your function here
    elif choice == "23":
        print(f"{RED}Exiting...{NC}")
        exit(0)
    else:
        print(f"{RED}Invalid choice. Try again.{NC}")
        menu()

# Run the menu
menu()