import inspect
from os import curdir
import os
import sys
import inspect
from unittest import TestCase

curdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(curdir)
sys.path.insert(0, parentdir)

from backend_requests import *

class TestBackendRequests(TestCase):
  def setUp(self):
    self.base_url = '127.0.0.1:3000'
    self.timeout = 0.1

  def test_upload_obstacle_event(self):
    obstacle_event = ObstacleEvent(vx=0, vy=0, obstacle_image_filepath='test.png')
    result = upload_obstacle_event(obstacle_event)
    self.assertTrue(obstacle_event in obstacle_events)
    self.assertTrue(obstacle_event in unsynced_obstacle_events)

  def test_store_unsynced_obstacle_events(self):
    # Given
    obstacle_event = ObstacleEvent(vx=0, vy=0, obstacle_image_filepath='test.png')
    unsynced_obstacle_events = [obstacle_event]
    
    # When
    was_successful = store_unsynced_obstacle_events()

    # Then
    self.assertTrue(was_successful)
    self.assertTrue(obstacle_event in unsynced_obstacle_events)
    with open('data/obstacle_events.pkl', 'rb') as f:
      unsynced_obstacle_events = pickle.load(f)
      self.assertTrue(obstacle_event in unsynced_obstacle_events)