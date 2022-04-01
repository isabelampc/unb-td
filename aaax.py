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
        atual = valor[0]
        msg = []
        cont = 0
        for char in valor:
            if char == atual:
                cont += 1
            else:
                msg.append(atual)
                msg.append(str(cont))
                atual = char
                cont = 1

        msg.append(atual) #adicionar o ultimo 
        msg.append(str(cont))
        
        manda = "".join(msg)
        conn.send(manda.encode('utf-8'))
          #  conn.send(err.encode('utf-8'))
    conn.close()