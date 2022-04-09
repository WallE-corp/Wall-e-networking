from dataclasses import dataclass
import requests

base_url = 'http://127.0.0.1:3000'
timeout = 0.1

def ping():
  """
  Sends a 'ping' to the backend server and awaits a 'pong' response waiting at most
  the set timeout.

  Returns:
    Boolean on whether a 'pong' response was received.
  """
  res = requests.get(base_url + '/router', timeout=timeout)
  if (res.status_code == 200 and res.text == 'pong'):
    return True
  return False

@dataclass
class ObstacleEvent:
  """
  Represents an obstacle event.

  Attributes:
  -----------
  vx: int
    The virtual x coordinate of the obstacle.
  vy: int
    The virtual y coordinate of the obstacle.
  obstacle_image_filepath: str
    The file path of the obstacle image.
  is_uploaded: bool
    Whether the obstacle event has been uploaded to the backend.
  """
  vx: int
  vy: int
  obstacle_image_filepath: str
  is_uploaded: bool = 0

  def __str__(self) -> str:
    return f'ObstacleEvent(vx={self.vx}, vy={self.vy}, obstacle_image_filepath={self.obstacle_image_filepath}, is_uploaded={self.is_uploaded})'

def upload_obstacle_event(obstacle_event: ObstacleEvent):
  """
  Locally stores an ObstacleEvent then attempts to upload
  it to the backend server.

  Returns:
    Boolean on whether the ObstacleEvent was successfully uploaded to the backend.
  """
  pass
