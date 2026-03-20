import time
import board
import digitalio
#set BLINKA_FT232H=1


relay_ch1 = digitalio.DigitalInOut(board.C0)
relay_ch2 = digitalio.DigitalInOut(board.C1)
relay_ch1.direction = digitalio.Direction.OUTPUT
relay_ch2.direction = digitalio.Direction.OUTPUT

relay_ch1.value = True
time.sleep(5)
relay_ch1.value = False
time.sleep(2)
relay_ch2.value = True
time.sleep(5)
relay_ch2.value = False
time.sleep(2)