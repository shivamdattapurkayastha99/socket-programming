import socket


host = 'local host'
port = 5000


s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

s.bind(('', port))


s.listen(1)


c, addr = s.accept()


print("CONNECTION FROM:", str(addr))

c.send(b"Hello \
	My name is Shivam Datta Purkayastha")

msg = "Bye.............."
c.send(msg.encode())


c.close()
