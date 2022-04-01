from email import header
import http.client

def HTTPclient(host,port):
    #insira seu código aqui
    L = int(input())
    for i in range(L):
        content = input()
        conn = http.client.HTTPConnection(host, port)
        conn.request("GET", content)
        r1 = conn.getresponse()
        header = r1.getheaders()
        cont = header[2][1]
        if cont == "audio/mpeg":
            print("Playing audio:", content)
        elif cont == "text/html":
            print("Browsing:", content)
        elif cont == "video/x-msvideo":
            print("Playing media:", content)
        elif cont == "application/json":
            print("Processing JSON:", content) 
        elif cont == "close":
            print("Content not found")  
        else:
            print("Unknown file/media: "+cont+"-"+content)
        
        conn.close()
    

HTTPclient("localhost","8888")

