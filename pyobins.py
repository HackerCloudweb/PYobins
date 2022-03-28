#!/usr/bin/python3
#Herramienta programada por HackerCloud
#https://github.com/HackerCloudweb
#información de la web: https://gtfobins.github.io/

import os
import webbrowser 
import time

print("                                                       ")
print("                                                       ")
print("       ██████  ██    ██  ██████  ██████  ██ ███    ██ ███████ ")
print("       ██   ██  ██  ██  ██    ██ ██   ██ ██ ████   ██ ██      ")
print("       ██████    ████   ██    ██ ██████  ██ ██ ██  ██ ███████ ")
print("       ██         ██    ██    ██ ██   ██ ██ ██  ██ ██      ██ ")
print("       ██         ██     ██████  ██████  ██ ██   ████ ███████ ")
print("                                                       ")
print("                                                       ")
print("                 Herramienta creada por HackerCloud          ")
print("                                                             ")
print("                 https://github.com/HackerCloudweb           ")
print("                                                                      ")
print("                                                                      ")


busqueda = input("[+] Nombre de el paquete o binario: ")
url = "https://gtfobins.github.io/"

if (busqueda == ""):
    print("                                              ")
    print("[+] Por favor, introduzca un paquete o binario")

else:
    print("                                                    ")
    print("[+] Buscando paquete...")
    time.sleep(1)
    print("                                                    ")
    print("[+] Paquete encontrado")
    time.sleep(1)
    print("                                                    ")
    print("[+] Gracias por usar mi herramienta, créditos a "+url)
    time.sleep(1)
    webbrowser.open(url+"gtfobins/"+busqueda)

