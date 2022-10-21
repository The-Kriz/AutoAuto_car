# SENDER
import time
import pygame
import socket
#from keyboard import is_pressed
import pickle

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
   # msg = [0,0,0,0,0,0]


    axes = controller1.get_numaxes()
    for i in range(axes):
        axis[i] = int(map_range(controller1.get_axis(i)))
    print(axis)
    # try:

        # if is_pressed('w'):
        #     msg = b'w'
        # elif is_pressed('a'):
        #     msg = b'a'
        # elif is_pressed('s'):
        #     msg = b's'
        # elif is_pressed('d'):
        #     msg = b'd'

        # if (axis[0] > 170 or axis[0] < 85):
        #     msg[0] = (axis[0])
        # if (axis[1] > 170 or axis[1] < 85):
        #     msg[1] = (axis[1])
        # if (axis[2] > 170 or axis[2] < 85):
        #     msg[2] = (axis[2])
        # if (axis[3] > 170 or axis[3] < 85):
        #     msg[3] = (axis[3])
        # if (axis[4] > 170 or axis[4] < 85):
        #     msg[4] = (axis[4])
        # if (axis[5] > 170 or axis[5] < 85):
        #     msg[5] = (axis[5])

    # except:
    #     break
    #
    # print(msg)
    # data_string = bytearray(msg)
    # #data_string = msg

    data_string = bytearray(axis)


 #   print(f'Sending {msg} to {ip}:{port}')
    print(f'Sending data string {data_string} to {ip}:{port}')
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.connect((ip, port))
    sock.send(data_string)
    # sock.sendto(arr (ip, port))
    time.sleep(0.2)
 #   print (msg)


