import socket

targetPort = 9999

service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
s.settimeout(2)
result = False
end = None
for ip in range(1, 256):
    s = socket.socket()
    s.settimeout(2)
    result = False
    end = None
    try:
        testingip = "192.168.0." + str(ip)
        testingFull = testingip, targetPort
        s.connect((testingip, targetPort))
        s.close()
        print(testingip)

    except:
        print("fail: " + testingip)

a = input()
