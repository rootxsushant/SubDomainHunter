import requests
import sys
import argparse
import time
from tqdm import tqdm

# Define the parser
parser = argparse.ArgumentParser(description='Subdomain enumeration tool')
parser.add_argument('-t', '--target', required=True, help='Target domain')
parser.add_argument('-w', '--wordlist', required=True, help='Wordlist file')
parser.add_argument('-o', '--output', default='output.txt', help='Output file')

args = parser.parse_args()

# Load the wordlist
with open(args.wordlist, 'r') as f:
    wordlist = [line.strip() for line in f.readlines()]

# Initialize the request counter
request_count = 0

# Send HEAD requests to the target domain with each subdomain
with open(args.output, 'w') as f:
    with tqdm(total=len(wordlist), desc='Scanning for subdomains', unit='subdomains', bar_format='{l_bar}{bar} | {n_fmt}/{total_fmt} subdomains') as pbar:
        for subdomain in wordlist:
            url = f"https://{subdomain}.{args.target}"
            headers = {'Host': f"{subdomain}.{args.target}"}
            try:
                response = requests.head(url, headers=headers, stream=True)
                if response.status_code == 200:
                    f.write(f"Found subdomain: {subdomain}\n")
                    f.write(f"Content-Length: {response.headers.get('Content-Length', 'Unknown')}\n")
                    f.write("\n")
                    print(f"\033[92m{subdomain}\033[0m" + " is a valid subdomain")
            except requests.exceptions.ConnectionError:
                pass

            # Update the request counter and progress bar
            request_count += 1
            pbar.update(1)

            # Add a delay after every 50 requests
            if request_count % 50 == 0:
                print(f"\nSent {request_count} requests, {len(wordlist) - request_count} remaining...")
                time.sleep(20)  # Freeze for 20 seconds

print("\nScanning complete!")
