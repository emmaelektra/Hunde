import time
import digitalio
import board

# set BLINKA_FT232H=1

# Initialize the motors using digitalio on available GPIO pins

motor_1 = digitalio.DigitalInOut(board.D4)
motor_1.direction = digitalio.Direction.OUTPUT
motor_1.value = False  # Set MOTOR_1_PIN to LOW

motor_2 = digitalio.DigitalInOut(board.D5)
motor_2.direction = digitalio.Direction.OUTPUT
motor_2.value = False  # Set MOTOR_2_PIN to LOW

motor_3 = digitalio.DigitalInOut(board.D6)
motor_3.direction = digitalio.Direction.OUTPUT
motor_3.value = False  # Set MOTOR_3_PIN to LOW

time.sleep(2)  # Brief delay to allow pins to stabilize

try:
    # Trigger Motor 1
    print("Triggering Motor 1")
    motor_1.value = True  # Set MOTOR_1_PIN to HIGH
    time.sleep(0.5)  # Keep it high for 0.5 seconds

    # Set Motor 1 Pin to LOW
    motor_1.value = False  # Set MOTOR_1_PIN to LOW
    time.sleep(5)  # Wait for 5 seconds before triggering the next motor

    # Trigger Motor 2
    print("Triggering Motor 2")
    motor_2.value = True  # Set MOTOR_2_PIN to HIGH
    time.sleep(0.5)  # Keep it high for 0.5 seconds

    # Set Motor 2 Pin to LOW
    motor_2.value = False  # Set MOTOR_2_PIN to LOW
    time.sleep(5)  # Wait for 5 seconds before triggering the next motor

    # Trigger Motor 3
    print("Triggering Motor 3")
    motor_3.value = True  # Set MOTOR_3_PIN to HIGH
    time.sleep(0.5)  # Keep it high for 0.5 seconds

    # Set Motor 3 Pin to LOW
    motor_3.value = False  # Set MOTOR_3_PIN to LOW
    time.sleep(5)  # Wait for 5 seconds before finishing

finally:
    # Optional cleanup, if needed
    motor_1.value = False
    motor_2.value = False
    motor_3.value = False

print("Motors have been triggered.")
