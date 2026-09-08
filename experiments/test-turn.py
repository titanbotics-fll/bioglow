from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor=Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor=Motor(Port.B, Direction.CLOCKWISE)
right_attachment_motor=Motor(Port.F)
left_attachment_motor=Motor(Port.E)
robot=DriveBase(left_motor, right_motor, 43.2,81)
robot.settings(straight_speed=750, straight_acceleration=580)
robot.use_gyro(True)
robot.straight(710)
robot.straight(-45)
robot.settings(straight_speed=750, straight_acceleration=750)
robot.turn(-35)
robot.straight(-10)
robot.turn(-32)
robot.straight(-10)

