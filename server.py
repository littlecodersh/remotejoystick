from config import SERVER, VERIFY_CODE
from models.communication.server import server

s = server(('0.0.0.0', VERIFY_CODE))
s.start()
raw_input('Started\n')
s.stop()
