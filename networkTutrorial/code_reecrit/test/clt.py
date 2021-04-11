import socket

host,port=('`127.0.0.1', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host,port))
    print("client conn")
    data = "Bonjour a toi!"
    data = data.encode('utf8')
    socket.sendall(data)
except:
    print("connection a échoué")
finally:
    socket.close()