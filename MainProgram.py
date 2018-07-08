import socket
from enum import IntEnum
from MotorModule.Motor import Motor
import traceback

def getLocalIp():
    '''Get the local ip'''
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

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
    else:
        motor.stop()

def main():
    '''The main thread, control the motor and camera'''
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

    while True:
        try:
            (client,addr)=tcpServer.accept()
            print('accept the client!')
            while True:
                try:
                    data=client.recv(1024)
                    data=bytes.decode(data)
                    if(len(data)==0):
                        print('client is closed')
                        break
                    motorAction(motor,data)
                except socket.error:
                    pass
        except socket.error:
            pass
        except Exception,e:
            traceback.print_exc()
            motor.clear()
            tcpServer.close()
    motor.clear()
    tcpServer.close()

main()
