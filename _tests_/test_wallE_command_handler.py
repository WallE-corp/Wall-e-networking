from unittest import TestCase
from wallE_command_handler import WallECommandHandler

class TestWallECommandHandler(TestCase):
  def setUp(self):
    self.cmdh = WallECommandHandler()

  def test_handle_message(self):
    self.fail()

  def test_handle_movement_command(self):
    self.fail()

  def test_move(self):
    @self.cmdh.move('left')
    def left(action):
      pass

    self.assertIn('left', self.cmdh.movement_commands)
