from backend_requests import base_url, timeout
import requests
import threading

x = 0
y = 0

def upload_position_data():
  """
  Attempts to upload position data to the backend
  Args:
    data: object
      Object containing at minimum the x and y position data to upload.

  Returns:
    True if the data was successfully uploaded
  """
  global x, y
  data = {
    "x": x,
    "y": y
  }
  print("uploading", x, y)
  res = requests.post(f'{base_url}/pathpoints', data)
  if res.status_code >= 400:
    return False
  x = 0
  y = 0
  return True


def handle_postion_data(_x, _y):
  """
  Adds the give x, y data to a local x, y which is then uploaded at next interval

  """

  global x, y
  x += _x
  y += _y

def start_uploading_position_data(interval):
  """
  Starts uploading position data on separate thread at the interval
  provided in arguments.
  Args:
    interval: number
      Rate in seconds at which to upload position data
  """
  threading.Timer(interval, upload_position_data).start()
  

start_uploading_position_data(1)
