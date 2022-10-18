# SENDER
import time
import socket
from keyboard import is_pressed

ip = "192.168.1.193"
port = 8089
msg = b" "
while True :
    try:
        if is_pressed('w'):
            msg = b'w'
        elif is_pressed('a'):
            msg = b'a'
        elif is_pressed('s'):
            msg = b's'
        elif is_pressed('d'):
            msg = b'd'
        elif is_pressed('j'):
            msg = b'j'
        elif is_pressed('k'):
            msg = b'k',
        elif is_pressed('l'):
            msg = b'l'
    except:
        break
        
print(f'Sending {msg} to {ip}:{port}')

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(msg, (ip, port))
time.sleep(0.2)
msg = b' '
