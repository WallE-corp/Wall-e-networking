from src.command_handler import WallECommandHandler, Commands
import threading
import time

ch = WallECommandHandler()


@ch.move('left')
def left(action):
  print(action, 'moving left')


@ch.move('right')
def right(action):
  print(action, 'moving right')


@ch.move('forward')
def forward(action):
  print(action, 'moving forward')


@ch.move('backward')
def backward(action):
  print(action, 'moving backward')


@ch.command(Commands.START_CALIBRATION)
def start_calibration(data):
  print('Starting calibration')


def read_serial_data():
  while True:
    time.sleep(3)
    print(time.ctime(time.time()))


t = threading.Thread(target=read_serial_data)
t.start()

ch.start_listening()

