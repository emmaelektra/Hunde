import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit

# Initialize I2C bus
i2c_bus = busio.I2C(SCL, SDA)

# Initialize PCA9685 controller
pca = PCA9685(i2c_bus)
pca.frequency = 50  # Set the PWM frequency (you may need to adjust this based on your servo specifications)

# Initialize ServoKit
kit = ServoKit(channels=16)

# Define servo channels on PCA9685
servo_channels = [0, 1, 2, 3]  # Use the channels connected to your servo motors

# Function to set servo angle
def set_servo_angle(channel, angle):
    kit.servo[servo_channels[channel]].angle = angle  # Set servo angle directly

# Control servo motors
for channel in servo_channels:
    set_servo_angle(channel, 0)  # Set initial angle (0 degrees)

time.sleep(2)  # Wait for initialization

try:
    # Move servo motors
    for channel in servo_channels:
        set_servo_angle(channel, 180)  # Set angle to 90 degrees
        time.sleep(1)

        set_servo_angle(channel, 0)  # Set angle back to 0 degrees
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Clean up
    for channel in servo_channels:
        set_servo_angle(channel, 0)  # Set all servo angles back to 0 degrees

    pca.deinit()
