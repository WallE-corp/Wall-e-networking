from wallE_commands import *
import json
from wallE_socketio_server import SocketIOServer


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


cmdHandler = WallECommandHandler()
cmdHandler.start_listening()
