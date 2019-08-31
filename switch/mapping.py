import math

STATE_OUT_OF_SYNC   = 0
STATE_SYNC_START    = 1
STATE_SYNC_1        = 2
STATE_SYNC_2        = 3
STATE_SYNC_OK       = 4

# Actual Switch DPAD Values
A_DPAD_CENTER    = 0x08
A_DPAD_U         = 0x00
A_DPAD_U_R       = 0x01
A_DPAD_R         = 0x02
A_DPAD_D_R       = 0x03
A_DPAD_D         = 0x04
A_DPAD_D_L       = 0x05
A_DPAD_L         = 0x06
A_DPAD_U_L       = 0x07

# Enum DIR Values
DIR_CENTER    = 0x00
DIR_U         = 0x01
DIR_R         = 0x02
DIR_D         = 0x04
DIR_L         = 0x08
DIR_U_R       = DIR_U + DIR_R
DIR_D_R       = DIR_D + DIR_R
DIR_U_L       = DIR_U + DIR_L
DIR_D_L       = DIR_D + DIR_L

BTN_NONE         = 0x0000000000000000
BTN_Y            = 0x0000000000000001
BTN_B            = 0x0000000000000002
BTN_A            = 0x0000000000000004
BTN_X            = 0x0000000000000008
BTN_L            = 0x0000000000000010
BTN_R            = 0x0000000000000020
BTN_ZL           = 0x0000000000000040
BTN_ZR           = 0x0000000000000080
BTN_MINUS        = 0x0000000000000100
BTN_PLUS         = 0x0000000000000200
BTN_LCLICK       = 0x0000000000000400
BTN_RCLICK       = 0x0000000000000800
BTN_HOME         = 0x0000000000001000
BTN_CAPTURE      = 0x0000000000002000

DPAD_CENTER      = 0x0000000000000000
DPAD_U           = 0x0000000000010000
DPAD_R           = 0x0000000000020000
DPAD_D           = 0x0000000000040000
DPAD_L           = 0x0000000000080000
DPAD_U_R         = DPAD_U + DPAD_R
DPAD_D_R         = DPAD_D + DPAD_R
DPAD_U_L         = DPAD_U + DPAD_L
DPAD_D_L         = DPAD_D + DPAD_L

LSTICK_CENTER    = 0x0000000000000000
LSTICK_R         = 0x00000000FF000000 #   0 (000)
LSTICK_U_R       = 0x0000002DFF000000 #  45 (02D)
LSTICK_U         = 0x0000005AFF000000 #  90 (05A)
LSTICK_U_L       = 0x00000087FF000000 # 135 (087)
LSTICK_L         = 0x000000B4FF000000 # 180 (0B4)
LSTICK_D_L       = 0x000000E1FF000000 # 225 (0E1)
LSTICK_D         = 0x0000010EFF000000 # 270 (10E)
LSTICK_D_R       = 0x0000013BFF000000 # 315 (13B)

RSTICK_CENTER    = 0x0000000000000000
RSTICK_R         = 0x000FF00000000000 #   0 (000)
RSTICK_U_R       = 0x02DFF00000000000 #  45 (02D)
RSTICK_U         = 0x05AFF00000000000 #  90 (05A)
RSTICK_U_L       = 0x087FF00000000000 # 135 (087)
RSTICK_L         = 0x0B4FF00000000000 # 180 (0B4)
RSTICK_D_L       = 0x0E1FF00000000000 # 225 (0E1)
RSTICK_D         = 0x10EFF00000000000 # 270 (10E)
RSTICK_D_R       = 0x13BFF00000000000 # 315 (13B)

NO_INPUT       = BTN_NONE + DPAD_CENTER + LSTICK_CENTER + RSTICK_CENTER

# Commands to send to MCU
COMMAND_NOP        = 0x00
COMMAND_SYNC_1     = 0x33
COMMAND_SYNC_2     = 0xCC
COMMAND_SYNC_START = 0xFF

# Responses from MCU
RESP_USB_ACK       = 0x90
RESP_UPDATE_ACK    = 0x91
RESP_UPDATE_NACK   = 0x92
RESP_SYNC_START    = 0xFF
RESP_SYNC_1        = 0xCC
RESP_SYNC_OK       = 0x33

# axis conversion constants
R_AXIS_Y_CONVER = 24425 / 31075
R_AXIS_X_CONVER = 31500 / 23500
L_AXIS_X_CONVER = 30100 / 24900
L_AXIS_Y_CONVER = 24950 / 33850


def map_button(event):
    if event.type in [1,2]:
        if event.code == 304:
            return BTN_B
        if event.code == 305:
            return BTN_A
        if event.code == 306:
            return BTN_Y
        if event.code == 307:
            return BTN_X
        if event.code == 308:
            return BTN_L
        if event.code == 309:
            return BTN_R
        if event.code == 310:
            return BTN_ZL
        if event.code == 311:
            return BTN_ZR
        if event.code == 312:
            return BTN_MINUS
        if event.code == 313:
            return BTN_PLUS
        if event.code == 314:
            return BTN_LCLICK
        if event.code == 315:
            return BTN_RCLICK
        if event.code == 316:
            return BTN_HOME
        if event.code == 317:
            return BTN_CAPTURE
    else:
        return BTN_NONE

def map_dpad(event):
    if event.type == 3:
        if event.code == 16:
            if event.val == -1:
                return DPAD_L
            if event.val == 1:
                return DPAD_R
            else:
                return DPAD_CENTER

        if event.code == 17:
            if event.val == -1:
                return DPAD_U
            if event.val == 1:
                return DPAD_D
            else:
                return DPAD_CENTER
    else:
        return BTN_NONE

def get_lx_axis(event):
    if event.code == 0:
        return event.val
    else:
        return LSTICK_CENTER

def get_ly_axis(event):
    if event.code == 1:
        return event.val
    else:
        return LSTICK_CENTER

def get_rx_axis(event):
    if event.code == 3:
        return event.val
    else:
        return RSTICK_CENTER

def get_ry_axis(event):
    if event.code == 4:
        return event.val
    else:
        return RSTICK_CENTER

def map_l_axis(x, y):
    x = (_x / 24900) - L_AXIS_X_CONVER
    y = -(_y / 33850) + L_AXIS_Y_CONVER

    intensity = math.hypot(x, y)
    angle = (math.atan2(y, x) * 180 / math.pi) + 360

    return intensity, angle

def map_r_axis(_x, _y):
    x = (_x / 23500) - R_AXIS_X_CONVER
    y = -(_y / 31075) + R_AXIS_Y_CONVER

    intensity = math.hypot(x, y)
    angle = (math.atan2(y, x) * 180 / math.pi) + 360

    return intensity, angle
