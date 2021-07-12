import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))
payload='hi shivam server'
try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data=client_socket.recv(1024)
        print(str(data))
        more=input('Want to send more data server shivam')
        if more.lower()=='y':
            payload=input('Enter payload')
        else:
            break
except:
    print("Exited by user")
client_socket.close()

