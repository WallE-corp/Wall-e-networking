from src.command_handler import WallECommandHandler, Commands

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

ch.start_listening()

