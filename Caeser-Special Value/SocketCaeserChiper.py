# -*- coding: utf-8 -*- 
 
import socket
import time
 

recv = ''
dada = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('Server Address', Port)
#sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(server_address)
time.sleep(0.1)
recvdata = sock.recv(10000)
print(recvdata)
data = recvdata.split('>\n\n')[1]
data = data.split('\n\n')[0]

strrrr= data#'WPKT VJNH WXAA APBQ WDDZ TAHT TCKN RDPI RDDA EAJB ODCT KDXS JHTG QDDB VDDS QXGS RGPQ RPAB UAPV HZXC SDAA KPXC KDIT EJHW UXCT VGDL EAPC AXHI EGPN BTDL'
#socket input = strrrr
#strrrr='' #here

finish=0

for j in range(1,27):
    result=''
    for i in range(0,len(strrrr)):
        if strrrr[i] == ' ':
            result+=' '
        
        elif ord(strrrr[i])-j >=65:
            #strrrr[i]=chr(ord(strrrr[i])-20)
            result+=chr(ord(strrrr[i])-j)

        else:
            #strrrr[i]=chr(90-(20-((ord(strrrr[i])-65)+1)))
            result+=chr(90-(j-((ord(strrrr[i])-65)+1)))
            
    for i in range(0,len(result),5):
        if result[i]=='F' and result[i+1]=='L' and result[i+2]=='A' and result[i+3]=='G':
            finish=1
    if finish==1:
        break
    else:
        result
        
print result

sock.send(result + "\n")


recvdata = sock.recv(10000)
print(recvdata)
 
 
sock.close()
