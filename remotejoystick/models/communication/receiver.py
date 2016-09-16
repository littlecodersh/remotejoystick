import threading, select, socket

from .jssocket import jssocket

class receiver(object):
    __client = jssocket()
    __msgPipe = []
    __connected = False
    def __init__(self):
        pass
    def __recv_fn(self):
        while self.__connected:
            msgType, msgData = self.__client.pull()
            if msgType == jssocket.CLOSE:
                self.disconnect()
            else:
                self.__msgPipe.insert(jssocket.CLOSE, msgData)
    def connect(self, serverInfo, verifyCode):
        if self.__connected == True: return True
        try:
            self.__client.connect(serverInfo)
        except socket.error:
            return False
        self.__client.push(jssocket.RECEIVER, ('0000' + verifyCode)[-4:])
        try:
            while not select.select([self.__client], [], [], .5)[0]: pass
        except KeyboardInterrupt:
            self.__client.push(jssocket.CLOSE, '\x00\x00\x00\x00')
            self.__client.close()
            return False
        else:
            msgType, msgData = self.__client.pull()
            if msgType == jssocket.RECEIVER and msgData == verifyCode:
                self.__connected = True
                recvThread = threading.Thread(target=self.__recv_fn)
                recvThread.setDaemon(True)
                recvThread.start()
                return True
    def disconnect(self):
        if self.__connected == False: return
        self.__client.push(jssocket.CLOSE, '\x00\x00\x00\x00')
        self.__client.close()
        self.__connected = False
    def getMsg(self):
        if self.__msgPipe: return self.__msgPipe.pop()
        return None
    def isAlive(self):
        return self.__connected

if __name__ == '__main__':
    r = receiver()
    while not r.connect(('120.27.119.189', 2333), '1234'): pass
    print('connected')
    try:
        while r.isAlive():
            msg = r.getMsg()
            if msg: print(msg)
    except KeyboardInterrupt:
        r.disconnect()
