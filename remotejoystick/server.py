import time

from models.communication.server import server

def run_server(serverPort, accessPair):
    s = server(('0.0.0.0', serverPort), accessPair)
    s.start()
    print('Server started, press Ctrl-C to exit.')
    try:
        while 1: time.sleep(1)
    except KeyboardInterrupt:
        s.stop()
