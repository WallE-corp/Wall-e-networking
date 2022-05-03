# Wall-e-networking
This repository contains the code to handle connections with WallE's mobile and backend applications.

## Description
### Socket Server WallE commands
Sets up a socket server using `python-socketio`. 

Each message received is delegated to 
a command handler class which handles parsing the command data sent via the socket. 

Using decorators provided in the command handler, you can create and register your own functions that should be run
when a specific command is received.

## Structure
* `main.py` contains example code using the developed package.
* The main code that is developed here lies in the package `wallE_networking`.
* Unittests are located under the `__tests__` folder.

## Setup
To use just copy over the package and install the dependencies listed in `requirements.txt`.

For example:
```console
pip install -r requirements.txt
```

## Usage
### Socket Connection - Listening for WallE commands
To begin listening for commands:
1.  Instantiate the `WallECommandHandler` class. 
2.  For e.g. movement commands use the `move` method to decorate your own functions (_see below_).
3.  Call `start_listening` on the WallECommandHandler instance you created.

```python
  ch = wen.WallECommandHandler()

  @ch.move('left')
  def left(action):
    print(action, 'moving left')
    
  @ch.move('right')
  def right(action):
    print(action, 'moving right')

  ch.start_listening()
```
`action` Is either equal to 'start' or 'stop' to express when the command starts/stops.

## Documentation
_(comming soon)_
