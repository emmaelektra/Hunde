import time
import board
import digitalio

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

# Define relay pins
relay1_pin = board.C0  # Assigning to pin C0
relay2_pin = board.C1  # Assigning to pin C1

# Set up relay pins as digital outputs
relay1 = digitalio.DigitalInOut(relay1_pin)
relay1.direction = digitalio.Direction.OUTPUT

relay2 = digitalio.DigitalInOut(relay2_pin)
relay2.direction = digitalio.Direction.OUTPUT

# Function to toggle relay state
def toggle_relay(relay, state):
    relay.value = state
    time.sleep(5)  # Adjust the delay as needed

relay1.value = True
relay2.value = True

# Control servo motors
for channel in servo_channels:
    set_servo_angle(channel, 0)  # Set initial angle (0 degrees)

time.sleep(2)  # Wait for initialization

set_servo_angle(0, 180)  # Set angle to 90 degrees
time.sleep(1)
# Switch relay 1 on
toggle_relay(relay1, False)
print("Relay 1 ON")

set_servo_angle(0, 0)  # Set angle back to 0 degrees
time.sleep(1)
# Switch relay 2 off
toggle_relay(relay1, True)
print("Relay 1 OFF")

set_servo_angle(1, 180)  # Set angle to 90 degrees
time.sleep(1)
# Switch relay 1 on
toggle_relay(relay2, False)
print("Relay 1 ON")

set_servo_angle(1, 0)  # Set angle back to 0 degrees
time.sleep(1)
# Switch relay 2 off
toggle_relay(relay2, True)
print("Relay 1 OFF")

# Clean up
for channel in servo_channels:
    set_servo_angle(channel, 0)  # Set all servo angles back to 0 degrees

    pca.deinit()
