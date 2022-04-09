import inspect
from os import curdir
import os
import sys
import inspect
from unittest import TestCase

curdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(curdir)
sys.path.insert(0, parentdir)

from command_handler import WallECommandHandler

class TestWallECommandHandler(TestCase):
  def setUp(self):
    self.cmdh = WallECommandHandler()

  def test_handle_message(self):
    data_string = '{"type":4,"data":{"movement":"left","action":"start"}}'
    result = self.cmdh.handle_message(data_string)
    self.assertTrue(result)

  def test_handle_movement_command(self):
    self.cmdh.movement_commands = {
      'left': lambda action: print(action)
    }
    data = {
      'movement': 'left',
      'action': 'start'
    }
    result = self.cmdh.handle_movement_command(data)
    self.assertTrue(result)

  def test_move(self):
    @self.cmdh.move('left')
    def left(action):
      pass

    self.assertIn('left', self.cmdh.movement_commands)

  def test_command(self):
    @self.cmdh.command(2)
    def set_movement_speed(data):
      pass

    self.assertIn(2, self.cmdh.commands)
