import sys

from models.controller.joystick import joystick
from models.controller.keyboard import keyboard
from config import BUTTON_DICT, DIRECTION_LIST, HAT_LIST

def run_local(joystickNumber):
    js = joystick()
    kb = keyboard()

    def registe_button(k, v):
        @js.button_register(k)
        def button_fn(motion):
            if motion == 'down':
                kb.key_down(v)
            elif motion == 'up':
                kb.key_up(v)
    def registe_axis_or_hat(register, i, neg, pos):
        @register(i)
        def axis_fn(status):
            if status == 0:
                kb.key_up(neg); kb.key_up(pos)
            elif status == 1:
                kb.key_down(pos)
            elif status == -1:
                kb.key_down(neg)

    for k, v in BUTTON_DICT.items(): registe_button(k, v)
    for directionTuple in DIRECTION_LIST: registe_axis_or_hat(js.axis_register, *directionTuple)
    for hatTuple in HAT_LIST: registe_axis_or_hat(js.hat_register, *hatTuple)

    if js.init(joystickNumber):
        js.start()
        try:
            print('Your joystick can be used as keyboard now.')
            sys.stdin.read()
        except:
            pass
        js.stop()
    else:
        print('Specified joystick not detected, please restart after plugged in')
