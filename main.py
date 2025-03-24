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

# settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
# straight_speed (speed: mm/s) – Speed of the robot during straight().
# straight_acceleration (linear acceleration: mm/s/s) – Acceleration and deceleration of the robot at the start and end of straight().
# turn_rate (rotational speed: deg/s) – Turn rate of the robot during turn().
# turn_acceleration (rotational acceleration: deg/s/s) – Angular acceleration and deceleration of the robot at the start and end of turn().

robot.settings(1,1,1,1) # sets the onfiguration of the motor speeds

