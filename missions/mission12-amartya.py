from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor=Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor=Motor(Port.D, Direction.CLOCKWISE)
right_attachment_motor=Motor(Port.F)
left_attachment_motor=Motor(Port.E)
robot=DriveBase(left_motor, right_motor, 43.2,81)
robot.settings(straight_speed=750, straight_acceleration=580)
robot.use_gyro(True)
robot.straight(-10)
robot.straight(670)
robot.turn(70)
robot.straight(10)
right_attachment_motor.run_angle(1110, 90)
robot.straight(-10)
robot.turn(-30)
robot.straight(-50)
robot.turn(-40)
robot.straight(-200)
robot.arc(900, -100)

