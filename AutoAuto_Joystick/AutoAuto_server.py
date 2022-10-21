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
