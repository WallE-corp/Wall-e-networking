from abc import ABC, abstractmethod


class Command(ABC):
  @abstractmethod
  def execute(self, data_dict):
    pass

# =========== Movement commands ================================
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


