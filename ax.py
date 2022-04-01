texto = "VVVVVVVVVVVVVVVVVVVV"

atual = texto[0]
msg = []
cont = 0
for char in texto:
    if char == atual:
        cont += 1
    else:
        msg.append(atual)
        msg.append(str(cont))
        atual = char
        cont=1

msg.append(atual) #adicionar o ultimo 
msg.append(str(cont))
        
manda = "".join(msg)
print(manda)