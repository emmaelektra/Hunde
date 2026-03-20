import time
import board
import digitalio

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
    time.sleep(2)  # Adjust the delay as needed

relay1.value = True
relay2.value = True
time.sleep(2)

# Switch relay 1 on and off
toggle_relay(relay1, False)
print("Relay 1 ON")
toggle_relay(relay1, True)
print("Relay 1 OFF")

# Switch relay 2 on and off
toggle_relay(relay2, False)
print("Relay 2 ON")
toggle_relay(relay2, True)
print("Relay 2 OFF")
