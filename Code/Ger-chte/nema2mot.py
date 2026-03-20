import time
from pyftdi.gpio import GpioController

# Initialize FT232H GPIO controller
gpio = GpioController()

# Open the first FT232H device and configure the pins
gpio.configure('ftdi://ftdi:232h/1', direction=0xF8)  # 0x30 configures D4 and D5 as outputs

# Define pin mappings
MOTOR_1_PIN = 0x01  # D4 pin for Motor 1
MOTOR_2_PIN = 0x02  # D5 pin for Motor 2
MOTOR_3_PIN = 0x04  # D3

try:
    # Set all control pins to LOW initially, multiple times to ensure state
    #for _ in range(3):
    # gpio.write(0)  # Set all pins to LOW
    # time.sleep(2)  # Brief delay to allow pins to stabilize

    #time.sleep(1)  # Wait briefly to ensure the pins are stable at LOW

    # Trigger Motor 1
    print("Triggering Motor 1")
    gpio.write(MOTOR_1_PIN)  # Set MOTOR_1_PIN to HIGH
    time.sleep(3)  # Keep it high for 2 seconds (adjust as needed)

    # Set Motor 1 Pin to LOW
    gpio.write(0)  # Set MOTOR_1_PIN to LOW
    time.sleep(1)  # Wait for 1 second before triggering the next motor

    # Trigger Motor 2
    print("Triggering Motor 2")
    gpio.write(MOTOR_2_PIN)  # Set MOTOR_2_PIN to HIGH
    time.sleep(3)  # Keep it high for 2 seconds (adjust as needed)

    # Set Motor 2 Pin to LOW
    gpio.write(0)  # Set MOTOR_2_PIN to LOW
    time.sleep(1)  # Wait for 1 second before finishing

    # Trigger Motor 3
    print("Triggering Motor 3")
    gpio.write(MOTOR_3_PIN)  # Set MOTOR_3_PIN to HIGH
    time.sleep(3)  # Keep it high for 2 seconds (adjust as needed)

    # Set Motor 3 Pin to LOW
    gpio.write(0)  # Set MOTOR_3_PIN to LOW
    time.sleep(1)  # Wait for 1 second before finishing

finally:
    # Keep the last state or close the GPIO
    # gpio.close()  # Comment this out to maintain the last state if necessary
    pass

print("Motors have been triggered.")
