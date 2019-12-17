import socket
import pickle

MAXBYTES = 4056
def show_board(board):
    tabuleiro = '''
     1     2     3
          |       |   
 A   {}  |  {}  |  {}
   _______|_______|_____
          |       |
 B   {}  |  {}  |  {}
   _______|_______|_____
          |       |
 C   {}  |  {}  |  {}
          |       |
        '''.format(board['A']['1'], board['A']['2'], board['A']['3'],
                   board['B']['1'], board['B']['2'], board['B']['3'],
                   board['C']['1'], board['C']['2'], board['C']['3'])
    return tabuleiro


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5656
s.connect((host, port))
print("conectado, esperando o outro jogador")

res = s.recv(MAXBYTES).decode("utf8")
print(res)

while True:
    res = pickle.loads(s.recv(MAXBYTES))
    if res == "end":
        res = pickle.loads(s.recv(MAXBYTES))
        print(res)
        break
    else:
        print(show_board(res))
        while True:

            value = str(input("Digite a Letra (maiuscula) e o numero\n"))
            if ord(value[0]) < ord("A") or ord(value[0]) > ord("C") or int(value[1]) < 1 or int(value[1]) > 3 or res[value[0]][value[1]] != None:
                print("Essa casa este ocupada ou voce digitou alguma letra ou numero inexistente");
            else:
                s.send(pickle.dumps(value.upper()))
                break