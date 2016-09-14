import time, threading, copy
import win32api, win32con

SCAN_TIME = 1.0 / 50
KEY_VALUE_LIST = {
    'left': 37, 'up': 38,
    'right': 39, 'down': 40, }

class keyboard(object):
    __keyList = set()
    def __init__(self):
        self.mainThread = threading.Thread(target=self.__main_thread_fn)
        self.mainThread.setDaemon(True)
        self.mainThread.start()
    def __main_thread_fn(self):
        while 1:
            for keyValue in copy.copy(self.__keyList):
                win32api.keybd_event(keyValue, 0, 0, 0)
            time.sleep(SCAN_TIME)
    def __get_key_value(self, key):
        if key.isdigit() and 0 <= int(key) <= 9:
            return int(key)
        elif len(key) == 1 and 65 <= ord(key.upper()) <= 90:
            return ord(key.upper())
        elif key in KEY_VALUE_LIST.keys():
            return KEY_VALUE_LIST[key]
    def key_down(self, key):
        keyValue = self.__get_key_value(key)
        if keyValue is None: return False
        self.__keyList.add(keyValue)
        return True
    def key_up(self, key):
        keyValue = self.__get_key_value(key)
        if keyValue is None: return False
        if keyValue in self.__keyList: self.__keyList.remove(keyValue)
        return True

if __name__ == '__main__':
    kb = keyboard()
    time.sleep(2)
    kb.key_down('v')
    time.sleep(2)
    kb.key_up('v')
    try:
        sys.stdin.read()
    except:
        print('Finish')
