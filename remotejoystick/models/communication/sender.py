import sys, select, socket

from .jssocket import jssocket

class sender(object):
    __client = jssocket()
    __connected = False
    def __init__(self):
        pass
    def connect(self, serverInfo, verifyCode):
        if self.__connected == True: return True
        try:
            self.__client.connect(serverInfo)
        except socket.error:
            return False
        self.__client.push(jssocket.SENDER, ('0000' + verifyCode)[-4:])
        try:
            while not select.select([self.__client], [], [], .5)[0]: pass
        except KeyboardInterrupt:
            self.__client.push(jssocket.CLOSE, '\x00\x00\x00\x00')
            self.__client.close()
            return False
        else:
            msgType, msgData = self.__client.pull()
            if msgType == jssocket.SENDER and msgData == verifyCode:
                self.__connected = True
                return True
    def disconnect(self):
        if self.__connected == False: return
        self.__client.push(jssocket.CLOSE, '\x00\x00\x00\x00')
        self.__client.close()
        self.__connected = False
    def sendMsg(self, data):
        if not self.__connected: return False
        self.__client.push(jssocket.DATA, ('\x00\x00\x00\x00' +
            data)[-4:])
        return True

if __name__ == '__main__':
    s = sender()
    while not s.connect(('120.27.119.189', 2333), '1234'): pass
    print('Connected')
    try:
        while s.sendMsg(sys.stdin.readline('>')[:-1]): pass
    except KeyboardInterrupt:
        s.disconnect()
