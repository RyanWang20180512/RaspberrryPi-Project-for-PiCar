from SteeringModule.Rotation import Rotation

class Steering:
    def __init__(self,channelH,min_thetaH,max_thetaH,
            channelV,min_thetaV,max_thetaV,init_thetaH=0,init_thetaV=0):
        self.hRotation=Rotation(channelH,min_thetaH,max_thetaH,init_thetaH)
        self.vRotation=Rotation(channelV,min_thetaV,max_thetaV,init_thetaV)

    def setup(self):
        self.hRotation.setup()
        self.vRotation.setup()

    def Up(self):
        self.vRotation.positiveRotation()

    def Down(self):
        self.vRotation.reverseRotation()

    def Left(self):
        self.hRotation.positiveRotation()

    def Right(self):
        self.hRotation.reverseRotation()

    def specify(self,thetaH,thetaV):
        self.hRotation.specifyRotation(thetaH)
        self.vRotation.specifyRotation(thetaV)

    def cleanup(self):
        self.hRotation.cleanup()
        self.vRotation.cleanup()
