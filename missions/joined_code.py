from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu, multitask, run_task
from pybricks.tools import wait as _wait
# --- The hub -------------------------------------------------------
# top_side and front_side tell the gyro how the hub sits in the robot.
# This line is for a hub lying flat, USB port facing forward.
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub.display.orientation(Side.BOTTOM)
hub.system.set_stop_button((Button.LEFT, Button.RIGHT))
# --- Driving motors ------------------------------------------------
# One of them must run counterclockwise to go forward. Try it; if the
# robot spins on the spot instead of driving, swap which line has
# Direction.COUNTERCLOCKWISE.
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)

# --- Attachment motors ---------------------------------------------
left_arm = Motor(Port.E)
right_arm = Motor(Port.F)   

# --- Sensors -------------------------------------------------------
center_eye = ColorSensor(Port.A)

# --- The drive base ------------------------------------------------
# Measure these two on YOUR robot. Lesson 10 shows how to fine-tune.
WHEEL_DIAMETER = 43.2     # millimetres, printed on the side of the tyre
AXLE_TRACK = 112        # millimetres between where the wheels touch

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
robot.use_gyro(True)

robot.settings(
    straight_speed=300,           # mm per second
    straight_acceleration=600,    # mm per second, per second
    turn_rate=200,                # degrees per second
    turn_acceleration=500,
)

class RunCancelled(Exception):
    pass

mission_running = False

def check_cancel():
    if mission_running and Button.CENTER in hub.buttons.pressed():
        raise RunCancelled()


def wait(milliseconds):
    """Wait while checking for cancellation."""
    check_cancel()

    while milliseconds > 0:
        interval = min(10, milliseconds)
        _wait(interval)
        milliseconds -= interval
        check_cancel()

def move(device, command, *args, **kwargs):
    """Complete a movement while checking for cancellation."""
    check_cancel()

    kwargs["wait"] = False
    getattr(device, command)(*args, **kwargs)

    while not device.done():
        wait(10)

    check_cancel()

async def _watch_cancel():
    """Monitor Center while an awaitable hardware command is running."""
    while True:
        check_cancel()
        await _wait(10)


async def _run_action(device, command, args, kwargs):
    await getattr(device, command)(*args, **kwargs)


def cancellable_action(device, command, *args, **kwargs):
    """Run commands without a wait=False option, including arm homing."""
    check_cancel()
    run_task(multitask(
        _run_action(device, command, args, kwargs),
        _watch_cancel(),
        race=True,
    ))
    check_cancel()


def stop_all():
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    left_arm.brake()
    right_arm.brake()


def build_arms(
    left_direction=Direction.CLOCKWISE,
    right_direction=Direction.CLOCKWISE,
):
    """Rebuild attachment motors without physically homing them."""
    global left_arm, right_arm

    left_arm.stop()
    right_arm.stop()

    left_arm.close()
    right_arm.close()

    left_arm = Motor(Port.E, left_direction)
    right_arm = Motor(Port.F, right_direction)



def square_on_wall(power=35, settle_ms=900):
    """Reverse against the alignment wall."""
    robot.stop()

    left_motor.dc(-power)
    right_motor.dc(-power)

    wait(settle_ms)

    left_motor.brake()
    right_motor.brake()

    wait(100)
    robot.reset()


def get_ready(
    left_direction=Direction.CLOCKWISE,
    right_direction=Direction.CLOCKWISE,
    align_on_wall=True,
):
    """Prepare motors, gyro, and starting alignment."""
    robot.stop()
    build_arms(left_direction, right_direction)

    hub.display.char("-")

    # Manually position attachments before starting.
    # No automatic attachment homing is performed.

    while not hub.imu.ready():
        wait(50)

    # Start near the alignment wall when enabled.
    if align_on_wall:
        square_on_wall()
    robot.reset()
    robot.reset(distance=0, angle=0)
    hub.display.char("G")
    cancellable_action(hub.speaker, "beep", 1000, 100)


def run_1(): 
    check_cancel()
    get_ready()
    check_cancel()
    robot.settings(straight_speed=300, straight_acceleration=600, turn_acceleration=500, turn_rate=750)
    check_cancel()
    move(robot, "straight", -10)
    check_cancel()
    move(robot, "straight", 380)
    check_cancel()
    move(robot, "straight", -380, then=Stop.COAST)
    check_cancel()
    
