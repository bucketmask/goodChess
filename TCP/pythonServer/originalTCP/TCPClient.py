import socket
target_host = "127.0.0.1"
target_port = 9999

#-Create a socket object
# -AF_INET is saying we are going to use ipv4
# -SOCK_STREAM is saying we are using TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print("hostname: " + hostname)
print("hostname: " + ipaddr)





#We then connect to the client
client.connect((target_host, target_port))

while True:
    try:
        print("Send>>", end="")
        msg = input()
        client.send(msg.encode())

        response = client.recv(4096)
        print("[*] Response: " + response.decode())
    except:
        print("Connection lost")