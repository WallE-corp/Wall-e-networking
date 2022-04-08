import wallE_networking as wen

if __name__ == "__main__":
  ch = wen.WallECommandHandler()


  @ch.move('left')
  def left(action):
    print(action, 'moving left')


  @ch.move('right')
  def right(action):
    print(action, 'moving right')


  @ch.move('forward')
  def forward(action):
    print(action, 'moving forward')


  @ch.move('backward')
  def backward(action):
    print(action, 'moving backward')


  ch.start_listening()

