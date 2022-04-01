import http.client

def HTTPclient(host,port):
    #insira seu código aqui
    L = int(input())
    for i in range(L):
        content = input()
        conn = http.client.HTTPConnection(host, port)
        conn.request("GET", content)
        r1 = conn.getresponse()
        dado = r1.read()
        print(dado.decode())
        conn.close()

HTTPclient("localhost","8888")