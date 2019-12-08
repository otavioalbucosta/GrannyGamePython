import socket
import random
MAXBYTES = 4056

def start_gaming(socket1,socket2):
    while True:
        board = {"A": {"1": None, "2":None, "3":None}, 
                "B": {"1": None, "2":None, "3":None},
                "C": {"1": None, "2":None, "3":None}}
        
        
        sock = random.randrange(1,2)
        if sock == 1: 
            socket1.send("você irá iniciar".encode("utf8"))
            socket2.send("o adversário iniciará".encode('utf8'))
        else:
            socket2.send("você irá iniciar".encode("utf8"))
            socket1.send("o adversário iniciará".encode('utf8'))
        if sock == 1:
            while true:
                socket1.send(board)
                res = socket1.recv(MAXBYTES).decode("utf8")
                board[res[0]][res[1]] = X
                

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 5656
serversocket.bind((host, port))
serversocket.listen(10)