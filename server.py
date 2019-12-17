import socket
import random
import pickle
MAXBYTES = 4056

serversocket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 5656
serversocket1.bind((host, port))
serversocket1.listen(2)
print("working")
clisock, addr = serversocket1.accept()
print("Um usuario conectou")
clisock2, addr2 = serversocket1.accept()




def check_game_win_condition(board):
    if board["A"]["1"] == "X" and board["B"]["2"] == "X" and board["C"]["3"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["A"]["3"] == "X" and board["B"]["2"] == "X" and board["C"]["1"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["A"]["1"] == "X" and board["A"]["2"] == "X" and board["A"]["3"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["B"]["1"] == "X" and board["B"]["2"] == "X" and board["B"]["3"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["C"]["1"] == "X" and board["C"]["2"] == "X" and board["C"]["3"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["A"]["1"] == "X" and board["B"]["1"] == "X" and board["C"]["1"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["A"]["2"] == "X" and board["B"]["2"] == "X" and board["C"]["2"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["A"]["3"] == "X" and board["B"]["3"] == "X" and board["C"]["3"] == "X" :
        print("TEMOS UM VENCEDOR!!!")
        return "X"
    elif board["A"]["1"] == "O" and board["B"]["2"] == "O" and board["C"]["3"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["A"]["3"] == "O" and board["B"]["2"] == "O" and board["C"]["1"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["A"]["1"] == "O" and board["A"]["2"] == "O" and board["A"]["3"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["B"]["1"] == "O" and board["B"]["2"] == "O" and board["B"]["3"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["C"]["1"] == "O" and board["C"]["2"] == "O" and board["C"]["3"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["A"]["1"] == "O" and board["B"]["1"] == "O" and board["C"]["1"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["A"]["2"] == "O" and board["B"]["2"] == "O" and board["C"]["2"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif board["A"]["3"] == "O" and board["B"]["3"] == "O" and board["C"]["3"] == "O" :
        print("TEMOS UM VENCEDOR!!!")
        return "O"
    elif  board["A"]["3"] != None and board["B"]["3"] != None and board["C"]["3"] != None and board["A"]["2"] != None and board["B"]["2"] != None and board["C"]["2"] != None  and board["A"]["1"] != None and board["B"]["1"] != None and board["C"]["1"] != None:
        print("TEMOS UM VENCEDOR!!!")
        return "D"
    else: 
        return "N"

def start_gaming(socket1,socket2):
    board = {   "A": {"1": None, "2":None, "3":None}, 
                "B": {"1": None, "2":None, "3":None},
                "C": {"1": None, "2":None, "3":None}}
    while True:
        sock = random.randrange(1,2)
        if sock == 1: 
            socket1.send("voce ira iniciar".encode("utf8"))
            socket2.send("o adverserio iniciara".encode('utf8'))
        else:
            socket2.send("voce ira iniciar".encode("utf8"))
            socket1.send("o adversario iniciara".encode('utf8'))
        if sock == 1:
            while True:
                socket1.send(pickle.dumps(board))
                res = pickle.loads(socket1.recv(MAXBYTES))
                board[res[0]][res[1]] = "X"
                ans = check_game_win_condition(board)
                if ans == "N":
                    socket2.send(pickle.dumps(board))
                    res = pickle.loads(socket2.recv(MAXBYTES))
                    board[res[0]][res[1]] = "O"
                    ans = check_game_win_condition(board)
                    if ans == "N":
                        continue
                    elif ans == "D":
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("EMPATE!"))
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("EMPATE!"))
                        break
                    elif ans == "X":
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("VOCE PERDEU!"))
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("VOCE GANHOU!"))
                        break
                    elif ans == "O":
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("VOCE PERDEU!"))
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("VOCE GANHOU!"))
                        break
                elif ans == "D":
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("EMPATE!"))
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("EMPATE!"))
                        break
                elif ans == "X":
                    socket2.send(pickle.dumps("end"))
                    socket2.send(pickle.dumps("VOCE PERDEU!"))
                    socket1.send(pickle.dumps("end"))
                    socket1.send(pickle.dumps("VOCE GANHOU!"))
                    break
                elif ans == "O":
                    socket1.send(pickle.dumps("end"))
                    socket1.send(pickle.dumps("VOCE PERDEU!"))
                    socket2.send(pickle.dumps("end"))
                    socket2.send(pickle.dumps("VOCE GANHOU!"))
                    break
        elif sock == 2:
            while True:
                socket2.send(pickle.dumps(board))
                res = pickle.loads(socket2.recv(MAXBYTES))
                board[res[0]][res[1]] = "X"
                ans = check_game_win_condition(board)
                if ans == "N":
                    socket1.send(pickle.dumps(board))
                    res = pickle.loads(socket1.recv(MAXBYTES))
                    board[res[0]][res[1]] = "O"
                    ans = check_game_win_condition(board)
                    if ans == "N":
                        continue
                    elif ans == "D":
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("EMPATE!"))
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("EMPATE!"))
                        break
                    elif ans == "X":
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("VOCE PERDEU!"))
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("VOCE GANHOU!"))
                        break
                    elif ans == "O":
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("VOCE PERDEU!"))
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("VOCE GANHOU!"))
                        break
                elif ans == "D":
                        socket2.send(pickle.dumps("end"))
                        socket2.send(pickle.dumps("EMPATE!"))
                        socket1.send(pickle.dumps("end"))
                        socket1.send(pickle.dumps("EMPATE!"))
                        break
                elif ans == "X":
                    socket2.send(pickle.dumps("end"))
                    socket2.send(pickle.dumps("VOCE PERDEU!"))
                    socket1.send(pickle.dumps("end"))
                    socket1.send(pickle.dumps("VOCE GANHOU!"))
                    break
                elif ans == "O":
                    socket1.send(pickle.dumps("end"))
                    socket1.send(pickle.dumps("VOCE PERDEU!"))
                    socket2.send(pickle.dumps("end"))
                    socket2.send(pickle.dumps("VOCE GANHOU!"))
                    break

                
                    

start_gaming(clisock,clisock2)
                    

                





