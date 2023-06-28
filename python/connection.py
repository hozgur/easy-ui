
socket = None
clientHandler = None
def send(id, value):
    global socket
    socket.emit("from_server", {'id': id, 'value': value})
    