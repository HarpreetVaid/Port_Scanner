import sys
import socket

def scan_port(host,port):
    try:
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sc.settimeout(1)
        result = sc.connect_ex((host,port))
        sc.close()
        if result == 0:
            return True
        else:
            return False         
    except socket.error as e:
        print("Something Went Wrong")


def resolve_website_to_ip(host):
    if not host.replace('.','').isdigit():
        try:
            ip_host = socket.gethostbyname(host)
            print(f"Scanning on {host} ip {ip_host}")
            return ip_host
        except socket.gaierror:
            print(f"Could not resolve the IP address of {host}")
    else:
        print(f"Scanning on {host}")
        return host
        

if __name__ == '__main__':
    host = None  
    if len(sys.argv) == 4:
        host = resolve_website_to_ip(sys.argv[3])
        if sys.argv[1] == '-p':  
            port = sys.argv[2].split('-')
            if len(port) == 2:
                for i in range(int(port[0]),int(port[1])+1):
                    if scan_port(host,i):
                        print(f"Port no. {i} is still alive")
                    else:
                        print(f"Port {i} is Not open")
            else:
                print("Please specify port no. in specfic format -p start-ending ")
        else:
            print("Port please enter argument -p")
    else:
        print("Argumnet are not fully defined")
