
socket = None
clientHandler = None
send_queue = []
def send(id, value, event_name):
    global socket
    socket.emit("from_server", {'id': id, 'value': value, 'event_name': event_name})

def queue_for_send(id, value, event_name):
    global send_queue
    print("queueing for send", id, value, event_name)
    send_queue.append({'id': id, 'value': value, 'event_name': event_name})

def flush_send_queue():
    global send_queue
    for item in send_queue:
        print("sending", item)
        send(item['id'], item['value'], item['event_name'])
    send_queue = []