from config import SERVER, VERIFY_CODE
from models.communication.sender import sender
from models.controller.keyboard import KEY_VALUE_LIST
from models.controller.joystick import joystick

KEY_VALUE_LIST = {k: chr(v) for k, v in KEY_VALUE_LIST.items()}
BUTTON_LIST = {
    0: 'A', 1: 'B',
    2: 'X', 3: 'Y', }

def key_down(key):
    s.sendMsg(b'\x01' + b'\x00' * 2 + key)
def key_up(key):
    s.sendMsg(b'\x00' * 3 + key)

s = sender()
while not s.connect(SERVER, VERIFY_CODE): pass
print('Sender connected')

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
            key_up(KEY_VALUE_LIST[neg])
            key_up(KEY_VALUE_LIST[pos])
        elif status == 1:
            key_down(KEY_VALUE_LIST[pos])
        elif status == -1:
            key_down(KEY_VALUE_LIST[neg])

for k, v in BUTTON_LIST.items(): registe_button(k, v)
for directionTuple in ((0, 'left', 'right'), (1, 'up', 'down')):
    registe_axis(*directionTuple)

js.init()
js.start()

try:
    raw_input('Ready\n')
except:
    pass
js.stop()
s.disconnect()
