# Subdomain Scanner

## About

A multithreaded subdomain scanner built in Python. It's designed for enumerating subdomains quickly, useful for cybersecurity practice, bug bounty work, or general penetration testing exploration.

## Features

- Multithreaded scanning
- CLI and interactive mode
- Real time subdomain discovery
- Colored terminal output
- Scan summary and statistics
- Save results to a file
- Thread safe execution

## How It Works

The tool takes a target domain, loads subdomains from a wordlist, performs DNS resolution on each one, and shows live results as it goes. Once finished, it generates a summary of what it found.

## Installation

```bash
git clone https://github.com/aayan0620/subdomain-scanner.git
cd subdomain-scanner
pip install -r requirements.txt
```

## Usage

Basic scan:

```bash
python subdomain_scanner.py -d example.com
```

With a custom thread count:

```bash
python subdomain_scanner.py -d example.com -t 100
```

Save output to a file:

```bash
python subdomain_scanner.py -d example.com -o results.txt
```

Full command with all options:

```bash
python subdomain_scanner.py -d example.com -t 100 -o output.txt
```

## Project Structure
