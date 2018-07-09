from SteeringModule.Steering import Steering
import time
steer=Steering(14,0,180,15,90,180,36,160)
steer.setup()
time.sleep(2)
for i in range(0,900):
    steer.Up()

for i in range(0,900):
    steer.Down()

for i in range(0,900):
    steer.Left()

for i in range(0,900):
    steer.Right()

steer.specify(80,120)
steer.specify(20,100)
steer.specify(170,180)

steer.cleanup()
