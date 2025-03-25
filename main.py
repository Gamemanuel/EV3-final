from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.media.ev3dev import SoundFile
from random import randint

# Initialize the EV3 brick.
ev3 = EV3Brick()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# constants 
WHEEL_DIAMETER = 45 # this is in mm
AXLE_TRACK = 150 # this is in mm

# DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
# left_motor (Motor) – The motor that drives the left wheel.
# right_motor (Motor) – The motor that drives the right wheel.
# wheel_diameter (dimension: mm) – Diameter of the wheels.
# axle_track (dimension: mm) – Distance between the points where both wheels touch the ground.

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

# draws a shape based on the number of sides 1 and 2 will not work
def shapes(numberOfSides, lengthOfSides, speed):
    if numberOfSides < 3:
        pass
    else:
        angle: float = 180 - ((180 * ((numberOfSides) - 2))/ 2)
        for _ in range(numberOfSides):
            move(lengthOfSides, 0, speed)
            move(0, angle, speed)
        

def move(forward, turn, speed):
    robot.straight(forward * speed)
    robot.turn(turn * speed)
    robot.stop()
