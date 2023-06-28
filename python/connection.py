
socket = None
clientHandler = None
def send(id, value, event_name):
    global socket
    socket.emit("from_server", {'id': id, 'value': value, 'event_name': event_name})
    