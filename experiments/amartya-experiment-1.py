from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
motor = Motor(Port.A, Direction.CLOCKWISE)
motor_2 = Motor(Port.B, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(motor_2, motor, 40, 65)


# The main program starts here.
drive_base.use_gyro(True)
drive_base.settings(straight_speed=200)
drive_base.straight(600)
drive_base.turn(90)
drive_base.straight(600)
drive_base.turn(90)
drive_base.straight(600)
