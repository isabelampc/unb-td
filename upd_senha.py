import socket

def UDPserver(host, port):
    global udpd
    udpd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_adress = (host, port)
    udpd.bind(server_adress)
    while 1:
        data, address = udpd.recvfrom(1024)
        if not data:
            break
        senha = data.decode('utf-8')
        carac_valido = senha.isalnum()
        maiuscula = senha.isupper() #caso todas maiusculas retorna true
        minuscula = senha.islower() #caso todas minusculas retorna true 
        tamanho = len(senha)
        if(carac_valido and not maiuscula and not minuscula and tamanho > 5 and tamanho < 33):
            msg = "Senha valida."
        else :
            msg = "Senha inválida!"

        udpd.sendto(msg.encode('utf-8'), address)
    udpd.close()

UDPserver("localhost", 8888)

   # for caractere in senha:
    #    if(caractere >= 65 and caractere <= 90):
     #       maiuscula = True
      #  if(caractere >= 97 and caractere <= 122):
       #     minuscula = True
