from MotorModule.Motor import Motor
import time

motor=Motor(5,21,22,23,24,13)
motor.setup()
motor.ahead()
time.sleep(1)
motor.left()
time.sleep(3)
motor.right()
time.sleep(3)
motor.rear()
time.sleep(1)
motor.stop()
motor.clear()