def run_2(): 
    check_cancel()
    get_ready(align_on_wall=False)
    check_cancel()
    robot.settings(straight_speed=750, straight_acceleration=300)
    check_cancel()
    move(robot, "straight", 790)
    check_cancel()
    move(robot, "turn", 3.9999985788477587738778727865748569999999999999999999999990)
    check_cancel()
    move(robot, "straight", 73)
    check_cancel()
    robot.settings(straight_speed=750, straight_acceleration=700)
    check_cancel()
    move(robot, "turn", -3.999998578847758773877872786574856999999999999999999999999)
    check_cancel()
    move(robot, "straight", -870)
    check_cancel()
    cancellable_action(left_arm, "run_until_stalled", -300, then=Stop.HOLD, duty_limit=40)
def run_3():  
    check_cancel()
    get_ready()
    check_cancel()
    robot.settings(straight_speed=650, straight_acceleration=400)
    check_cancel()
    cancellable_action(left_arm, "run_until_stalled", -300, then=Stop.HOLD, duty_limit=29)
    check_cancel()
    left_arm.reset_angle(0)
    check_cancel()
    cancellable_action(right_arm, "run_until_stalled", 300, then=Stop.HOLD, duty_limit=29)
    check_cancel()
    right_arm.reset_angle(0)
    check_cancel()
    move(robot, "straight", -10)
    check_cancel()
    move(right_arm, "run_angle", 1110, -240)
    check_cancel()
    move(robot, "straight", 770)
    check_cancel()
    move(right_arm, "run_angle", 1110, 60)
    check_cancel()
    move(robot, "straight", -100)
    check_cancel()
    move(right_arm, "run_angle", 1110, -85)
    check_cancel()
    robot.settings(turn_rate=120, turn_acceleration=400)
    check_cancel()
    move(robot, "turn", 6)
    check_cancel()
    move(robot, "straight", 85)
    check_cancel()
    move(right_arm, "run_angle", 1110, 180)
    check_cancel()
    move(robot, "turn", -12)
    check_cancel()
    move(robot, "straight", -590)
    check_cancel()
    robot.settings(turn_rate=750, turn_acceleration=400)
    check_cancel()
    move(robot, "turn",50)
    check_cancel()
    move(robot, "straight", 200)
    check_cancel()
    move(right_arm, "run_angle", 1110, -150)
    check_cancel()
    move(robot, "straight", -300)
    check_cancel
    move(right_arm, "run_angle", 1110, 150)
    check_cancel()
    move(robot, "straight", 250)
    check_cancel()
    move(robot, "straight", -450)
    check_cancel()
def run_4():
    check_cancel()
    get_ready(
        align_on_wall=True,
    )
    robot.use_gyro(True)
    robot.settings(straight_speed=400, straight_acceleration=500)
    cancellable_action(right_arm, "run_until_stalled", 300, duty_limit=40)
    robot.arc(radius=695, angle=60)
    move(robot, "straight", 20)
    move(robot, "turn", -57)
    move(robot, "straight", 70)
    move(right_arm, "run_angle", 1000, -130)
    move(robot, "straight", -45)
    move(right_arm, "run_angle", 1000, 130)
    move(robot, "straight", -40)
    move(robot, "turn", 50)
    move(right_arm, "run_angle", 1110, -170)
    move(robot, "straight", 300)
    check_cancel()

    # Remaining driving route.
    move(robot, "turn", 30)
    check_cancel()
    move(robot, "straight", 240)
    check_cancel()
    move(robot, "turn", 20)
    check_cancel()
    move(robot, "straight",130)
    move(robot, "turn", -30)

    robot.settings(
        straight_speed=100,
        straight_acceleration=100,
    )
    check_cancel()
    move(robot, "straight", 200)
    #move(robot, "arc", radius=-315, angle=35)
    check_cancel()

    robot.settings(
        straight_speed=400,
        straight_acceleration=500,
    )
    check_cancel()

    move(robot, "straight", -80)
    check_cancel()
    print("Before - angle:", robot.angle(), "heading:", hub.imu.heading())
    move(robot, "turn", 126, absolute=True)  
    print("After - angle:", robot.angle(), "heading:", hub.imu.heading())
    check_cancel()
    move(robot, "straight", 250)
    check_cancel()
    move(robot, "straight", -100)
    check_cancel()
    move(robot, "turn", -10)
    check_cancel()
    move(robot, "straight", 250)
    check_cancel()
    move(robot, "turn", 30)
    check_cancel()
    move(robot, "straight", 530)
    check_cancel()

    robot.stop()
    check_cancel()
    left_arm.stop()
    right_arm.stop()
    check_cancel()

