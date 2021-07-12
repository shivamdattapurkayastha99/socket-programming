import socket
import threading
server_socket=socket.socket()
host='127.0.0.1'
port=1233
threadcount=0
try:
    server_socket.bind((host,port))
except socket.error as e:
    print(str(e))
print('waiting')
server_socket.listen(5)
def client_thread(connection):
    connection.send('Welcome to server shivam')
    while True:
        data=connection.recv(2048)
        reply=f"Hello I am server{data.decode('utf-8')}"
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
while True:
    client,address=server_socket.accept()
    print(f"Connected to{address[0]}{str(address[1])}")
    threading.Thread(target=client_thread(client)).start()
    threadcount+=1
    print(f"Threadcount is {str(threadcount)}")
server_socket.close()
