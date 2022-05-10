import asyncio
import json
import nest_asyncio
import websockets
from src import *

nest_asyncio.apply()

ch = WallECommandHandler()
client = None


@ch.move('left')
def left(action):
  mc = {
    "type": 2,
    "direction": "left",
    "action": action
  }

  asyncio.run(client.send(json.dumps(mc)))


@ch.move('right')
def right(action):
  mc = {
    "type": 2,
    "direction": "right",
    "action": action
  }

  asyncio.run(client.send(json.dumps(mc)))


@ch.move('forward')
def forward(action):
  mc = {
      "type": 2,
      "direction": "forward",
      "action": action
    }

  asyncio.run(client.send(json.dumps(mc)))


@ch.move('backward')
def backward(action):
  mc = {
    "type": 2,
    "direction": "backward",
    "action": action
  }

  asyncio.run(client.send(json.dumps(mc)))


@ch.command(Commands.START_CALIBRATION)
def start_calibration(data):
  print('Starting calibration')


async def handler(socket):
  global client
  client = socket
  while True:
    try:
      message = await socket.recv()
      messageData = json.loads(message)
      type = int(messageData["type"])

      if type == 6:
        print(messageData)
        oe = ObstacleEvent(x, y, messageData["imagePath"])
        upload_obstacle_event(oe)
      elif type == 1:
        handle_postion_data(messageData["x"], messageData["y"])


    except websockets.ConnectionClosed:
      print("Client disconnected")
      return


async def main():
  start_uploading_position_data(1)
  async with websockets.serve(handler, "0.0.0.0", 8765):
    await ch.start_listening()

if __name__ == "__main__":
  asyncio.run(main())