def run_5():#____
    check_cancel()
    get_ready(align_on_wall=False)
    check_cancel()
    move(robot, "straight", -10)
    check_cancel()
    move(robot, "straight", 675)
    check_cancel()
    move(robot, "turn", -34)
    check_cancel()
    robot.settings(straight_speed=500, straight_acceleration=580, turn_rate=750, turn_acceleration=400)
    check_cancel()
    move(robot, "straight", -100)
    check_cancel()
    move(robot, "straight", 40)
    check_cancel()
    move(right_arm, "run_angle", 1100, 180)
    check_cancel()
    robot.settings(straight_speed=750, straight_acceleration=750, turn_rate=750, turn_acceleration=750)
    check_cancel()
    move(robot, "turn", 20)
    check_cancel()
    move(robot, "straight", -638)
    check_cancel()
def run_6():#____
    cancellable_action(left_arm, "run_until_stalled", 300, then=Stop.HOLD, duty_limit=29)
    check_cancel()
    get_ready(align_on_wall=False)
    robot.settings(straight_speed=600, straight_acceleration=300, turn_rate=750, turn_acceleration=750)
    check_cancel()
    move(robot, "straight", 200)
    check_cancel()
    move(robot, "turn", -2.567464546623237458623765)
    check_cancel()
    move(robot, "straight", 105)
    check_cancel()
    move(left_arm, "run_angle", 250, -110)
    check_cancel()
    wait(250)
    check_cancel()
    move(left_arm, "run_angle", 500, 50)
    check_cancel()
    move(robot, "straight", -45)
    check_cancel()
    move(left_arm, "run_angle", 1100, -39)
    check_cancel()
    move(robot, "turn", 10.99999999999999)
    check_cancel()
    move(robot, "straight", 7)
    check_cancel()
    move(left_arm, "run_angle", 750, 94)
    check_cancel()
    move(robot, "turn", -10)
    check_cancel()
    move(robot, "straight", -350, then=Stop.HOLD)
    check_cancel()

def run_7():#____    
    check_cancel()
    get_ready()
    check_cancel()
    robot.settings(straight_speed=600, straight_acceleration=500, turn_rate=750, turn_acceleration=500)
    check_cancel()
    move(robot, "straight", 695)
    check_cancel()
    move(robot, "turn", 50)
    check_cancel()
    move(robot, "straight", 50)
    check_cancel()
    move(right_arm, "run_angle", 1110, 60)
    check_cancel()
    move(robot, "turn", 18)
    check_cancel()
    move(robot, "straight", -20)
    check_cancel()
    move(robot, "turn", -20)
    check_cancel()
    move(robot, "straight", 100)
    check_cancel()
    move(left_arm, "run_angle", 400, 290)
    check_cancel()
    wait(119)
    check_cancel()
    move(left_arm, "run_angle", 1100, -280)
    check_cancel()
    move(robot, "straight", -200)
    check_cancel()
    move(robot, "turn", -65)
    check_cancel()
    move(robot, "straight", -650)
    check_cancel()

def run_8():#____    
    get_ready(align_on_wall=False)
    robot.settings(straight_speed=750, straight_acceleration=750, turn_rate=750, turn_acceleration=500)
    move(right_arm, "run_angle", 1000, 250)
    move(robot, "straight", 850)
    #drive_base.turn(-20)
    move(robot, "turn", -20)
    move(robot, "straight", 350)
    #drive_base.turn(45)
    move(robot, "turn", 45)
    move(robot, "straight", 300)
    #drive_base.turn(22)
    move(robot, "turn", 30)
    move(robot, "straight", 500)
    move(right_arm, "run_angle", 1000, -250)
    move(robot, "straight", -80)
    move(robot, "turn", 50)
    #drive_base.turn(50)
    move(robot, "straight", -700)
def wait_for_release():
    """Require a fresh button press for each menu action."""
    while hub.buttons.pressed():
        wait(10)
    wait(50)
    
def menu():
    global mission_running

    runs = (
        run_1,
        run_2,
        run_3,
        run_4,
        run_5,
        run_6,
        run_7,
        run_8,
    )

    

    selected = 1

    hub.system.set_stop_button((Button.LEFT, Button.RIGHT))
    wait_for_release()

    while True:
        hub.display.char(str(selected))
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed and Button.RIGHT in pressed:
            # The configured stop combination exits the program.
            wait(10)

        elif Button.LEFT in pressed:
            selected = 1 if selected == 8 else selected + 1
            hub.display.char(str(selected))
            wait_for_release()

        elif Button.RIGHT in pressed:
            selected = 8 if selected == 1 else selected - 1
            hub.display.char(str(selected))
            wait_for_release()

        elif Button.CENTER in pressed:
            # Release the start press before enabling cancellation.
            wait_for_release()
            mission_running = True

            try:
                runs[selected - 1]()

            except RunCancelled:
                pass

            finally:
                mission_running = False
                stop_all()

            hub.display.char(str(selected))
            wait_for_release()
        wait(20)
menu()
