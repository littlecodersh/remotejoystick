import time, threading, socket

from jssocket import jssocket

WAIT_TIME = 60

class server(object):
    __server = jssocket()
    __verificationList = {}
    __alive = False
    def __init__(self, serverInfo, accessPair=1):
        self.__server.bind(serverInfo)
        self.__server.listen(accessPair * 2)
        self.__pairThread = threading.Thread(target=self.__wait_for_pair)
        self.__pairThread.setDaemon(True)
    def __wait_for_pair(self):
        while self.__alive:
            remoteClient, address = self.__server.accept()
            order, data = self.__server.format_pull(remoteClient)
            if order not in (1, 2): continue
            if self.__verificationList.get(data, -1) == None:
                self.__verificationList[data] = remoteClient
            else:
                self.__verificationList[data] = None
                communicateThread = threading.Thread(target=self.__communicate_fn,
                    args=(data, order, remoteClient))
                communicateThread.setDaemon(True)
                communicateThread.start()
    def __communicate_fn(self, verifyCode, clientType, client):
        print('%s: %s' % (clientType, verifyCode))
        stopTime = time.time() + WAIT_TIME
        while self.__alive and time.time() < stopTime:
            if self.__verificationList[verifyCode] is None:
                time.sleep(.5)
            else:
                sender, receiver = client, self.__verificationList[verifyCode]
                if clientType != 1: sender, receiver = receiver, sender
                if not (self.__server.format_push(sender, 1, verifyCode)
                        and self.__server.format_push(receiver, 2, verifyCode)):
                    break
                msgType, msgData = self.__server.format_pull(sender)
                while self.__alive and msgType != 0:
                    self.__server.format_push(receiver, msgType, msgData)
                    msgType, msgData = self.__server.format_pull(sender)
        self.__server.format_push(client, 0, b'\x00\x00\x00\x00')
        if self.__verificationList[verifyCode] is not None:
            self.__server.format_push(
                self.__verificationList[verifyCode], 0, b'\x00\x00\x00\x00')
            self.__verificationList[verifyCode].close()
        client.close()
        del self.__verificationList[verifyCode]
    def start(self):
        self.__alive = True
        self.__pairThread.start()
    def stop(self):
        self.__alive = False
        self.__server.close()

if __name__ == '__main__':
    s = server(('127.0.0.1', 2333))
    s.start()
    raw_input('Started\n')
    s.stop()
