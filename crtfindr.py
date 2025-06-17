import requests
import argparse
import json

def command():
    global args
    parser = argparse.ArgumentParser(
        prog='crtfindr',
        description='Find certificates information through your own terminal.',
        epilog='Thanks for supporting me!',
        formatter_class=argparse.RawTextHelpFormatter,
        )

    parser.add_argument('url')
    parser.add_argument('-d', '--domains', action='store_true', help='Obtain the subdomains related to the certificate.')
    parser.add_argument('-c', '--common-name', action='store_true', help='Obtain the subdomains related to the certificate.')
    parser.add_argument('-S', '--serial', help='Obtain the serial number of the certificates related to the domain')
    parser.add_argument('-s', '--silent', action='store_true', help='Suppresses all messages from the output. Only shows the data.')
    args = parser.parse_args()
    if not args.url:
        parser.error(f"No input provided. You must specify the URL of the domain that you want to obtain information about.")

def main():
    global args, response, domain_list
    print('''
                __  _____           __    
     __________/ /_/ __(_)___  ____/ /____
    / ___/ ___/ __/ /_/ / __ \/ __  / ___/
   / /__/ /  / /_/ __/ / / / / /_/ / /    
   \___/_/   \__/_/ /_/_/ /_/\__,_/_/     
                                       
Github: daemoncibsec / Instagram: @daemoncibsec
''')
    print(f'[+] Sending request to "crt.sh" ...')
    print(f'[+] Waiting for an answer...\n')
    request()
    if args.domains is True:
        gather_domains()
        entries = len(domain_list)
        print(f'\n[+] {entries} results have been detected.')
    elif args.domains is False:
        display_info()

def request():
    global args, response
    try:
        req = requests.get(f'https://crt.sh/json?q={args.url}')
        # If the execution is successful, store the result of the request in a variable to process it's information later.
        if req.status_code == 200:
            response = json.loads(req.text)
        else:
            print(f'[-] Could not gather the information required. Request status code: {req.status_code}')
    except Exception as e:
        print(f'[Function - request] Error: {e}')

def gather_domains():
    global args, response, domain_list
    domain_list = []
    try:
        for line in response:
            # Checks if the name of the subdomain is repeated and, if not, stores it in a list.
            if line["common_name"] not in domain_list:
                domain_list.append(line["common_name"])
        for entry in domain_list:
            print(entry)
    except Exception as e:
        print(f'[Function - gather_domains] Error: {e}')

def display_info():
    global args, response, domain_list
    try:
        for line in response:
            # This is just the for formatting the output so it shows as I'd like, but you can change it if you want to
            print(f'Entry ID: {line["issuer_ca_id"]}\nIssuer Name: {line["issuer_name"]}\nCommon Name: {line["common_name"]}\nName: {line["name_value"]}\nID: {line["id"]}\nEntry Timestamp: {line["entry_timestamp"]}\nSerial Number: {line["serial_number"]}\n')
    except Exception as e:
        print(f'[Fuction - display_info] Error: {e}')

if __name__=='__main__':
    command()
    if args.silent is False:
        main()
    else:
        if args.domains is True:
            request()
            gather_domains()
        else:
            request()
            display_info()
