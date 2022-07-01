#!/usr/bin/env python

from urllib import response
import requests
from colorama import init
from termcolor import colored

init()

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print('\033[1;33;40m| \ | |    /_ |        |  _ \| |')
print ("|  \| | ___ | |___  ___| |_) | |")
print ("| . ` |/ _ \| / __|/ _ \  _ <| __/ __|")
print ("| |\  | (_) | \__ \  __/ |_) | || (")
print ("|_|_\_|\___/|_|___/\___|____/_\__\___|")
print ("|  _ \__   __/ ____| |  __ \|  __ \|_   _/ ____|  ____|")
print ("| |_) | | | | |      | |__) | |__) | | || |    | |__  ")
print ("|  _ <  | | | |      |  ___/|  _  /  | || |    |  __|")
print ("| |_) | | | | |____  | |    | | \ \ _| || |____| |")
print ("|____/  |_|  \_____| |_|    |_|  \_\_____\_____|______") 
print(colored(data["bpi"]["USD"]["rate"] , 'green', 'on_red'))
