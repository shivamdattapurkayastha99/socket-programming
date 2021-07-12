import socket
import argparse
class Client:
    def __init__(self,h,p,n) -> None:
        self.host=h
        self.port=int(p)
        self.nu=int(n)
    def job(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((self.host,self.port))
            b=self.nu
            s.sendall(b.to_bytes(2,byteorder='big'))
            data=s.recv(1024)
        print('Factorial is ',int.from_bytes(data,byteorder='big'))
        s.close()
class CommandLineParser:
    def __call__(self, *args , **kwds) :
        parser=argparse.ArgumentParser(description='to get host and port')
        required_arguments=parser.add_argument_group('Required command line arguments')
        required_arguments.add_argument("--host",nargs='*',required=True,help='Enter the host')
        required_arguments.add_argument("--port",nargs='*',required=True,help='Enter the port')
        required_arguments.add_argument("--number",nargs='*',required=True,help='Enter the number to get factorial')
        args=parser.parse_args()
        conn_obj=Client(args.host[0],args.port[0],args.number[0])
        conn_obj.job()
def main():
    CommandLineParser()()
if __name__=="__main__":
        main()