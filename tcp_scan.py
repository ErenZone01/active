import socket

def tcp_scan(ip, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        # Test connection
        test = s.connect_ex((ip, int(port)))
        if test == 0:
            print(f'Port {port} is open')
        else:
            print(f"Port {port} is close")
    except socket.timeout:
        print("Not conneected")
    except:
        print(f"Not connected")    
    s.close()