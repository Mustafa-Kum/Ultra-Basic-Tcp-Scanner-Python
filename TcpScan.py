#python3
import socket

ip = input("Ip : ")
port = [80,443,8080,9090]
## port = input("Port: ")

def tcp_scan(ip, port):

    try:
        for scan in port :

                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                if not tcp.connect_ex((ip, scan)):
                        print(f"[+] TCP port is open {ip, scan}")
                
                elif tcp.connect_ex((ip,scan)):
                        print(f"[-] TCP port is closed {scan}")
                

    except:
            print("[-] TCP port is closed")

tcp_scan(ip, port)

