# SubDomainHunter
SubdomainHunter is a Python script designed to perform a subdomain enumeration attack on a target domain. It utilizes a wordlist of potential subdomain names to send HEAD requests to the target domain, identifying valid subdomains by analyzing the HTTP response status codes and content lengths.

### Usage:

```
Clone the repository: git clone https://github.com/your-username/SubdomainHunter.git
```
Install the required dependencies
```
pip3 install -r requirements.txt
``` 
Run the script 
```
python3 subdomainhunter.py -t <target-domain> -w <wordlist-file> -o <output-file>
```
### Arguments
- -t or --target: The target domain to scan.
- -w or --wordlist: The file containing a list of subdomain names to test.
- -o or --output: The file to write the results to (default is output.txt).

### Output
The script will output the discovered subdomains to the specified output file and print them to the console. The output file will contain the following information for each valid subdomain
```
Found subdomain: subdomain1
Content-Length: 1234

Found subdomain: subdomain2
Content-Length: 5678
```
