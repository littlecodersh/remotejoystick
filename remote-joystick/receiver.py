from config import SERVER, VERIFY_CODE
from models.communication.receiver import receiver
from models.controller.keyboard import keyboard, KEY_VALUE_LIST

KEY_VALUE_LIST = {chr(v): k for k, v in KEY_VALUE_LIST.items()}

kb = keyboard()
def produce_command(cmd):
    if len(cmd) != 4:
        return
    elif cmd[0] == '\x00':
        kb.key_up(KEY_VALUE_LIST.get(cmd[3], cmd[3]))
    elif cmd[0] == '\x01':
        kb.key_down(KEY_VALUE_LIST.get(cmd[3], cmd[3]))


r = receiver()
while not r.connect(SERVER, VERIFY_CODE): pass
print('Receiver connected')

try:
    while r.isAlive():
        msg = r.getMsg()
        if msg: produce_command(msg)
except KeyboardInterrupt:
    r.disconnect()
