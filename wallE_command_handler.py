import functools
import json
from wallE_socketio_server import SocketIOServer


class WallECommandHandler(object):
  def __init__(self):
    self.sio_server = SocketIOServer()
    self.sio_server.delegate = self

    self.command_map = {
      4: self.handle_movement_command
    }
    self.movement_commands = {}

  def start_listening(self):
    self.sio_server.run()

  def handle_message(self, message):
      message_data = json.loads(message)
      print(message_data)
      command = self.command_map.get(message_data['type'])
      command(message_data['data'])


  def handle_movement_command(self, data):
    movement = data['movement']
    movement_command = self.movement_commands.get(movement)
    movement_command(data['action'])

  # ======= Decorator functions ===================
  def move(self, movement):
    def decorator_move(func):
      self.movement_commands[movement] = func
    return decorator_move


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


ch.start_listening()
