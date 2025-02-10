import ipaddress


def ip_validator(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def port_validator(port):
    list_ports = []
    if port.__contains__('-') == False and port.isdigit():
        list_ports.append(port)
        return (True, list_ports)
    elif port.__contains__('-') == True:
        parts = port.split('-')
        if len(parts) == 2:
            port1 = parts[0]
            port2 = parts[1]
            if port1.isdigit() and port2.isdigit():
                if int(port1) <= int(port2):
                    for i in range(int(port1), int(port2)):
                        list_ports.append(i)
                    list_ports.append(int(port2))
                    return (True, list_ports)
            
    return (False, list_ports)

