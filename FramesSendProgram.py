#!/usr/bin/python
import cv2
import numpy
import socket
import time
import struct

#HOST='192.168.191.1'
HOST='255.255.255.255'
PORT=5051
WIDTH=320
HEIGHT=240

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) #enable broadcast
server.connect((HOST,PORT))
print('now starting to send frames...')
capture=cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)
try:
    while True:
        time.sleep(0.01)
        success,frame=capture.read()
        if success and frame is not None:
            result,imgencode=cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,90])
            #result,imgencode=cv2.imencode('.webp',frame,[cv2.IMWRITE_WEBP_QUALITY,20])
            #print(len(imgencode))
            server.sendall(imgencode)
            #print('have sent one frame')
except Exception as e:
    server.sendall(struct.pack('b',1))
    print(e)
    capture.release()
    server.close()
    
