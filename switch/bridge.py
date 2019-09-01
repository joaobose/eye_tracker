#import evdev
from evdev import InputDevice, categorize, ecodes
from mapping import *
from client import *
import time

gamepad = InputDevice('/dev/input/event4')
port = '/dev/ttyUSB0'

#prints out device info at start
print(gamepad)

while not connect(port):
    print('Retrying')
    time.sleep(0.01)

print('Connected')
rx = R_AXIS_X_CENTER
ry = R_AXIS_Y_CENTER
lx = L_AXIS_X_CENTER
ly = L_AXIS_Y_CENTER

last_dpad_h = 0
last_dpad_v = 0

buffer = BTN_NONE
while True:
    buffer = buffer & 0xFFFFF
    while True:
        time.sleep(0.001)
        event = gamepad.read_one()

        if event == None:
            break
            
        button = map_button(event)
        dpad = map_dpad(event)

        # button release
        if event.value == 0:
            buffer -= button
        # button press
        elif event.value == 1:
            buffer += button

        # dpad release
        if event.value == 0:
            # horizontal dpad
            if event.code == 16:
                buffer -= last_dpad_h
            # vertical dpad
            elif event.code == 17:
                buffer -= last_dpad_v
        # dpad press
        else:
            # horizontal dpad
            if event.code == 16:
                last_dpad_h = dpad
            # vertical dpad
            elif event.code == 17:
                last_dpad_v = dpad
            buffer += dpad

        rx = get_rx_axis(event,rx)
        ry = get_ry_axis(event,ry)
        lx = get_lx_axis(event,lx)
        ly = get_ly_axis(event,ly)

    intensity_r, angle_r = map_r_axis(rx,ry)
    intensity_l, angle_l = map_l_axis(lx,ly)
    cmd_r = rstick_angle(int(angle_r), int(intensity_r * 255))
    cmd_l = lstick_angle(int(angle_l), int(intensity_l * 255))

    buffer += cmd_l + cmd_r
    send_cmd(buffer)


ser.close()
