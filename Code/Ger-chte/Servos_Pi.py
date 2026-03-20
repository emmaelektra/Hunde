# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
import numpy as np
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=8)

angles = np.linspace(0,180,100)
anglesback = np.linspace(180,0,100)
servoNo = [0,1,2]
for no in servoNo:
	for a in angles:
		kit.servo[no].angle = a
		time.sleep(0.02)
	time.sleep(2)
	for a in anglesback:
		kit.servo[no].angle = a
		time.sleep(0.02)
