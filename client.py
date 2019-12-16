import socket
import pickle

MAXBYTES = 4056
def show_board(board):
    tabuleiro = '''
     |     |   
  {} |  {} |  {}
_____|_____|_____
     |     |
  {} |  {} |  {}
_____|_____|_____
     |     |
  {} |  {} |  {}
     |     |
        '''.format(board['A']['1'], board['A']['2'], board['A']['3'],
                   board['B']['1'], board['B']['2'], board['B']['3'],
                   board['C']['1'], board['C']['2'], board['C']['3'])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5656
s.connect((host, port))

res = s.recv(MAXBYTES).decode("utf8")
print(res)
if res == "você irá iniciar":
    while True:
        res = pickle.loads(s.recv(MAXBYTES))
        if res == "end":
            break;
        else:
            print(show_board(res))
            value = input("Digite a Letra (maiúscula) e o número")
            if res[value[0]][value[1]] != None or ord(value[0]) < ord("A") or ord(value[0]) > ord("C") or int(value[1]) < 1 or int(value[1]) > 3 :
                print("Essa casa está ocupada ou você digitou alguma letra ou numero inexistente");
            else:
                s.send(pickle.dumps(value.upper()))