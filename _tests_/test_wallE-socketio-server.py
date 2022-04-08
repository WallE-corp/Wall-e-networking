import socketio
import asyncio
import json


class SocketIOClient(socketio.ClientNamespace):
  def __init__(self):
    super().__init__()
    self.sioClient = socketio.Client()
    self.sioClient.register_namespace(self)
    self.connect()

  def connect(self):
    self.sioClient.connect('http://localhost:8080')
    self.sioClient.wait()

  def on_connect(self):
    data = {
      'type': 4,
      'data': {
        'movement': 'left',
        'action': 'start'
      }
    }
    data_string = json.dumps(data)
    self.sioClient.emit('message', data_string)

  def on_disconnect(self):
    print("Client disconnected")


sioClient = SocketIOClient()
