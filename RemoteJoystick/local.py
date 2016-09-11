from models.controller.keyboard import KEY_VALUE_LIST
from models.controller.joystick import joystick
from models.controller.keyboard import keyboard
from config import BUTTON_DICT, DIRECTION_LIST, HAT_LIST

JOY_VALUE_LIST = {k: chr(v) for k, v in KEY_VALUE_LIST.items()}

def run_local():
    js = joystick()
    kb = keyboard()

    def key_down(key):
        kb.key_down(key)
    def key_up(key):
        kb.key_up(key)
    def registe_button(k, v):
        @js.button_register(k)
        def button_fn(motion):
            if motion == 'down':
                key_down(v)
            elif motion == 'up':
                key_up(v)
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

    js.init()
    js.start()
    try:
        while 1: raw_input()
    except:
        pass
