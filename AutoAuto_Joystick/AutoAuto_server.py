# SENDER
import time
import pygame
import socket

pygame.init()
pygame.joystick.init()
try:
    controller1 = pygame.joystick.Joystick(0)
    controller1.init()
except:
    print("Controller Not Intialised")

ip = "192.168.137.161"
port = 8089


def map_range(x):
      return (x + 1) * (256 - 0) // (1 + 1) + 0

while True :
    pygame.event.get()
    axis=[0,0,0,0,0,0]
    axes = controller1.get_numaxes()
    for i in range(axes):
        axis[i] = int(map_range(controller1.get_axis(i)))
    print(axis)
    data_string = bytearray(axis)
    print(f'Sending data string {data_string} to {ip}:{port}')
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.connect((ip, port))
    sock.send(data_string)
    time.sleep(0.2)


