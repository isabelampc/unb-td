import socket

def TCPserver(host, port):
    # insira seu códido aqui
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host,port))
    tcp_server.listen()
    conn, addr = tcp_server.accept()
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        valor = data.decode('utf8')
        contador = {}
        for char in valor:
            contador.setdefault(char, 0)
            contador[char] += 1
        msg = []
        for chave in contador.keys():
            msg.append(chave)
            msg.append(str(contador[chave]))
        
        manda = "".join(manda)
        conn.send(manda.encode('utf-8'))
          #  conn.send(err.encode('utf-8'))
    conn.close()