import sys
import udp_scan
import tcp_scan
import untils

args = sys.argv
if args.__len__() > 1:
    match args[1]:
        case "--help" :
            if args.__len__() != 2:
                print("Error Option")
                exit()
            print("Usage: tinyscanner [OPTIONS] [HOST] [PORT]\nOptions:\n    -p         Range of ports to scan\n    -u         UDP scan\n    -t         TCP scan\n    --help     Show this message and exit.")
        case "-u":
            if args.__len__() != 5 or args[3] != "-p":
                print("Error Option")
                exit()
            ip = args[2]
            port= args[4]
            result = untils.port_validator(port)
            if result[0] == False:
                print("Port is invalid")
                exit()
            for p in result[1]:
                actif = udp_scan.udp_scan(ip, p)
        case "-t":
            if args.__len__() != 5 or args[3] != "-p":
                print("Error Option")
                exit()
            ip = args[2]
            port= args[4]
            result = untils.port_validator(port)
            if result[0] == False:
                print("Port is invalid")
                exit()
            for p in result[1]:
                actif =tcp_scan.tcp_scan(ip, p)
        case _:
            print("Error Option")
            exit