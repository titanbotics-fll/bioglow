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
robot.settings(straight_speed=750, straight_acceleration=750, turn_rate=750, turn_acceleration=500)
robot.use_gyro(True)
robot.straight(300)
right_attachment_motor.run_angle(250, -70)
wait(250)
right_attachment_motor.run_angle(500, 20)
robot.straight(-40)
robot.turn(15)
robot.straight(10)
right_attachment_motor.run_angle(734, 60)
robot.turn(-10)
robot.straight(-400, then=Stop.COAST)
