from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor=Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor=Motor(Port.D, Direction.CLOCKWISE)
right_attachment_motor=Motor(Port.E)
left_attachment_motor=Motor(Port.F)
robot=DriveBase(left_motor, right_motor, 43.2,81)
robot.settings(straight_speed=700, straight_acceleration=520)
robot.use_gyro(True)
robot.straight(-10)
robot.straight(380)
robot.straight(-300)
robot.turn(7.9)
robot.straight(265)
robot.straight(-385, then=Stop.COAST)
