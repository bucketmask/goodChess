import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Listing on %s:%d" % (bind_ip, bind_port))




def custom_handel(clientSocket):
    while True:
        try:
            recived = clientSocket.recv(4096)
            if not recived:
                break
            print("[*] Recived: %s" % recived.decode())
            response = "ACK!\n"
            clientSocket.send(response.encode())
            print("Sent ACK!, waiting for response")
        except:
            print("[*]connection lost")
            return







while True:
    client, addr = server.accept()
    print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

    clientHandler = threading.Thread(target=custom_handel, args=(client,))
    clientHandler.start()