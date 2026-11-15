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
robot.settings(straight_speed=750, straight_acceleration=750, turn_rate=750, turn_acceleration=750)
robot.use_gyro(True)
right_attachment_motor.run_until_stalled(-300, then=Stop.HOLD, duty_limit=29)
right_attachment_motor.reset_angle(0)
robot.straight(-10)
robot.arc(-488, 51)
right_attachment_motor.run_angle(1110, 210)
robot.arc(-488, -51, then=Stop.COAST)
