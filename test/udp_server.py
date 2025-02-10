import socket

def udp_server(host='0.0.0.0', port=5000):
    # Création du socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Liaison du socket à l'adresse et au port
    server_socket.bind((host, port))
    print(f"Serveur UDP en écoute sur {host}:{port}")

    while True:
        # Réception des données (jusqu'à 1024 octets)
        data, addr = server_socket.recvfrom(1024)
        print(f"Message reçu de {addr}: {data.decode()}")

        # Réponse au client
        response = "Message reçu"
        server_socket.sendto(response.encode(), addr)

# Lancement du serveur
udp_server()
