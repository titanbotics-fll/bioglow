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
robot.settings(straight_speed=750, straight_acceleration=580)
robot.use_gyro(True)
robot.straight(-10)
robot.straight(675)
robot.turn(-33)
robot.straight(-150)
robot.straight(40)
left_attachment_motor.run_angle(1100, 90)
robot.straight(-650, then=Stop.COAST)