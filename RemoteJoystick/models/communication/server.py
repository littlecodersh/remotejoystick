import time, threading, socket

from jssocket import jssocket

CONNECT_WAIT_TIME, CMD_WAIT_TIME = 5, 180
CLIENT_LIST = [[], []]

class server(object):
    __server = jssocket()
    __verificationDict = {}
    # verificationDict has three status:
    # 1. 1 | 2 (client type) for waiting for another client
    # 2. client for client is set
    # 3. Deleted for waiting for first client
    __alive = False
    def __init__(self, serverInfo, accessPair=1):
        self.__server.bind(serverInfo)
        self.__server.listen(accessPair * 2)
        self.__pairThread = threading.Thread(target=self.__wait_for_pair)
        self.__pairThread.setDaemon(True)
    def __wait_for_pair(self):
        while self.__alive:
            remoteClient, address = self.__server.accept()
            remoteClient.settimeout(CONNECT_WAIT_TIME)
            try:
                order, data = self.__server.format_pull(remoteClient)
                remoteClient.settimeout(None)
            except socket.timeout:
                remoteClient.close()
                continue # no message in some seconds will cause close of socket
            if order not in (jssocket.SENDER, jssocket.RECEIVER):
                remoteClient.close() # invalid cmd
            elif self.__verificationDict.get(data) in (jssocket.SENDER, jssocket.RECEIVER):
                # means this socket is the second socket
                if self.__verificationDict.get(data) == order:
                    # same verify code is currently used
                    self.__server.format_push(remoteClient, 0, b'\x00\x00\x00\x00')
                    remoteClient.close()
                else:
                    # set value so that first socket can go on with it
                    self.__verificationDict[data] = remoteClient
            elif self.__verificationDict.get(data) is None:
                # means this socket is the first socket
                self.__verificationDict[data] = order
                communicateThread = threading.Thread(target=self.__communicate_fn,
                    args=(data, order, remoteClient))
                communicateThread.setDaemon(True)
                communicateThread.start()
                self.__print_status(order)
    def __print_status(self, clientType):
        print('%s updated, current code: ' % {jssocket.SENDER: 'SENDER', jssocket.RECEIVER: 'RECVER'}.get(clientType)
            + ', '.join(filter(lambda x: self.__verificationDict[x] == clientType, self.__verificationDict.keys())))
    def __communicate_fn(self, verifyCode, clientType, client):
        stopTime = time.time() + CMD_WAIT_TIME
        while self.__alive and time.time() < stopTime:
            if self.__verificationDict[verifyCode] in (jssocket.SENDER, jssocket.RECEIVER):
                time.sleep(.5)
            else:
                sender, receiver = client, self.__verificationDict[verifyCode]
                del self.__verificationDict[verifyCode]
                self.__print_status(clientType)
                if clientType != jssocket.SENDER: sender, receiver = receiver, sender
                if not (self.__server.format_push(sender, jssocket.SENDER, verifyCode)
                        and self.__server.format_push(receiver, jssocket.RECEIVER, verifyCode)):
                    break
                sender.settimeout(CMD_WAIT_TIME) # timeout will cause return (0, b'\x00'*4)
                msgType, msgData = self.__server.format_pull(sender)
                while self.__alive and msgType != 0:
                    self.__server.format_push(receiver, msgType, msgData)
                    msgType, msgData = self.__server.format_pull(sender)
                if msgType == 0: self.__alive = False
        try: # exit main loop so socket will be closed
            for c in (sender, receiver): 
                self.__server.format_push(c, 0, b'\x00\x00\x00\x00')
                c.close()
        except NameError: # cannot get second socket in CMD_WAIT_TIME
            self.__server.format_push(client, 0, b'\x00\x00\x00\x00')
            client.close()
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
