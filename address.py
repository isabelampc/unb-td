import socket

L = int(input())
for i in range(L):
    IP = input()
    dominio = socket.gethostbyaddr(IP)[0]
    print(dominio)

