#script Subdomain Enumeration
#exemple subenum.py wordlist site

import os 
import requests
import sys

file = f"{sys.argv[1]}"
sub_list = open("subdomains.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[2]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_domains)



