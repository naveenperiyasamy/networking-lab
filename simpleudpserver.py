# networking-lab
import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
serversock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("server waiting") 
while True:
 data, addr = serversock.recvfrom(1024)
 print ("message:", data)
