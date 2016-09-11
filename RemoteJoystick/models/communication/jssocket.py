import socket, re

# b'\x08\x00\x01\x00\x00\x00\x00\x00'
# 0. \x08\x00
# 2. \x00: close \x01: sender \x02: receiver \x03: data
# 3. \x00\x00\x00\x00 data
# 7. \x00

msgRegex = re.compile(b'\x08\x00[\x00\x01\x02\x03][\s\S]{4}\x00')

class jssocket(socket.socket):
    CLOSE, SENDER, RECEIVER, DATA = 0, 1, 2, 3
    def pull(self):
        return self.format_pull(self)
    def push(self, msgType, msg):
        return self.format_push(self, msgType, msg)
    def format_push(self, remoteClient, msgType, msg):
        try:
            remoteClient.sendall(b'\x08\x00' + chr(msgType)
                + msg + b'\x00')
            return True
        except:
            return False
    def format_pull(self, remoteClient):
        try:
            msg = remoteClient.recv(8)
        except:
            return 0, b'\x00\x00\x00\x00'
        if not msgRegex.match(msg): return None, None
        return ord(msg[2]), msg[3:7]
