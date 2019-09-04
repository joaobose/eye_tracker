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


class SwitchControllerMapping():
    '''
        Botones:
            Todos son type 1

            Release: val 0
            Press: val 1
            Hold: val 2

            B: code 304
            A: code 305
            Y: code 306
            X: code 307

            L: 308
            R: 309
            ZL: 310
            ZR: 311

            -: code 312
            +: code 313
            Bump left: code 314
            Bump right: code 315
            home: code 316
            capture: code 317


        Evento nada:
            code 00, type 00, val 00

        Evento random:
            code 04, type 04, val random ???

        joystick y flechas son type3

        Joystick Izquierdo:
        	code 0 horizontal:
        		minimo: 5200 izquierdo
        		max:	55000 derecho
        	code 1 vertical:
        		minimo: 8600 arriba
        		max: 59000 abajo

        Joystick derecho:
        	code 3 horizontal:
        		minimo: 7000 izquierdo
        		max: 55000 derecha
        	code 4 vertical
        		minimo: 6500 arriba
        		max: 57000 abajo

        Flechas:
            val 0 centro para todos
            izquierda code 16 val -1
            derecho code 16 val 1
            arriba code 17 val -1
            abajo code 17 val 1
    '''

    # axis conversion constants
    R_AXIS_Y_CONVER = 31075 / 24425
    R_AXIS_X_CONVER = 31500 / 23500
    L_AXIS_X_CONVER = 30100 / 24900
    L_AXIS_Y_CONVER = 33850 / 24950

    # axis center
    R_AXIS_Y_CENTER = 31075
    R_AXIS_X_CENTER = 31500
    L_AXIS_X_CENTER = 30100
    L_AXIS_Y_CENTER = 33850

    def map_button(self,event):
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

    def map_dpad(self,event):
        if event.type == 3:
            if event.code == 16:
                if event.value == -1:
                    return DPAD_L
                if event.value == 1:
                    return DPAD_R
                else:
                    return DPAD_CENTER

            if event.code == 17:
                if event.value == -1:
                    return DPAD_U
                if event.value == 1:
                    return DPAD_D
                else:
                    return DPAD_CENTER

        return DPAD_CENTER

    def get_lx_axis(self,event,lx):
        if event.code == 0 and event.type == 3:
            return event.value
        else:
            return lx

    def get_ly_axis(self,event,ly):
        if event.code == 1 and event.type == 3:
            return event.value
        else:
            return ly

    def get_rx_axis(self,event,rx):
        if event.code == 3 and event.type == 3:
            return event.value
        else:
            return rx

    def get_ry_axis(self,event,ry):
        if event.code == 4 and event.type == 3:
            return event.value
        else:
            return ry

    def map_l_axis(self,_x, _y):
        x = (_x / 24900) - self.L_AXIS_X_CONVER
        y = -(_y / 24950) + self.L_AXIS_Y_CONVER

        intensity = math.hypot(x, y)
        angle = (math.atan2(y, x) * 180 / math.pi)
        if angle < 0:
            angle += 360

        if intensity < 0.1:
            intensity = 0

        intensity = min(intensity, 1)

        return intensity, angle

    def map_r_axis(self,_x, _y):
        x = (_x / 23500) - self.R_AXIS_X_CONVER
        y = -(_y / 24425) + self.R_AXIS_Y_CONVER

        intensity = math.hypot(x, y)
        angle = (math.atan2(y, x) * 180 / math.pi)
        if angle < 0:
            angle += 360

        if intensity < 0.1:
            intensity = 0

        intensity = min(intensity, 1)

        return intensity, angle

class PS4ControllerMapping():
    '''
        Botones:
            Todos son type 1

            Release: val 0
            Press: val 1
            Hold: DOESN'T EXIST !

            B: code 304
            A: code 305
            Y: code 308 !
            X: code 307

            L: 310 !
            R: 311 !
            ZL: 312 !
            ZR: 313 !

            -: code 314 !
            +: code 315 !
            Bump left: code 317 !
            Bump right: code 318 !
            home: code 316
            capture: DOESN'T EXIST !


        Evento nada:
            code 00, type 00, val 00

        Evento random:
            code 04, type 04, val random ???

        joystick y flechas son type3

        Joystick Izquierdo:!
        	code 0 horizontal:
        		minimo: 0 izquierdo !
        		max:	255 derecho !
        	code 1 vertical:
        		minimo: 0 arriba !
        		max: 255 abajo !

        Joystick derecho:!
        	code 3 horizontal:
        		minimo: 0 izquierdo !
        		max: 255 derecha !
        	code 4 vertical
        		minimo: 0 arriba !
        		max: 255 abajo !

        Flechas:
            val 0 centro para todos
            izquierda code 16 val -1
            derecho code 16 val 1
            arriba code 17 val -1
            abajo code 17 val 1
    '''

    # axis center
    R_AXIS_Y_CENTER = 127
    R_AXIS_X_CENTER = 127
    L_AXIS_X_CENTER = 127
    L_AXIS_Y_CENTER = 127

    def map_button(self,event):
        if event.type in [1,2]:
            if event.code == 304:
                return BTN_B
            if event.code == 305:
                return BTN_A
            if event.code == 308:
                return BTN_Y
            if event.code == 307:
                return BTN_X
            if event.code == 310:
                return BTN_L
            if event.code == 311:
                return BTN_R
            if event.code == 312:
                return BTN_ZL
            if event.code == 313:
                return BTN_ZR
            if event.code == 314:
                return BTN_MINUS
            if event.code == 315:
                return BTN_PLUS
            if event.code == 317:
                return BTN_LCLICK
            if event.code == 318:
                return BTN_RCLICK
            if event.code == 316:
                return BTN_HOME
            else:
                return BTN_NONE
        else:
            return BTN_NONE

    def map_dpad(self,event):
        if event.type == 3:
            if event.code == 16:
                if event.value == -1:
                    return DPAD_L
                if event.value == 1:
                    return DPAD_R
                else:
                    return DPAD_CENTER

            if event.code == 17:
                if event.value == -1:
                    return DPAD_U
                if event.value == 1:
                    return DPAD_D
                else:
                    return DPAD_CENTER

        return DPAD_CENTER

    def get_lx_axis(self,event,lx):
        if event.code == 0 and event.type == 3:
            return event.value
        else:
            return lx

    def get_ly_axis(self,event,ly):
        if event.code == 1 and event.type == 3:
            return event.value
        else:
            return ly

    def get_rx_axis(self,event,rx):
        if event.code == 3 and event.type == 3:
            return event.value
        else:
            return rx

    def get_ry_axis(self,event,ry):
        if event.code == 4 and event.type == 3:
            return event.value
        else:
            return ry

    def map_l_axis(self,_x, _y):
        x = (2 * _x / 255) - 1
        y = -(2 * _y / 255) + 1

        intensity = math.hypot(x, y)
        angle = (math.atan2(y, x) * 180 / math.pi)
        if angle < 0:
            angle += 360

        if intensity < 0.1:
            intensity = 0

        intensity = min(intensity, 1)

        return intensity, angle

    def map_r_axis(self,_x, _y):
        x = (2 * _x / 255) - 1
        y = -(2 * _y / 255) + 1

        intensity = math.hypot(x, y)
        angle = (math.atan2(y, x) * 180 / math.pi)
        if angle < 0:
            angle += 360

        if intensity < 0.1:
            intensity = 0

        intensity = min(intensity, 1)

        return intensity, angle
