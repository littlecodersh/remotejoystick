import time

from models.communication.receiver import receiver
from models.controller.keyboard import keyboard, KEY_VALUE_LIST

KEY_VALUE_LIST = {chr(v): k for k, v in KEY_VALUE_LIST.items()}

def run_receiver(serverIp, serverPort, verifyCode):
    kb = keyboard()
    def produce_command(cmd):
        if len(cmd) != 4:
            return
        elif cmd[0] == '\x00':
            kb.key_up(KEY_VALUE_LIST.get(cmd[3], cmd[3]))
        elif cmd[0] == '\x01':
            kb.key_down(KEY_VALUE_LIST.get(cmd[3], cmd[3]))

    r = receiver()
    print('Receiver started, press Ctrl-C to exit.')
    try:
        while not r.connect((serverIp, serverPort), verifyCode): pass
        print('Receiver successfully connected.')
        while r.isAlive():
            msg = r.getMsg()
            if msg: produce_command(msg)
            time.sleep(.05)
    except KeyboardInterrupt:
        r.disconnect()
