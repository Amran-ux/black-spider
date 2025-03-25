#!/bin/bash

# Color Codes for Better Visibility
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
BOLD='\033[1m'
NC='\033[0m'  # No Color

# Banner with Beautiful Colors (BLACK-SPIDER)
function banner() {
    echo -e "${CYAN}"
    echo -e "██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗████████╗    ${BOLD}${CYAN}██████╗ ██████╗ ██████╗ ${NC}"
    echo -e "██╔══██╗██║  ██║██╔══██╗██║   ██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗"
    echo -e "██████╔╝███████║██║  ██║██║   ██║   ██║       ██████╔╝██████╔╝██████╔╝"
    echo -e "██╔═══╝ ██╔══██║██║  ██║██║   ██║   ██║       ██╔═══╝ ██╔═══╝ ██╔═══╝ "
    echo -e "██║     ██║  ██║██████╔╝╚██████╔╝   ██║       ██║     ██║     ██║     "
    echo -e "╚═╝     ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝     ╚═╝     "
    echo -e "${BOLD}${CYAN}        BLACK-SPIDER - All-in-One Information Gathering Tool${NC}"
    echo -e "${NC}"
}

# Main Menu with Colors
function menu() {
    banner
    echo -e "${YELLOW}[+] ${GREEN}Select an option from the menu below:${NC}"
    echo -e "1. ${BOLD}${CYAN}IP Info Gathering${NC}"
    echo -e "2. ${BOLD}${CYAN}Domain Info Gathering${NC}"
    echo -e "3. ${BOLD}${CYAN}DNS Lookup${NC}"
    echo -e "4. ${BOLD}${CYAN}Whois Lookup${NC}"
    echo -e "5. ${BOLD}${CYAN}Reverse IP Lookup${NC}"
    echo -e "6. ${BOLD}${CYAN}Geolocation Lookup${NC}"
    echo -e "7. ${BOLD}${CYAN}OS & Version Detection${NC}"
    echo -e "8. ${BOLD}${CYAN}Sitemap Generator${NC}"
    echo -e "9. ${BOLD}${CYAN}SSL Certificate Info${NC}"
    echo -e "10. ${BOLD}${CYAN}Subdomain Enumeration${NC}"
    echo -e "11. ${BOLD}${CYAN}Port Scanning${NC}"
    echo -e "12. ${BOLD}${CYAN}Vulnerability Scanner${NC}"
    echo -e "13. ${BOLD}${CYAN}Google Dorking${NC}"
    echo -e "14. ${BOLD}${CYAN}Web Archive Lookup${NC}"
    echo -e "15. ${BOLD}${CYAN}Email Address Finder${NC}"
    echo -e "16. ${BOLD}${CYAN}Social Media Profile Lookup${NC}"
    echo -e "17. ${BOLD}${CYAN}API Endpoint Finder${NC}"
    echo -e "18. ${BOLD}${CYAN}HTTP Headers Lookup${NC}"
    echo -e "19. ${BOLD}${CYAN}Email Spoofing Check${NC}"
    echo -e "20. ${BOLD}${CYAN}Subdomain Takeover Detection${NC}"
    echo -e "21. ${BOLD}${CYAN}Nmap Scan${NC}"
    echo -e "22. ${BOLD}${CYAN}Social Engineering Toolkit (SET) Integration${NC}"
    echo -e "23. ${BOLD}${RED}Exit${NC}"

    read -p "Select an option (1-23): " choice

    case $choice in
        1) echo -e "${GREEN}Running IP Info Gathering...${NC}"; bash modules/ip_info.sh ;;
        2) echo -e "${GREEN}Running Domain Info Gathering...${NC}"; bash modules/domain_info.sh ;;
        3) echo -e "${GREEN}Running DNS Lookup...${NC}"; bash modules/dns_lookup.sh ;;
        4) echo -e "${GREEN}Running Whois Lookup...${NC}"; bash modules/whois_lookup.sh ;;
        5) echo -e "${GREEN}Running Reverse IP Lookup...${NC}"; bash modules/reverse_ip_lookup.sh ;;
        6) echo -e "${GREEN}Running Geolocation Lookup...${NC}"; bash modules/geolocation_lookup.sh ;;
        7) echo -e "${GREEN}Running OS & Version Detection...${NC}"; bash modules/os_version_detection.sh ;;
        8) echo -e "${GREEN}Running Sitemap Generator...${NC}"; bash modules/sitemap_generator.sh ;;
        9) echo -e "${GREEN}Running SSL Certificate Info...${NC}"; bash modules/ssl_info.sh ;;
        10) echo -e "${GREEN}Running Subdomain Enumeration...${NC}"; bash modules/subdomain_enum.sh ;;
        11) echo -e "${GREEN}Running Port Scanning...${NC}"; bash modules/port_scanning.sh ;;
        12) echo -e "${GREEN}Running Vulnerability Scanner...${NC}"; bash modules/vuln_scanner.sh ;;
        13) echo -e "${GREEN}Running Google Dorking...${NC}"; bash modules/google_dorking.sh ;;
        14) echo -e "${GREEN}Running Web Archive Lookup...${NC}"; bash modules/web_archive_lookup.sh ;;
        15) echo -e "${GREEN}Running Email Address Finder...${NC}"; bash modules/email_finder.sh ;;
        16) echo -e "${GREEN}Running Social Media Profile Lookup...${NC}"; bash modules/social_media_lookup.sh ;;
        17) echo -e "${GREEN}Running API Endpoint Finder...${NC}"; bash modules/api_finder.sh ;;
        18) echo -e "${GREEN}Running HTTP Headers Lookup...${NC}"; bash modules/http_headers.sh ;;
        19) echo -e "${GREEN}Running