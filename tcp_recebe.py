import socket

def TCPserver(host, port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host,port))
    tcp_server.listen()
    conn, addr = tcp_server.accept()
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        msg = "Hello, world! From " + host + ":" + str(port)
        sucess = 'Sucesso'
        err = 'Erro'
        if data.decode('utf8') == msg:
            print('Servidor recebeu a mensagem correta')
            conn.send(sucess.encode('utf-8'))
        else :
            print('Servidor nao recebeu a mensagem correta')
            conn.send(err.encode('utf-8'))
    conn.close()

TCPserver("localhost", 8888)