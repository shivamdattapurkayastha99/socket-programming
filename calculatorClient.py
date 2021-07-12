import sys
import socket
import ipaddress
s=socket.socket()
try:
    host=str(ipaddress.ip_address(sys.argv[1]))
    port=int(sys.argv[2])
    s.connect((host,port))
    print("IP address of the server is ",host)
    print("Port number of the server is ",port)
    while True:
        equ=input("Please give your equation to shivam calculator.Press Q to exit")
        s.send(equ.encode())
        result=s.recv(1024).decode()
        if result=="Quit":
            print("Closing client connection")
            break
        elif result=="ZeroDiv":
            print("Cant divide by zero")
        elif result=="MathError":
            print("Error with math")    
        elif result=="SyntaxError":
            print("Error with syntax")
        elif result=="NameError":
            print("Did not enter equation")
        else:
            print("Answer is",result)
    s.close()
except(IndexError,ValueError):
    print("You did not specify ip address and port number")
