#! /usr/bin/python
import socket
from enum import IntEnum
from MotorModule.Motor import Motor
import traceback
import threading
import time
from SteeringModule.Steering import Steering
import cv2
import numpy
from OledModule.OLED import OLED

def getLocalIp():
    '''Get the local ip'''
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def cameraAction(steer,command):
    if command=='CamUp':
        steer.Up()
    elif command=='CamDown':
        steer.Down()
    elif command=='CamLeft':
        steer.Left()
    elif command=='CamRight':
        steer.Right()


def motorAction(motor,command):
    '''Set the action of motor according to the command'''
    if command=='DirForward':
        motor.ahead()
    elif command=='DirBack':
        motor.rear()
    elif command=='DirLeft':
        motor.left()
    elif command=='DirRight':
        motor.right()
    elif command=='DirStop':
        motor.stop()

def setCameraAction(command):
    if command=='CamUp' or command=='CamDown' or command=='CamLeft' or command=='CamRight':
        return command
    else:
        return 'CamStop'

            

def main():
    '''The main thread, control the motor'''
    host=getLocalIp()
    print('localhost ip :'+host)
    port=5050

    #Init the tcp socket
    tcpServer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpServer.bind((host,port))
    tcpServer.setblocking(0) #Set unblock mode
    tcpServer.listen(5)

    #Init motor module
    motor=Motor(5,21,22,23,24,13)
    motor.setup()

    #Init steering module
    steer=Steering(14,0,180,15,90,180,36,160)
    steer.setup()
    global cameraActionState #Set a state variable for steering module
    cameraActionState='CamStop'

    #Init oled module
    oled=OLED(16,20,0,0)
    oled.setup()

    oled.writeArea1(host)
    oled.writeArea3('State:')
    oled.writeArea4(' Disconnect')
    while True:
        try:
            time.sleep(0.001)
            (client,addr)=tcpServer.accept()
            print('accept the client!')
            oled.writeArea4(' Connect')
            client.setblocking(0)
            while True:
                time.sleep(0.001)
                cameraAction(steer,cameraActionState)
                try:
                    data=client.recv(1024)
                    data=bytes.decode(data)
                    if(len(data)==0):
                        print('client is closed')
                        oled.writeArea4(' Disconnect')
                        break
                    motorAction(motor,data)
                    cameraActionState=setCameraAction(data)
                except socket.error:
                    continue
                except KeyboardInterrupt,e:
                    raise e
        except socket.error:
            pass
        except KeyboardInterrupt:
            motor.clear()
            steer.cleanup()
            tcpServer.close()
            oled.clear()
        except Exception,e1:
            traceback.print_exc()
            motor.clear()
            steer.cleanup()
            tcpServer.close()
            oled.clear()
main()
