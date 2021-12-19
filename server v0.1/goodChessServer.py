import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999
games = []
avalibleGames = ["hanna", "tom", "bob"]


class User:
    def __init__(self, name, playerIP):
        playertag = name
        playerip = playerIP

class games:
    def __init__(self, player1):
        games.append(self)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen()
print("[*] Listing on %s:%d" % (bind_ip, bind_port))



def sendData(clientSocket, msg):
    msg = msg + "\n"
    clientSocket.send(msg.encode())


def reciveData(clientSocket):
    try:
        recived = clientSocket.recv(4096)
        recived = recived.decode()
    except:
        print("[*]connection lost")
    return recived

def newClient(clientSocket, addr):
    recived = reciveData(clientSocket)
    if "playerName:" in recived:
        text = recived.split(":", 1)
        print(text)
        player = User(text[1], addr[0])
        print("games: " + avalibleGames)
        sendData(clientSocket, packageList(avalibleGames))
        option = reciveData(clientSocket)
        if "createGame" in option:
            avalibleGames.append(player.playertag)


def packageList(list):
    output = ""
    for item in list:
        if item == list[len(list) - 1]:
            output = output + item
        else:
            output = output + item + ":"
    print(output)
    return output




def handelClient(clientSocket, addr):
    newClient(clientSocket, addr)
    while True:
        pass
        







while True:
    client, addr = server.accept()
    print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

    clientHandler = threading.Thread(target=handelClient, args=(client,addr))
    clientHandler.start()