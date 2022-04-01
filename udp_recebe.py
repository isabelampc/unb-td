import socket

def UDPserver(host, port):
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_adress = (host, port)
    udp_server.bind(server_adress)
    while 1:
        data, address = udp_server.recvfrom(1024)
        if not data:
            break
        msg = "Hello, world! From " + host + ":" + str(port)
        sucess = 'Sucesso'
        err = 'Erro'
        if data.decode('utf8') == msg:
            print('Servidor recebeu a mensagem correta')
            udp_server.sendto(sucess.encode('utf-8'), address)
        else :
            print('Servidor nao recebeu a mensagem correta')
            udp_server.sendto(err.encode('utf-8'), address)
    udp_server.close()