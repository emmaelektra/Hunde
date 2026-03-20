import time
from pyftdi.gpio import GpioController

# Initialize FT232H GPIO controller
gpio = GpioController()

# Open the first FT232H device
gpio.configure('ftdi://ftdi:232h/1', direction=0x10)  # 0x10 configures D4 as output

# Define pin mappings
CONTROL_PIN = 0x10  # D4 pin (TXD)

try:
    # Set CONTROL_PIN (D4) to LOW initially
    print("Setting CONTROL_PIN LOW")
    gpio.write(0)  # This sets D4 to LOW (0V)

    time.sleep(5)  # Wait for 2 seconds

    # Set CONTROL_PIN (D4) to HIGH to trigger the Arduino
    print("Setting CONTROL_PIN HIGH")
    gpio.write(CONTROL_PIN)  # This sets D4 to HIGH (3.3V)

    time.sleep(10)  # Keep it high for 5 seconds

    # Set CONTROL_PIN (D4) to LOW again
    print("Setting CONTROL_PIN LOW")
    gpio.write(0)  # This sets D4 to LOW (0V)

    time.sleep(5)

finally:
    # gpio.close()
    pass
