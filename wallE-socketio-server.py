import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
  print('connect', sid)


@sio.event
def disconnect(sid):
  print('disconnect', sid)


@sio.on('message')
def print_message(sid, data):
  print('message', data)


eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
