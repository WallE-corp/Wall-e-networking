from dataclasses import dataclass
import requests
import pickle

base_url = 'http://127.0.0.1:3000'
timeout = 0.1
obstacle_events = []
unsynced_obstacle_events = []

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
  is_uploaded: bool = False

  def __str__(self) -> str:
    return f'ObstacleEvent(vx={self.vx}, vy={self.vy}, obstacle_image_filepath={self.obstacle_image_filepath}, is_uploaded={self.is_uploaded})'

def upload_obstacle_event(obstacle_event: ObstacleEvent):
  """
  Locally stores an ObstacleEvent then attempts to upload
  it to the backend server.

  Parameters:
  -----------
  obstacle_event: ObstacleEvent
    The obstacle event to upload.

  Returns:
  --------
    Boolean on whether the ObstacleEvent was successfully uploaded to the backend.
  """
  # Push event to obstacle_events list
  obstacle_events.append(obstacle_event)
  unsynced_obstacle_events.append(obstacle_event)

  # Update local storage of obstacle_events
  with open('obstacle_events.pkl', 'wb') as f:
    pickle.dump(unsynced_obstacle_events, f)

  # Attempt to upload event to backend
  ## If successful, update is_uploaded to True and return True
  ## If unsuccessful, return False
  return True
