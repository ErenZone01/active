import socket


def udp_scan(ip, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)
    # Test connection
    try:
        u= s.sendto(b'', (ip, int(port)))
        b, adrr= s.recvfrom(1024)
        print(f"receive : {b}, {adrr}")
        print(f"Port {port} is open")
    except socket.timeout:
        print(f"Port {port} is closed")
    except:
        print(f"Port {port} is close")
    finally:
        s.close()