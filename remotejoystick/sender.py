import time

from models.communication.sender import sender
from models.controller.keyboard import KEY_VALUE_LIST
from models.controller.joystick import joystick
from config import BUTTON_DICT, DIRECTION_LIST, HAT_LIST

KEY_VALUE_LIST = {k: chr(v) for k, v in KEY_VALUE_LIST.items()}

def run_sender(serverIp, serverPort, verifyCode, joystickNumber):
    s = sender()
    def key_down(key):
        s.sendMsg(b'\x01' + b'\x00' * 2 + key)
    def key_up(key):
        s.sendMsg(b'\x00' * 3 + key)
    print('Sender started, press Ctrl-C to exit.')
    try:
        while not s.connect((serverIp, serverPort), verifyCode): pass
        print('Sender successfully connected.')

        js = joystick()
        def registe_button(k, v):
            @js.button_register(k)
            def button_fn(motion):
                if motion == 'down':
                    key_down(v)
                elif motion == 'up':
                    key_up(v)
        def registe_axis(i, neg, pos):
            @js.axis_register(i)
            def axis_fn(status):
                if status == 0:
                    key_up(KEY_VALUE_LIST.get(neg, neg))
                    key_up(KEY_VALUE_LIST.get(pos, pos))
                elif status == 1:
                    key_down(KEY_VALUE_LIST.get(pos, pos))
                elif status == -1:
                    key_down(KEY_VALUE_LIST.get(neg, neg))
        def registe_hat(i, neg, pos):
            @js.hat_register(i)
            def hat_fn(status):
                if status == 0:
                    key_up(KEY_VALUE_LIST.get(neg, neg))
                    key_up(KEY_VALUE_LIST.get(pos, pos))
                elif status == 1:
                    key_down(KEY_VALUE_LIST.get(pos, pos))
                elif status == -1:
                    key_down(KEY_VALUE_LIST.get(neg, neg))

        for k, v in BUTTON_DICT.items(): registe_button(k, v)
        for directionTuple in DIRECTION_LIST: registe_axis(*directionTuple)
        for hatTuple in HAT_LIST: registe_hat(*hatTuple)

        if js.init(joystickNumber):
            js.start()
            while 1: raw_input()
        else:
            print('Specified joystick not detected, please restart after plugged in.')
    except Exception as e:
        if not e in (NameError, EOFError): raise e
        try:
            s.disconnect()
            js.stop()
        except NameError:
            pass
