import logging
from ctypes import CDLL
import time
try:
    import click
except ImportError:
    print("Try using 'pip install python-snap7[cli]'")
    raise
from snap7 import __version__
from snap7.common import load_library
from snap7.server import mainloop
from snap7 import client
logger = logging.getLogger("Snap7.Server")
def run_client():
    SERVER_IP = input("Enter remote server ip:")
    if len(SERVER_IP.strip()) == 0:
        SERVER_IP = "127.0.0.1"
    SERVER_PORT = 102
    s7_client = client.Client()
    s7_client.connect(SERVER_IP, 0, 0, SERVER_PORT)
    s7_client.get_connected()
    while 1:
        data = s7_client.db_read(1, 0, 4)
        print(data)
        time.sleep(1)
def run_server(port: int) -> None:
    logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)
    mainloop(port, init_standard_values=True)


if __name__ == "__main__":
    choice = int(input("1.Run as server\n2.Run as client\nEnter your choice:"))
    if choice == 1:
        run_server(102)
    elif choice == 2:
        run_client()
    else:
        print("Give valid input")
