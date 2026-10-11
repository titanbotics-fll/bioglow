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
left_attachment_motor.run_angle(1110, -185)
robot.straight(750)
left_attachment_motor.run_angle(1110, 60)
robot.straight(-100)
left_attachment_motor.run_angle(1110, -76)
robot.straight(80)
left_attachment_motor.run_angle(1110, 180)
robot.straight(-550)
robot.turn(55)
robot.straight(205)
left_attachment_motor.run_angle(1110, -180)
robot.straight(-300)
robot.straight(250)
robot.straight(-450)
