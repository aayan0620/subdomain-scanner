import socket
import argparse
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from colorama import Fore, Style, init

init(autoreset=True)

# 🔥 BANNER
def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
   _____       _     _                                  
  / ____|     | |   | |                                 
 | (___  _   _| |__ | | ___   __ _  __ _  ___ _ __      
  \___ \| | | | '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|     
  ____) | |_| | |_) | | (_) | (_| | (_| |  __/ |        
 |_____/ \__,_|_.__/|_|\___/ \__, |\__, |\___|_|        
                             __/ | __/ |               
                            |___/ |___/                

   🔥 Subdomain Scanner 🔥
   👨‍💻 Author: AAYAN 
""")

# Argument parser
parser = argparse.ArgumentParser(description="Subdomain Scanner by AAYAN")

parser.add_argument("-d", "--domain", help="Target domain (e.g. example.com)")
parser.add_argument("-t", "--threads", type=int, help="Number of threads")
parser.add_argument("-o", "--output", help="Save results to file")

args = parser.parse_args()

banner()

# 🔥 INPUT SYSTEM
domain = args.domain or input(Fore.YELLOW + "🌐 Enter target domain: ")
threads = args.threads or int(input(Fore.YELLOW + "⚡ Threads (default 50): ") or 50)
output_file = args.output or input(Fore.YELLOW + "💾 Output file (optional): ")

print(Fore.GREEN + f"\n🚀 Starting scan on {domain} with {threads} threads...\n")

# Load wordlist
try:
    with open("wordlist.txt", "r") as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print(Fore.RED + "❌ wordlist.txt not found!")
    exit()

found_list = []
lock = Lock()

total = len(subdomains)
found_count = 0

start_time = time.time()

# Scan function
def scan(sub):
    global found_count
    subdomain = sub + "." + domain

    try:
        ip = socket.gethostbyname(subdomain)

        with lock:
            print(Fore.GREEN + f"[FOUND] {subdomain}  →  {ip}")
            found_list.append(f"{subdomain} | {ip}")
            found_count += 1
    except:
        pass

# Multithreading
with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scan, subdomains)

time_taken = round(time.time() - start_time, 2)

# Save results
if output_file:
    with open(output_file, "w") as f:
        for sub in found_list:
            f.write(sub + "\n")
    print(Fore.CYAN + f"\n💾 Results saved in {output_file}")

# 🔥 SUMMARY
print(Fore.MAGENTA + "\n📊 ===== SCAN SUMMARY =====")
print(Fore.WHITE + f"🌐 Domain        : {domain}")
print(f"📌 Total Tested  : {total}")
print(f"✅ Found         : {found_count}")
print(f"❌ Not Found     : {total - found_count}")
print(f"⚡ Threads       : {threads}")
print(f"⏱ Time Taken    : {time_taken} sec")

# 🔥 FOOTER BRANDING
print(Fore.CYAN + Style.BRIGHT + "\n🔥 Powered by AAYAN")
print(Fore.YELLOW + "💻 Cyber Security Researcher\n")