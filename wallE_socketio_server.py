import eventlet
import socketio
import json
from aiohttp import web
from abc import ABC, abstractmethod


class Command(ABC):
  @abstractmethod
  def execute(self, data_dict):
    pass


class MoveLeftCommand(Command):
  def execute(self, data_dict=None):
    print('Executing move left command.')


class MoveRightCommand(Command):
  def execute(self, data_dict=None):
    print('Executing move right command.')


class MoveForwardCommand(Command):
  def execute(self, data_dict=None):
    print('Executing move forward command.')


class MoveBackwardCommand(Command):
  def execute(self, data_dict=None):
    print('Executing move backward command.')


class MovementCommand(Command):
  def __init__(self):
    self.movement_commands = {
      'left': MoveLeftCommand(),
      'right': MoveRightCommand(),
      'forward': MoveForwardCommand(),
      'backward': MoveBackwardCommand()
    }

  def execute(self, data):
    movement_command = self.movement_commands.get(data)
    movement_command.execute()


class WallECommandHandler(object):
  def __init__(self):
    self.sio_server = SocketIOServer()
    self.sio_server.delegate = self

    self.command_map = {
      4: MovementCommand()
    }

  def start_listening(self):
    self.sio_server.run()

  def handle_message(self, message):
    try:
      message_data = json.loads(message)
      command = self.command_map.get(message_data['type'])
      command.execute(message_data['data'])
    except:
      pass


class SocketIOServer(socketio.AsyncNamespace):
  def __init__(self):
    super().__init__()
    self.sio = socketio.AsyncServer()
    self.sio.register_namespace(self)
    self.app = web.Application()
    self.sio.attach(self.app)

    self.delegate = None

  def run(self):
    web.run_app(self.app, port=8080)

  def on_connect(self, sid, environ):
    print('connect', sid)

  def on_disconnect(self, sid):
    print('disconnect', sid)

  def on_message(self, sid, message):
    print(self.delegate, message)
    if self.delegate is not None:
      self.delegate.handle_message(message)
    return 'OK'


cmdHandler = WallECommandHandler()
cmdHandler.start_listening()
