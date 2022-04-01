import socket

def UDPclient(host,port):
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_adress = (host, port)
    msg = "Hello, world! From " + host + ":" + str(port)
    bin_msg = msg.encode('utf-8')
    status = udp_client.sendto(bin_msg, server_adress)
    if status > 0:
        data = udp_client.recv(1024)
        print("Saida: " + data.decode('utf-8'))
    udp_client.close()
