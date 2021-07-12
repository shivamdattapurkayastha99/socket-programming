from os import name
import socket 
import argparse
class CalFactorial:
    def __init__(self,a) -> None:
        self.p=a
    def factorial(self):
        s=1
        while self.p>0:
            s=s*self.p
            self.p=self.p-1
        return s
class Host:
    def __init__(self,h,p) -> None:
        self.host=h
        self.port=int(p)
    def job(self):
        try:
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                s.bind((self.host,self.port))
                s.listen()
                connection,address=s.accept()
                print('Host(Shivam) has started')
                with connection:
                    print('address is ',address)
                    while True:
                        data=connection.recv(1024)
                        if not data:
                            break
                        a=int.from_bytes(data,byteorder='big')
                        j=CalFactorial(a)
                        jc=j.factorial()
                        data=jc.to_bytes(2,byteorder='big')
                        connection.sendall(data)
                s.close()
        except:
            print('error estabilishing the host')
            s.close()
class CommandLineParser:
    def __call__(self, *args, **kwds):
        parser=argparse.ArgumentParser(description='to get host and port')
        required_arguments=parser.add_argument_group('Required command line arguments')
        required_arguments.add_argument("--host",nargs='*',required=True,help='Enter the host')
        required_arguments.add_argument("--port",nargs='*',required=True,help='Enter the port')
        args=parser.parse_args()
        conn_obj=Host(args.host[0],args.port[0])
        conn_obj.job()
def main():
    CommandLineParser()()
if __name__=="__main__":
        main()




                