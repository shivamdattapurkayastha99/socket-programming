# from socket import *
# s=socket.socket(family=AF_INET,type=SOCK_STREAM,port=0)
import socket
import sys
try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Error in creating socket")
    print("Reason:",str(err))
    sys.exit()
print("Socket Created")
target_host=input("Enter the target host name")
target_port=input("Enter the target port")
try:
    sock.connect((target_host,int(target_port)))
    print("Socket connected is",target_host+target_port)
    sock.shutdown(2)
except socket.error as err:
    print("Failed to connect ",target_host+target_port)
    print("Reason is ",str(err))
    sys.exit()
