import socket
from concurrent.futures import ThreadPoolExecutor

# Target input
domain = input("Enter target domain (e.g. example.com): ")

print("\nScanning...\n")

# Load wordlist
with open("wordlist.txt", "r") as file:
    subdomains = file.read().splitlines()

# Function to scan each subdomain
def scan(sub):
    subdomain = sub + "." + domain

    try:
        socket.gethostbyname(subdomain)
        print("[FOUND]", subdomain)
    except:
        pass

# Multithreading
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan, subdomains)

print("\nScan Completed 🔥")